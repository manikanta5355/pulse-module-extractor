import requests
from bs4 import BeautifulSoup
import json
import sys

def extract_modules(url):
    response = requests.get(url, timeout=10)
    soup = BeautifulSoup(response.text, "html.parser")

    modules = []
    current_module = None

    for tag in soup.find_all(["h2", "h3"]):
        text = tag.get_text(strip=True)

        if tag.name == "h2":
            current_module = {
                "module": text,
                "Description": f"This module covers documentation related to {text}.",
                "Submodules": {}
            }
            modules.append(current_module)

        elif tag.name == "h3" and current_module:
            current_module["Submodules"][text] = (
                f"This submodule explains functionality related to {text}."
            )

    return modules


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python module_extractor.py <documentation_url>")
        sys.exit(1)

    url = sys.argv[1]
    result = extract_modules(url)
    print(json.dumps(result, indent=2))
