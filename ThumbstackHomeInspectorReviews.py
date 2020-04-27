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

csv_file = open('reviews.csv', 'w', encoding='utf-8', newline='')
writer = csv.writer(csv_file)
# Page index used to keep track of where we are.
index = 1
while True:
    try:
        print("Scraping Page number " + str(index))
        index = index + 1
        # Find all the reviews on the page
        wait_review = WebDriverWait(driver, 10)
        reviews = wait_review.until(EC.presence_of_all_elements_located((By.XPATH,
                                    '//div[@class="flex w-100 m_justify-between m_flex-row flex-column _1FgKgbKOPF8cM7Sp7AHU-m"]')))
        for review in reviews:
            # Initialize an empty dictionary for each review
            review_dict = {}
            # Use relative xpath to locate the title, text, username, date, rating.
            # Once you locate the element, you can use 'element.text' to return its string.
            # To get the attribute instead of the text of each element, use 'element.get_attribute()'
            try:
                title = review.find_element_by_xpath('//div[@class="mr1 black hover-blue _17VKJeOfCzec21S--Lf85J truncate"]/span').text
            except:
                continue

            # OPTIONAL PART 1a
            # Attempts to click the "read more" button to expand the text. This needs to be clicked
            # a second time otherwise the button click in the next review will collapse the previous
            # review text (and won't expand the current text).

            # We also need to scroll to the review element first because the button is not in the current view yet.
            driver.execute_script("arguments[0].scrollIntoView();", review)

            read_more_exists = False
            try:
                
               #read_more = review.find_element_by_xpath('.//a[@class="border_gray onlyBottomBorder color_000 fontSize_1"]')
                read_more = review.find_element_by_xpath('.//span[@class="blue ml1"]')
                read_more.click()
                read_more_exists = True
                # Slows down the text expansion so the text can be scraped
                time.sleep(.5)
            except:
                pass  

            #Here the text variable refers to the rectangular region that holds the details needed for the proj
            text = review.find_element_by_xpath('//div[@class="flex w-100 m_justify-between m_flex-row flex-column _1FgKgbKOPF8cM7Sp7AHU-m"]').text
            #Username referes to the name name of the service provider
            username = review.find_element_by_xpath('//span[@class="padLeft6 NHaasDS55Rg fontSize_12 pad3 noBottomPad padTop2"]').text
            
           # Using the below variable to get the nbr of reviews in numeric format
            NbrOfReviews = review.find_element_by_xpath('//span[@class="u-visuallyHidden"]/span').text
            #rating = review.find_element_by_xpath('.//span[@class="positionAbsolute top0 left0 overflowHidden color_000"]').get_attribute('style')
            rating = review.find_element_by_xpath('//span[@class="_3gx0PQezdIxb5WhHjK1ZOE StarRating-numericRating"]').text
            #COmmenting out SM the below ,uses regular expressions
            #rating = int(re.findall('\d+', rating)[0])/20  


            # OPTIONAL PART 1b
            # Click the read more button if it exists in order to collapse the text for the current review
            if read_more_exists:
                read_more.click()

            review_dict['title'] = title
            review_dict['text'] = text
            review_dict['username'] = username
            review_dict['NbrOfReviews'] = NbrOfReviews
            review_dict['rating'] = rating

            writer.writerow(review_dict.values())

        # We need to scroll to the bottom of the page because the button is not in the current view yet.
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        # Locate the next button on the page.
        wait_button = WebDriverWait(driver, 10)
        next_button = wait_button.until(EC.element_to_be_clickable((By.XPATH,
                                    '//li[@class="nextClick displayInlineBlock padLeft5 "]')))
        next_button.click()
    except Exception as e:
        print(e)
        csv_file.close()
        driver.close()
        break








SCROLL_PAUSE_TIME = 0.5

titles=driver.find_elements_by_xpath('//div[@class="mr1 black hover-blue _17VKJeOfCzec21S--Lf85J truncate"]/span')

[title.text for title in title]


csv_file = open('reviews.csv', 'w', encoding='utf-8', newline='')
writer = csv.writer(csv_file)