from selenium.webdriver.common.by import By
from time import sleep

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_add_to_basket_button(browser):
    browser.get(link)
    button = browser.find_elements(By.CSS_SELECTOR, "#add_to_basket_form button")

    sleep(30)

    assert button, "no add to basket button!"