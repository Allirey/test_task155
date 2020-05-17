import os
from celery import Celery
from posts.config import POSTS_CELERY_BEAT_SCHEDULE

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "news_board.settings")

app = Celery("news_board")

app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()

app.conf.beat_schedule = POSTS_CELERY_BEAT_SCHEDULE
