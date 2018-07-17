from django.conf import settings
from django.utils.translation import ugettext as _
from django.utils import translation


# TODO: https://cloud.google.com/translate/docs/reference/translate
"""

GENERATOR_LANGUAGES_TEXT = {}

_english_sample_text = "Lorem ipsum dolor sit amet, put on her trial to be expanded on, or the obstinacy of no, it says to the contentions them. Even with the force seen him since the world to establish command it to say it. In order that none of the books of which the first, but not to tritani albucius, when an animal by the time of an. With these Zril be explained to him, and do not seek to know whether all of the top. But neither of these sensitivity."

for language_code, language_name in settings.LANGUAGES:

    # Activate the language
    translation.activate(language_code)

    with translation.override(language_code):
        # Create the translated lorem ipsum
        GENERATOR_LANGUAGES_TEXT[language_code] = translation.ugettext(_english_sample_text)
"""

# FIXME: Use the django / python language utility to translate on the fly!!!
GENERATOR_LANGUAGES_TEXT = {
    'en': 'Lorem ipsum dolor sit amet, put on her trial to be expanded on, or the obstinacy of no, it says to the contentions them. Even with the force seen him since the world to establish command it to say it. In order that none of the books of which the first, but not to tritani albucius, when an animal by the time of an. With these Zril be explained to him, and do not seek to know whether all of the top. But neither of these sensitivity.',
    'de': 'Lorem ipsum dolor sit amet, auf ihrem Gericht gestellt werden erweitert, oder die Hartnäckigkeit nicht, sagt es das Vorbringen sie. Auch mit der Kraft ihn seit der Welt gesehen Befehl zu schaffen es, es zu sagen. Damit keines der Bücher, von denen die ersten, aber nicht albucius tritani, wenn ein Tier zum Zeitpunkt der ein. Mit diesem Zril ihn erklärt werden, und versuche nicht, ob alle oben zu kennen. Aber keiner dieser Empfindlichkeit.',
    'ng': 'Awọn ẹya ara ẹrọ ni atejade, wipe awọn lilo ti a ọmọ ninu awọn miiran. Fun ko ani gbogbo ti kọọkan ni, ti o ti o corrupts awọn ile-ti wa ni jọ pọ nwọn si korira o, fun apẹẹrẹ, meji tijoba si awọn ise ti akọkọ. Mi àdánù consulate ati ki o gbà o pẹlu ọtá bi. Pẹlu awọn wọnyi, dignissim, awọn miiran ti irin, nwọn si wà mnesarchum beere boya o jẹ, lati duis ti awọn ọta. Sugbon ma ọlọgbọn lati iwe.',
    'ag': 'Awọn ẹya ara ẹrọ ni atejade, wipe awọn lilo ti a ọmọ ninu awọn miiran. Fun ko ani gbogbo ti kọọkan ni, ti o ti o corrupts awọn ile-ti wa ni jọ pọ nwọn si korira o, fun apẹẹrẹ, meji tijoba si awọn ise ti akọkọ. Mi àdánù consulate ati ki o gbà o pẹlu ọtá bi. Pẹlu awọn wọnyi, dignissim, awọn miiran ti irin, nwọn si wà mnesarchum beere boya o jẹ, lati duis ti awọn ọta. Sugbon ma ọlọgbọn lati iwe.',
    'bg': 'Awọn ẹya ara ẹrọ ni atejade, wipe awọn lilo ti a ọmọ ninu awọn miiran. Fun ko ani gbogbo ti kọọkan ni, ti o ti o corrupts awọn ile-ti wa ni jọ pọ nwọn si korira o, fun apẹẹrẹ, meji tijoba si awọn ise ti akọkọ. Mi àdánù consulate ati ki o gbà o pẹlu ọtá bi. Pẹlu awọn wọnyi, dignissim, awọn miiran ti irin, nwọn si wà mnesarchum beere boya o jẹ, lati duis ti awọn ọta. Sugbon ma ọlọgbọn lati iwe.',
    'cg': 'Awọn ẹya ara ẹrọ ni atejade, wipe awọn lilo ti a ọmọ ninu awọn miiran. Fun ko ani gbogbo ti kọọkan ni, ti o ti o corrupts awọn ile-ti wa ni jọ pọ nwọn si korira o, fun apẹẹrẹ, meji tijoba si awọn ise ti akọkọ. Mi àdánù consulate ati ki o gbà o pẹlu ọtá bi. Pẹlu awọn wọnyi, dignissim, awọn miiran ti irin, nwọn si wà mnesarchum beere boya o jẹ, lati duis ti awọn ọta. Sugbon ma ọlọgbọn lati iwe.',
    'dg': 'Awọn ẹya ara ẹrọ ni atejade, wipe awọn lilo ti a ọmọ ninu awọn miiran. Fun ko ani gbogbo ti kọọkan ni, ti o ti o corrupts awọn ile-ti wa ni jọ pọ nwọn si korira o, fun apẹẹrẹ, meji tijoba si awọn ise ti akọkọ. Mi àdánù consulate ati ki o gbà o pẹlu ọtá bi. Pẹlu awọn wọnyi, dignissim, awọn miiran ti irin, nwọn si wà mnesarchum beere boya o jẹ, lati duis ti awọn ọta. Sugbon ma ọlọgbọn lati iwe.',
    'eg': 'Awọn ẹya ara ẹrọ ni atejade, wipe awọn lilo ti a ọmọ ninu awọn miiran. Fun ko ani gbogbo ti kọọkan ni, ti o ti o corrupts awọn ile-ti wa ni jọ pọ nwọn si korira o, fun apẹẹrẹ, meji tijoba si awọn ise ti akọkọ. Mi àdánù consulate ati ki o gbà o pẹlu ọtá bi. Pẹlu awọn wọnyi, dignissim, awọn miiran ti irin, nwọn si wà mnesarchum beere boya o jẹ, lati duis ti awọn ọta. Sugbon ma ọlọgbọn lati iwe.',
    'fg': 'Awọn ẹya ara ẹrọ ni atejade, wipe awọn lilo ti a ọmọ ninu awọn miiran. Fun ko ani gbogbo ti kọọkan ni, ti o ti o corrupts awọn ile-ti wa ni jọ pọ nwọn si korira o, fun apẹẹrẹ, meji tijoba si awọn ise ti akọkọ. Mi àdánù consulate ati ki o gbà o pẹlu ọtá bi. Pẹlu awọn wọnyi, dignissim, awọn miiran ti irin, nwọn si wà mnesarchum beere boya o jẹ, lati duis ti awọn ọta. Sugbon ma ọlọgbọn lati iwe.',
    'gg': 'Awọn ẹya ara ẹrọ ni atejade, wipe awọn lilo ti a ọmọ ninu awọn miiran. Fun ko ani gbogbo ti kọọkan ni, ti o ti o corrupts awọn ile-ti wa ni jọ pọ nwọn si korira o, fun apẹẹrẹ, meji tijoba si awọn ise ti akọkọ. Mi àdánù consulate ati ki o gbà o pẹlu ọtá bi. Pẹlu awọn wọnyi, dignissim, awọn miiran ti irin, nwọn si wà mnesarchum beere boya o jẹ, lati duis ti awọn ọta. Sugbon ma ọlọgbọn lati iwe.',
    'hg': 'Awọn ẹya ara ẹrọ ni atejade, wipe awọn lilo ti a ọmọ ninu awọn miiran. Fun ko ani gbogbo ti kọọkan ni, ti o ti o corrupts awọn ile-ti wa ni jọ pọ nwọn si korira o, fun apẹẹrẹ, meji tijoba si awọn ise ti akọkọ. Mi àdánù consulate ati ki o gbà o pẹlu ọtá bi. Pẹlu awọn wọnyi, dignissim, awọn miiran ti irin, nwọn si wà mnesarchum beere boya o jẹ, lati duis ti awọn ọta. Sugbon ma ọlọgbọn lati iwe.',
    'ig': 'Awọn ẹya ara ẹrọ ni atejade, wipe awọn lilo ti a ọmọ ninu awọn miiran. Fun ko ani gbogbo ti kọọkan ni, ti o ti o corrupts awọn ile-ti wa ni jọ pọ nwọn si korira o, fun apẹẹrẹ, meji tijoba si awọn ise ti akọkọ. Mi àdánù consulate ati ki o gbà o pẹlu ọtá bi. Pẹlu awọn wọnyi, dignissim, awọn miiran ti irin, nwọn si wà mnesarchum beere boya o jẹ, lati duis ti awọn ọta. Sugbon ma ọlọgbọn lati iwe.',
    'jg': 'Awọn ẹya ara ẹrọ ni atejade, wipe awọn lilo ti a ọmọ ninu awọn miiran. Fun ko ani gbogbo ti kọọkan ni, ti o ti o corrupts awọn ile-ti wa ni jọ pọ nwọn si korira o, fun apẹẹrẹ, meji tijoba si awọn ise ti akọkọ. Mi àdánù consulate ati ki o gbà o pẹlu ọtá bi. Pẹlu awọn wọnyi, dignissim, awọn miiran ti irin, nwọn si wà mnesarchum beere boya o jẹ, lati duis ti awọn ọta. Sugbon ma ọlọgbọn lati iwe.',
    'kg': 'Awọn ẹya ara ẹrọ ni atejade, wipe awọn lilo ti a ọmọ ninu awọn miiran. Fun ko ani gbogbo ti kọọkan ni, ti o ti o corrupts awọn ile-ti wa ni jọ pọ nwọn si korira o, fun apẹẹrẹ, meji tijoba si awọn ise ti akọkọ. Mi àdánù consulate ati ki o gbà o pẹlu ọtá bi. Pẹlu awọn wọnyi, dignissim, awọn miiran ti irin, nwọn si wà mnesarchum beere boya o jẹ, lati duis ti awọn ọta. Sugbon ma ọlọgbọn lati iwe.',
    'lg': 'Awọn ẹya ara ẹrọ ni atejade, wipe awọn lilo ti a ọmọ ninu awọn miiran. Fun ko ani gbogbo ti kọọkan ni, ti o ti o corrupts awọn ile-ti wa ni jọ pọ nwọn si korira o, fun apẹẹrẹ, meji tijoba si awọn ise ti akọkọ. Mi àdánù consulate ati ki o gbà o pẹlu ọtá bi. Pẹlu awọn wọnyi, dignissim, awọn miiran ti irin, nwọn si wà mnesarchum beere boya o jẹ, lati duis ti awọn ọta. Sugbon ma ọlọgbọn lati iwe.',
    'mg': 'Awọn ẹya ara ẹrọ ni atejade, wipe awọn lilo ti a ọmọ ninu awọn miiran. Fun ko ani gbogbo ti kọọkan ni, ti o ti o corrupts awọn ile-ti wa ni jọ pọ nwọn si korira o, fun apẹẹrẹ, meji tijoba si awọn ise ti akọkọ. Mi àdánù consulate ati ki o gbà o pẹlu ọtá bi. Pẹlu awọn wọnyi, dignissim, awọn miiran ti irin, nwọn si wà mnesarchum beere boya o jẹ, lati duis ti awọn ọta. Sugbon ma ọlọgbọn lati iwe.',
}
