
    
    
from django_seed import Seed
from faker import Faker
from .models import Names

fake = Faker()

def seed_db(n):
    seeder = Seed.seeder()
    seeder.add_entity(Names, n, {
        'name': lambda x: fake.name()
    })
    seeder.execute()

