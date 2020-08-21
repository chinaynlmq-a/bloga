// $(function(){
  $('.j_opentURL').on('click',function(){
    window.location.href = '/yule/bizdetail?getUrl='+encodeURIComponent($(this).attr('data-link'));
    return false;
  })
// });