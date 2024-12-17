from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from bs4 import BeautifulSoup
import pandas as pd
import time

# Initialize Selenium WebDriver
driver = webdriver.Chrome()  # Ensure ChromeDriver is installed and in PATH

# URL of the target page
url = 'https://infosec-conferences.com/'

# Open the webpage
driver.get(url)

# Wait for the dropdown to be interactable
try:
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "eventsTable_length"))
    )
    select_element = driver.find_element(By.NAME, "eventsTable_length")  # Adjust selector if needed
    dropdown = Select(select_element)
    dropdown.select_by_value("-1")  # Attempt to select 'All' programmatically
    time.sleep(5)  # Allow time for all entries to load
except Exception as e:
    print(f"Error selecting 'All' entries: {e}")

def expand_rows():
    # Click all "+" buttons to expand child rows
    expand_buttons = driver.find_elements(By.CSS_SELECTOR, "td .child-control")
    for button in expand_buttons:
        try:
            ActionChains(driver).move_to_element(button).click(button).perform()
            time.sleep(0.5)  # Small delay to ensure content loads
        except Exception as e:
            print(f"Error clicking button: {e}")

def parse_page():
    # Get the fully rendered HTML
    html = driver.page_source

    # Parse the rendered HTML with BeautifulSoup
    soup = BeautifulSoup(html, 'html.parser')

    # Initialize event data list for this page
    page_event_data = []

    # Find all main rows
    main_rows = soup.find_all('tr', {"itemscope": True})

    # Iterate through each main row
    for main_row in main_rows:
        columns = main_row.find_all('td')
        if len(columns) >= 6:  # Check valid row structure
            # Extract event details
            event_name_tag = columns[0].find('a')
            event_name = event_name_tag.text.strip() if event_name_tag else "N/A"
            event_link = event_name_tag['href'] if event_name_tag and 'href' in event_name_tag.attrs else "N/A"
            event_date = columns[1].text.strip()
            event_type = columns[2].text.strip()
            country = columns[3].text.strip()
            region = columns[4].text.strip()
            us_state = columns[5].text.strip()
            city = columns[6].text.strip()
            event_format = columns[7].text.strip() if len(columns) > 7 else "N/A"

            # Append data to the list
            page_event_data.append({
                "Event Name": event_name,
                "Event Link": event_link,
                "Event Date": event_date,
                "Event Type": event_type,
                "Country": country,
                "Region": region,
                "US State": us_state,
                "City": city,
                "Event Format": event_format
            })
    return page_event_data

# Expand all rows on the page
expand_rows()

# Parse the page for data
all_event_data = parse_page()

# Close the browser
driver.quit()

# Convert extracted data to a DataFrame
df = pd.DataFrame(all_event_data)
df = df[df["Country"] == "United States"]

# Save to CSV
df.to_csv("us_conferences.csv", index=False)

print("CSV file saved: us_conferences.csv")
print(df)

