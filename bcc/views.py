import atexit
from django.shortcuts import render
from bcc.meetup import MEETUP
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.interval import IntervalTrigger
import config

meetup_api = MEETUP()


def index(request):
    return render(request, 'index.html', {'events': meetup_api.events})


def updateEvents():
    scheduler = BackgroundScheduler()
    scheduler.start()
    scheduler.add_job(
        meetup_api.get_events,
        trigger=IntervalTrigger(seconds=config.REFRESH_EVENTS),
        id='meetup_update_job',
        name='Update meetup events',
        replace_existing=True)

    # Initial load
    meetup_api.get_events()

    # Shut down the scheduler when exiting the app
    atexit.register(lambda: scheduler.shutdown())


updateEvents()
