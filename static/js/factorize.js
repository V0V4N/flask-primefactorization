$(function(){
	$('#btnFactorize').click(function(){
		
		$.ajax({
			url: '/',
			data: $('form').serialize(),
			type: 'POST',
			success: function(response){
				result = response.replace(/"/g, '');  // удаление кавычек из полученных данных
				document.getElementById("resultNumber").value = result;  // вывод данных в поле результата
			}
		});
	});
});