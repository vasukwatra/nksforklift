
// INITIALIZE
  $(document).ready(function(){
    $('.main-carousel').flickity({
      // options
      cellAlign: 'center',
      contain: true,
      draggable: true,
      wrapAround: true,
      prevNextButtons: true,
      fullscreen: true,
      groupCells: true
    });

    // ARROW COLOR
    $('.flickity-button-icon').css('fill','#272727');
  });
