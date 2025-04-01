from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time


class QASelectionProcess:
    def __init__(self):
        self.SITE_URL = "https://questions-dev.mege.com.br/login"
        self.driver = webdriver.Chrome()

    def open_site(self):
        self.driver.get(self.SITE_URL)

    def login_user(self):
        try:
            time.sleep(5)

            email_input = self.driver.find_element(By.XPATH, '//input[@placeholder="E-mail"]')
            email_input.send_keys("choumicha4995@uorak.com")

            password_input = self.driver.find_element(By.XPATH, '//input[@placeholder="Senha"]')
            password_input.send_keys("#123#123QA")

            login_button = self.driver.find_element(By.XPATH, '//button[text()="Acessar"]')
            login_button.click()

            time.sleep(5)
            error_message = self.driver.find_elements(By.XPATH, '//div[contains(text(), "Email ou senha inválido")]')

            if error_message:
                print("Error message found!")
                return False
            else:
                print("No error message found!")
                return True

        except Exception as e:
            print(f"Error during login: {e}")
            return False

    def create_account(self):
        try:
            time.sleep(5)
            create_account_button = self.driver.find_element(By.XPATH, '//button[text()="Criar nova conta"]')
            create_account_button.click()
        except Exception as e:
            print(f"Error during account creation: {e}")

    def fill_user_details(self):
        try:
            time.sleep(5)

            name_input = self.driver.find_element(By.XPATH, '//input[@placeholder="Nome"]')
            name_input.send_keys("Edimar Monteiro")

            email_input = self.driver.find_element(By.XPATH, '//input[@placeholder="E-mail"]')
            email_input.send_keys("choumicha4995@uorak.com")

            phone_input = self.driver.find_element(By.XPATH, '//input[@placeholder="Telefone"]')
            phone_input.send_keys("(99)912345678")

            birthdate_input = self.driver.find_element(By.XPATH, '//input[@placeholder="Data de nascimento"]')
            birthdate_input.send_keys("2000-01-10")

            password_input = self.driver.find_element(By.XPATH, '//input[@placeholder="Senha"]')
            password_input.send_keys("#123#123QA")

            confirm_password_input = self.driver.find_element(By.XPATH, '//input[@placeholder="Confirme a senha"]')
            confirm_password_input.send_keys("#123#123QA")

            terms_checkbox = self.driver.find_element(By.NAME, "connection")
            if not terms_checkbox.is_selected():
                terms_checkbox.click()

            register_button = self.driver.find_element(By.
                                                       XPATH, '//button[text()="Registrar-se"]')
            register_button.click()
            time.sleep(5)

        except Exception as e:
            print(f"Error filling user details: {e}")

if __name__ == "__main__":
    qa_process = QASelectionProcess()
    qa_process.open_site()

    if qa_process.login_user():
        print("Logged in successfully!")
        qa_process.filter_questions()
    else:
        print("Login failed. Creating a new account...")
        qa_process.create_account()
        qa_process.fill_user_details()
