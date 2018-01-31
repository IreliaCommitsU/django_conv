$(document).foundation()

var checkCount = 0;
$(document).ready(function(){
  //BEHAVOURS FOR SOME CONTROLLERS
  initRestrict();
  label322();
  pesosSign();
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
  $('.popup-youtube, .popup-vimeo, .popup-gmaps').magnificPopup({
    disableOn: 700,
    type: 'iframe',
    mainClass: 'mfp-fade',
    removalDelay: 160,
    preloader: false,
    fixedContentPos: false
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

// JUST DEPRECATED SOON
/*  var div = $("#scrollMenuLogo");
  var pos = div.position();
  $(window).scroll(function () {
    var windowpos = $(window).scrollTop();
    if (windowpos >= 50) {
      div.removeClass("hide");
    }
    else {
      div.addClass("hide");
    }
  });
*/
//INITIALIZATION FOR SIDE MENU (NOT STILL IMPLEMENTED)
  //new gnMenu( document.getElementById( 'gn-menu' ) );

  trigger_ck('introVidFT');
  loadVids();

//INITIALIZATION AN INSTANTIATION FOR DATEPICKERS
  initDatePickers();
});
