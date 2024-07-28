import allure

from pages.base_page import BasePage


class MainPage(BasePage):

    @allure.step('Открыть главную страницу')
    def open_main_page(self):
        self.open_url(self.BASE_URL)

    @allure.step('Проскроллить страницу до тестируемого вопроса')
    def scroll_to_question(self, question):
        self.scroll_to_element(question)

    @allure.step('Тап на вопрос')
    def click_on_question(self, question):
        self.click_element(question)

    @allure.step('Проверить, что текст ответа на вопрос соответствует требованиям')
    def get_answer(self, answer):
        return self.check_text(answer)
