import unittest
import subprocess
import sys

class TestApp(unittest.TestCase):
    def run_app(self, *args):
        cmd = [sys.executable, 'app.py', 'get_tpl'] + list(args)
        result = subprocess.run(cmd, capture_output=True, text=True)
        print('ARGS:', args)
        print('STDOUT:', result.stdout)
        print('STDERR:', result.stderr)
        return result.stdout.strip()

    def test_user_data(self):
        res = self.run_app('--login=vasya@pukin.ru', '--tel=+7 903 123 45 78')
        self.assertEqual(res, 'Данные пользователя')

    def test_order_form(self):
        res = self.run_app('--customer=Иван', '--order_id=123', '--дата_заказа=2024-06-01', '--contact=+7 999 111 22 33')
        self.assertEqual(res, 'Форма заказа')

    def test_extra_fields(self):
        res = self.run_app('--login=vasya@pukin.ru', '--tel=+7 903 123 45 78', '--extra=123')
        self.assertEqual(res, 'Данные пользователя')

    def test_not_found(self):
        res = self.run_app('--foo=bar')
        self.assertEqual(res, '{"result": "not found"}')

    def test_order_form_date(self):
        res = self.run_app('--customer=John Smith', '--order_id=123', '--дата_заказа=27.05.2025', '--contact=+7 111 222 33 44')
        self.assertEqual(res, 'Форма заказа')

    def test_proba(self):
        res = self.run_app('--f_name1=vasya@pukin.ru', '--f_name2=27.05.2025')
        self.assertEqual(res, 'Проба')

if __name__ == '__main__':
    unittest.main() 