import os
import urllib.request
import subprocess
import tempfile
from bs4 import BeautifulSoup
#import zipfile

print("Procurando... ")

html = urllib.request.urlopen("https://builder.blender.org/download").read()
soup = BeautifulSoup(html, 'html.parser')
site = "https://builder.blender.org"
name = "blender2.8.zip"

#for link in soup.find_all('a'):
#    print(link.get('href'))

print("Baixando... ")
print("(uma progress bar até que cairia bem agora, né)")
urllib.request.urlretrieve(site + soup.find_all('a')[9].get('href'), name)
print("Pronto.")

#print("Extract it yourself")
#with zipfile.ZipFile(name) as thedamnfile:
#    print("(well, why am I writing this in English?)")
#    thedamnfile.extractall()
#    print("All done.")

print("Extraindo...")
subprocess.run(["7z", "x", name])
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