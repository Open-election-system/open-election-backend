from faker import Faker
import random
import requests
import string
import json


class DataPoster:

    API = 'https://lyrical-amulet-276713.ew.r.appspot.com/api/1/'

    names = ['Аліна', 'Оксана', 'Марина', 'Антон', 'Остап', 'Михайло', 'Юлія', 'Анастасія', 'Олег', 'Віталій', 'Максим']
    surnames = ['Кузів', 'Петренко', 'Іваненко', 'Мельник', 'Бойко', 'Ковальчук', 'Лисенко', 'Мазур', 'Хоменко', 'Гончар', 'Бондарчук']
    email_names = ['alina', 'oksana', 'maryna', 'anton', 'ostap', 'mykhailo', 'yulia', 'nastya', 'oleg', 'vitalii', 'maksym']
    email_surnames = ['kysiv', 'petrenko', 'ivanenko', 'melnyk', 'boyko', 'kovalchuk', 'lysenko', 'mazur', 'homenko', 'honchar', 'bondarchuk']
    emails = ['@gmail.com', '@ukr.net', '@yahoo.com', '@yandex.ru']

    districts = ['Сихівський', 'Майорівка', 'Галицький', 'Франківський', 'Залізничний', 'Личаківський', 'Шекченківський']
    cities = ['Львів', 'Київ', 'Одеса', 'Тернопіль', 'Запоріжжя', 'Івано-Франківськ', 'Миколаїв', 'Чернігів', 'Чернівці', 'Стрий', 'Дрогобич']
    regions = ['Львівська', 'Київська', 'Одеська', 'Тернопільська', 'Запорізька', 'Івано-Франківська', 'Миколаївська', 'Чернігівська', 'Чернівецька', 'Львівська', 'Львівська']

    organizations = ['Студент', 'Львівська політехніка', 'Університет ім. Франка', 'Медичний університет', 'Міська рада']

    el_name1 = ['президента ', 'голови ', 'відповідального щодо ', 'депутата ']
    el_name2 = ['карантину', 'університету', 'студради', 'екології', 'інтернету', 'інстаграму']

    lorem_ipsum = ['Lorem ipsum dolor sit amet consectetur adipiscing elit.', 'Ut in magna ac ex elementum placerat.', 'Quisque molestie dui nec eleifend.',
              'Vivamus aliquam odio id nibh bibendum vulputate.', 'Aenean ut sem tincidunt gravida sapien varius porta neque.', 'Integer a finibus enim ut blandit turpis.',
              'Donec nec dapibus libero.', 'Vivamus quis ipsum tortor.', 'Sed ultrices risus vitae malesuada bibendum turpis elit aliquam ex facilisis.']

    records_count = 30

    def generate_user(self, iter):
        i_name = random.randint(0, len(self.names) - 1) 
        i_surname = random.randint(0, len(self.surnames) - 1)
        name = self.names[i_name]
        surname = self.surnames[i_surname]
        email = str(self.email_names[i_name]) + '.' + str(self.email_surnames[i_surname]) + str(iter) + self.emails[random.randint(0, len(self.emails) - 1)]
        password = ''
        range_pass = random.randint(5, 15)
        for i in range(range_pass):
            password += random.choice(string.ascii_letters)
        age = random.randint(10, 70)
        ident_code = random.randint(100000000, 999999999)
        organization = self.organizations[random.randint(0, len(self.organizations) - 1)]
        district = self.districts[random.randint(0, len(self.districts) - 1)]
        i_city = random.randint(0, len(self.cities) - 1)
        city = self.cities[i_city]
        region = self.regions[i_city]

        user = {'email': email, 'password': password}
        user_info = {'age': age, 'identification_code': ident_code, 'name': name, 'surname': surname}
        organization = {'organization': organization}
        location = {'district': district, 'city': city, 'region': region}
        post_user = {'user': user, 'user_info': user_info, 'organization': organization, 'location': location}
        return post_user


    def generate_election(self):
        name = 'Вибір ' + self.el_name1[random.randint(0, len(self.el_name1) - 1)] + self.el_name2[random.randint(0, len(self.el_name2) - 1)]
        description = self.lorem_ipsum[random.randint(0, len(self.lorem_ipsum) - 1)]
        age_from = random.randint(10, 18)
        age_to = age_from + random.randint(5, 70)
        votes_number = int(str(random.randint(1, 10)) + '00')
        reatract = bool(random.randint(0, 1))
        start = random.randint(100000, 200000)
        end = start + random.randint(50000, 200000)
        organization = self.organizations[random.randint(0, len(self.organizations) - 1)]

        election = {'name': name, 'description': description}
        restrictions = {'age_from': age_from, 'age_to': age_to, 'votes_number': votes_number, 'reatract': reatract, 'start': start, 'end': end, 'organization': organization}
        post_election = {'election': election, 'restrictions': restrictions, 'options': self.generate_options()}
        return post_election

    def generate_options(self):
        amount = random.randint(5, 15)
        options = []
        for i in range(amount):
            opt_name = 'Кандидат №' + str(i+1)
            opt_description = 'Опис виборчої програми кандидата №' + str(i+1)
            options.append({'name': opt_name, 'description': opt_description})
        return options
    

    def post_users(self, data):
        print(requests.post(url='https://lyrical-amulet-276713.ew.r.appspot.com/api/1/users', json=data))

    def post_elections(self, data):
        print(requests.post(url='https://lyrical-amulet-276713.ew.r.appspot.com/api/1/elections', json=data))


if __name__ == '__main__':
        data_poster = DataPoster()
        for i in range(data_poster.records_count):
            post_user = data_poster.generate_user(i)
            data_poster.post_users(post_user)
        # for i in range(data_poster.records_count):
        #     post_election = data_poster.generate_election()
        #     data_poster.post_elections(post_election)
        print("All data posted")
    