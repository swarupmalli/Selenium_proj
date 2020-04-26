from selenium import webdriver
import time
import re

# Windows users need to specify the path to chrome driver you just downloaded.
# You need to unzip the zipfile first and move the .exe file to any folder you want.
# driver = webdriver.Chrome(r'path\to\the\chromedriver.exe')
driver = webdriver.Chrome(r'C:\Users\19082\chromedriver.exe')

# Go to the page that we want to scrape
driver.get("https://www.thumbtack.com/instant-results/?zip_code=08831&keyword_pk=102906936653958006&project_pk=")


SCROLL_PAUSE_TIME = 0.5



while True:

    # Get scroll height
    ### This is the difference. Moving this *inside* the loop
    ### means that it checks if scrollTo is still scrolling 
    last_height = driver.execute_script("return document.body.scrollHeight")

    # Scroll down to bottom
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # Wait to load page
    time.sleep(SCROLL_PAUSE_TIME)

    # Calculate new scroll height and compare with last scroll height
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:

        # try again (can be removed)
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        # Wait to load page
        time.sleep(SCROLL_PAUSE_TIME)

        # Calculate new scroll height and compare with last scroll height
        new_height = driver.execute_script("return document.body.scrollHeight")

        # check if the page height has remained the same
        if new_height == last_height:
            # if so, you are done
            break
        # if not, move on to the next loop
        else:
            last_height = new_height
            continue

print('Reaching the end')
print('='*50)

courses = driver.find_elements_by_xpath('//li[@class="item"]')
print(len(courses))

links = [course.find_element_by_xpath('.//div[@class="item-inner"]/a').get_attribute('href') for course in courses]
print(len(links))

for link in links:
    driver.get(link)
    course_dict = {}
    title = course.find_element_by_xpath('title_xpath')
    price = course.find_element_by_xpath('title_xpath')
    author = course.find_element_by_xpath('title_xpath')



# for course in courses:
#   link = course.find_element_by_xpath()


#   course_dict = {}
#   title = course.find_element_by_xpath('title_xpath')
#   price = course.find_element_by_xpath('title_xpath')
#   author = course.find_element_by_xpath('title_xpath')

    # csv_file_writer.write_row(course_dict.values())
driver.close()