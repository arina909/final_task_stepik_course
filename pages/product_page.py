from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import ProductPageLocators
from .locators import LoginPageLocators

class ProductPage(BasePage):

    def add_product_to_basket(self):
        button = self.browser.find_element(*ProductPageLocators.BASKET_BUTTON)
        button.click()
        self.solve_quiz_and_get_code()
        self.should_be_certain_book_name()
        self.should_be_the_same_prise()
        
    def should_be_certain_book_name(self):
        
        assert (self.browser.find_element(*ProductPageLocators.MESSAGE_BOOK_NAME).text == self.browser.find_element(*ProductPageLocators.BOOK_NAME).text), "names are not equal" 

    def should_be_the_same_prise(self):
        assert (self.browser.find_element(*ProductPageLocators.BASKET_BOOK_PRICE).text == self.browser.find_element(*ProductPageLocators.BOOK_PRICE).text), "prices are not equal"
