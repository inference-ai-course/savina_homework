import pytesseract
from PIL import Image
#from trafilatura.settings import Extractor
import trafilatura
from playwright.sync_api import sync_playwright
import os, re, math,json,datetime

class WebScraper:
    def __init__(self, category="cs.CL", item_numbers=200, outputs_path="./outputs"):
        
        self.category = category
        self.item_numbers = item_numbers
        self.skip = 0 
        self.item_num_per_page = 100
        self.outputs_path = outputs_path
        

    def get_papers_url(self, page_number):
        """
        Get the page arXiv url based on the page number to retrive.
        """
        self.skip = (page_number-1) * self.item_num_per_page

        self.url = f"https://arxiv.org/list/{self.category}/recent?skip={self.skip}&show={self.item_num_per_page}"
        print(f"Fetching papers from: {self.url}")
        return self.url

    def save_webpage_to_image(self, url):
        """Saves the webpage content of a paper to an image file.
        """
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")

        screenshot_name = os.path.join(self.outputs_path, f"{self.category}_{timestamp}.png")

        with sync_playwright() as p:
            browser = p.chromium.launch(headless=True)
            page = browser.new_page()   
            page.goto(url)
            page.screenshot(path=screenshot_name, full_page=True)
            browser.close()
            print(f"Webpage saved to {screenshot_name}")
        return screenshot_name

    def get_scraped_text_from_image(self, image_path, lang='eng', config='--psm 6'):
        """Extracts text from an image using OCR.
        """
        try:

            img = Image.open(image_path)
            data = pytesseract.image_to_string(img, output_type=pytesseract.Output.STRING, lang=lang, config=config)
            txt_output_path = os.path.splitext(image_path)[0] + '.txt'
            # Join all detected text lines, skipping empty ones
           
            with open(txt_output_path, "w", encoding="utf-8") as f:
                f.write(data)
            print(f"Text extracted from {image_path} and saved to {txt_output_path}")
            return txt_output_path

        except Exception as e:
            print(f"An error occurred while processing the image: {e}")
            return None
        
    def extract_arviv_ids(self, text):
        """Extracts arXiv IDs from the given text using regex.
        """
        matches = re.findall(r'arxiv:(\d{4}\.\d+)\s*\[', text)
        return matches
    
    def get_scraped_text_from_url(self):
        """Extracts text from a URL using trafilatura.
        """
        """Extracts text from .txt files, fetches arXiv metadata, and saves all structured results to one JSON file."""
        results = []
        for txt_file in os.listdir(self.outputs_path):
            if txt_file.endswith('.txt'):
                print(f"Extracting arXiv IDs from {txt_file}")
                with open(os.path.join(self.outputs_path, txt_file), 'r', encoding='utf-8') as f:
                    text = f.read()
                arxiv_ids = self.extract_arviv_ids(text)
                if arxiv_ids:
                    options = trafilatura.settings.Extractor(output_format="json", with_metadata=True)
                    for arxiv_id in arxiv_ids:
                        url = f"https://arxiv.org/abs/{arxiv_id}"
                        print(f"Fetching data from {url}")
                        downloaded = trafilatura.fetch_url(url)
                        extracted_data = trafilatura.extract(downloaded, options=options)
                        if extracted_data:
                            data = json.loads(extracted_data)
                            structured = {
                                "url": url,
                                "title": data.get("title", ""),
                                "authors": data.get("author", ""),
                                "abstract": data.get("description", data.get("raw_text", "")),
                                "date": data.get("date", "")
                            }
                            results.append(structured)
                        else:
                            print(f"Failed to extract data for {url}")
        # Save all results to a single JSON file
        output_path = os.path.join(self.outputs_path, "all_arxiv_structured.json")
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(results, f, indent=2, ensure_ascii=False)
        print(f"All structured results saved to {output_path}")

        # Check file size and split if needed
        max_size = 1048576  # 1MB in bytes
        if os.path.getsize(output_path) > max_size:
            print("File is larger than 1MB, splitting into smaller files...")
            chunk_size = math.ceil(len(results) / (os.path.getsize(output_path) // max_size + 1))
            for i in range(0, len(results), chunk_size):
                chunk = results[i:i+chunk_size]
                chunk_path = os.path.join(self.outputs_path, f"all_arxiv_structured_part{i//chunk_size+1}.json")
                with open(chunk_path, 'w', encoding='utf-8') as f:
                    json.dump(chunk, f, indent=2, ensure_ascii=False)
                print(f"Saved chunk to {chunk_path}")



if __name__ == "__main__":

    max_item_number=200
    page_number = 1
    category="cs.CL"
    outputs_path = "./outputs"
    screenshots=[]
    pagers=[]

    print("*"*20+f" Downloading recent {max_item_number} papers for {category} from arxiv.org "+"*"*20)

    scraper = WebScraper(category=category, item_numbers=200, outputs_path=outputs_path)

    while page_number <= max_item_number/scraper.item_num_per_page:
        # Get the expected url for the page number
        url=scraper.get_papers_url(page_number)
        print(url)

        screen_shot_file = scraper.save_webpage_to_image(url)
        screenshots.append(screen_shot_file)
        page_number +=1

    print(screenshots)

    # Extract text from the screenshots
    for screenshot in screenshots:
        print("*"*20+f" Processing screenshot: {screenshot} "+"*"*20)
        txt_output_path = scraper.get_scraped_text_from_image(screenshot)
        if txt_output_path:
            print(f"Extracted text from {screenshot}:\n{txt_output_path}\n")
        else:
            print(f"No text extracted from {screenshot}.\n")

    # Extract arXiv IDs from the text files
    print("*"*20+f" Processing json result file "+"*"*20)
    scraper.get_scraped_text_from_url()












