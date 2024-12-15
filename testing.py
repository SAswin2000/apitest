import json

import pytest

from fastapi.testclient import TestClient

from app.main import app

 

@pytest.fixture

def input_data():

    with open('tests/input.json') as f:

        return json.load(f)

 
 

@pytest.fixture

def client():

    with TestClient(app) as client:

        yield client

 

def test_movement_api(client, input_data):

    # Send a POST request to /api/move with JSON input

    response = client.post(

        '/stats/',

        json={'input_data': input_data}

    )

   

    # Check if the status code is 200 (OK)

    assert response.status_code == 200

   

    # Parse the JSON response

    result = response.json()

   

    # Assertions based on the expected behavior

    assert result['status'] == 'success'

    assert result['movement_type'] == input_data["movement_type"]

    assert result['speed'] == input_data["speed"]

 

def test_speed_exceeds_maximum(client, input_data, config_data):

    # Modify input data to exceed max speed

    input_data['speed'] = 30

    response = client.post(

        '/api/move',

        json={'input_data': input_data}

    )

   

    assert response.status_code == 200

    result = response.json()

   

    # Expect an error when speed exceeds maximum

    assert result['status'] == 'error'

    assert result['message'] == "Speed exceeds maximum limit"