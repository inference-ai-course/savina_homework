from pdf2image import convert_from_path
import os

pdf_file = '2507.23785v1.pdf'  
try:
    images = convert_from_path('2507.23785v1.pdf', dpi=500, poppler_path=r'C:\poppler\poppler-24.08.0\Library\bin')
    output_path = './output'
    if images:
        count = len(images)
        for i, image in enumerate(images):
            image_file=os.path.join(output_path, f'{pdf_file}_{i + 1}.jpg')  
            print(image_file)          

            image.save(f'{image_file}', 'JPEG')  
        print(f"Converted {pdf_file} to images and saved to {output_path}. {count} images created.")
except Exception as e:
    print(f"An error occurred while converting the PDF to images: {e}")





