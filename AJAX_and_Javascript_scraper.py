# AJAX and Javascript scraper

import requests
from bs4 import BeautifulSoup
import json

base_url = "https://www.scrapethissite.com/pages/ajax-javascript/"

years = [2010, 2011, 2012, 2013, 2014, 2015]

all_films = []

for year in years:
	url = f"{base_url}?ajax=true&year={year}"
	response = requests.get(url)
	data = response.json()
	for film in data:
		all_films.append({
			"year": year,
			"title": film["title"],
			"nomination": film["nominations"],
			"award": film["awards"],
			"best_picture": film.get("best_picture", False),
		})
	print(f"Year {year} done.")

with open("JSON/oscars_films.json", "w", encoding="utf-8") as f:
	json.dump(all_films, f, indent=4, ensure_ascii=False)
