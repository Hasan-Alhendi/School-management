frappe.pages['gradebook-entry'].on_page_load = function(wrapper) {
    const page = frappe.ui.make_app_page({
        parent: wrapper,
        title: __('Gradebook Entry'),
        single_column: true
    });

    $(page.body).html(`
        <div class="frappe-card p-4 school-management-gradebook">
            <h3>دفتر الدرجات</h3>
            <p>هذه صفحة أولية. المرحلة التالية: توليد أعمدة العلامات تلقائياً حسب Assessment Scheme.</p>
        </div>
    `);
};
