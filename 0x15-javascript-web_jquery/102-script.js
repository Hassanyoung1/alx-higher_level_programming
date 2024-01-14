$(function() {
    const url = 'https://www.fourtonfish.com/hellosalut/?';
  
    $('INPUT#btn_translate').click(function() {
      const languageCode = $('INPUT#language_code').val();
      $.get(url, { lang: languageCode }, function(info) {
        $('DIV#hello').html(info.hello);
      });
    });
  });