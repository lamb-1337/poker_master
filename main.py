import time
from ocr_module import capture_screen, perform_ocr

def main():
    print("Starting EasyOCR real-time detection (Press Ctrl+C to stop)...\n")

    # Define screen region to capture (x, y, width, height)
    region = (0, 0, 1024, 800)  # Customize as needed

    try:
        while True:
            screenshot = capture_screen(region)
            ocr_results = perform_ocr(screenshot)

            if ocr_results:
                print("Detected Text:")
                for (bbox, text, confidence) in ocr_results:
                    print(f"  {text} (Confidence: {confidence:.2f})")
                print("-" * 50)

            time.sleep(1)  # Delay between captures

    except KeyboardInterrupt:
        print("\n[!] OCR stopped by user.")

if __name__ == "__main__":
    main()