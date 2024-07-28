import allure
import pytest
from pages.main_page import MainPage
from locators.faq_on_main_page_locators import FAQ


class TestQuestions():
    @pytest.mark.parametrize('question, answer, expected_text',
                             [
        [FAQ.QUESTION_1, FAQ.ANSWER_1, 'Сутки — 400 рублей. Оплата курьеру — наличными или картой.'],
        [FAQ.QUESTION_2, FAQ.ANSWER_2, 'Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим.'],
        [FAQ.QUESTION_3, FAQ.ANSWER_3, 'Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30.'],
        [FAQ.QUESTION_4, FAQ.ANSWER_4, 'Только начиная с завтрашнего дня. Но скоро станем расторопнее.'],
        [FAQ.QUESTION_5, FAQ.ANSWER_5, 'Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010.'],
        [FAQ.QUESTION_6, FAQ.ANSWER_6, 'Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится.'],
        [FAQ.QUESTION_7, FAQ.ANSWER_7, 'Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои.'],
        [FAQ.QUESTION_8, FAQ.ANSWER_8, 'Да, обязательно. Всем самокатов! И Москве, и Московской области.']
                                 ]
                             )
    @allure.title('Корректное отображение ответов на вопросы')
    def test_answer_text(self, driver, wait, question, answer, expected_text):
        main_page = MainPage(driver, wait)
        main_page.open_main_page()
        main_page.scroll_to_question(question)
        main_page.click_on_question(question)
        assert main_page.get_answer(answer) == expected_text
