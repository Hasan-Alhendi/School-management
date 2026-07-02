FORMAT_NAME = 'صحيفة الطالب - الجلاء الرسمي'
DOCTYPE = 'Student Report Card'


def execute():
    import frappe
    html_path = frappe.get_app_path('school_management', 'reporting', 'official_student_report_card.html')
    with open(html_path, 'r', encoding='utf-8') as f:
        html = f.read()

    if frappe.db.exists('Print Format', FORMAT_NAME):
        doc = frappe.get_doc('Print Format', FORMAT_NAME)
    else:
        doc = frappe.new_doc('Print Format')
        doc.name = FORMAT_NAME

    doc.doc_type = DOCTYPE
    doc.module = 'School Management'
    doc.print_format_type = 'Jinja'
    doc.custom_format = 1
    doc.html = html
    doc.disabled = 0

    if doc.meta.has_field('standard'):
        doc.standard = 'No'
    if doc.meta.has_field('orientation'):
        doc.orientation = 'Landscape'
    if doc.meta.has_field('margin_top'):
        doc.margin_top = 0
    if doc.meta.has_field('margin_bottom'):
        doc.margin_bottom = 0
    if doc.meta.has_field('margin_left'):
        doc.margin_left = 0
    if doc.meta.has_field('margin_right'):
        doc.margin_right = 0

    if doc.is_new():
        doc.insert(ignore_permissions=True)
    else:
        doc.save(ignore_permissions=True)

    frappe.db.commit()
    return doc.name
