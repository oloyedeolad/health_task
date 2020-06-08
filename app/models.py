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
    name = database.Column(database.String(100), nullable=False, unique=True)
    age = database.Column(database.Integer, nullable=False)
    gender = database.Column(database.Enum("MALE", "FEMALE", name="gender"), nullable=False)
    diagnosis = database.Column(database.TEXT(1000), nullable=False)
    hmo_provider = database.Column(
        database.Enum("HM01", "HM02", "HM03", "HM04", name="hmo_provider"), nullable=False
    )
    patient_services = database.relationship('PatientService', backref='patient', lazy=True)


class PatientService(database.Model):
    __tablename__ = 'patient_services'
    id = database.Column(database.Integer, autoincrement=True, primary_key=True)
    provided_service = database.Column(database.String(255), nullable=False)
    service_date = database.Column(database.Date, nullable=False)
    service_name = database.Column(database.String(100), nullable=False)
    service_type = database.Column(database.String(255), nullable=False)
    provider_name = database.Column(database.String(100), nullable=False)
    provider_source = database.Column(database.String(150), nullable=False)
    cost = database.Column(database.DECIMAL, nullable=False)
    patient_id = database.Column(database.Integer, database.ForeignKey('patient.id'), nullable=False)
