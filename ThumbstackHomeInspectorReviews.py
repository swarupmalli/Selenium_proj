from selenium import webdriver
import time
import re
import csv
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Windows users need to specify the path to chrome driver you just downloaded.
# You need to unzip the zipfile first and move the .exe file to any folder you want.
# driver = webdriver.Chrome(r'path\to\the\chromedriver.exe')
driver = webdriver.Chrome(r'C:\Users\19082\chromedriver.exe')

# Go to the page that we want to scrape
driver.get("https://www.thumbtack.com/instant-results/?zip_code=08831&keyword_pk=102906936653958006&project_pk=")

# Click review button to go to the review section
#review_button.click()

csv_file = open('companies.csv', 'w', encoding='utf-8', newline='')
writer = csv.writer(csv_file)
writer.writerow(['title', 'num_reviews', 'num_hires', 'rating'])
# Page index used to keep track of where we are.

# Find all the reviews on the page
wait_company = WebDriverWait(driver, 10)
companies = wait_company.until(EC.presence_of_all_elements_located((By.XPATH,
                            '//div[@class="flex w-100 m_justify-between m_flex-row flex-column _1FgKgbKOPF8cM7Sp7AHU-m"]')))
for company in companies:
    # Initialize an empty dictionary for each review
    company_dict = {}
    # Use relative xpath to locate the title, text, username, date, rating.
    # Once you locate the element, you can use 'element.text' to return its string.
    # To get the attribute instead of the text of each element, use 'element.get_attribute()'
    try:
        title = company.find_element_by_xpath('.//div[@class="mr1 black hover-blue _17VKJeOfCzec21S--Lf85J truncate"]/span').text
    except:
        continue

    # Number of reviews
    try:
        num_reviews = company.find_element_by_xpath('.//span[@class="StarRating-numberOfReviews"]/span/span[2]').text
    except:
        num_reviews = 0

    try:
        rating = float(company.find_element_by_xpath('.//span[@class="_3gx0PQezdIxb5WhHjK1ZOE StarRating-numericRating"]').text)
    except:
        rating = None

    try:
        num_hires = company.find_element_by_xpath('.//li[@class="_3gx0PQezdIxb5WhHjK1ZOE nowrap black-300 flex items-center"]/span[2]').text
        num_hires = int(re.findall('\d+', num_hires)[0])
    except Exception as e:
        print(type(e), e)
        num_hires = 0

    try:
        price = something

    except:
        price = None

    company_dict['title'] = title
    company_dict['num_reviews'] = num_reviews
    company_dict['num_hires'] = num_hires
    company_dict['rating'] = rating

    writer.writerow(company_dict.values())

driver.close()