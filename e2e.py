import sys

import chromedriver_autoinstaller
from selenium import webdriver
from selenium.webdriver.common.by import By

opt = webdriver.ChromeOptions()
#chromedriver_autoinstaller.install()
driver = webdriver.Chrome(options=opt)

def test_scores_service():
    driver.get('http://127.0.0.1:30001/content')
    result = driver.find_element(By.XPATH, '//*[@id="score"]').text
    assert result == '666', f"The value is an invalid: {result}"
   # input()
    return result


def main_function():
    result = test_scores_service()
    if result == 0:
        sys.exit(0)
    else:
        sys.exit(-1)

test_scores_service()
