from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
import time

def parse_sprosivracha(prep_name, chrome_path='chromedriver.exe', pages_count=20):
    service = Service(chrome_path)
    options = webdriver.ChromeOptions()
    # options.add_argument("--headless")
    options.add_argument("--disable-blink-features=AutomationControlled")
    driver = webdriver.Chrome(service=service, options=options)
    # driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
    #     "source": """
    #         delete window.cdc_adoQpoasnfa76pfcZLmcfl_Array;
    #         delete window.cdc_adoQpoasnfa76pfcZLmcfl_Object;
    #         delete window.cdc_adoQpoasnfa76pfcZLmcfl_Promise;
    #         delete window.cdc_adoQpoasnfa76pfcZLmcfl_JSON;
    #         delete window.cdc_adoQpoasnfa76pfcZLmcfl_Proxy;
    #         delete window.cdc_adoQpoasnfa76pfcZLmcfl_Window;
    #         delete window.cdc_adoQpoasnfa76pfcZLmcfl_Symbol;
    #                        """
    # })
    print("driver loaded")
    questions = []
    url = f"https://sprosivracha.com/search/?q={prep_name}"
    driver.get(url)
    time.sleep(10)
    # Проходим по 20 страницам (номер страницы подставляется в URL)
    for page in range(1, pages_count + 1):
        url = f"https://sprosivracha.com/search/{page}?q={prep_name}"
        driver.get(url)
        print(f"url goten: {url}")
        time.sleep(1)
        html = driver.page_source
        print("html goten")
        soup = BeautifulSoup(html, 'html.parser')
        # берем текст из поля div с классом text(нужное поле можно посмотреть открыв страницу, пкм, просмотреть код,
        # потом там есть elements concole sources и слева от этих вкладок 2 значка, нажимаем на первый, выбираем текст, который хотим находить и смотрим,
        # че у него за тег(обычно div) и его класс, должно быть class=
        for a in soup.find_all('div', class_='text'):
            text = a.getText().strip()
            questions.append(text)

    driver.quit()

    return questions
if __name__ == "__main__":
    questions = parse_sprosivracha("Эсциталопрам", chrome_path="chromedriver.exe")
    print(len(questions), "вопросов получено")
    for i in questions:
        print(i)

