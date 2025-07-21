import requests
from bs4 import BeautifulSoup
import json
from urllib.parse import urljoin

url = "https://www.scrapethissite.com/pages/frames/?frame=i"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

results = []

families = soup.find_all("div", class_="turtle-family-card")
for fam in families:
	name_tag = fam.find("h3", class_="family-name")
	name = name_tag.text.strip() if name_tag else ""

	img_tag = fam.find("img", class_="turtle-image")
	img_url = img_tag["src"] if img_tag else ""

	link_tag = fam.find("a", class_="btn")
	link_url = link_tag["href"] if link_tag else ""
	if link_url and not link_url.startswith("http"):
		link_url = requests.compat.urljoin(url, link_url)

	desc = ""
	if link_url:
		detail_response = requests.get(link_url)
		detail_soup = BeautifulSoup(detail_response.text, "html.parser")
		desc_tag = detail_soup.find("p", class_="lead")
		desc = desc_tag.text.strip() if desc_tag else ""

	results.append({
		"name": name,
		"description": desc,
		"image_url": img_url,
		"learn_more_url": link_url
	})

with open("JSON/turtles.json", "w", encoding="utf-8") as f:
	json.dump(results, f, indent=4, ensure_ascii=False)
