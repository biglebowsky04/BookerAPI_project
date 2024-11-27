from utils.http_methods import HttpMethods

"""Методы для тестирования Restful-booker"""

base_url = 'https://restful-booker.herokuapp.com/booking'


class BookerApi():
    """Метод для создания бронирования"""

    @staticmethod
    def create_booking():
        json_post_body = {
            "firstname": "Jim",
            "lastname": "Brown",
            "totalprice": 111,
            "depositpaid": True,
            "bookingdates": {
                "checkin": "2018-01-01",
                "checkout": "2019-01-01"
            },
            "additionalneeds": "Breakfast"
        }
        post_url = base_url
        result_post = HttpMethods.post(post_url, json_post_body)
        print('Был отправлен post запрос:', post_url)
        print('Ответ запроса:', result_post.text)
        print()
        return result_post

    """Метод для проверки, что бронирование создано"""

    @staticmethod
    def get_created_booking(booking_id):
        get_url = base_url + '/' + str(booking_id)

        result_get = HttpMethods.get(get_url)
        print('Был отправлен get запрос:', get_url)
        print('Ответ запроса:', result_get.text)
        print()
        return result_get

    """Метод для изменения информации в бронировании"""

    @staticmethod
    def update_created_booking(booking_id):
        put_url = base_url + '/' + str(booking_id)
        json_put_body = {
            "firstname": "James",
            "lastname": "Brown",
            "totalprice": 111,
            "depositpaid": True,
            "bookingdates": {
                "checkin": "2018-01-01",
                "checkout": "2019-01-01"
            },
            "additionalneeds": "Breakfast"
        }

        result_put = HttpMethods.put(put_url, json_put_body)

        print('Был отправлен put запрос:', put_url)
        print('Ответ запроса:', result_put.text)
        print()
        return result_put

    """Метод для частичного изменения информации в бронировании"""

    @staticmethod
    def partial_update_created_booking(booking_id):
        patch_url = base_url + '/' + str(booking_id)
        json_patch_body = {
            "totalprice": 150,
            "additionalneeds": "Breakfast, Lunch"
        }

        result_patch = HttpMethods.patch(patch_url, json_patch_body)

        print('Был отправлен patch запрос:', patch_url)
        print('Ответ запроса:', result_patch.text)
        print()
        return result_patch

    """Метод для удаления бронирования"""

    @staticmethod
    def delete_created_booking(booking_id):
        delete_url = base_url + '/' + str(booking_id)

        result_delete = HttpMethods.delete(delete_url)

        print('Был отправлен delete запрос:', delete_url)
        print('Ответ запроса:', result_delete.text)
        print()
        return result_delete
