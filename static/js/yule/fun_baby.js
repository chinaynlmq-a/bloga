// $(function(){
  $('.j_opentURL').on('click',function(){
    window.location.href = '/yule/babydetail/'+encodeURIComponent($(this).attr('data-link'));
    return false;
  })
// });