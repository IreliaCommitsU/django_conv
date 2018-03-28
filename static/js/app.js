$(document).foundation()

var checkCount = 0;
$(document).ready(function(){
  //BEHAVOURS FOR SOME CONTROLLERS
  initRestrict();
  label322();
  //pesosSign();
  cropAndLoad();
  trigger_ck('infoExitosa');
  trigger_ck('trigger');
  enterPressed();
  imageControls('modulo_2_5');
  imageControls('modulo_2_5_1');
  imageControls('modulo_2_5_2');
  onlyTwo();
  disableAndUncheck('modulo_2_6');
  disableAndUncheck('modulo_2_7');
  yesNo();
  disableOthers('radio','modulo_2_4','operacion');
  disableOthers('checkbox','modulo_4_1','otro');
  disableOthers('checkbox','modulo_5_1','otro');
  disableOthers('radio','modulo_5_2','si_cuales');
  disableOthers('checkbox','modulo_5_3','otro');
  disableOthers('radio','modulo_5_4','si_cuales');
  disableOthers('checkbox','modulo_6_2','otro');
  disableOthers('checkbox','modulo_6_3','otro');
  verticalsTrigger();
  preg31();
  change_fn_PSW();
// FOR DISPLAYING VIDEOS AS POP-UPS
  $('.popup-youtube, .popup-gmaps').magnificPopup({
    disableOn: 700,
    type: 'iframe',
    mainClass: 'mfp-fade',
    removalDelay: 160,
    preloader: false,
    fixedContentPos: false
  });
  $('.popup-vimeo').magnificPopup({
    disableOn: 700,
    type: 'iframe',
    mainClass: 'mfp-fade',
    removalDelay: 160,
    preloader: false,
    fixedContentPos: false,
    showCloseBtn: false
  });
  $("#id_id_estado").change(function(){
    $("#id_municipio").val('');
    $("#profile_f").submit();
  });
// TOGGLE LOGIN-REG IN LOGIN
  login_reg_handler();
//TOGGLE VIDEOS SECTION
  tutoringVideosControl();
// TOGGLE CANVAS INFO AND VERTICALS
  pageSwapper();
// SUBMIT METHOD FOR LOGIN-REG BUTTONS
  login_reg_submitBtns();
//SUBMIT FOR CHANGE PSW
  changePSW();


  if($(document).width() > 479) //DISABLED VIDEO BECAUSE IT DISAPPEARED, WHEN UPLOADED NEW PLS REACTIVATE BUT CHANGE PROFILE.HTML TO ADDRESS NEW VIDEO
    trigger_ck('introVidFT');
  else
    trigger_ck('phoneClick');
  
  loadVids();
  loadVals();

  redVals();
//INITIALIZATION AN INSTANTIATION FOR DATEPICKERS
  initDatePickers();
  $("#gn-menu")[0] && new gnMenu( document.getElementById( 'gn-menu' ) );
  
  	function mostrar(ev) {
		num = ev.target.selectedIndex; 
		var cop;
		var copi;
		obj = document.getElementById('c'+(num+1));
		cop = document.getElementById('d'+(num+1));
		copi = document.getElementById('e'+(num+1));
		$(".direcciones").hide()
		obj.style.display = 'block';
		document.getElementById("direccionn").innerHTML = cop.innerText;
		document.getElementById("dia2").innerHTML = copi.innerText;
		document.getElementById("dia3").innerHTML = copi.innerText;
	}
  	$('#lugares')[0] && $('#lugares').change(mostrar);
  	
	$('#lugares')[0] && $('#lugares').change();
	
	$(function(){
	    $('#lugares').change(function() {
	        $('#sede2').text( $(this).val() );
	    });
	    
	    $('#horass').change(function() {
	        $('#hora2').text( $(this).val() );
	    });    
	});
  
});
