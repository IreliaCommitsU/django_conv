PS_STATES = (
    ('',''),
    ('1', 'Aguascalientes'),
    ('2', 'Baja California'),
    ('3', 'Baja California Sur'),
    ('4', 'Campeche'),
    ('5', 'Coahuila de Zaragoza'),
    ('6', 'Colima'),
    ('7', 'Chiapas'),
    ('8', 'Chihuahua'),
    ('9', 'Ciudad de México'),
    ('10', 'Durango'),
    ('11', 'Guanajuato'),
    ('12', 'Guerrero'),
    ('13', 'Hidalgo'),
    ('14', 'Jalisco'),
    ('15', 'Estado de México'),
    ('16', 'Michoacán de Ocampo'),
    ('17', 'Morelos'),
    ('18', 'Nayarit'),
    ('19', 'Nuevo León'),
    ('20', 'Oaxaca'),
    ('21', 'Puebla'),
    ('22', 'Querétaro'),
    ('23', 'Quintana Roo'),
    ('24', 'San Luis Potosí'),
    ('25', 'Sinaloa'),
    ('26', 'Sonora'),
    ('27', 'Tabasco'),
    ('28', 'Tamaulipas'),
    ('29', 'Tlaxcala'),
    ('30', 'Veracruz de Ignacio de la Llave'),
    ('31', 'Yucatán'),
    ('32', 'Zacatecas'),
    
)

ENTERASTE = (
    ('tv','Televisión'),
    ('radio','Radio'),
    ('anuncio_revista','Anuncio en revista'),
    ('anuncio_exterior','Anuncio en exterior'),
    ('redes_sociales','Redes sociales'),
    ('recomendacion','Otra recomendación'),
    ('evento','Eventos'),
    ('email','Correo electrónico'),
    ('medios_digitales','Medios digitales'),
    ('recomendacion_emprendedor','Recomendación de emprendedor POSiBLE'),
)


GENDER = (
    ('Hombre','Masculino'),
    ('Mujer','Femenino'),
)

GRADE_STUDIES = (
    ('',''),
    ('Primaria','Primaria'),
    ('Secundaria','Secundaria'),
    ('Media Superior','Media superior'),
    ('Licenciatura','Licenciatura'),
    ('Diplomado','Diplomado'),
    ('Especialidad','Especialidad'),
    ('Maestría','Maestría'),
    ('Doctorado','Doctorado'),
)

P_S =(
    ('producto','Producto'),
    ('servicio','Servicio'),
)


IDEA_CATEGORIES = (
    ('educacion_capacitacion','Educación o Capacitación                                       '),
    ('salud_nutricion_deporte','Salud / Nutrición / Deporte'),
    ('vivienda_servicios_hogar','Vivienda / Servicios para el hogar'),
    ('energia_recnaturales_medioambiente','Energía / Recursos naturales / Medio Ambiente'),
    ('transporte_logistica','Transporte / Logística'),
    ('turismo_hoteleria_tiempolibre','Turismo / Hotelería / Tiempo Libre'),
    ('servagropecuario_animalesmascotas','Servicios Agropecuarios / Animales y mascotas'),
    ('infraestructura','Infraestructura'),
    ('serv_profesionales','Servicios Profesionales'),
    ('disenio_moda','Diseño y Moda'),
)
DEV_STAGE =(
    ('idea','Idea'),
    ('creacion','Proceso de creación (prototipo)'),
    ('operacion','En operación (Indica la fecha de inicio de operación)'),
)

DEVELOPMENTS_TECH =(
    ('pagina_web','Tienes una página web'),
    ('app_movil','Tienes una aplicación móvil'),
    ('tansacc_enlinea','Realizas transacciones en línea'),
    ('sw_hw','Tienes software o hardware propio'),
    ('prototipo','Cuentas con algún prototipo funcional'),
    ('no_aplica','No aplica'),
)

DEVELOPMENTS_SCIENCE = (
    ('laboratory','Realizas pruebas en laboratorio'),
    ('laboratory','Tienes alguna patente'),
    ('derechos_autor','Tienes derechos de autor'),
    ('investigacion_prod_serv','Realizaste alguna investigación para tu producto o servicio'),
    ('grupo_expertos','Hay un grupo de expertos que te orienta'),
    ('no_aplica','No aplica'),
)

INNOVATION = (
    ('inno_producto','Innovación en producto: Aporta un bien o servicio nuevo, o significativamente mejorado, en cuanto a sus características técnicas o en cuanto a su uso u otras funcionalidades, la mejora se logra con conocimiento o tecnología, con mejoras en materiales, en componentes, o con informática integrada.'),
    ('inno_proceso','Innovación en proceso: Se logra mediante cambios significativos en las técnicas, los materiales y/o los programas informáticos empleados, que tengan por objeto la disminución de los costes unitarios de producción o distribución, la mejorar la calidad, o la producción o distribución de productos nuevos o sensiblemente mejorados.'),
    ('inno_mercadotecnia','Innovación en mercadotecnia: Consiste en utilizar un método de comercialización no utilizado antes en la empresa que puede consistir en cambios significativos en diseño, envasado, posicionamiento, promoción o tarificación, siempre con el objetivo de aumentar la ventas.'),
    ('inno_organizacion','Innovación en organización: Cambios en las prácticas y procedimientos de la empresa, modificaciones en el lugar de trabajo, en las relaciones exteriores como aplicación de decisiones estratégicas con el propósito de mejorar los resultados mejorando la productividad o reduciendo los costes de transacción internos para los clientes y proveedores.'),
    ('ninguno','Ninguno'),
)

TYPE_CLIENTS = (
    ('personas','Personas'),
    ('empresas','Empresas'),
)

AGE = (
    ('ninios','Niños'),
    ('adolescentes','Adolescentes'),
    ('adultos','Adultos'),
    ('adultos_mayores','Adultos Mayores'),
)

INCOME = (
    ('bajo','Bajo'),
    ('medio','Medio'),
    ('alto','Alto'),
)

POPULATION = (
    ('rural','Rural'),
    ('urbana','Urbana'),
)


ENTERPRISE_SIZE = (
    ('micro_empresa','Microempresa'),
    ('pequenia_empresa','Pequeña Empresa'),
    ('mediana_empresa','Mediana Empresa'),
)

CLIENT_VOLUME = (
    ('1_50','1 a 50'),
    ('51_100','51 a 100'),
    ('101_250','101 a 250'),
    ('251_1000','251 a 1000'),
    ('1001_5000','1001 a 5000'),
    ('5000plus','más de 5000'),
    ('ninguno','No tengo'),
)
PRODUCT_BENEFITS = (
    ('buen_precio','Buen precio'),
    ('art_adicion_prod_serv','Artículos adicionales que se ofrecen al comprar el producto o servicio'),
    ('innovador','Innovador'),
    ('rapido','Rápido'),
    ('buena_calidad','Buena calidad'),
    ('disenio_func_atract','Diseño funcional / Atractivo'),
    ('seguir_client_desp_compra','Seguimiento al cliente después de la compra'),
    ('respeto_med_amb','Respeto del medio ambiente'),
    ('tiempo_entrega_adecuado','Tiempo de entrega adecuado'),
    ('mejora_cal_vida','Mejora calidad de vida'),
    ('facil_manejo','Facilidad de manejo'),
    ('garantia','Garantía'),
    ('confiabilidad_prod_seguro','Confiabilidad de que es un producto seguro'),
    ('facil_adquirir','Facilidad de adquirir'),
    ('otro','Otro'),
)

PRODUCT_MARKETING = (
    ('recomend_boca_boca','Recomendación de boca en boca (Recomendación personal)'),
    ('venta_directa','Venta directa'),
    ('demostraciones','Demostraciones'),
    ('particip_eventos','Participación en eventos'),
    ('volantes','Volantes'),
    ('espectaculares','Espectaculares'),
    ('revistas','Revistas'),
    ('prensa','Prensa'),
    ('radio','Radio'),
    ('television','Televisión'),
    ('redes_sociales','Redes sociales'),
    ('pagina_d_internet','Página de internet'),
    ('correo_electronico','Correo electrónico'),
    ('particip_blogs','Participación en blogs'),
    ('otro','Otro'),
)

PRODUCT_AVAILABILITY = (
    ('venta_directa','Venta directa'),
    ('tiendas_propios','Tiendas o establecimiento propios'),
    ('ventas_telefono','Ventas por teléfono'),
    ('tiendas_terceros','Tiendas o establecimiento terceros'),
    ('ventas_internet','Ventas por internet'),
    ('otro','Otro'),
)

YES_WHICH_NO =  (
    ('no','No'),
    ('si_cuales','Si (¿Cuál es?)'),
)

YES_NO =  (
    ('no','No'),
    ('si','Si'),
)

INCOME_GENERATION = (
    ('venta_producto_servicio','Venta de producto o servicio'),
    ('membresía_suscripción','Membresía o suscripción'),
    ('licencias','Licencias'),
    ('ventas_espacios_publicitarios','Ventas de espacios publicitarios'),
    ('cuota_mantenimiento','Cuota de mantenimiento'),
    ('intercambio','Intercambio'),
    ('cobro_interes','Cobro de interés'),
    ('otro','Otro'),
)

FINANCIAL_SUPPORT = (
    ('ninguno','No he recibido financiamiento'),
    ('fondeo_colectivo','Fondeo colectivo'),
    ('capital_semilla','Capital semilla'),
    ('credito_bancario','Crédito bancario'),
    ('prestamos_familiares','Préstamos familiares'),
    ('otro','Otro'),
)


NUMBER_EMPLOYEES = (
    ('1_3_empleos','1 - 3 empleos'),
    ('4_6_empleos','4 - 6 empleos'),
    ('6_10_empleos','6 - 10 empleos'),
    ('10_plus_empleos','Más de 10 empleos'),
    ('no_empleos','Aún no he generado empleos'),
)


NUMBERS_CHOICE = (
    ('1','1'),
    ('2','2'),
    ('3','3'),
    ('4','4'),
    ('5','5'),
)

horas = (
    ('Mensaje','Seleccione una hora por favor'),
    ('8:30-8:45am', '8:30-8:45 a.m.'),
    ('8:45-9:00am', '8:45-9:00 a.m.'),
    ('9:00-9:15am', '9:00-9:15 a.m.'),
    ('9:15-9:30am', '9:15-9:30 a.m.'),
    ('9:30-9:45am', '9:30-9:45 a.m.'),
    ('9:45-10:00am', '9:45-10:00 a.m.'),
    ('10:00-10:15am', '10:00-10:15 a.m.'),
    ('10:15-10:30am', '10:15-10:30 a.m.'),
    ('10:30-10:45am', '10:30-10:45 a.m.'),
    ('10:45-11:00am.', '10:45-11:00 a.m.'),
    ('11:00-11:15am', '11:00-11:15 a.m.'),
    ('11:15-11:30am', '11:15-11:30 a.m.'),
    ('11:30-11:45am', '11:30-11:45 a.m.'),
    ('11:45-12:00am', '11:45-12:00 a.m.'),
    ('12:00-12:15pm', '12:00-12:15 p.m.'),
    ('12:15-12:30pm', '12:15-12:30 p.m.'),
    ('12:30-12:45pm', '12:30-12:45 p.m.'),
    ('12:45-13:00pm', '12:45-13:00 p.m.'),
    ('13:00-13:15pm', '13:00-13:15 p.m.'),
    ('13:15-13:30pm', '13:15-13:30 p.m.'),
    ('13:30-13:45pm', '13:30-13:45 p.m.'),
    ('13:45-14:00pm', '13:45-14:00 p.m.'),
    ('15:30-15:45pm', '15:30-15:45 p.m.'),
    ('15:45-16:00pm', '15:45-16:00 p.m.'),
    ('16:00-16:15pm', '16:00-16:15 p.m.'),
    ('16:15-16:30pm', '16:15-16:30 p.m.'),
    ('16:30-16:45pm', '16:30-16:45 p.m.'),
    ('16:45-17:00pm', '16:45-17:00 p.m.'),
    ('17:00-17:15pm', '17:00-17:15 p.m.'),
    ('17:15-17:30pm', '17:15-17:30 p.m.'),
    ('17:30-17:45pm', '17:30-17:45 p.m.'),
    ('17:45-18:00pm', '17:45-18:00 p.m.'),
    ('18:00-18:15pm', '18:00-18:15 p.m.'),
    ('18:15-18:30pm', '18:15-18:30 p.m.')
)