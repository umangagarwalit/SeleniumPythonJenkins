import unittest
from selenium import webdriver
import time
from selenium.webdriver.common.by import By


class MyTestCase(unittest.TestCase):

    def test01(self):

        filePath = "\\drivers\\chromedriver.exe"

        url = "https://www.google.com/"

        driver = webdriver.Chrome(filePath)

        time.sleep(1)

        driver.maximize_window()

        time.sleep(1)

        driver.get(url)

        time.sleep(1)

        searchBox = driver.find_element(By.NAME, "q")
        searchBox.send_keys("india")

        time.sleep(1)

        searchButton = driver.find_element(By.NAME, "btnK")
        searchButton.click()

        expectedTitle = "india - Google Search"
        actualTitle = driver.title
        print("Page title is: " + actualTitle)
        self.assertEqual(expectedTitle, actualTitle, "Title is not same")

        time.sleep(2)

        driver.quit()


if __name__ == '__main__':
    unittest.main()
