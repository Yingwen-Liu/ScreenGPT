from PIL import Image
import pytesseract
import mss
import re
import json


def perform_ocr(area, path):
    # Set the Tesseract path
    pytesseract.pytesseract.tesseract_cmd = path
    
    # Capture the defined area
    with mss.mss() as sct:
        screenshot = sct.grab(area)
        img = Image.frombytes('RGB', (screenshot.width, screenshot.height), screenshot.rgb)
    
    return pytesseract.image_to_string(img)


def handle(text):    
    # Remove newline characters NOT followed by A, B, C or D
    text = re.sub(r'\n(?![ABCD])', ' ', text)
    text = re.sub('  ', ' ', text)
    return text.strip()


def get_text():
    with open('config.json', 'r') as file:
        config = json.load(file)

    # Perform OCR on the defined area
    text = perform_ocr(config['area'], config['path'])
    handled_text = handle(text)
    print(">> Text:\n", handled_text)
    
    return handled_text


if __name__ == "__main__":
    text = get_text()
    print(text)
