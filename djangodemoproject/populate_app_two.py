import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE','djangodemoproject.settings')

import django
django.setup()

#FAKE POP script

import random
from AppTwo.models import Topic,Webpage,Accessrecord
from faker import Faker

fakegn = Faker()
topics = ['Search','Social','MarketPlace','News','Games']

def add_topic():
    t = Topic.objects.get_or_create(top_name = random.choice(topics))[0]
    t.save()
    return t

def populate(N=5):
    for i in range(N):

        #get the topics of the entry
        top = add_topic()

        #create the fake data for the entry
        fake_url = fakegn.url()
        fake_date =  fakegn.date()
        fake_name = fakegn.company()

        #Create the new Web Page Entry
        webpg = Webpage.objects.get_or_create(topic = top,name =fake_name ,url = fake_url)[0]

        #create the fake access record entry for that web page
        acc_rec = Accessrecord.objects.get_or_create(name = webpg ,date=fake_date)[0]

if __name__ == '__main__':
    print("Populating data")
    populate(20)