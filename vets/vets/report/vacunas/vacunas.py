# Copyright (c) 2022, Lewin Villar and contributors
# For license information, please see license.txt

import frappe

from frappe import _
from frappe.utils import add_days, cint
from pypika import CustomFunction, Criterion, Query, Field, functions as fn


def execute(filters=None):
	return get_columns(), get_data(filters)

def get_columns():
		return [
			{
				"label": _("Encounter"),
				"fieldname": "encounter",
				"fieldtype": "Link",
				"options": "Patient Encounter",
				"width": 165,
			},
			{
				"label": _("Customer"),
				"fieldname": "customer",
				"fieldtype": "Link",
				"options": "Customer",
				"width": 220,
			},
			{
				"label": _("Patient"),
				"fieldname": "patient",
				"fieldtype": "Link",
				"options": "Patient",
				"width": 150,
			},
			{
				"label": _("Servicio de Vacunas"),
				"fieldname": "vaccine_service",
				"fieldtype": "Link",
				"options": "Servicio de Vacunas",
				"width": 220,
			},
			{
				"label": _("Date"),
				"fieldname": "date",
				"fieldtype": "Date",
				"width": 100,
			},
			{
				"label": _("Days"),
				"fieldname": "days",
				"fieldtype": "Int",
				"width": 60,
			},
			{
				"label": _("Expiration"),
				"fieldname": "due_date",
				"fieldtype": "Date",
				"width": 120,
			}
		]
	

def get_data(filters):
	Encounter = frappe.qb.DocType('Patient Encounter')
	Vaccine = frappe.qb.DocType('Vacuna')
	Patient = frappe.qb.DocType('Patient')
	Customer = frappe.qb.DocType('Customer')
	
	conditions  = [ Encounter.docstatus == 1 ]

	if filters.get("customer"):
		conditions.append(Patient.customer == filters.get("customer"))

	if filters.get("patient"):
		conditions.append(Encounter.patient == filters.get("patient"))

	if filters.get("vaccine_service"):
		conditions.append(Vaccine.naming_series == filters.get("vaccine_service"))

	results = frappe.qb.from_(Encounter).join(Vaccine).on(
		Encounter.name == Vaccine.parent
	).join(Patient).on(
		Encounter.patient == Patient.name
	).join(Customer).on(
		Patient.customer == Customer.name
	).select(
		Encounter.name.as_('encounter'),
		Customer.name.as_('customer'),
		Patient.name.as_('patient'),
		Vaccine.naming_series.as_('vaccine_service'),
		Encounter.encounter_date.as_('date'),
		Vaccine.repetir_en.as_('days'),

	).where(
		Criterion.all(conditions)
	).orderby(Encounter.name, Vaccine.naming_series).run(as_dict=True)
 
	data = list()
 
	print(results)
 
	for row in results:
		row.due_date = add_days(row.date, cint(row.days))
		data.append(row)
  
	return data