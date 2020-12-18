import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE','djangodemoproject.settings')

import django
django.setup()

from faker import Faker
from first_app.models import User as U

fake = Faker()

def adduserdata(N):
    for i in range(N):
        fname = fake.first_name()
        lname = fake.last_name()
        eml = fake.email()

        T = U.obejcts.get_or_create(first_name = fname,last_name =lname,Email=eml )[0]

if __name__ == '__main__':
    print("Populating data to first_app")
    adduserdata(20)