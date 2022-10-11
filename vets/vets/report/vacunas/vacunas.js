// Copyright (c) 2022, Lewin Villar and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["Vacunas"] = {
	"filters": [
		{
			"label": __("Customer"),
			"fieldname": "customer",
			"fieldtype": "Link",
			"options": "Customer",
		},
		{
			"label": __("Patient"),
			"fieldname": "patient",
			"fieldtype": "Link",
			"options": "Patient",
		},
		{
			"label": __("Servicio de Vacunas"),
			"fieldname": "vaccine_service",
			"fieldtype": "Link",
			"options": "Servicio de Vacunas",
		}
	],
	"formatter": function (value, row, column, data, default_formatter) {
		value = default_formatter(value, row, column, data);
		
		if(column.id == "due_date"){
			let color = get_indicator(data.due_date)

			value = `
				<span style="font-size: 10px; margin-left:-5px;" class="indicator-pill ${color}">
					<span  style="font-size: 12px; ${color}"><b>${value}</b></span>
				</span>
			`

		} 
		if(column.id == "days"){
			
			value = `
				<span style="text-align:center">
					<div style="text-align: center">${data.days}</div>
				</span>
			`
		} 

		return value
		
	}
};

function get_indicator(expiration){
	const today = frappe.datetime.now_date();
	const day_diff = frappe.datetime.get_day_diff(expiration, today);
	
	if (day_diff >= 0 && day_diff <= 30)
		return 'blue'
	
	return today > expiration ? 'red': 'green'
}
