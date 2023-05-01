import pytest
from selenium import webdriver


def test_open_practice():
    driver = webdriver.Chrome()

    driver.get("https://stepik.org/learn")

    assert "Stepik" in driver.title
    driver.quit()
