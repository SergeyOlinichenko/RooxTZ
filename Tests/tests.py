import unittest
from app import app


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.server = app.test_client()

    # Проверка действительного Id возвращающего json с полным набором данных
    def test_UserIdIsFound(self):
        response = self.server.get('/user?id=1')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, b'{"id": "1", "firstName": "Ivan", "secondName": "Petrov"}')

    # Проверка действительного Id возвращающего json с набором данных без фамилии
    def test_UserWithoutFirstName(self):
        response = self.server.get('/user?id=2')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, b'{"id": "2", "firstName": "Petr", "secondName": ""}')

    # Проверка действительного Id возвращающего json с набором данных без имени
    def test_UserWithoutSecondName(self):
        response = self.server.get('/user?id=3')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, b'{"id": "3", "firstName": "", "secondName": "Alexeev"}')

    # Проверка действительного Id возвращающего json без данных пользователя
    def test_UserWithoutName(self):
        response = self.server.get('/user?id=4')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, b'{"id": "4", "firstName": "", "secondName": ""}')

    # Проверка недействительного Id без значения
    def test_UserIdIsEmpty(self):
        response = self.server.get('/user?id=')
        self.assertEqual(response.data, b'Id is empty')

    # Проверка недействительного вызова метода без параметра Id
    def test_UserIdIsNotFound(self):
        response = self.server.get('/user')
        self.assertEqual(response.data, b'Id is none')

    # Проверка недействительного вызова метода с некорректным Id
    def test_UserIdIsInvalid(self):
        response = self.server.get('/user?id=something')
        self.assertEqual(response.data, b'Id is not found')


if __name__ == '__main__':
    unittest.main()
