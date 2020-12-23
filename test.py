import requests


BASE = 'http://127.0.0.1:5000/'

print('test table user')
data = {'id': 3, 'fullname': 'Петров Иван', 'avatar': 'app/tmp/avatar/avatar.jpg', 'birth_date': '2021-12-02',
        'residence_address': 'Красноярск'}
#
response = requests.put(BASE + 'user', json=data)
print(response.json())
# data_telephones = {'phone_type': 'Городской', 'phone_number': '8-999-999-99-99', 'user_id': 1}
#
# response = requests.put(BASE + 'telephones', json=data_telephones)
# print(response.json())
#
#
# data_email = {'mail_type': 'Личная', 'email': 'mail@mail.ru', 'user_id': 1}
#
# response = requests.put(BASE + 'email', json=data_email)
# print(response.json())
#
# input()
# response = requests.post(BASE + 'user/sort_field=fullname')
# print(response.json())

#
# input()
# response = requests.patch(BASE + 'user/id=1', json={'fullname': 'petuh'})
# print(response.json())

# input()
#
# response = requests.delete(BASE + 'user/id=1')
# print(response)
#
# input()
# response = requests.post(BASE + 'user')
# print(response.json())
#
# input()
# print('test table telephones')
# data_telephones = {'kind': 'gorod', 'phone_number': '8-999-999-99-99', 'user_id': 5}
#
# response = requests.put(BASE + 'telephones', json=data_telephones)
# print(response.json())
#
# input()
# response = requests.post(BASE + 'telephones')
# print(response.json())
#
# input()
# response = requests.patch(BASE + 'telephones/1', json={'kind': 'mobil'})
# print(response.json())
#
# input()
# response = requests.delete(BASE + 'telephones/id=2')
# print(response)
#
# input()
# response = requests.post(BASE + 'telephones')
# print(response.json())

# print('test table telephones')
# data_email = {'type_of_mail': 'job', 'email': 'mail@mail.ru', 'user_id': 5}
#
# response = requests.put(BASE + 'email', json=data_email)
# print(response.json())
#
# input()
# response = requests.post(BASE + 'email')
# print(response.json())
#
# input()
# response = requests.patch(BASE + 'email/id=2', json={'type_of_mail': 'lichnaya'})
# print(response.json())
#
# input()
# response = requests.delete(BASE + 'email/id=2')
# print(response)
#
# input()
# response = requests.post(BASE + 'email')
# print(response.json())
