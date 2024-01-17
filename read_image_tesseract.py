from PIL import Image
import pytesseract

# Specify the path to the Tesseract executable
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'  # Adjust this path


def ocr_on_image(image_path):
    image = Image.open(image_path)
    text_content = pytesseract.image_to_string(image, lang='eng')
    return text_content


# Example usage
img_path = r'C:\Users\Marlon\Pictures\Screenshots\Partidas Arancelarias 4.png'
result = ocr_on_image(img_path)
print(result)

# 1. Install Tesseract in machine
