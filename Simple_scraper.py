# Simple scraper

import requests
from bs4 import BeautifulSoup
import json

url = "https://www.scrapethissite.com/pages/simple/"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

countries = []
for country in soup.find_all("div", class_="country"):
	name = country.find("h3", class_="country-name").text.strip()
	capital = country.find("span", class_="country-capital").text.strip()
	population = country.find("span", class_="country-population").text.strip()
	area = country.find("span", class_="country-area").text.strip()
	countries.append({
		"name": name,
		"capital": capital,
		"population": population,
		"area": area,
	})

with open("JSON/countries.json", "w", encoding="utf-8") as f:
	json.dump(countries, f, indent=4, ensure_ascii=False)



