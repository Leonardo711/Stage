$(function(){
	var from = sessionStorage.getItem('data_id')
    console.log(from)
    var select = "[data-id='" + from + "']"
    $(select).click()
    sessionStorage.setItem('data_id', '')
})