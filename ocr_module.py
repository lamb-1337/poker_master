import easyocr
import pyautogui
from PIL import Image
import numpy as np

# Initialize the EasyOCR reader (once)
reader = easyocr.Reader(['en'], gpu=False)  # Set gpu=True if you have GPU support

def capture_screen(region=None):
    """
    Captures part of the screen using pyautogui.
    region = (left, top, width, height)
    """
    screenshot = pyautogui.screenshot(region=region)
    return screenshot

def perform_ocr(image: Image.Image):
    """
    Performs OCR on a PIL Image using EasyOCR.
    Returns list of tuples: (bbox, text, confidence)
    """
    if image.mode != 'RGB':
        image = image.convert('RGB')
    
    image_np = np.array(image)
    results = reader.readtext(image_np)
    return results