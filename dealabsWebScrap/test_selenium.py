from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# Remplacez par le chemin vers votre ChromeDriver
service = Service("C:/WebDrivers/chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get("https://www.google.com")
print(driver.title)  # Devrait afficher "Google"
driver.quit()