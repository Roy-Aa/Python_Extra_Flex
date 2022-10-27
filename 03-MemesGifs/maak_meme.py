from PIL import Image, ImageFont, ImageDraw

achtergrond = Image.open("drake.jpg")

# Afmetingen opslaan in eigen variabelen
breedte = achtergrond.width
hoogte = achtergrond.height 

lettertype = ImageFont.truetype("impact.ttf", 30)

# Vraag aan de ImageDraw module om een tekengebied te maken op de achtergrond afbeelding
tekengebied = ImageDraw.Draw(achtergrond)


# Tekst schrijven
tekst = "Script Errors"

# Bereken de breedte en hoogte van de tekst
tekst_breedte, tekst_hoogte = tekengebied.textsize(tekst, font=lettertype) 
print("tekstbreedte=" + str(tekst_breedte) + ", tekst_hoogte=" + str(tekst_hoogte))

# Tekst positie berekenen
tekst_x = (breedte - tekst_breedte) / 2
tekst_y = (hoogte - tekst_hoogte) / 2   

tekengebied.multiline_text((tekst_x+33, tekst_y-50), tekst, font=lettertype, fill=(255,255,255))

# Het resultaat tonen
achtergrond.show()

# En opslaan onder een andere naam
achtergrond.save("meme_met_tekst.jpg")


