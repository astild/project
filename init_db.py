from tinydb import TinyDB

# Явно указываем encoding при открытии файла
import io
with io.open('forms_db.json', 'w', encoding='utf-8') as f:
    f.write('')

db = TinyDB('forms_db.json')
db.truncate()
db.insert({
    "name": "Данные пользователя",
    "login": "email",
    "tel": "phone"
})
db.insert({
    "name": "Форма заказа",
    "customer": "text",
    "order_id": "text",
    "дата_заказа": "date",
    "contact": "phone"
})
db.insert({
    "name": "Проба",
    "f_name1": "email",
    "f_name2": "date"
})
print('База forms_db.json создана') 