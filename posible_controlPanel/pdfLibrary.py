from reportlab.lib.units import inch, mm
from reportlab.lib.enums import TA_JUSTIFY
from reportlab.lib.pagesizes import letter, A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Image
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from posible_controlPanel.labels import LABELS_QUESTIONS, LABELS_QUESTIONS_PDF
from posible_controlPanel.choices import *
from posible_controlPanel.helpers import jsonify
from django.conf import settings


class PdfPrint():
    def __init__(self, buffer, pageSize):
        self.buffer = buffer
        # default format is Letter
        if pageSize == 'Letter':
            self.pageSize = letter
        elif pageSize == 'A4':
            self.pageSize = A4
        self.width, self.height = self.pageSize
    
    
    def pageNumber(self, canvas, doc):
        # Save the state of our canvas so we can draw on it
        canvas.saveState()
        number = canvas.getPageNumber()
        canvas.drawCentredString(100*mm, 15*mm, str(number))
        # Release the canvas
        canvas.restoreState()
    
    def report(self,title, folio, content):
        transformable = {
                'modulo_2_2':dict(P_S),
                'modulo_2_3':dict(IDEA_CATEGORIES),
                'modulo_2_4':dict(DEV_STAGE),
                'modulo_2_6':dict(DEVELOPMENTS_TECH),
                'modulo_2_7': dict(DEVELOPMENTS_SCIENCE),
                'modulo_2_8':dict(INNOVATION),
                'modulo_3_1':dict(TYPE_CLIENTS),
                'modulo_3_1_2':dict(AGE),
                'modulo_3_1_3':dict(GENDER),
                'modulo_3_1_4':dict(INCOME),
                'modulo_3_1_5':dict(POPULATION),
                'modulo_3_2_2':dict(ENTERPRISE_SIZE),
                'modulo_3_4':dict(CLIENT_VOLUME),
                'modulo_4_1': dict(PRODUCT_BENEFITS),
                'modulo_5_1':dict(PRODUCT_MARKETING),
                'modulo_5_2': dict(YES_WHICH_NO),
                'modulo_5_3': dict(PRODUCT_AVAILABILITY),
                'modulo_5_4':dict(YES_WHICH_NO),
                'modulo_6_2': dict(INCOME_GENERATION),
                'modulo_6_3': dict(FINANCIAL_SUPPORT),
                'modulo_7_1':dict(NUMBER_EMPLOYEES)     
            }
        # set some characteristics for pdf document
        doc = SimpleDocTemplate(
            self.buffer,
            title=folio,
            rightMargin=72,
            leftMargin=72,
            topMargin=30,
            bottomMargin=72,
            pagesize=self.pageSize)
        styles = getSampleStyleSheet()
        styles.add(ParagraphStyle(name='questions_text', parent=styles['Heading4'],alignment=TA_JUSTIFY ))
        #styles.add(ParagraphStyle( name="ParagraphTitle", fontSize=11, alignment=TA_JUSTIFY))
        styles.add(ParagraphStyle(name='justified', alignment=TA_JUSTIFY))
        # create document
        data = []
        data.append(Paragraph(title, styles['Title']))
        data.append(Paragraph(content.modulo_2_1, styles['Title']))
        data.append(Paragraph('Folio: ' + folio, styles['Title']))
        
        for l in LABELS_QUESTIONS_PDF:
            if 'MODULE' in l:
                data.append(Paragraph(str(LABELS_QUESTIONS.get(l)),styles['Heading2']))
            elif 'modulo_' in l: #AT THIS POINT ANY LABEL WITH EMPTY VALUE WAS A QUESTION THAT SHOULD NOT APPEAR
                
                if 'modulo_2_5' not in l:
                    value = getattr(content,l)
                    if 'modulo_7_2' not in l:
                        if value and value.strip()!='':
                            if  value[0]=='[' and value[len(value)-1] == ']':
                                value = jsonify(value)
                                if value:
                                    data.append(Paragraph(str(LABELS_QUESTIONS.get(l)), styles['questions_text']))
                                    t = transformable.get(l)
                                    for v in value:
                                        data.append(Paragraph(t.get(v), styles['justified']))
                            else:
                                data.append(Paragraph(str(LABELS_QUESTIONS.get(l)), styles['questions_text']))
                                t =  transformable.get(l)
                                if t:
                                    data.append(Paragraph(t.get(value), styles['justified']))
                                else:
                                    data.append(Paragraph(value, styles['justified']))
                    else:
                        data.append(Paragraph(str(LABELS_QUESTIONS.get(l)), styles['questions_text']))
                        value = getattr(content,l)
                        if value.strip != "":
                            data.append(Paragraph(value, styles['justified']))
                        value2 = getattr(content,'modulo_7_2_2')
                        if value2.strip != "":
                            data.append(Paragraph(value2, styles['justified']))
                        value3 = getattr(content,'modulo_7_2_3')
                        if value3.strip != "":
                            data.append(Paragraph(value3, styles['justified']))
                        value4 = getattr(content,'modulo_7_2_4')
                        if value4.strip != "":
                            data.append(Paragraph(value4, styles['justified']))
                        value5 = getattr(content,'modulo_7_2_5')
                        if value5.strip != "":
                            data.append(Paragraph(value5, styles['justified']))
                else:
                    data.append(Paragraph(str(LABELS_QUESTIONS.get(l)), styles['questions_text']))
                    if content.modulo_2_5.url != '/imgs/projectPics/proyectos/no-img.png':
                        data.append( Image(settings.BASE_DIR + content.modulo_2_5.url, 2*inch, 2*inch))
                    if content.modulo_2_5_1.url != '/imgs/projectPics/proyectos/no-img.png':
                        data.append( Image(settings.BASE_DIR + content.modulo_2_5_1.url, 2*inch, 2*inch))
                    if content.modulo_2_5_2.url != '/imgs/projectPics/proyectos/no-img.png':
                        data.append( Image(settings.BASE_DIR + content.modulo_2_5_2.url, 2*inch, 2*inch))
        # create other flowables
        doc.build(data , onFirstPage=self.pageNumber, onLaterPages=self.pageNumber)
        pdf = self.buffer.getvalue()
        self.buffer.close()
        return pdf