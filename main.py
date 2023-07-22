from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///patients.db"
db = SQLAlchemy(app)


class Patient(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    date = db.Column(db.String(50), nullable=False)
    contact = db.Column(db.Integer, nullable=True)
    age = db.Column(db.Integer, nullable=True)
    description = db.Column(db.String(500), nullable=True)
    address = db.Column(db.String(250), nullable=False)
    profession = db.Column(db.String(50), nullable=False)
    blood_grp = db.Column(db.String(20), nullable=True)
    guardian_contact = db.Column(db.Integer, nullable=True)
    doctor_name = db.Column(db.String(50), nullable=False)
    payment = db.Column(db.String(100), nullable=False)


with app.app_context():
    db.create_all()


@app.route("/")
def home():
    result = db.session.execute(db.select(Patient).order_by(Patient.name))
    all_patients = result.scalars()
    return render_template("index.html", patients=all_patients)


@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        new_patient = Patient(
            name=request.form["name_p"],
            email=request.form["email"],
            date=request.form["date_p"],
            contact=request.form["phone"],
            age=request.form["age"],
            description=request.form["problem"],
            address=request.form["address"],
            profession=request.form["profession"],
            blood_grp=request.form["blood_grp"],
            guardian_contact=request.form["guardian_contact"],
            doctor_name=request.form["doctor_name"],
            payment=request.form["transaction"]
        )
        db.session.add(new_patient)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template("add.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0")
