# 📌 أضف هذا الكود داخل ملف app.py الخاص بك

from datetime import datetime

class Attendance(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    employee_id = db.Column(db.Integer, db.ForeignKey('employee.id'), nullable=False)
    check_in = db.Column(db.DateTime, nullable=True)
    check_out = db.Column(db.DateTime, nullable=True)

@app.route('/checkin/<int:id>')
def checkin(id):
    record = Attendance(employee_id=id, check_in=datetime.now())
    db.session.add(record)
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/checkout/<int:id>')
def checkout(id):
    record = Attendance.query.filter_by(employee_id=id).order_by(Attendance.id.desc()).first()
    if record and not record.check_out:
        record.check_out = datetime.now()
        db.session.commit()
    return redirect(url_for('index'))

class Attendance(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    employee_id = db.Column(db.Integer, db.ForeignKey('employee.id'), nullable=False)
    check_in = db.Column(db.DateTime, nullable=True)
    check_out = db.Column(db.DateTime, nullable=True)

@app.route('/checkin/<int:id>')
def checkin(id):
    record = Attendance(employee_id=id, check_in=datetime.now())
    db.session.add(record)
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/checkout/<int:id>')
def checkout(id):
    record = Attendance.query.filter_by(employee_id=id).order_by(Attendance.id.desc()).first()
    if record and not record.check_out:
        record.check_out = datetime.now()
        db.session.commit()
    return redirect(url_for('index'))
