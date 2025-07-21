# 🐢 Scraping Project - Python Web Scrapers

Welcome to this Python web scraping demonstration project on [scrapethissite.com](https://www.scrapethissite.com/)!

---

## 🚀 Main Features

- Data extraction from pages using **frames** and **iframes**
- Scraping of **AJAX**-loaded content
- Automatic saving of results in **JSON** format

---

## 📁 Project Structure

```
Scraper/
├── Frames_IFrames_scraping.py       # 🐢 Turtle families scraping via frames/iframes
├── AJAX_and_Javascript_scraper.py   # 🎬 AJAX scraping of Oscar-winning films
├── JSON/                            # 📦 Generated JSON results
└── README.md                        # 📖 This file
```

### 🐢 Frames_IFrames_scraping.py
- Navigates through the complex frames/iframes structure to extract turtle families
- For each turtle: name, description, image, "Learn more" link
- Output: `JSON/turtles.json`

### 🎬 AJAX_and_Javascript_scraper.py
- Uses AJAX endpoints to retrieve Oscar-winning films by year
- For each film: title, nominations, awards, best picture status
- Output: `JSON/oscars_films.json`

---

## ⚙️ Prerequisites

- Python 3.7+
- Libraries: `requests`, `beautifulsoup4`

### 🔒 Using a Virtual Environment (Recommended)

Before installing dependencies, create a virtual environment dedicated to the project:
```bash
python3 -m venv venv
source venv/bin/activate
```

Then, install the dependencies:
```bash
pip install requests beautifulsoup4
```

---

## ▶️ Usage

1. Clone or download this folder
2. Make sure the `JSON/` folder exists (`mkdir JSON` if needed)
3. Run the desired script:
   ```bash
   python3 Frames_IFrames_scraping.py
   python3 AJAX_and_Javascript_scraper.py
   ```
4. Results are generated in `JSON/` in `.json` format

---

## 💡 Educational Notes

- These scripts are designed for learning web scraping:
  - Handling frames/iframes
  - AJAX requests
  - Multi-page navigation
- The target site is intentionally complex for practice
