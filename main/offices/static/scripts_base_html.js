$(document).ready(function(){
  
    //collapse header after scroll from top script (only for fixed header, you can change that in css (.header -> position: fixed; ))
      $(window).scroll(function(){
        var scroll = $(this).scrollTop();
        
        if(scroll > 1){
          //$('.top').addClass('scrolled');
        }else{
          //$('.top').removeClass('scrolled');
        }
      })
    
  
      var suma = 0;
    
    //2. način racunanja širine svih itema u navbaru
      $(".navbar-item").each(function(index, value){
        var bcr = value.getBoundingClientRect();
        suma = suma + bcr.width;
      }); 
    //2. način
    console.log(suma);
    
    //dio koda koji otvara sidebar (TO DO!)
    $('.hamburger-menu').click(function(){
      $('.sidebar').toggleClass('active');
      $('.navbar-item-wrapper').toggleClass('active');
    })
    //stavlja focus na search input na klik povečala
    $('.search-icon').click(function(){
      $('.search-input').focus();
    });
    
    
    function responsiveNavbar(){
       //0.9 je 90% zbog margina s lijeve i desne strane
      //356 je širina .search-wrappera, 76 je širina collapsaong .search-wrappera
      //širina diva ispod linkova bez search wrappera i margina 5% sa svake strane
      var a = $(window).width() * 0.9 - 356;
      //širina diva ispod linkova bez collapsanog search wrappera i margina 5% sa svake strane
      var b = $(window).width() * 0.9 - 76
     
      
     // console.log(sum);
      //logika za okidanje breakpointa
      //prvi brakepoing smanji search-wrapper
      if(a < suma)
        {
          //drugi breakpoint sakrije linkove
          if(b < suma)
          {
            $('.navbar').addClass('second-breakpoint');
          }
          else{
            $('.navbar').removeClass('second-breakpoint');
            $('.sidebar').removeClass('active');
            $('.navbar-item-wrapper').removeClass('active');
          }
          $('.navbar').addClass('first-breakpoint');
        }
      else
        {
          $('.navbar').removeClass('first-breakpoint');
          
        }
      
      
      };  
    // na kraju koda pozovem funkciju zbog slučaja ako se header otvori u granicama prvog breakpointa, inace search-wrapper ne zna koliko su linkovi široki
    responsiveNavbar()
    
    //funkcija se okida na svaku promjenu širine windowa
    $(window).on('resize', function(){
      responsiveNavbar()
    });
  });