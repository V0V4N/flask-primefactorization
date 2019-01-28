from app import app
import unittest


class FactorizationTest(unittest.TestCase):

    # Проверка работы Flask
    def test_app(self):
        tester = app.test_client(self)
        response = tester.get('/', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    # Проверка работы с заведомо верным вводом
    def test_correct_input(self):
        tester = app.test_client(self)
        response = tester.post('/', data=dict(inputNumber=12),
                               follow_redirects=True)
        self.assertIn(b'2*2*3', response.data)

    # Проверка работы с заведомо верным вводом в экспоненциальной форме
    def test_correct_input_scientific_notation(self):
        tester = app.test_client(self)
        response = tester.post('/', data=dict(inputNumber=1.2e1),
                               follow_redirects=True)
        self.assertIn(b'2*2*3', response.data)

    # Проверка работы с заведомо неверным вводом (текст)
    # в реальности такая ситуация вряд ли возникнет в силу валидации на
    # стороне HTML
    def test_incorrect_input_text(self):
        tester = app.test_client(self)
        response = tester.post('/', data=dict(inputNumber="тест"),
                               follow_redirects=True)
        self.assertIn(b'NON-INTEGER INPUT', response.data)

    # Проверка работы с заведомо неверным вводом (число вне области работы
    # алгоритма - 2 <= n <= 1e+21)
    # в реальности такая ситуация вряд ли возникнет в силу валидации на
    # стороне HTML
    def test_incorrect_input_out_of_range(self):
        tester = app.test_client(self)
        response = tester.post('/', data=dict(inputNumber="1e25"),
                               follow_redirects=True)
        self.assertIn(b'INPUT OUT OF RANGE', response.data)


if __name__ == '__main__':
    unittest.main()
