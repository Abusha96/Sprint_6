import allure
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from locators.order_page_locators import OrderPageLocator
from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC


class OrderPage(BasePage):

    @allure.step('Открыть страницу заказа')
    def open_order_page(self, button):
        self.open_url(self.BASE_URL)
        self.scroll_to_element(button)
        self.click_element(button)

    @allure.step('Ввести имя')
    def input_name(self, text):
        self.input(OrderPageLocator.NAME_FIELD, text)

    @allure.step('Ввести фамилию')
    def input_surname(self, text):
        self.input(OrderPageLocator.SURNAME_FIELD, text)

    @allure.step('Ввести адрес')
    def input_address(self, text):
        self.input(OrderPageLocator.ADDRESS_FIELD, text)

    @allure.step('Выбрать станцию метро')
    def input_metrostation(self, metro_station):
        self.wait.until(EC.element_to_be_clickable(OrderPageLocator.METRO_STATION_FIELD)).click()
        metro = f'.//div[text()="{metro_station}"]'
        self.wait.until(EC.element_to_be_clickable((By.XPATH, metro))).click()

    @allure.step('Ввести номер телефона')
    def input_telephone_number(self, text):
        self.input(OrderPageLocator.TELEPHONE_NUMBER_FIELD, text)

    @allure.step('Нажать "Далее"')
    def click_next(self):
        self.click_element(OrderPageLocator.NEXT_STEP_BUTTON)

    @allure.step('Выбрать дату аренды самоката')
    def input_date(self, text):
        self.input(OrderPageLocator.DATE_OF_RENT, text+Keys.RETURN)

    @allure.step('Выбрать период аренды')
    def input_period(self, period):
        self.wait.until(EC.element_to_be_clickable(OrderPageLocator.PERIOD_OF_RENT)).click()
        period = f'.//div[text()="{period}"]'
        self.wait.until(EC.element_to_be_clickable((By.XPATH, period))).click()

    @allure.step('Выбрать цвет самоката')
    def choose_color(self, button):
        self.click_element(button)

    @allure.step('Указать комментарий к заказу')
    def input_comments(self, text):
        self.input(OrderPageLocator.COMMENTS, text)

    @allure.step('Нажать "Заказать"')
    def click_order(self):
        self.click_element(OrderPageLocator.ORDER_BUTTON)

    @allure.step('Подтвердить заказ самоката')
    def click_confirm(self):
        self.click_element(OrderPageLocator.CONFIRM_BUTTON)

    @allure.step('Проверка информационного сообщения об успешном заказе самоката')
    def check_success(self):
        return self.check_text(OrderPageLocator.SUCCESS_MESSAGE)
