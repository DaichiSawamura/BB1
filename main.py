from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

URI = 'https://goldapple.ru/parfjumerija'
driver = webdriver.Chrome()


def get_source_code(URI) -> None:
    driver.get(url=URI)

    while True:
        try:
            element = WebDriverWait(driver=driver, timeout=2).until(
                expected_conditions.presence_of_element_located((By.CLASS_NAME, "u8yk8"))
            )
            with open("result.txt", "w+", encoding="utf-8") as f:
                f.write(element.text)

            time.sleep(2)
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

            break
        except TimeoutException as _ex:
            print(_ex)
            break


def main() -> None:
    get_source_code(URI)


if __name__ == "__main__":
    main()
