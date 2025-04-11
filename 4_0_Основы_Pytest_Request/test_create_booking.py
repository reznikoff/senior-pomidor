import requests
import pytest

class TestBooking:
    base_url = "https://restful-booker.herokuapp.com"
    headers = {"Content-Type": "application/json", "Accept": "application/json"}
    json = {"username": "admin", "password": "password123"}

    def get_token(self):
        response = requests.post(f"{self.base_url}/auth", headers=self.headers, json=self.json)
        assert response.status_code == 200, "Ошибка авторизации, статус код не 200"
        token = response.json().get("token")
        assert token is not None, "Токен не найден в ответе"
        return token
