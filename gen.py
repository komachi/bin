#!/usr/bin/env python3
from faker import Faker

faker = Faker()

username = faker.user_name()
name = faker.name()
address = faker.address()
phone = faker.phone_number()
birthdate = faker.date_time_between(start_date='-70y', end_date='-21y')

print(f'{username}\n\n{name}\n\n{birthdate}\n\n{address}\n\n{phone}')
