from selenium import webdriver
import time
from selenium.webdriver.common.by import By
import pandas as pd

URI = 'https://goldapple.ru/parfjumerija'
driver = webdriver.Chrome()
data = []
save = 'D:/Users/User/Desktop/data.csv'  # <--- здесь нужно указать путь куда будет сохраняться csv файл с результатами



def get_source_code(URI) -> None:
    driver.get(URI)

    while True:
        try:
            driver.maximize_window()

            button = driver.find_element(By.CLASS_NAME, 'IYYkW')  # нужно для корректного отображения html кода
            button.click()
            time.sleep(1)
            for i in range(1, 25):     # парсер первой страницы(24 товара)
                link = driver.find_element(By.XPATH,
                                           f'//*[@id="__layout"]/div/main/div[4]/div[1]/div/div{[i]}/article/a').get_attribute(
                    'href')
                driver.get(link)
                time.sleep(1)
                title = driver.find_element(By.CLASS_NAME, "E91uS").text.strip().replace('\n', ' ')
                des = driver.find_element(By.CLASS_NAME, 'ri-on').text.strip().replace('\n', ' ')
                price = driver.find_element(By.CLASS_NAME, 'HRcnL').text.strip().replace('\n', ' ')
                country_click = driver.find_elements(By.CLASS_NAME, 'ga-tabs-tab')[-1]
                country_click.click()
                time.sleep(1)
                country = driver.find_element(By.CLASS_NAME, 'ri-on').text.strip().replace('\n', ' ')
                data.append([link, title, des, price, country])
                driver.back()
                time.sleep(1)
            header = ['link', 'title', 'des', 'price', 'country']
            df = pd.DataFrame(data, columns=header)
            df.to_csv(save, sep=';', encoding='utf-8-sig')

            for page in range(2, 3):  # парсер 2-ой и следующих страниц(после первой страницы меняется html код сайта)
                driver.get(f'https://goldapple.ru/parfjumerija?p={page}')
                time.sleep(1)
                for i in range(1, 25):
                    link = driver.find_element(By.XPATH,
                                               f'//*[@id="__layout"]/div/main/div[5]/div[1]/div/div{[i]}/article/a'). \
                        get_attribute('href')
                    driver.get(link)
                    time.sleep(1)
                    title = driver.find_element(By.CLASS_NAME, "E91uS").text.strip().replace('\n', ' ')
                    des = driver.find_element(By.CLASS_NAME, 'ri-on').text.strip().replace('\n', ' ')
                    price = driver.find_element(By.CLASS_NAME, 'HRcnL').text.strip().replace('\n', ' ')
                    country_click = driver.find_elements(By.CLASS_NAME, 'ga-tabs-tab')[-1]
                    country_click.click()
                    time.sleep(1)
                    country = driver.find_element(By.CLASS_NAME, 'ri-on').text.strip().replace('\n', ' ')
                    data.append([link, title, des, price, country])
                    driver.back()
                    time.sleep(1)
                header = ['link', 'title', 'des', 'price', 'country']
                df = pd.DataFrame(data, columns=header)
                df.to_csv(save, sep=';', encoding='utf-8-sig')
            break
        except:
            print("ошибка")
            break


def main() -> None:
    get_source_code(URI)


if __name__ == "__main__":
    main()
