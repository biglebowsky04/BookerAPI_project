"""Методы для проверки ответов выполненных запросов"""
from pydantic import BaseModel
from datetime import date


class Checking():
    """Метод для проверки статус кода"""

    @staticmethod
    def check_status_code(response, status_code):
        assert response.status_code == status_code
        print(f'Успешно. Статус код = {response.status_code}')
        print()

    """Метод для проверки значения атрибутов метода post"""

    @staticmethod
    def check_attr_value_post(response, attribute, expected_value):
        attr_value = response.get(attribute)
        assert attr_value == expected_value
        print(f'Успешно. Значение атрибута {attribute} верно')
        print()

    """Метод для проверки значения атрибутов метода post"""

    @staticmethod
    def check_attr_value_other_methods(response, attribute, expected_value):
        response_json = response.json()
        attr_value = response_json.get(attribute)
        assert attr_value == expected_value
        print(f'Успешно. Значение атрибута {attribute} верно')
        print()


"""Создаем модели, которые описывают структуру ответа методов post/put/patch/get/delete"""


class BookingDates(BaseModel):
    checkin: date
    checkout: date


"""BookingModel может быть использована для put/patch/get/delete"""


class BookingModel(BaseModel):
    firstname: str
    lastname: str
    totalprice: int
    depositpaid: bool
    bookingdates: BookingDates
    additionalneeds: str


"""Используется для проверки респонса в методе post"""


class BookingResponsePost(BaseModel):
    bookingid: int
    booking: BookingModel
