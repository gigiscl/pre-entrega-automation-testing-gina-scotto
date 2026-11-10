from selenium.webdriver.common.by import By

class LoginPage:
    def __init__(self, driver):
        self.driver = driver

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

    