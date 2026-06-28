# ERD - School Management

```text
School Profile
Academic Year -> Academic Term
Grade Level -> School Section -> Student Enrollment -> School Student
School Subject -> Curriculum Subject
Assessment Scheme -> Assessment Component
Gradebook -> Student Component Score -> Subject Term Result -> Student Report Card
```

## أهم فكرة

توزيع العلامات مرن حسب المادة والصف، لذلك يتم الاعتماد على Assessment Scheme و Assessment Component بدلاً من أعمدة ثابتة.
