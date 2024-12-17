# Cybersecurity Conferences United States


This project is a Python script that uses **Selenium** and **BeautifulSoup** to scrape cybersecurity conference data from the website [infosec-conferences.com](https://infosec-conferences.com/). The script extracts details about events, including event name, link, date, type, country, region, state, city, and format, and saves the data into a CSV file.

## Features
- Uses Selenium to interact with dynamic content on the webpage.
- Expands all child rows to reveal hidden information such as the **City**.
- Extracts data like:
  - Event Name
  - Event Link
  - Event Date
  - Event Type
  - Country
  - Region
  - US State
  - City
  - Event Format
- Saves the extracted data into a CSV file for further use.

## Requirements
Make sure you have the following installed:
- Python 3.x
- Google Chrome browser
- ChromeDriver (compatible with your Chrome version)

### Python Libraries:
Install the required libraries with pip:
```bash
pip install selenium beautifulsoup4 pandas
```

## How to Use
1. **Setup ChromeDriver**:
   - Download ChromeDriver: [https://chromedriver.chromium.org/](https://chromedriver.chromium.org/)
   - Ensure it is in your system's PATH.

2. **Run the Script**:
   - Run the script using Python:
     ```bash
     python3 conferences.py
     ```

3. **Output**:
   - The script saves all event data into a CSV file named `us_conferences.csv` in the current directory.


## Example Output
The output CSV (`us_conferences.csv`) will contain rows similar to:

| Event Name                        | Event Link                        | Event Date  | Event Type | Country       | Region        | US State    | City         | Event Format |
|----------------------------------|----------------------------------|-------------|------------|---------------|---------------|-------------|--------------|--------------|
| FutureCon CyberSecurity Conf...  | https://futureconevents.com/...  | 2025-12-10  | Conference | United States | North America | Tennessee   | Nashville    | Physical     |
| SecureWorld: East Virtual Conf...| https://www.secureworld.io/...   | 2025-12-04  | Conference | United States | North America | Oregon      | Portland     | Online       |

## Notes
- The script assumes the webpage structure is consistent with the current format.
- If the website changes its structure, minor modifications to selectors may be required.
- Ensure a stable internet connection while running the script.

## Troubleshooting
- **ChromeDriver Error**:
   - Ensure your ChromeDriver version matches your Chrome browser version.
- **Selenium Timeout**:
   - Increase the WebDriver wait time if the page loads slowly.
- **Missing Data**:
   - Verify the webpage content is fully loaded before scraping.



