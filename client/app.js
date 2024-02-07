function predict() {
  var input = $('#image-input')[0].files[0];
  var form_data = new FormData();
  form_data.append('image', input);
  console.log(jQuery);
  $.ajax({
    type: 'POST',
    url: 'http://127.0.0.1:5000/predict',
    data: form_data,
    contentType: false,
    processData: false,
    success: function(response) {
      $('#result').text('The predicted digit is ' + response + '.');
    },
    error: function(error) {
      console.log(error);
      $('#result').text('Please choose a .png or .jpg or .jpeg file.');
    }
  });
}