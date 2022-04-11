from selenium import webdriver

# Here chrome webdriver is used
driver = webdriver.Chrome()

# URL of the website
url = "https://studio.youtube.com/channel/UCrLtsfmAKB03dd9ciTJfFoQ/livestreaming/dashboard"

# Opening the URL
driver.get(url)

# Getting current URL
get_url = driver.current_url

# Printing the URL
print(get_url)