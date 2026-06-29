FORMAT_NAME = 'x'

def execute():
    import frappe
    doc = frappe.new_doc('Print Format')
    doc.name = FORMAT_NAME
    doc.doc_type = 'Student Report Card'
    doc.module = 'School Management'
    doc.print_format_type = 'Jinja'
    doc.custom_format = 1
    doc.html = '<div>x</div>'
    doc.disabled = 0
    return FORMAT_NAME
