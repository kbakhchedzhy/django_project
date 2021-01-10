import os

from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djangoProject.settings')

app = Celery('Django')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()


@app.task(bind=True, queue='celery')
def first_task(self):
    return 120
