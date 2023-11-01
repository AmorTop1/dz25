from googletrans import Translator


with open("dz25.txt", "r", encoding="utf-8") as file:
    ukrainian_text = file.read()

translator = Translator()

translation = translator.translate(ukrainian_text, src='uk', dest='en')

print("Переклад на англійську:")
print(translation.text)

with open("dz25_pereklad.txt", "w", encoding="utf-8") as output_file:
    output_file.write(translation.text)
