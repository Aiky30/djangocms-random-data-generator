import random

from django.conf import settings
from django.db import IntegrityError, transaction
from django.utils import timezone

from cms.api import add_plugin, create_page, create_title, publish_page
from cms.models import CMSPlugin, Placeholder, Page, Title


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
                self.empty_db()
                self.generate()

            self.end(False)

        except Exception as err:
            self.end(err)
            raise
        except:
            self.end(True)
            raise

    def end(self, error=False):

        self.end_time = timezone.now()

        import_duration = (self.end_time - self.start_time).total_seconds()

        print("End:%s" % str(self.end_time))
        print("Duration:%s" % import_duration)

        if error:
            print("Error!!!")
            print(error)

    def empty_db(self):
        """
        Empty any entries in the DB!
        """
        CMSPlugin.objects.all().delete()
        Placeholder.objects.all().delete()
        Title.objects.all().delete()
        Page.objects.all().delete()

        return

    def generate(self):

        # Generate pages
        amount_of_pages = range(1, 10)
        amount_of_plugins = range(1, 10)
        languages = settings.LANGUAGES

        for page_index, page_arg in enumerate(amount_of_pages):

            page = None

            for language_index, language in enumerate(languages):

                language_code = language[0]
                language_name = language[1]
                translated_text = settings.GENERATOR_LANGUAGES_TEXT[language_code]

                page_title = "%s-%s" % (language_name, str(page_index))

                # Create a new page or title
                if page is None:
                    page = create_page(page_title, "homepage.html", language_code, published=True)
                else:
                    create_title(language_code, page_title, page)

                # Add the plugins to the page
                placeholder = page.placeholders.get(slot='placeholder_1')
                for plugin in enumerate(range(0, random.choice(amount_of_plugins) )):
                    add_plugin(
                        placeholder=placeholder,
                        plugin_type="TextPlugin",
                        language=language_code,
                        body=translated_text,
                    )
                # Publish the page changes
                page.publish(language_code)

        print("Generate")
        return