// $(function(){
  $('.j_opentURL').on('click',function(){
    window.location.href = '/yule/bizdetail/'+encodeURIComponent($(this).attr('data-link'));
    return false;
  })
// });