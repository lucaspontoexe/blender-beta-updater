import os
import platform
import urllib.request
import shutil
import tempfile
import locale
import json

from bs4 import BeautifulSoup

trfile = open("i18n.json", 'r', encoding='UTF-8').read()
i18n = json.loads(trfile)

# Try to get the language from the system variable. Defaults to en_US
lang = locale.getdefaultlocale()[0] or 'en_US'

def print_tr(part):
    """Prints translated text from the JSON file (i18n.json)
    
    Arguments:
        part {string} -- Gets the string from the file
    """
    try:
        print(i18n[lang][part])
    except KeyError:
        print(i18n['en_US'][part])


def select_blender_release():
    """Gets the correct link index depending on OS name and architecture.
    Returns:
            [integer] -- link index
    """

    #	More links can be found by running:
    #		for link in soup.find_all('a'):
    #			print(link.get('href'))

    platforms = {
        'Windows': 9,
        'Linux': 11,
        'Darwin': 13
    }

    if platform.machine().endswith('64'):
        return platforms[platform.system()]
    else:
        return platforms[platform.system() + 1]


print_tr('searching')

site = "https://builder.blender.org"
html = urllib.request.urlopen(site).read()
soup = BeautifulSoup(html, 'html.parser')
name = "blender2.81"

# Linux uses a different file format
if platform.system() == 'Linux':
    name += ".tar.bz2"
else:
    name += ".zip"

print_tr("downloading")
print_tr("rant")
urllib.request.urlretrieve(site + soup.find_all('a')
                           [select_blender_release()].get('href'), name)
print_tr("download_done")


print_tr("extracting")
shutil.unpack_archive(name)
print_tr("extract_done")
print_tr("updating")

# rename app to old-something
try:
    cheap_hashing = tempfile.gettempdir() + "\\old " + str(os.path.getctime("app"))
    os.rename("app", cheap_hashing)
except FileNotFoundError:
    print_tr("no_past_version")

# rename blender to app
for item in os.listdir():
    if "blender-2.81" in item:
        os.rename(item, "app")

print_tr("all_done")
