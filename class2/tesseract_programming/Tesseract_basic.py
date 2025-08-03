from os import path
from PIL import Image, ImageFilter

import pytesseract  #pip install pytesseract first


def ocr_core(img,lang, config, output_type):
    return pytesseract.image_to_string(img,lang=lang, config=config, output_type=output_type)  

def pre_processing_img(img):

    #Get the image in grayscale
    img = img.convert('L')

    # Remove noise using median filter
    img = img.filter(ImageFilter.MedianFilter(size=1))
    # Adjust brightness 
    img = img.point(lambda x: x * 1.5)  # Increase brightness by 50%

    # Adjust contrast
    img = img.point(lambda x: x * 1.2)  # Increase contrast by 20%
    return img

def get_text_from_image(file_name, **kwargs):

    image_path = kwargs.get('image_path', './images')
    print(f"Image path: {image_path}")
    if not image_path or not path.exists(image_path):
        raise FileNotFoundError(f"The image path {image_path} does not exist or is not provided.")
    
    output_path = kwargs.get('output_path', './output')
    print(f"Output path: {output_path}")
    if not output_path or not path.exists(output_path):
        raise FileNotFoundError(f"The output path {output_path} does not exist or is not provided.")
    
    lang = kwargs.get('lang', 'eng')
    print(f"Language: {lang}")  
    config = kwargs.get('config', '--psm 6')
    print(f"Config: {config}")  

    
    output_type = kwargs.get('output_type', pytesseract.Output.STRING)
    print(f"Output type: {output_type}")
    try:
        file_path = path.join(image_path, file_name)
        print(f"File path: {file_path}")
        #Load an image using PIL
        image = Image.open(file_path)
        # Pre-process the image to enhance OCR accuracy
        image = pre_processing_img(image)
        # Use pytesseract to do OCR on the image
        text = ocr_core(image, lang, config, output_type)

        print(text)
    except Exception as e:
        print(f"An error occurred: {e}")


get_text_from_image("tesseract_relase_note.png", 
                    image_path='.\images', 
                    output_path='.\output', 
                    lang='eng', 
                    config='--psm 6', 
                    output_type=pytesseract.Output.STRING)

