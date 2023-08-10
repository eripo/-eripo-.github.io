$(function(){
  $.ajax({
      url: 'ForDigitalText.py',
      type: 'get',
      data: '送信メッセージ'
  }).done(function(data){
      console.log(data);
      });
  }).fail(function(){
      console.log('failed');
  });


