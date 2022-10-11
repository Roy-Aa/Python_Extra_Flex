# De afbeelding is 480 pixels breed en 270 pixels hoog
import ImageFont
import ImageDraw

lettertype = ImageFont.truetype("impact.ttf", 40)

# Vraag aan de ImageDraw module om een tekengebied te maken op de achtergrond afbeelding
tekengebied = ImageDraw.Draw(achtergrond)

# Tekst schrijven
tekst = "Coding in Python\nNo problemo!"
tekengebied.multiline_text((10,10), tekst, font=lettertype, fill=(0,0,0))

# Het resultaat tonen
achtergrond.show()

# En opslaan onder een andere naam
achtergrond.save("meme_met_tekst.jpg")