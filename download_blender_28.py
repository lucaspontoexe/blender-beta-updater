import os
import platform
import urllib.request
import subprocess
import tempfile
import zipfile
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

html = urllib.request.urlopen("https://builder.blender.org/download").read()
soup = BeautifulSoup(html, 'html.parser')
site = "https://builder.blender.org"
name = "blender2.8.zip"

print("Baixando... ")
print("(uma progress bar até que cairia bem agora, né)")
urllib.request.urlretrieve(site + soup.find_all('a')[selectBlenderRelease()].get('href'), name)
print("Pronto.")

print("Extract it yourself")
with zipfile.ZipFile(name) as thedamnfile:
    print("(well, why am I writing this in English?)")
    thedamnfile.extractall()
    print("All done.")

print("Extraindo...")
#subprocess.run(["7z", "x", name])
print("Extraído. Atualizando...")

#rename app to old-something
try:
	hashingbarato = tempfile.gettempdir() + "\\old " + str(os.path.getctime("app"))
	os.rename("app", hashingbarato)
except:
	print("Não tinha versão anterior aqui. Continuando...")

#rename blender to app
for item in os.listdir():
	if "blender-2.80" in item:
		os.rename(item, "app")
			
print("tá pronto 👍 100% atualizado")