const url = 'http://192.168.33.100:5001/api/v1';


function inputCompaniesHtml(companie) {
	const html = ['<option value="'+companie.company_id+'">', companie.name, '</option>'];

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

function htmlProducts(product) {
  console.log(product);
  const html = ['<tr>',
                '<td>',product.name,'</td>', 
                '<td><input type="number" data-id="'+product.product_id+'"></td>',
                '<td>','<button type="submit" class="btn btn-primary mb-2">Add</button>','</td>',
                '</tr>']

  return html.join('');
}

function addProducts(products) {
  products.forEach(function(product){
    $('TBODY').append(htmlProducts(product));
  })
}

function getProducts(company_id) {
  const request = {
    url: url + '/company/'+company_id+'/products'
  }
  const r = $.ajax(request);

  r.done(function(data) {
    $('TBODY').html('');
    addProducts(data);
  })

  r.fail(function(data) {

  })
}

function init(){
  console.log('init');
  getCompanies();
}

$(document).on('change', 'SELECT', function(){
  console.log($(this).val());
  getProducts($(this).val());
});

$(document).ready(init);
