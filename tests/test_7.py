import pytest
import requests
import os
from dotenv import load_dotenv

load_dotenv()

class TestEmployeeApi:
    base_url = "http://5.101.50.27:8000"
    client_token = os.getenv('api_token')

    @pytest.mark.parametrize('data', [{
        "first_name": "Dmytro",
        "last_name": "Kopan",
        "middle_name": "",
        "company_id": 550,
        "email": "alpha@centurion.net",
        "phone": "+38098654321",
        "birthdate": "1900-01-01",
        "is_active": True
    }])
    def test_create_employee(self, data):
        assert requests.post(self.base_url + '/employee/create', json=data).status_code == 200

    @pytest.mark.parametrize('id', [201])
    def test_employee_info(self, id):
        resp = requests.get(self.base_url + f'/employee/info/{id}')
        assert resp.status_code == 200
        assert resp.json()['first_name'] == 'Dmytro'
        assert resp.json()['last_name'] == 'Kopan'
        assert resp.json()['company_id'] == 550
        assert resp.json()['phone'] == "+38098654321"

    @pytest.mark.parametrize('id, data', [(202, {"first_name": "Dmytro69", "phone": "+49987654321", })])
    def test_user_update(self, id, data):
        response = requests.patch(f"{self.base_url}/employee/change/{id}/?client_token={self.client_token}", json=data)
        assert response.json()['detail'] != 'Токен истек'
        assert 200 <= response.status_code < 400
        assert response.json()['first_name'] == 'Dmytro69'
        assert response.json()['phone'] == '+49987654321'
