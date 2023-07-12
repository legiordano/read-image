import pytesseract
from PIL import Image

def extract_text_from_image(image_path):
    image = Image.open(image_path)
    image = image.convert('L')
    text = pytesseract.image_to_string(image)
    return text

image_path = 'a.png'
text = extract_text_from_image(image_path)
print(text)
