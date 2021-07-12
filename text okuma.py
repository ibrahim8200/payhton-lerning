from PIL import Image
import pytesseract

image = Image.open("C:\\Users\\hh456\\PycharmProjects\\pythonProject\\ileri deneme\\img\\text.png")
text = pytesseract.image_to_string(image, lang="eng")
print(text)

