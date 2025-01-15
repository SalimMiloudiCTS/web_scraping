from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Initialize the WebDriver
driver = webdriver.Chrome()  # or webdriver.Firefox() for Firefox

# Go to https://www.google.com and print page title
driver.get("https://quotes.toscrape.com/page/1")
print(f"Page title: {driver.title}")

# Find all quote elements
quote_elements = driver.find_elements(By.CLASS_NAME, "quote")

# List to store the parsed data
data = []

# Loop through each quote element to extract details
for quote_element in quote_elements:
    dic = {}
    
    # Extract the quote text
    dic["quote"] = quote_element.find_element(By.CLASS_NAME, "text").text
    
    # Extract the author name
    dic["author"] = quote_element.find_element(By.CLASS_NAME, "author").text
    
    # Extract tags
    tag_elements = quote_element.find_elements(By.CLASS_NAME, "tag")
    dic["tags"] = [tag.text for tag in tag_elements]
    
    # Append the dictionary to the data list
    data.append(dic)

# Print the parsed data
for item in data:
    print(item)

#driver.quit()

# Wait for a few seconds to see the results
time.sleep(5)

# Close the browser
driver.quit()