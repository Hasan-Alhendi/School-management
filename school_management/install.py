import frappe


def after_install():
    """Reserved for initial setup after installing the app."""
    create_roles()


def create_roles():
    roles = [
        "School Admin",
        "School Registrar",
        "School Teacher",
        "School Supervisor",
        "School Principal",
        "School Parent",
        "School Student",
    ]
    for role in roles:
        if not frappe.db.exists("Role", role):
            frappe.get_doc({"doctype": "Role", "role_name": role}).insert(ignore_permissions=True)
    frappe.db.commit()
