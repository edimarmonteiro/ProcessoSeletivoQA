from selenium import webdriver
from selenium.webdriver.common.by import By
#from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
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
            email_input.send_keys("vivienne565@uorak.com")

            password_input = self.driver.find_element(By.XPATH, '//input[@placeholder="Senha"]')
            password_input.send_keys("#123#123QA")

            login_button = self.driver.find_element(By.XPATH, '//button[text()="Acessar"]')
            login_button.click()

            time.sleep(5)
            error_message = self.driver.find_elements(By.XPATH, '//div[contains(text(), "Email ou senha inválido")]')

            if error_message:
                print("Mensagem de erro encontrada!")
                return False
            else:
                print("Nenhuma mensagem de erro encontrada!")
                return True

        except Exception as e:
            print(f"Erro durante o login: {e}")
            return False

    def create_account(self):
        try:
            time.sleep(5)
            create_account_button = self.driver.find_element(By.XPATH, '//button[text()="Criar nova conta"]')
            create_account_button.click()
        except Exception as e:
            print(f"Erro durante a criação da conta: {e}")

    def fill_user_details(self):
        try:
            time.sleep(5)

            name_input = self.driver.find_element(By.XPATH, '//input[@placeholder="Nome"]')
            name_input.send_keys("Edimar Monteiro")

            email_input = self.driver.find_element(By.XPATH, '//input[@placeholder="E-mail"]')
            email_input.send_keys("vivienne565@uorak.com")

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

            register_button = self.driver.find_element(By.XPATH, '//button[text()="Registrar-se"]')
            register_button.click()
            time.sleep(5)

        except Exception as e:
            print(f"Erro ao preencher os detalhes do usuário: {e}")
    
    def filter_questions(self):
        try:
            filter_discipline = self.driver.find_element(By.CSS_SELECTOR, "div.flex.justify-between.items-center")
            filter_discipline.click()
            time.sleep(3)
            checkboxes = self.driver.find_elements(By.CSS_SELECTOR, "label.container-input .checkmark")
            checkboxes[0].click()
            time.sleep(5)
            
            filter_button = self.driver.find_element(By.XPATH, '//button[text()="Filtrar questões"]')
            self.driver.execute_script("arguments[0].click();", filter_button)
            time.sleep(10)

        except Exception as e:
            print(f"Erro ao realizar filtro: {e}")

if __name__ == "__main__":
    qa_process = QASelectionProcess()
    qa_process.open_site()

    if qa_process.login_user():
        print("Login efetuado com sucesso!")
        qa_process.filter_questions()
    else:
        print("Criando uma nova conta...")
        qa_process.create_account()
        qa_process.fill_user_details()
        qa_process.filter_questions()
