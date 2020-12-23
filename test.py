import requests


BASE = 'http://127.0.0.1:5000/'

print('test table user')
data = {'fullname': 'Алексеев Александр', 'avatar': 'app/tmp/avatar/avatar.jpg', 'birth_date': '2000-12-02',
        'residence_address': 'Красноярск'}

response = requests.put(BASE + 'user', json=data)
print(response.json())

input()
response = requests.post(BASE + 'user/sort_field=fullname')
print(response.json())


input()
response = requests.patch(BASE + 'user/id=6', json={'fullname': 'Илья Петрович'})
print(response.json())

input()

response = requests.delete(BASE + 'user/id=6')
print(response)

input()
response = requests.post(BASE + 'user')
print(response.json())

input()
print('test table telephones')
input()
data_telephones = {'phone_type': 'Городской', 'phone_number': '8-999-999-99-99', 'user_id': 5}

response = requests.put(BASE + 'telephones', json=data_telephones)
print(response.json())

input()
response = requests.post(BASE + 'telephones/sort_field=phone_number')
print(response.json())

input()
response = requests.patch(BASE + 'telephones/id=7', json={'phone_type': 'Мобильный'})
print(response.json())

input()
response = requests.delete(BASE + 'telephones/id=7')
print(response)

input()
response = requests.post(BASE + 'telephones')
print(response.json())

print('test table email_addr')
data_email = {'mail_type': 'Рабочая', 'email': 'mail@mail.ru', 'user_id': 5}

response = requests.put(BASE + 'email', json=data_email)
print(response.json())

input()
response = requests.post(BASE + 'email/sort_field=email')
print(response.json())

input()
response = requests.patch(BASE + 'email/id=7', json={'mail_type': 'Личная'})
print(response.json())

input()
response = requests.delete(BASE + 'email/id=7')
print(response)

input()
response = requests.post(BASE + 'email')
print(response.json())
