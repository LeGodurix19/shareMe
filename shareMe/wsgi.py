from django.core.wsgi import get_wsgi_application
import os
from dotenv import load_dotenv
load_dotenv()

os.environ.setdefault('DJANGO_SETTINGS_MODULE', os.getenv('PROJECT_NAME') + '.settings')
application = get_wsgi_application()
