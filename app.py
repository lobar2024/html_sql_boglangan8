with app.app_context():
    d1 = Departments(name="IT")
    d2 = Departments(name="HR")

    e1 = Employees(firstname="Ali", lastname="Valiyev", department=d1)
    e2 = Employees(firstname="Vali", lastname="Aliyev", department=d2)

    p1 = Projects(title="Website", employee=e1)

    t1 = Tasks(name="Frontend", project=p1)
    t2 = Tasks(name="Backend", project=p1)

    e1.tasks.append(t1)
    e1.tasks.append(t2)

    db.session.add_all([d1, d2, e1, e2, p1, t1, t2])
    db.session.commit()
