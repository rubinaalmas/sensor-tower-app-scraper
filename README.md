# Sensor Tower App Scraper

This Python automation tool scrapes **publisher country** data for mobile apps from [Sensor Tower](https://www.sensortower.com/) using **Playwright**, **Pandas**, and **AsyncIO**.

It handles login-required access and extracts data at scale — tested with over 8,000 app IDs — while mimicking human browsing patterns to avoid rate limiting.

---

## Features

- Scrapes publisher country per app from Sensor Tower
- Handles over 8,000 rows with:
  - Human-like delays
  - Breaks every 100 rows
  - Auto-save and resume capability
- Works in Jupyter, VS Code, or `.py` script
- Uses manual login (no need to store credentials)

---

## Required Tech Stack

- Python 3.x
- Playwright (async)
- Pandas
- nest_asyncio (for notebooks)

---

##  Usage Instructions

1. **Install Dependencies**  

2. **Run the Script**

3. **Manual Login**
When prompted, log in to Sensor Tower in the opened Chromium window and press Enter to continue.

4. **Wait & Save**
The script will:

Navigate to each app’s page, Scrape the publisher country, Auto-save results in the same CSV

