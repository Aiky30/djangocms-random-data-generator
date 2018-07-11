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

        print("Started at: %(start_time)s" % {
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

        print("Ended at: %s" % str(self.end_time))
        print("Duration (secs): %s" % import_duration)

        if error:
            print("Error!!!")
            print(error)

    def empty_db(self):
        """
        Empty any entries in the DB!
        """
        print("Emptying DB")
        CMSPlugin.objects.all().delete()
        Placeholder.objects.all().delete()
        Title.objects.all().delete()
        Page.objects.all().delete()

        return

    def generate(self):

        print("Populating DB")

        # Generate pages
        amount_of_pages = range(0, settings.GENERATOR_PAGE_NUMBERS)
        languages = settings.LANGUAGES
        homepage_set = False

        # Use the homepage as the first template
        page_template = 'homepage.html'

        for page_index, page_arg in enumerate(amount_of_pages):

            page = None

            for language_index, language in enumerate(languages):

                language_code = language[0]
                language_name = language[1]
                translated_text = settings.GENERATOR_LANGUAGES_TEXT[language_code]

                page_title = "%s-%s" % (language_name, str(page_index))

                # Create a new page or title
                if page is None:
                    page = create_page(page_title, page_template, language_code, in_navigation=True, published=True)
                else:
                    create_title(language_code, page_title, page)

                # FIXME: Get the placeholders available from the pages
                # Add the plugins to the page
                for placeholder in page.placeholders.all():
                    # Add a text plugin
                    add_plugin(
                        placeholder=placeholder,
                        plugin_type="TextPlugin",
                        language=language_code,
                        body=translated_text,
                    )
                    """
                    for plugin in enumerate(range(0, random.choice(amount_of_plugins) )):
                        add_plugin(
                            placeholder=placeholder,
                            plugin_type="TextPlugin",
                            language=language_code,
                            body=translated_text,
                        )
                    """

                # Publish the page changes
                page.publish(language_code)

                # Make the homepage
                if not homepage_set:
                    page.set_as_homepage()

            # After the first page (homepage is created) create all children
            page_template = 'page.html'
            homepage_set = True

        return