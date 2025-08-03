from trafilatura.settings import Extractor
import trafilatura
import json


url = "https://arxiv.org/abs/2507.23776"
options = Extractor(output_format="json", with_metadata=True)
downloaded = trafilatura.fetch_url(url)
extracted_data = trafilatura.extract(downloaded, options=options)

# Parse the extracted JSON string
data = json.loads(extracted_data)

# Build structured output
structured = {
    "url": url,
    "title": data.get("title", ""),
    "authors": data.get("author", ""),
    #"abstract": data.get("description", data.get("raw_text", "")),
    "abstract": data.get("raw_text", ""),
    "date": data.get("date", "")
    }

with open('arxiv_2507.23776_structured.json', 'w', encoding='utf-8') as f:
    json.dump(structured, f, indent=2, ensure_ascii=False)

print("Structured result saved to arxiv_2507.23776_structured.json")
