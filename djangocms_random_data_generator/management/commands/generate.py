from django.core.management.base import BaseCommand, CommandError
from djangocms_random_data_generator.data_generator import DataGenerator


class Command(BaseCommand):
    
    def handle(self, *args, **options):
        
        self.stdout.write("Starting data generation")
    
        data_generator = DataGenerator()
        data_generator.start()

