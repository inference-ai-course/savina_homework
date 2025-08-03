#This program converts PDF files to images using the pdf2image library. Then, extracts text from the images using OCR and saves the text to a json file.

from pdf2image import convert_from_path
from PIL import Image
import pytesseract
import os

def convert_pdf_to_images(pdf_file, output_path='./output', dpi=500, poppler_path=r'C:\poppler\poppler-24.08.0\Library\bin'):
    try:
        images = convert_from_path(pdf_file, dpi=dpi, poppler_path=poppler_path)

        if images:
            count = len(images)
            for i, image in enumerate(images):
                image_file=os.path.join(output_path, f'{pdf_file}_{i + 1}.jpg')  
                print(image_file)          

                image.save(f'{image_file}', 'JPEG')  
            print(f"Converted {pdf_file} to images and saved to {output_path}. {count} images created.")
            return count
    except Exception as e:
        print(f"An error occurred while converting the PDF to images: {e}")

def extract_text_from_image(image_path, lang='eng', config='--psm 6'):
   for filename in os.listdir(image_path):
        if filename.endswith('.jpg'):
            try:
                img = Image.open(os.path.join(image_path, filename))
                data = pytesseract.image_to_string(img, output_type=pytesseract.Output.STRING, lang=lang, config=config)
                txt_output_path = os.path.splitext(os.path.join(image_path, filename))[0] + '.txt'
                with open(txt_output_path, "w", encoding="utf-8") as f:
                    f.write(data)
            except Exception as e:
                print(f"An error occurred while processing the image {filename}: {e}")
                continue
    

pdf_file = '2507.23785v1.pdf' 
count = convert_pdf_to_images(pdf_file)
if count:
    print(f"Total images created: {count}")
    extract_text_from_image('./output')
else:
    print("No images were created.")    
    




