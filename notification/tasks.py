from notifier.celery import app as celery_app

@celery_app.task(name='send_notification', ignore_result=True)
def send_notification(user_ids, notification_payload):
	pass