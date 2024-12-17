from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from bs4 import BeautifulSoup
import pandas as pd
import time

driver = webdriver.Chrome()  

url = 'https://infosec-conferences.com/'

driver.get(url)

try:
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "eventsTable_length"))
    )
    select_element = driver.find_element(By.NAME, "eventsTable_length")  
    dropdown = Select(select_element)
    dropdown.select_by_value("-1")  
    time.sleep(5)  
except Exception as e:
    print(f"Error selecting 'All' entries: {e}")

def expand_rows():
    expand_buttons = driver.find_elements(By.CSS_SELECTOR, "td .child-control")
    for button in expand_buttons:
        try:
            ActionChains(driver).move_to_element(button).click(button).perform()
            time.sleep(0.5)  
        except Exception as e:
            print(f"Error clicking button: {e}")

def parse_page():
    html = driver.page_source

    soup = BeautifulSoup(html, 'html.parser')

    page_event_data = []

    main_rows = soup.find_all('tr', {"itemscope": True})

    for main_row in main_rows:
        columns = main_row.find_all('td')
        if len(columns) >= 6:  
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

expand_rows()

all_event_data = parse_page()

driver.quit()

df = pd.DataFrame(all_event_data)
df = df[df["Country"] == "United States"]

df.to_csv("us_conferences.csv", index=False)

print("CSV file saved: us_conferences.csv")
print(df)

