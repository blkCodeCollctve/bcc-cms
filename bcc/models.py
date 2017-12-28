import atexit
from wagtail.wagtailcore.models import Page
from wagtail.wagtailcore.models import Page, Orderable
from wagtail.wagtailimages.blocks import ImageChooserBlock
from wagtail.wagtailcore import blocks
from wagtail.wagtailcore.fields import StreamField
from wagtail.wagtailadmin.edit_handlers import StreamFieldPanel
from wagtail.wagtailcore.blocks import URLBlock
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.interval import IntervalTrigger
from bcc.meetup import MEETUP
import config

meetup_api = MEETUP()


class SponsershipBlock(blocks.StructBlock):
    heading = blocks.CharBlock(required=False)
    image = ImageChooserBlock(required=False)
    url = URLBlock(required=False)

    class Meta:
        icon = 'image'


class HomePage(Page):
    sponsers = StreamField([
        ('sponsers', SponsershipBlock())
    ], blank=True)

    content_panels = Page.content_panels + [
        StreamFieldPanel('sponsers')
    ]

    def get_context(self, request):
        context = super(HomePage, self).get_context(request)

        # Add extra variables and return the updated context
        context['events'] = meetup_api.events
        return context

    template = 'index.html'


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
