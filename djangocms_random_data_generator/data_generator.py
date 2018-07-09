import random

from django.conf import settings
from django.db import IntegrityError, transaction
from django.utils import timezone

from cms.api import create_page, add_plugin, create_title, publish_page


class DataGenerator():

    def __init__(self):
        self.start_time = ""
        self.end_time = ""

    def start(self):

        self.start_time = timezone.now()

        print("Start: %(start_time)s" % {
            'start_time': self.start_time})

        try:
            with transaction.atomic():
                self.generate()

            self.end(False)

        except Exception as err:
            self.end(err)
        except:
            self.end(True)

    def end(self, error=False):

        self.end_time = timezone.now()

        import_duration = (self.end_time - self.start_time).total_seconds()

        print("End:" % self.end_time)
        print("Duration:" % import_duration)

    def generate(self):

        # Generate pages
        amount_of_pages = range(1, 10)
        amount_of_plugins = range(1, 10)
        languages = settings.LANGUAGES

        for page_number in amount_of_pages:

            page = None

            for language in languages:
                language_code = language[0]

                # Create a new page or title
                if page:
                    create_title(language_code, "french inner", page)
                else:
                    page = create_page("inner", "nav_playground.html", language_code, published=True)

                # Add the plugins to the page
                placeholder = page.placeholders.get(slot='body')
                for plugin in enumerate(random.choice(amount_of_plugins)):
                    add_plugin(
                        placeholder=placeholder,
                        plugin_type="PluginWithFKFromModel",
                        language=language_code,
                    )