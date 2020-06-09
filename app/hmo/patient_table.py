from flask import url_for
from flask_table import Table, Col, LinkCol


class PatientTable(Table):
    id = Col('Id')
    name = Col('Name')
    age = Col('Age')
    gender = Col('Gender')
    diagnosis = Col('diagnosis')
    hmo_provider = Col('hmo_provider')
    add_services = LinkCol('Add Services', 'hmo.add_services', url_kwargs=dict(id='id'))


class PatientServiceTable(Table):

    id = Col('ID')
    patient = Col('Patient')
    provided_service = Col('Service Provided')
    service_date = Col('Date')
    service_name = Col('Name of Lab Test')
    service_type = Col('Service Type')
    provider_name = Col('Doctor Name')
    provider_source = Col('Name of Hospital')
    cost = Col('Cost of Services')
    allow_sort = True

    def sort_url(self, col_key, reverse=False):
        if reverse:
            direction = 'desc'
        else:
            direction = 'asc'
        return url_for('hmo.all_services', sort=col_key, direction=direction)
