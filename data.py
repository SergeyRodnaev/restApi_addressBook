import requests

BASE = 'http://127.0.0.1:5000/'

user_data = [
    {'fullname': 'Петров Иван', 'avatar': 'app/tmp/avatar/avatar.jpg', 'birth_date': '1972-02-12',
     'residence_address': 'Красноярск'},
    {'fullname': 'Иванов Иван', 'avatar': 'app/tmp/avatar/avatar.jpg', 'birth_date': '1984-11-10',
     'residence_address': 'Москва'},
    {'fullname': 'Цветков Сергей', 'avatar': 'app/tmp/avatar/avatar.jpg', 'birth_date': '1991-04-21',
     'residence_address': 'Назарово'},
    {'fullname': 'Духовкин Алексей', 'avatar': 'app/tmp/avatar/avatar.jpg', 'birth_date': '1986-10-13',
     'residence_address': 'Иркутск'},
    {'fullname': 'Стрижов Антон', 'avatar': 'app/tmp/avatar/avatar.jpg', 'birth_date': '1999-06-04',
     'residence_address': 'Красноярск'}
]

for data in user_data:
    requests.put(BASE + 'user', json=data)
print('The user table has been filled')

telephone_data = [
    {'phone_type': 'Мобильный', 'phone_number': '8-999-963-12-21', 'user_id': 1},
    {'phone_type': 'Городской', 'phone_number': '225-12-11', 'user_id': 1},
    {'phone_type': 'Мобильный', 'phone_number': '8-963-255-48-49', 'user_id': 2},
    {'phone_type': 'Мобильный', 'phone_number': '8-121-236-55-74', 'user_id': 3},
    {'phone_type': 'Городской', 'phone_number': '436-11-99', 'user_id': 4},
    {'phone_type': 'Мобильный', 'phone_number': '8-999-998-98-99', 'user_id': 5},
]

for data in telephone_data:
    requests.put(BASE + 'telephones', json=data)
print('The telephone table has been filled')

email_data = [
    {'mail_type': 'Личная', 'email': 'petrovIvan@mail.ru', 'user_id': 1},
    {'mail_type': 'Рабочая', 'email': 'petrovIvanJob@mail.ru', 'user_id': 1},
    {'mail_type': 'Рабочая', 'email': 'ivanovIvan@mail.ru', 'user_id': 2},
    {'mail_type': 'Личная', 'email': 'cvetkovSerg@mail.ru', 'user_id': 3},
    {'mail_type': 'Рабочая', 'email': 'duhovkinAlex@mail.ru', 'user_id': 4},
    {'mail_type': 'Личная', 'email': 'strijovAnton@mail.ru', 'user_id': 5},

]

for data in email_data:
    requests.put(BASE + 'email', json=data)
print('The email_addr table has been filled')
