from selenium.webdriver.common.by import By


class OrderPageLocator():
    ORDER_BUTTON_IN_HEADER = By.XPATH, "//div[contains(@class, 'Header_Nav')]/button[text()='Заказать']"
    ORDER_BUTTON_ON_FOOTER = By.XPATH, "//div[contains(@class, 'Home_FinishButton')]/button[text()='Заказать']"
    NAME_FIELD = By.XPATH, ".//input[@placeholder = '* Имя']"
    SURNAME_FIELD = By.XPATH, ".//input[@placeholder = '* Фамилия']"
    ADDRESS_FIELD = By.XPATH, ".//input[@placeholder = '* Адрес: куда привезти заказ']"
    METRO_STATION_FIELD = By.XPATH, ".//input[@placeholder = '* Станция метро']"
    TELEPHONE_NUMBER_FIELD = By.XPATH, ".//input[@placeholder = '* Телефон: на него позвонит курьер']"
    NEXT_STEP_BUTTON = By.XPATH, "//button[text()='Далее']"
    DATE_OF_RENT = By.XPATH, ".//input[@placeholder = '* Когда привезти самокат']"
    PERIOD_OF_RENT = By.XPATH, "//*[contains(@class, 'Dropdown-control')]"
    DROPDOWN = By.XPATH, "//div[@class='Dropdown-option' and text() = 'сутки']"
    COLOR_OF_SCOOTER_1 = By.XPATH, ".//input[@id = 'black']"
    COLOR_OF_SCOOTER_2 = By.XPATH, ".//input[@id = 'grey']"
    COMMENTS = By.XPATH, ".//input[@placeholder = 'Комментарий для курьера']"
    ORDER_BUTTON = By.XPATH, "//*[contains(@class, 'Button_Middle') and contains(text(), 'Заказать')]"
    CONFIRM_BUTTON = By.XPATH, "//button[text()='Да']"
    SUCCESS_MESSAGE = By.XPATH, "//div[contains(text(), 'Заказ оформлен')]"
