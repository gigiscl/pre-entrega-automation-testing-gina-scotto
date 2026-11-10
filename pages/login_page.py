from selenium.webdriver.common.by import By

# Modulos necesarios para agregar esperas con excepciones
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ex


class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.espera = WebDriverWait(driver,10)

    def ingresar_usuario(self, usuario):
        self.driver.find_element(By.ID, "user-name").send_keys(usuario)

    def ingresar_contraseña(self, contraseña):
        self.driver.find_element(By.ID, "password").send_keys(contraseña)

    def click_login(self):
        self.driver.find_element(By.ID, "login-button").click()

    def login(self, usuario="standard_user", contraseña="secret_sauce"):
        self.ingresar_usuario(usuario)
        self.ingresar_contraseña(contraseña)
        self.click_login()

    def sigue_en_login(self):
        # Retorna si sigue o no en la pagina del login.
        return self.driver.current_url == "https://www.saucedemo.com/"

    def mensaje_errpr(self):
        texto_error = self.espera.until(ex.visibility_of_element_located((By.CSS_SELECTOR, ".error > h3")))
        return texto_error.text    

    