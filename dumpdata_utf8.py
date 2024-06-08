import io
import os
import django
from django.core.management import call_command

# Set the settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'HOFvidz.settings')

# Initialize Django
django.setup()

# Dump data
with io.open('seed_data.json', 'w', encoding='utf-8') as f:
    call_command('dumpdata', stdout=f)
