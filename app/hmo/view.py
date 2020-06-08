from flask import request, render_template, flash

from app import database
from app.forms import PatientForm
from app.models import Patient
from . import hmo as hmo_blueprint


@hmo_blueprint.route('/create', methods=['GET', 'POST'])
def create_patient():
    """
      Create Patient
    """

    form = PatientForm(request.form)
    if request.method == 'GET':
        patients = Patient.query.all()
        print(patients)
        return render_template('hmo/claim.html', form=form, patients=patients)
    if request.method == 'POST' and form.validate():
        patient = Patient(name=form.data['name'],
                          age=form.data['age'],
                          gender=form.data['gender'],
                          diagnosis= form.data['diagnosis'],
                          hmo_provider=form.data['hmo_provider'])
        database.session.add(patient)
        database.session.commit()
        flash("Patient creation successful")
        patients = Patient.query.all()
        return render_template('hmo/claim.html', form=form, patients=patients)
    return "Bad response"
