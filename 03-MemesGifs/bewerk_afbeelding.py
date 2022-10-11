from PIL import Image

# Afbeelding openen en opslaan in de variabele met de naam: afbeelding
afbeelding = Image.open("PIP.png")

# De afbeelding tonen in de standaard image viewer van jouw systeem
afbeelding.show()

# De breedte en hoogte van de afbeelding lezen en tonen 
# Met str() zet je een getal naar een string om. Dan kan print() het gebruiken.
breedte = str(afbeelding.width)
hoogte = str(afbeelding.height)

# breedte en hoogte door twee delen (en afronden naar beneden)

helft_breedte = afbeelding.width // 2
helft_hoogte = afbeelding.height // 2

# Met het resize commando kun je de afmetingen van afbeelding aanpassen
# Deze verwacht een Tuple variabele:
nieuwe_afmeting = (helft_breedte, helft_hoogte)

# Hier wordt de afbeelding kleiner gemaakt en opgeslagen in een nieuwe variabele!
kleinere_afbeelding = afbeelding.resize(nieuwe_afmeting)

# Nu de kleinere afbeelding opslaan me save(). Gebruik de originele bestandsnaam met ergens "klein" er in. 
kleinere_afbeelding.save('PIP.png')

# Zet hier nu zelf de Python code onder om de kleinere afbeelding op het scherm te tonen