from django.core.management.base import BaseCommand
from core.models import Journal, Author, Category
import faker
import random
from datetime import datetime as dt

faker.Faker.seed(100)

faker = faker.Faker()

categories = [
    "Sports",
    "Entertainment",
    "Travelling",
    "Business",
    "Fashion"
];

author_names = [faker.name()  for _ in range(1,6)]


class Command(BaseCommand):
    def handle(self, *args, **options):

        for x in range(0, 50):
            title = " ".join(faker.words(random.randint(2, 4)))
            views = random.randint(1,100)
            reviewed = random.randint(0,1) == 1
            author_name = random.choice(author_names)
            published = faker.date_time_between(start_date='-7y', end_date='now')
            category_name = random.choice(categories)
            
            #create the author instance & save to db
            author = Author.objects.get_or_create(name=author_name)

            #create the journal instance
            journal = Journal(
                title=title, 
                author=Author.objects.get(name=author_name),
                published=published,
                views=views,
                reviewed=reviewed
            )
            
            #create the journal instance and save
            journal.save()

            category = Category.objects.get_or_create(name=category_name)

            journal.categories.add(Category.objects.get(name=category_name))
    
        self.stdout.write(self.style.SUCCESS('Data imported sucessfully'))
