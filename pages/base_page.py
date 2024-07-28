import allure
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:

    BASE_URL = 'https://qa-scooter.praktikum-services.ru/'

    def __init__(self, driver: webdriver.Firefox, wait: WebDriverWait):
        self.driver = driver
        self.wait = wait

    @allure.step('Перейти на страницу')
    def open_url(self, url):
        self.driver.get(url)

    @allure.step('Тап по элементу')
    def click_element(self, locator):
        element = self.wait.until(EC.element_to_be_clickable(locator))
        self.driver.execute_script("arguments[0].click();", element)

    @allure.step('Ввести данные')
    def input(self, locator, keys):
        self.wait.until(EC.visibility_of_element_located(locator)).send_keys(keys)

    @allure.step('Получить URL')
    def get_url(self):
        return self.driver.current_url

    @allure.step('Проверить текст')
    def check_text(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator)).text

    @allure.step('Проскроллить до элемента')
    def scroll_to_element(self, locator):
        Q = self.wait.until(EC.visibility_of_element_located(locator))
        self.driver.execute_script(
            "arguments[0].scrollIntoView();", Q)

    @allure.step('Открыть новую страницу')
    def open_new_page(self, text):
        self.wait.until(EC.number_of_windows_to_be(2))
        self.driver.switch_to.window(self.driver.window_handles[-1])
        self.wait.until(lambda driver: text in driver.current_url)
