import json
import pytest
from fastapi.testclient import TestClient
from app.main import app

@pytest.fixture
def input_data():
    # Sample input data to test the stat function
    return {
        "data": [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]  # Example dataset
    }

@pytest.fixture
def client():
    with TestClient(app) as client:
        yield client

def test_movement_api(client, input_data):
    # Send a POST request to /stats/ with the input data
    response = client.post(
        '/stats/',  # Assuming your FastAPI endpoint is '/stats/'
        json={'input_data': input_data}
    )

    # Check if the status code is 200 (OK)
    assert response.status_code == 200

    # Parse the JSON response
    result = response.json()

    # Assertions based on the expected behavior
    assert "meanval" in result
    assert "medianval" in result
    assert "IQR" in result
    assert "Lowerlimit" in result
    assert "upperlimit" in result
    assert "stdlimits" in result

    # Compare the returned values with the expected ones
    assert result["meanval"] == 85.76
    assert result["medianval"] == 89.5
    assert result["IQR"] == 38.25
    assert result["Lowerlimit"] == 9.875
    assert result["upperlimit"] == 162.875
    assert result["stdlimits"]["1_std_limits"] == [57.50433862037556, 114.01566137962445]
    assert result["stdlimits"]["2_std_limits"] == [29.248677240751128, 142.27132275924887]
    assert result["stdlimits"]["3_std_limits"] == [0.9930158611266933, 170.52698413887333]

def test_invalid_data(client):
    # Send a POST request with invalid input (e.g., non-numeric data)
    response = client.post(
        '/stats/',
        json={'input_data': {"data": ["a", "b", "c"]}}  # Invalid data
    )

    # Check if the status code is 422 Unprocessable Entity (for invalid input)
    assert response.status_code == 422
    assert "detail" in response.json()
