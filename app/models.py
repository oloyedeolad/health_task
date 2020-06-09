import enum
from datetime import datetime

from app import database


class User(database.Model):
    __tablename__ = 'Users'

    id = database.Column(database.Integer, autoincrement=True, primary_key=True)
    name = database.Column(database.String(100), nullable=False, unique=True)
    salary = database.Column(database.Integer, nullable=False)
    time_created = database.Column(database.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return '<User: {}>'.format(self.name)


class HmoEnumProvider(enum.Enum):
    HM01 = 'HM01'
    HM02 = 'HM02'
    HM03 = 'HM03'
    HM04 = 'HM04'


class Patient(database.Model):
    __tablename__ = 'patient'
    id = database.Column(database.Integer, autoincrement=True, primary_key=True)
    name = database.Column(database.String(100), nullable=False, info={'label': 'Full Name'})
    age = database.Column(database.Integer, nullable=False, info={'label': 'Age', 'max': 150})
    gender = database.Column(database.Enum("MALE", "FEMALE", name="gender"), nullable=False, info={'label': 'Gender'})
    diagnosis = database.Column(database.TEXT(1000), nullable=False, info={'label': 'Diagnosis'})
    hmo_provider = database.Column(
        database.Enum("HM01", "HM02", "HM03", "HM04", name="hmo_provider"), nullable=False,
        info={'label': 'HMO Provider'}
    )

    def __str__(self):
        return self.name


class PatientService(database.Model):
    __tablename__ = 'patient_services'
    id = database.Column(database.Integer, autoincrement=True, primary_key=True, info={'label': 'ID'})
    provided_service = database.Column(database.String(255), nullable=False, info={'label': 'Service Provided'})
    service_date = database.Column(database.Date, nullable=False, info={'label': 'Date'})
    service_name = database.Column(database.String(100), nullable=False, info={'label': 'Name of Lab Test'})
    service_type = database.Column(
        database.Enum('Hematology', 'Microbiology', 'Chemical Pathology', 'Histopathology', 'Immunology'
                      ), nullable=False, info={'label': 'Service Type'})
    provider_name = database.Column(database.String(100), nullable=False, info={'label': 'Doctor Name'})
    provider_source = database.Column(database.String(150), nullable=False, info={'label': 'Name of Hospital'})
    cost = database.Column(database.DECIMAL, nullable=False, info={'label': 'Cost of Services'})
    patient_id = database.Column(database.Integer, database.ForeignKey('patient.id'), nullable=False,
                                 info={'label': 'Patient ID'})
    patient = database.relationship(Patient, backref=database.backref("services"), lazy=True)
