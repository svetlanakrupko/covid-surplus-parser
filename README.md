# covid surplus parser

This repository contains a Python script developed to scrape search statistics from Yandex, a popular Russian search engine, for analyzing COVID-19 symptoms. The goal is to estimate surplus COVID-19 cases compared to official statistics by examining search trends.

## Overview

The script extracts data from Yandex search result HTML files related to specific COVID-19 symptoms. The data is then saved to a CSV file for further analysis.

## Requirements

- **Python 3.x**
- **Library**: `beautifulsoup4`

Install the required library:

```bash
pip install beautifulsoup4
```

## Usage
1. Prepare HTML File: Save your Yandex search result HTML as `query.txt`.
2. Set Parameters: Modify `key_word`, `city`, and `region` in the script.
3. Run the Script: Execute the script to extract data into `regions_sep.csv`.