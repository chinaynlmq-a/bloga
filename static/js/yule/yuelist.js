// $(function(){
  $('.j_clicka').on('click',function(){
    window.location.href = '/yule/details?getUrl='+encodeURIComponent('https:'+$(this).attr('data-link'));
    return false;
  })
  $('.j_clickb').on('click',function(){
    window.location.href = '/yule/pictures?getUrl='+encodeURIComponent('https:'+$(this).attr('data-link'));
    return false;
  })
  
// });