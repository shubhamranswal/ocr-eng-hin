# Manage imports
import pytesseract
from PIL import Image

# Load OCR model (For Tesseract, there's no specific model to load)
def load_ocr_model():
    return None, None

# Perform OCR and get bounding boxes
def perform_ocr(image_file, processor=None, model=None):
    image = Image.open(image_file)
    extracted_text = pytesseract.image_to_string(image, lang='eng+hin')
    boxes = pytesseract.image_to_boxes(image, lang='eng+hin')
    return extracted_text, boxes