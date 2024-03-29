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
			"get_query": () => {
				let customer = frappe.query_report.get_filter_value("customer")
				if (!!customer)
					return {
						"filters": {
							"customer": frappe.query_report.get_filter_value("customer"),
						} 
					}
				else
					return {
						"filters": {}
					}

			},
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
			value = `
				<span style="font-size: 10px; margin-left:-5px;" class="indicator-pill ${data.color}">
					<span  style="font-size: 12px; ${data.color}"><b>${value}</b></span>
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
