const url = 'http://192.168.33.100:5000/api/v1';


function inputCompaniesHtml(companie) {
	const html = ['<option value="'+companie.id+'">', companie.name, '</option>'];

	return html.join('');
}

function addCompanies(data) {
	const options = [];
	data.forEach(function(companie){
		options.push(inputCompaniesHtml(companie));
	})

	$('select').append(options.join(''));
}

function getCompanies() {
	const request = {
		url: url + '/companies'
	}
	const r = $.ajax(request)

	r.done(function(data) {
		addCompanies(data);
	})

	r.fail(function(jqXHR, textStatus, errorThrown) {
	
	})
}

function init(){
	
}

$(document).ready(init)
