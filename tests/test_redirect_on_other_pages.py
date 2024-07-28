import allure

from locators.redirect_page_locators import RedirectButtons
from pages.main_page import MainPage


class TestRedirectPage:
    @allure.title('Редирект на Дзен при клике на лого "Яндекс"')
    def test_redirect_to_dzen(self, driver, wait):
        redirect_page = MainPage(driver, wait)
        redirect_page.open_main_page()
        redirect_page.click_element(RedirectButtons.YANDEX_LOGO)
        redirect_page.open_new_page('dzen')
        assert 'dzen' in redirect_page.get_url()

    @allure.title('Редирект на главную при клике на лого "Самокат"')
    def test_redirect_to_scooter(self, driver, wait):
        redirect_page = MainPage(driver, wait)
        redirect_page.open_main_page()
        redirect_page.click_element(RedirectButtons.SAMOKAT_LOGO)
        assert redirect_page.get_url() == redirect_page.BASE_URL
