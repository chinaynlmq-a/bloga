$('.j_opentURL').on('click',function(){
  window.location.href = '/yule/bizdetail?getUrl='+encodeURIComponent($(this).attr('data-link'));
  return false;
})

$('.j_clicka').on('click',function(){
  var len = $(this).attr('len');
  var url='/yule/details';
  if(len === '4'){
    url = '/yule/pictures'
  }
  window.location.href = url+'?getUrl='+encodeURIComponent('https:'+$(this).attr('data-link'));
  return false;
})