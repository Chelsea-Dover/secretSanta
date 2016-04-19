/**
 * Created by Chelsea on 4/18/16.
 */


$(window).bind('resize', function () {
      if($(window).width() < 900){
          $(' #mainBody ').fadeOut();
    }else{
        $(' #mainBody ').fadeIn();

}});

