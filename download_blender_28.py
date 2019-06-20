import os
import platform
import urllib.request
import shutil
import tempfile
from bs4 import BeautifulSoup

def selectBlenderRelease():
	"""Gets the correct link index depending on OS name and architecture.
	
	More links can be found by running:
		for link in soup.find_all('a'):
    	print(link.get('href'))

	Returns:
		[integer] -- link index
	"""

	platforms = {
		'Windows': 9,
		'Linux': 13,
		'Darwin': 17
	}

	if platform.machine().endswith('64'):
		return platforms[platform.system()]
	else: 
		return platforms[platform.system() + 1]


print("Procurando... ")

site = "https://builder.blender.org"
html = urllib.request.urlopen(site).read()
soup = BeautifulSoup(html, 'html.parser')
name = "blender2.8"

#Linux uses a different file format
if platform.system() == 'Linux':
	name += ".tar.bz2"
else:
	name += ".zip"

print("Baixando... ")
print("(uma progress bar até que cairia bem agora, né)")
urllib.request.urlretrieve(site + soup.find_all('a')[selectBlenderRelease()].get('href'), name)
print("Pronto.")


print("Extraindo...")
shutil.unpack_archive(name)

print("Extraído. Atualizando...")

#rename app to old-something
try:
	cheaphashing = tempfile.gettempdir() + "\\old " + str(os.path.getctime("app"))
	os.rename("app", cheaphashing)
except:
	print("Não tinha versão anterior aqui. Continuando...")

#rename blender to app
for item in os.listdir():
	if "blender-2.80" in item:
		os.rename(item, "app")

print("tá pronto 👍 100% atualizado")