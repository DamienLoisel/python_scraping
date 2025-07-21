# Pagination scraper

import requests
from bs4 import BeautifulSoup
import json

base_url = "https://www.scrapethissite.com/pages/forms/"
page_num = 1
hockey_teams = []

while True:
	if page_num == 1:
		response = requests.get(base_url)
	else:
		response = requests.get(base_url + "?page_num=" + str(page_num))

	soup = BeautifulSoup(response.text, "html.parser")

	for row in soup.find_all("tr", class_="team"):
		name = row.find("td", class_="name").text.strip()
		year = row.find("td", class_="year").text.strip()
		wins = row.find("td", class_="wins").text.strip()
		losses = row.find("td", class_="losses").text.strip()
		ot_losses = row.find("td", class_="ot-losses").text.strip()
		pct = row.find("td", class_="pct").text.strip()
		gf = row.find("td", class_="gf").text.strip()
		ga = row.find("td", class_="ga").text.strip()
		diff = row.find("td", class_="diff").text.strip()
		hockey_teams.append({
			"name": name,
			"year": year,
			"wins": wins,
			"losses": losses,
			"ot_losses": ot_losses,
			"pct": pct,
			"gf": gf,
			"ga": ga,
			"diff": diff,
		})

	next_link = soup.find("a", attrs={"aria-label": "Next"})
	if next_link and "href" in next_link.attrs:
		print("Page " + str(page_num) + " done.")
		page_num += 1
	else:
		print("Page " + str(page_num) + " done.")
		break

with open("JSON/hockey_teams.json", "w", encoding="utf-8") as f:
	json.dump(hockey_teams, f, indent=4, ensure_ascii=False)
