import frappe
from school_management.school_management.services.gradebook import calculate_term_result


@frappe.whitelist()
def ping():
    return "school_management_ok"


@frappe.whitelist()
def calculate_preview(scores, scheme=None):
    return calculate_term_result(scores=scores, scheme=scheme)
