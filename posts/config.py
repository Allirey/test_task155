from celery.schedules import crontab

POSTS_CELERY_BEAT_SCHEDULE = {
    "reset-upvotes": {
        "task": "reset_posts_upvotes",
        "schedule": crontab(minute="0", hour="0",),
    },
}
