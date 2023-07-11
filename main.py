import pytesseract
from PIL import Image

image_path = 'a.png'

image = Image.open(image_path)

image = image.convert('L')

text = pytesseract.image_to_string(image)

print(text)
