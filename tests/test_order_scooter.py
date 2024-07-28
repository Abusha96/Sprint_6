import allure
import pytest

from locators.order_page_locators import OrderPageLocator
from pages.order_page import OrderPage


class TestOrderPage():
    @pytest.mark.parametrize('button, name, surname, address, metro_station, phone, date, period, color, comment', [
        [OrderPageLocator.ORDER_BUTTON_IN_HEADER, 'Иван', 'Смирнов', 'ул. Ленина, 45', 'Черкизовская', '79151234567', '01.08.2014', 'сутки', OrderPageLocator.COLOR_OF_SCOOTER_1, 'Привет'],
        [OrderPageLocator.ORDER_BUTTON_ON_FOOTER, 'Татьяна', 'Иванова', 'ул. Маркса, 26', 'Сокольники', '78005553535', '25.07.2014', 'двое суток', OrderPageLocator.COLOR_OF_SCOOTER_2, 'Андрей']
    ])
    @allure.title('Заказ самоката')
    def test_order_scooter(self, driver, wait, button, name, surname, address, metro_station, phone, date, period, color, comment):
        order_page = OrderPage(driver, wait)
        order_page.open_order_page(button)
        order_page.input_name(name)
        order_page.input_surname(surname)
        order_page.input_address(address)
        order_page.input_metrostation(metro_station)
        order_page.input_telephone_number(phone)
        order_page.click_next()
        order_page.input_date(date)
        order_page.input_period(period)
        order_page.choose_color(color)
        order_page.input_comments(comment)
        order_page.click_order()
        order_page.click_confirm()
        assert 'Заказ оформлен' in order_page.check_success()
