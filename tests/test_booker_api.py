import pytest

from utils.api import BookerApi
from utils.checking import Checking
from utils.checking import BookingResponsePost, BookingModel

"""Создание, обновление и удаление бронирования"""


class TestCreateBooking():

    def test_create_new_booking(self):
        print('Создание нового бронирования')
        result_post = BookerApi.create_booking()
        Checking.check_status_code(result_post, 200)

        """для проверки структуры ответа и типа данных передаем ответ
        в метод model_validate"""
        BookingResponsePost.model_validate(result_post.json())

        booking = result_post.json().get('booking')
        Checking.check_attr_value_post(booking, 'firstname', 'Jim')

        response_body_post = result_post.json()
        booking_id = response_body_post.get('bookingid')

        print('Проверяем, что новое бронирование создано')
        result_get = BookerApi.get_created_booking(booking_id)
        Checking.check_status_code(result_get, 200)
        BookingModel.model_validate(result_get.json())

        print('Обновить информацию созданного бронирования')
        result_put = BookerApi.update_created_booking(booking_id)
        Checking.check_status_code(result_put, 200)
        BookingModel.model_validate(result_put.json())
        Checking.check_attr_value_other_methods(result_put, 'firstname', 'James')

        print('Проверяем, что метод put отработал и информация изменилась')
        result_get = BookerApi.get_created_booking(booking_id)
        Checking.check_status_code(result_get, 200)
        BookingModel.model_validate(result_get.json())
        Checking.check_attr_value_other_methods(result_get, 'firstname', 'James')

        print('Частично обновить информацию созданного бронирования')
        result_patch = BookerApi.partial_update_created_booking(booking_id)
        Checking.check_status_code(result_patch, 200)
        BookingModel.model_validate(result_patch.json())
        Checking.check_attr_value_other_methods(result_patch, 'totalprice', 150)

        print('Проверяем, что метод patch отработал и информация изменилась')
        result_get = BookerApi.get_created_booking(booking_id)
        Checking.check_status_code(result_get, 200)
        BookingModel.model_validate(result_get.json())
        Checking.check_attr_value_other_methods(result_patch, 'totalprice', 150)

        print('Удаляем бронирование')
        result_delete = BookerApi.delete_created_booking(booking_id)
        Checking.check_status_code(result_delete, 201)

        print('Проверяем, что метод delete отработал и информация удалилась')
        result_get = BookerApi.get_created_booking(booking_id)
        Checking.check_status_code(result_get, 404)
