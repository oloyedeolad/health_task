from flask import request, render_template, flash

from app import database
from app.forms import PatientForm, PatientServiceForm
from app.models import Patient, PatientService
from . import hmo as hmo_blueprint
from .patient_table import PatientTable, PatientServiceTable


@hmo_blueprint.route('/create', methods=['GET', 'POST'])
def create_patient():
    """
      Create Patient
    """

    form = PatientForm(request.form)
    if request.method == 'GET':
        patients = Patient.query.all()
        print(patients)
        table = data_in_table(patients)
        return render_template('hmo/claim.html', form=form, table=table)
    if request.method == 'POST' and form.validate():
        patient = Patient(name=form.data['name'],
                          age=form.data['age'],
                          gender=form.data['gender'],
                          diagnosis=form.data['diagnosis'],
                          hmo_provider=form.data['hmo_provider'])
        database.session.add(patient)
        database.session.commit()
        flash("Patient creation successful")
        patients = Patient.query.all()
        table = data_in_table(patients)
        return render_template('hmo/claim.html', form=form, table=table)
    return "Bad response"


def data_in_table(data):
    table = PatientTable(data)
    table.border = True
    table.classes = ['table']

    return table


# Save patient services method
def save_changes(patient_services, form):
    patient_services.patient_id = form.data['patient_id']
    patient_services.provided_service = form.data['provided_service']
    patient_services.service_date = form.data['service_date']
    patient_services.service_name = form.data['service_name']
    patient_services.service_type = form.data['service_type']
    patient_services.provider_name = form.data['provider_name']
    patient_services.provider_source = form.data['provider_source']
    patient_services.cost = form.data['cost']
    database.session.add(patient_services)
    database.session.commit()


# End point to create the services
@hmo_blueprint.route('/<int:id>/service', methods=['GET', 'POST'])
def add_services(id):
    patient = Patient.query.filter_by(id=id).first()

    print(patient)
    if patient:
        patient_service = PatientService(patient_id=patient.id)
        form = PatientServiceForm(formdata=request.form, obj=patient_service)
        patient_services = PatientService.query.filter_by(patient_id=patient.id).all()
        table = PatientServiceTable(patient_services)
        table.border = True
        table.classes = ['table table-striped']
        total = sum([patient_service.cost for patient_service in patient_services])
        print(form)
        if request.method == 'POST' and form.validate():
            save_changes(patient_service, form)
            flash('Patient services Added successfully')
        return render_template('hmo/add_services.html', form=form, table=table, total=total)
    return "found noting"


@hmo_blueprint.route('/services', methods=['GET'])
def all_services():
    patient_services = PatientService.query.all()
    print(patient_services)
    table = PatientServiceTable(patient_services)
    table.border = True
    table.classes = ['table table-striped']
    return render_template('hmo/read_claims.html', table=table)
