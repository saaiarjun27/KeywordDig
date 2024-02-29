# Install packages
from selenium import webdriver
from selenium.webdriver.common.by import By
import csv

def google_search(keyword, output_file_name):

    # Asking the webdriver to use Chrome browser for the automation
    driver = webdriver.Chrome()
    
    # try, exeception, finally block to try the logic, except if any known exceptions occur and finally close the browser
    try:

        # Mentioning the url that needs to be scrapped for
        url = f"https://www.bing.com/search?q={keyword}"
        driver.get(url)

        # Finding all the SERP on the Bing search by the classname
        results = driver.find_elements(By.CLASS_NAME, "b_algo")

        # Creating the csv and opening it to write the scrapped content
        with open(output_file_name, 'w', encoding='utf-8', newline='') as f:
            csv_writer = csv.writer(f)

            # Scrapping the title, link and short description from the SERP and writing it to the csv
            csv_writer.writerow(['Title', 'Link', 'Detail'])

            # Looping through the search results to scrape every individual results
            for result in results:

                # Scrapping the title by the h2 tag present in the above mentioned class and extracting the text alone
                title = result.find_element(By.CSS_SELECTOR, "h2").text

                # Scrapping the link by the a tag present in the above mentioned class
                link = result.find_element(By.CSS_SELECTOR, "a").get_attribute("href")

                # Scrapping the short description using the below mentioned class
                description_elem = result.find_elements(By.CLASS_NAME, "b_paractl")

                # If the description is not found in the above class, the bot will look for description in the below mentioned class
                if not description_elem:
                    description_elem = result.find_elements(By.CSS_SELECTOR, ".b_lineclamp2.b_algoSlug")

                # Extracting the text alone from the scrapped result
                if description_elem:
                    description = description_elem[0].text

                # If the description cannot be found then leave a message
                else:
                    description = "No description available"

                # Check for None values before replacing commas
                title = title.replace(',', '|') if title else ''
                link = link.replace(',', '|') if link else ''
                description = description.replace(',', '|') if description else ''

                csv_writer.writerow([title, link, description])

    # Excepting the error and printing it 
    except Exception as e:
        print(f"An error occurred: {e}")

    # Closing the browser then the csv file
    finally:
        driver.quit()
        f.close()