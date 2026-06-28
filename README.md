# School Management for ERPNext

Custom ERPNext/Frappe app for school management without relying on ERPNext Education.

## الهدف

هذا التطبيق مصمم لإدارة المدارس داخل ERPNext مع منطق خاص مطابق لدفاتر الدرجات والجلاء المدرسي:

- الطلاب وأولياء الأمور.
- الصفوف والشعب والتسجيل السنوي.
- المواد الشرعية والتربوية.
- مخططات توزيع العلامات المرنة حسب المادة والصف.
- دفاتر الدرجات.
- نتائج الفصل الأول والثاني.
- الجلاء المدرسي النهائي.
- الحضور والغياب.
- الجداول الأسبوعية والامتحانات لاحقاً.

## أهم قرار تصميمي

لا نبني جداول منفصلة لكل مادة مثل `Arabic Marks` أو `Math Marks`.

الصحيح:

```text
Assessment Scheme
  └── Assessment Component
        └── Student Component Score
              └── Subject Term Result
                    └── Subject Year Result
                          └── Student Report Card
```

بهذا نستطيع تمثيل:

- اللغة العربية: شفهي، وظائف، نشاط، مذاكرة، امتحان.
- الرياضيات/العقيدة/المعلوماتية: شفهي، وظائف، مذاكرة، امتحان.
- الدعوة والخطابة: شفهي، خطابة عملي، مذاكرة، امتحان عملي، امتحان تحريري.

## التثبيت

من مجلد bench:

```bash
bench get-app https://github.com/Hasan-Alhendi/School-management.git
bench --site your-site.local install-app school_management
bench --site your-site.local migrate
bench restart
```

## التطوير المحلي

```bash
bench new-app school_management
# أو انسخ محتويات هذا المستودع إلى apps/school_management
bench --site your-site.local install-app school_management
```

## الحالة الحالية

هذه النسخة تؤسس الهيكل الأساسي والـ DocTypes الأولية. المرحلة التالية هي بناء شاشة إدخال العلامات Excel-like ثم Print Format للجلاء.
