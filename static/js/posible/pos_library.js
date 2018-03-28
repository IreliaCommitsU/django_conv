function enterPressed(){
  if($("#pswEnter").length){
    $("#pswEnter").keypress(function(e) {
        // Enter pressed?
        if(e.which == 10 || e.which == 13) {
            $("#loginSubmitButton").click();
        }
    });
  }
}
function cropAndLoad() {
  if(!$('#res')[0]){
    return;
  }
  var $uploadCrop;
  function resetCroppie() { destroyCroppie(); initCroppie(); }

  function destroyCroppie() { $uploadCrop.croppie('destroy'); }

  function initCroppie() {
    $uploadCrop = $('#imgCrop').croppie({
      url: '../img/no_photo.png',
      viewport: {width: 280,height: 250,},
      boundary: { width: 350, height: 280},
      //enforceBoundary: true,
      quality:1
    });
  }

  function readFile(input) {
    if (input.files && input.files[0]) {
            var reader = new FileReader();

            reader.onload = function (e) {
        $('.upload-demo').addClass('ready');
              $uploadCrop.croppie('bind', {
                url: e.target.result
              }).then(function(){
                console.log('jQuery bind complete');
              });

            }

            reader.readAsDataURL(input.files[0]);
        }
        else {
          swal("Sorry - you're browser doesn't support the FileReader API");
      }
  }

  $uploadCrop = $('#imgCrop').croppie({
    url: '../img/no_photo.png',
    viewport: {width: 280,height: 250,},
    boundary: { width: 350, height: 280},
    //enforceBoundary: true,
    quality:1
  });

  $('#upload').on('change', function () {
    resetCroppie();
    readFile(this);
   });
  $('.upload-result').on('click', function (ev) {
    $uploadCrop.croppie('result', {
      type: 'canvas',
      size: 'viewport'
    }).then(function (resp) {
      $('#imgData').attr('value',resp);
      $('#res').attr('src',resp);
    });
  });
}
function toggle_persons_controls(flag){
  if(flag){
    $('#modulo_3_1_2').show();
    $('#modulo_3_1_3').show();
    $('#modulo_3_1_4').show();
    $('#modulo_3_1_5').show();
    $('#modulo_3_1_6').show();
  } else {
    $('#modulo_3_1_2').hide();
    $('#modulo_3_1_3').hide();
    $('#modulo_3_1_4').hide();
    $('#modulo_3_1_5').hide();
    $('#modulo_3_1_6').hide();
  }
}
function toggle_enterprises_controls(flag){
  if(flag){
    $('#modulo_3_2_2').show();
    $('#modulo_3_2_3').show();
  } else {
    $('#modulo_3_2_2').hide();
    $('#modulo_3_2_3').hide();
  }
}
function embedIntro(video) {
  document.getElementById('embedIntro_div').innerHTML = unescape(video.html);
}
function embedMini(video) {
  document.getElementById('embedMini_div').innerHTML = unescape(video.html);
}
function loadVids(){
  var vidIntro = $('#vidInt').val();
  var vidMini = $('#vidMini').val();
  if(vidMini != undefined && vidIntro != undefined) {
    var endpoint = 'https://www.vimeo.com/api/oembed.json';
    var callback1 = 'embedIntro';
    var callback2 = 'embedMini';
    var url1 = endpoint + '?url=' + encodeURIComponent(vidIntro) + '&callback=' + callback1 + '&width=450&height=250';
    var url2 = endpoint + '?url=' + encodeURIComponent(vidMini) + '&callback=' + callback2 + '&width=450&height=250';


  function init() {
    var js1 = document.createElement('script');
    js1.setAttribute('type', 'text/javascript');
    js1.setAttribute('src', url1);
    var js2 = document.createElement('script');
    js2.setAttribute('type', 'text/javascript');
    js2.setAttribute('src', url2);
    document.getElementsByTagName('head').item(0).appendChild(js1);
    document.getElementsByTagName('head').item(0).appendChild(js2);
  }
  init();
  }
}
function readURL(input, ctrl_name) {
    var url = input.value;
    var ext = url.substring(url.lastIndexOf('.') + 1).toLowerCase();
    if (input.files && input.files[0]&& (ext == "gif" || ext == "png" || ext == "jpeg" || ext == "jpg")) {
        var reader = new FileReader();

        reader.onload = function (e) {
            $('#imgZone_'+ctrl_name).attr('src', e.target.result);
        }
        reader.readAsDataURL(input.files[0]);
    }else{
         $('#imgZone_'+ctrl_name).attr('src', '/imgs/projectPics/proyectos/no-img.png');
    }
}
function onlyTwo(){
  if($(':checkbox[name=modulo_2_3]') && $(':checkbox[name=modulo_2_3]:checked').length >= 2){
    $(':checkbox[name=modulo_2_3]').not(':checked').attr('disabled', true);
  }
  $(':checkbox[name=modulo_2_3]').change(function() {
    checkCount = $(':checkbox[name=modulo_2_3]:checked').length;
    if (checkCount >= 2) {
        $(':checkbox[name=modulo_2_3]').not(':checked').attr('disabled', true);
    } else {
        $(':checkbox[name=modulo_2_3]:disabled').attr('disabled', false);
    }
  });
}
function yesNo(){
  if($('input:radio[name=socios]')[0]){
    if($('input:radio[name=socios]:checked').val() == 'si')
      $('.sociosControl').removeClass("hide");
    else
      $('.sociosControl').addClass("hide");
  }
  $('input:radio[name=socios]' ).click(function (ev) {
    if(ev.target.value == 'si'){
      $('.sociosControl').removeClass("hide");
    }
    else{
      $('.sociosControl').addClass("hide");
    }
  });
}
function disableAndUncheck(e_n){
  if($(':checkbox[name='+e_n+']') && $(':checkbox[name='+e_n+']:checked').val()=='no_aplica'){
      $(':checkbox[name='+e_n+']').not(':checked').attr('disabled', true);
  }
  $(':checkbox[name='+e_n+']').change(function(ev){
      if(ev.target.value == 'no_aplica') {
        if(ev.target.checked){
          $(':checkbox[name='+e_n+']').not(ev.target).prop('checked', false);
            $(':checkbox[name='+e_n+']').not(ev.target).attr('disabled', true);
        }else{
          $(':checkbox[name='+e_n+']').attr('disabled', false);
        }
      }
  });
}
function label322(){
  var texto = '<p>* Consulta <a href="http://dof.gob.mx/nota_detalle_popup.php?codigo=5096849" target="_blank"><strong>Diario oficial de la Federación</strong> </a> </p>';
  if($("#modulo_3_2_2 label")[0])
    $(texto).insertBefore("#modulo_3_2_2 p")
}
function disableOthers(type_control, name_control, valiu){
  if($('input:'+type_control+'[name='+name_control+']').length >0 ){
    var has_Otro = false;
    $('input:'+type_control+'[name='+name_control+']:checked').each(function(index){
      if($(this).val()==valiu){
        has_Otro = true;
      }
    });
    if(has_Otro){
      $("#"+name_control+"_otro").fadeIn();
    }else{
      $("#"+name_control+"_otro").hide();
    }
  }
  $('input:'+type_control+'[name='+name_control+']').change(
    function(ev){
      if(ev.target.value == valiu && ev.target.checked){
        $("#"+name_control+"_otro").fadeIn();
      }else
        if(ev.target.value == valiu && !ev.target.checked){
          $("#"+name_control+"_otro").hide();
        }else{
          if(type_control == 'radio'){
            $("#"+name_control+"_otro").hide();
          }
        }
    }
  );
}
function imageControls(ctrl_name){
  $("#id_"+ctrl_name).change(function(){
        readURL(this,ctrl_name);
  });
  $("#id_"+ctrl_name).attr("accept","image/*")
}
function restrictWords(f_name,limit){
  if($("#id_"+f_name)[0]){
    var v = $("#id_"+f_name).val();
    var words = v.length? v.match(/\S+/g).length : 0;
    if (words <=limit) {
        $('#count_'+f_name).text('Quedan: '+(limit-words)+ ' palabras.')
    }
  }
  $("#id_"+f_name).on('keydown', function(e) {
       var words = $.trim(this.value).length ? this.value.match(/\S+/g).length : 0;
       if (words <=limit) {
           $('#count_'+f_name).text('Quedan: '+(limit-words)+ ' palabras.')
       }else{
           if (e.which !== 8) e.preventDefault();
       }
  });
}
function initRestrict(){
  restrictWords('modulo_1_1',70);
  restrictWords('modulo_1_2',70);
  restrictWords('modulo_2_1',15);
  restrictWords('modulo_2_9',100);
  restrictWords('modulo_3_1_6',150);
  restrictWords('modulo_3_2_3',200);
  restrictWords('modulo_3_5',150);
  restrictWords('modulo_4_1_otro',30);
  restrictWords('modulo_4_2',150);
  restrictWords('modulo_4_3',200);
  restrictWords('modulo_5_1_otro',30);
  restrictWords('modulo_5_3_otro',30);
  restrictWords('modulo_5_5',150);
  restrictWords('modulo_6_2_otro',30);
  restrictWords('modulo_6_3_otro',30);
}
function initDatePickers(){
  if($( ".datepicker" ).length){
    $.datepicker.regional['es'] = {
        closeText: 'Cerrar',
        prevText: '< Ant',
        nextText: 'Sig >',
        currentText: 'Hoy',
        monthNames: ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre'],
        monthNamesShort: ['Ene','Feb','Mar','Abr', 'May','Jun','Jul','Ago','Sep', 'Oct','Nov','Dic'],
        dayNames: ['Domingo', 'Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado'],
        dayNamesShort: ['Dom','Lun','Mar','Mié','Juv','Vie','Sáb'],
        dayNamesMin: ['Do','Lu','Ma','Mi','Ju','Vi','Sá'],
        weekHeader: 'Sm',
        dateFormat: 'dd/mm/yy',
        firstDay: 1,
        isRTL: false,
        showMonthAfterYear: false,
        yearSuffix: ''
        };
    $.datepicker.setDefaults( $.datepicker.regional[ "es" ] );
    $( ".datepicker" ).datepicker({
      autoSize: true,
      dateFormat: "yy-mm-dd",
      yearRange: "1940:2018",
      changeMonth: true,
      changeYear: true,
    });
  }
}
function trigger_ck(name_control){
  if($("#"+name_control).length)
    $("#"+name_control)[0].click();
}
function verticalsTrigger(){
  if($( "#id_id_estado" ).length){
    $("#id_id_estado").change(function(ev) {
      var verticals = {'20':'Oaxaca','25':'Sinaloa','2':'Baja California'}
        if(verticals[ev.target.value]!== undefined){
          $(".verticalMSG").removeClass('hide');
        }else{
          $(".verticalMSG").addClass('hide');
        }
    });
  }
}
function pesosSign(){
  if($('#id_modulo_5_4_otro').length){
    $('#id_modulo_5_4_otro').wrap('<div class="grid-x"><div class="cell small-3 medium-3 large-3 money"></div></div>');
    $('<div class="cell small-1 medium-1 large-1 moneySign">$</div>').insertBefore('.money');
  }
}
function login_reg_handler(){
  $("#reg").click(
    function(){
      $(".registerDiv").removeClass( "hide" );
      $(".loginDiv").addClass( "hide" );
    }
  );
  $("#login").click(
    function(){
      $(".loginDiv").removeClass( "hide" );
      $(".registerDiv").addClass( "hide" );
    }
  );
}
function changePSW(){
  $("#cambcontra").click(function(){
    $("#formCC").submit();
  });
}
function login_reg_submitBtns(){
  $("#loginSubmitButton").click(function(){
    var lc = $("#login_correo").val();
    var psE = $("#pswEnter").val();
    if(psE.trim() == "" ||lc.trim() == ""){
      alert('Algún campo se encuentra vacio porfavor verifica');
    }else{
      $("#login_form").submit();
    }
    return false;
  });
  $("#regSubmitButton").click(function(){
    var nom = $("#nombre").val();
    var crr = $("#correo").val();
    var crr_conf = $("#correo_conf").val();
    if(nom.trim() == "" ||crr.trim() == ""||crr_conf.trim() == "" ){
      alert('Algún campo se encuentra vacio porfavor verifica');
    }else{
      if(crr != crr_conf )
        alert('Los correos no coinciden')
      else{
        if(!$('#checkbox1').is(':checked')){
          alert('El aviso de privacidad no está marcado');
        }else{
          if(!$('#checkbox2').is(':checked')){
            alert('Los términos y condiciones no están marcados');
          }else {
              $("#reg_form").submit();
          }
        }

      }
    }
    return false;
  });
}
function tutoringVideosControl(){
  $("#introduc_vid").click(
    function(){
      $("#introduc_div").removeClass( "hide" );
      $("#minic_div").addClass( "hide" );
    }
  );
  $("#mini_class").click(
    function(){
      $("#minic_div").removeClass( "hide" );
      $("#introduc_div").addClass( "hide" );
    }
  );
}
function pageSwapper(){
  $(".togInfo").click(
    function(ev){
      var excepto = "";
      switch (ev.target.id) {
        case "ini":
          excepto = "Inicio";
          $(".infoPosible").css('background-image','url(/static/img/posible.marzo.png)');
          $(".infoSinaloa").css('background-image','url(https://cdn.posible.org.mx/images/vert/sinaloa_v2.png)');
          $(".infoOaxaca").css('background-image','url(https://cdn.posible.org.mx/images/vert/posible.oaxacav2.png)');
          $(".infoBC").css('background-image','url(https://cdn.posible.org.mx/images/vert/posible.bajav2.png)');
        break;
        case "convo":
          excepto = "Convocatoria";
          $(".infoPosible").css('background-image','url(https://cdn.posible.org.mx/images/vert/info_nacionalv5.jpg)');
          $(".infoSinaloa").css({'background-image':'url(https://cdn.posible.org.mx/images/vert/info_sinaloav3.png)','background-size': '100% 100%'});
          $(".infoOaxaca").css('background-image','url(https://cdn.posible.org.mx/images/vert/info_oaxacav3.png)');
          $(".infoBC").css('background-image','url(https://cdn.posible.org.mx/images/vert/info_bcv3.png)');
        break;
        case "vExp":
          excepto = "vCual";
        break;
        case "vOax":
          excepto = "vOAXA";
        break;
        case "vSin":
          excepto = "vSinaloa";
        break;
        case "vBC":
          excepto = "vBajaC";
        break;
      }
      var x = $(".pTabs");
      var keys = [];
      for (var key in x) {
        if (x.hasOwnProperty(key) && !isNaN(key))
          keys.push(key);
      }
      /*BEWARE EACH NEW CATEGORY MUST HAVE IN FIRST CLASS NAME MAPPED IN SWITCH OPTION ABOVE AND MENU TAG IN HEADER*/
      for (var i=0; i<keys.length; i++) {
        if(x[keys[i]].classList[0] != excepto)
          x[keys[i]].classList.add('hide');
        else {
          x[keys[i]].classList.remove('hide');
        }
      }
    }
  );
}
function change_fn_PSW(){
  $("#confirm_cpsw").click(function(){
    $("#form_change").submit();
  });
}

function preg31(){
  if(!$('#id_modulo_3_1_0').is(':checked'))
    toggle_persons_controls(false);
  if(!$('#id_modulo_3_1_1').is(':checked'))
    toggle_enterprises_controls(false);
  $('#id_modulo_3_1_0').change(function(ev){
    toggle_persons_controls(ev.target.checked);
  });
  $('#id_modulo_3_1_1').change(function(ev){
    toggle_enterprises_controls(ev.target.checked);
  });
}

var getUrlParameter = function getUrlParameter(sParam) {
    var sPageURL = decodeURIComponent(window.location.search.substring(1)),
        sURLVariables = sPageURL.split('&'),
        sParameterName,
        i;

    for (i = 0; i < sURLVariables.length; i++) {
        sParameterName = sURLVariables[i].split('=');

        if (sParameterName[0] === sParam) {
            return sParameterName[1] === undefined ? true : sParameterName[1];
        }
    }
};

function loadVals(){
  var fb= getUrlParameter('fb');
  var al = getUrlParameter('al');
  var nw = getUrlParameter('nw');
  var tw = getUrlParameter('tw');
  var ms = getUrlParameter('ms');
  var tec = getUrlParameter('TECNM');
  var ref='web';
  if(fb=='1'){
    ref = 'fb_org_2018';
  }else if(fb=='p'){
    ref = 'fb_pauta_2018';
  }
  if(al=='1'){
    ref = 'aliados_2018';
  }
  if(nw=='1'){
    ref = 'news_2018';
  }
  if(tw=='1'){
    ref = 'tw_2018';
  }
  if(ms=='1'){
    ref = 'messenger_2018';
  }
  if(tec=='1'){
  	ref = 'tecnologicos_2018';
  }
  if($("#m_a").length != 0)
    $("#m_a").val(ref);
}

function checar(ev){
  var control = $(ev.target);
  //if(apellido == ""){
  if(control.val().trim()==''){
      control.css('border','2px solid red');
  }else{
      control.css('border','1px solid #cacaca');
  }
}

function redVals(){
  $('#id_nombre').change(checar);
  $('#id_apellido').change(checar);
  $('#id_municipio').change(checar);
  $('#id_nacimiento').change(checar);
  $('#id_maximo_grado').change(checar);
  $('#id_escuela').change(checar);
  $('#id_tel_1_lada').change(checar);
  $('#id_tel_1').change(checar);
  $('#id_tel_2_lada').change(checar);
  $('#id_tel_2').change(checar);
  $('#id_area_experiencia').change(checar);
  $('#id_email_alt').change(checar);

  $('#id_apellido').change();
  $('#id_nombre').change();
  $('#id_municipio').change();
  $('#id_nacimiento').change();
  $('#id_maximo_grado').change();
  $('#id_escuela').change();
  $('#id_tel_1_lada').change();
  $('#id_tel_1').change();
  $('#id_tel_2_lada').change();
  $('#id_tel_2').change();
  $('#id_area_experiencia').change();
  $('#id_email_alt').change();
  if($('#id_id_estado')[0] && $('#id_id_estado').val().trim()==''){
    $('#id_id_estado').css('border','2px solid red');
  }
}
