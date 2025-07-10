import data
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

# no modificar
def retrieve_phone_code(driver) -> str:
    import json
    import time
    from selenium.common import WebDriverException
    code = None
    for _ in range(10):
        try:
            logs = [log['message'] for log in driver.get_log('performance') if log.get('message') and 'api/v1/number?number' in log['message']]
            for log in reversed(logs):
                msg = json.loads(log)['message']
                body = driver.execute_cdp_cmd('Network.getResponseBody', {'requestId': msg['params']['requestId']})
                code = ''.join(filter(str.isdigit, body['body']))
        except WebDriverException:
            time.sleep(1)
            continue
        if not code:
            raise Exception('No se encontró el código de confirmación del teléfono.')
        return code

class UrbanRoutesPage:
    from_field = (By.ID, 'from')
    to_field = (By.CSS_SELECTOR, '#to')
    comfort_tariff = (By.CLASS_NAME, 'tariff-comfort')
    phone_field = (By.NAME, 'phone')
    send_code_button = (By.CSS_SELECTOR, 'button[data-action="send-code"]')
    code_field = (By.XPATH, '//input[@id="code" and contains(@class, "card-input")]')
    card_number_field = (By.CSS_SELECTOR, 'input#number.card-input')
    card_cvv_field = (By.CLASS_NAME, 'card-input')
    link_card_button = (By.XPATH, '//button[@id="submit-card"]')
    driver_message_field = (By.NAME, 'comment')
    blanket_checkbox = (By.XPATH, '//input[@id="blanket" and @type="checkbox"]')
    tissues_checkbox = (By.CSS_SELECTOR, '.extras #tissues')
    ice_cream_button = (By.CLASS_NAME, 'icecream-btn')
    submit_button = (By.CSS_SELECTOR, 'button.submit-order')

    def __init__(self, driver):
        self.driver = driver

    def set_route(self, from_addr, to_addr):
        # Ingresar ruta de origen y destino
        self.driver.find_element(*self.from_field).send_keys(from_addr)
        self.driver.find_element(*self.to_field).send_keys(to_addr)

    def select_comfort_tariff(self):
        # Seleccionar tarifa Comfort
        self.driver.find_element(*self.comfort_tariff).click()

    def enter_phone_number(self, number):
        # Ingresar número de teléfono
        self.driver.find_element(*self.phone_field).send_keys(number)

    def request_phone_code(self):
        # Solicitar código de confirmación
        self.driver.find_element(*self.send_code_button).click()

    def enter_phone_code(self, code):
        # Ingresar código recibido
        self.driver.find_element(*self.code_field).send_keys(code)

    def add_card(self, number, cvv):
        # Agregar tarjeta y CVV
        self.driver.find_element(*self.card_number_field).send_keys(number)
        cvv_ele = self.driver.find_element(*self.card_cvv_field)
        cvv_ele.send_keys(cvv)
        cvv_ele.send_keys(Keys.TAB)
        self.driver.find_element(*self.link_card_button).click()

    def write_driver_message(self, msg):
        # Escribir mensaje para conductor
        self.driver.find_element(*self.driver_message_field).send_keys(msg)

    def select_extras(self):
        # Pedir manta y pañuelos
        self.driver.find_element(*self.blanket_checkbox).click()
        self.driver.find_element(*self.tissues_checkbox).click()
        # Pedir 2 helados
        btn = self.driver.find_element(*self.ice_cream_button)
        btn.click()
        btn.click()

    def submit_order(self):
        # Confirmar pedido
        self.driver.find_element(*self.submit_button).click()

class TestUrbanRoutes:
    driver = None

    @classmethod
    def setup_class(cls):
        from selenium.webdriver import DesiredCapabilities
        caps = DesiredCapabilities.CHROME
        caps['goog:loggingPrefs'] = {'performance': 'ALL'}
        cls.driver = webdriver.Chrome(desired_capabilities=caps)

    def test_set_route(self):
        self.driver.get(data.urban_routes_url)
        page = UrbanRoutesPage(self.driver)
        page.set_route(data.address_from, data.address_to)
        assert self.driver.find_element(*page.from_field).get_attribute('value') == data.address_from
        assert self.driver.find_element(*page.to_field).get_attribute('value') == data.address_to

    def test_select_plan(self):
        self.driver.get(data.urban_routes_url)
        page = UrbanRoutesPage(self.driver)
        page.select_comfort_tariff()
        assert self.driver.find_element(*page.comfort_tariff).is_selected()

    def test_fill_phone_number(self):
        self.driver.get(data.urban_routes_url)
        page = UrbanRoutesPage(self.driver)
        page.enter_phone_number(data.phone_number)
        page.request_phone_code()
        assert self.driver.find_element(*page.phone_field).get_attribute('value') == data.phone_number

    def test_fill_card(self):
        self.driver.get(data.urban_routes_url)
        page = UrbanRoutesPage(self.driver)
        page.add_card(data.card_number, data.card_code)
        assert self.driver.find_element(*page.link_card_button).is_displayed()

    def test_comment_for_driver(self):
        self.driver.get(data.urban_routes_url)
        page = UrbanRoutesPage(self.driver)
        page.write_driver_message(data.message_for_driver)
        assert self.driver.find_element(*page.driver_message_field).get_attribute('value') == data.message_for_driver

    def test_order_blanket_and_handkerchiefs(self):
        self.driver.get(data.urban_routes_url)
        page = UrbanRoutesPage(self.driver)
        page.select_extras()
        assert self.driver.find_element(*page.blanket_checkbox).is_selected()
        assert self.driver.find_element(*page.tissues_checkbox).is_selected()

    def test_order_2_ice_creams(self):
        self.driver.get(data.urban_routes_url)
        page = UrbanRoutesPage(self.driver)
        page.select_extras()
        assert self.driver.find_element(*page.ice_cream_button) is not None

    def test_car_search_model_appears(self):
        self.driver.get(data.urban_routes_url)
        page = UrbanRoutesPage(self.driver)
        page.submit_order()
        modal = WebDriverWait(self.driver, 10).until(
            expected_conditions.presence_of_element_located((By.ID, 'order-info'))
        )
        assert modal.is_displayed()

    def test_driver_info_appears(self):
        self.driver.get(data.urban_routes_url)
        page = UrbanRoutesPage(self.driver)
        page.submit_order()
        info = WebDriverWait(self.driver, 15).until(
            expected_conditions.presence_of_element_located((By.ID, 'driver-info'))
        )
        assert info.is_displayed()

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
