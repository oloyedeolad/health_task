import os
import tempfile

import pytest

from app import database
from application import application


@pytest.fixture
def client():
    db_fd, application.config['DATABASE'] = tempfile.mkstemp()
    application.config['TESTING'] = True
    application.config['DEBUG'] = False

    with application.test_client() as client:
        with application.app_context():
            database.init_app(application)
        yield client

    os.close(db_fd)
    os.unlink(application.config['DATABASE'])


def test_get_patient_page_db(client):
    response = client.get('/hmo/patient')
    assert response.status_code == 200


def create_patient(client, name, age, gender, diagnosis, hmo_provider):
    return client.post('/hmo/patient', data=dict(
        name=name, age=age, gender=gender, diagnosis=diagnosis, hmo_provider=hmo_provider
    ), follow_redirects=True)


def test_create_patient(client):
    res = create_patient(client, 'gbenga', 40, 'MALE', 'All good', 0)
    assert res.status_code == 201

