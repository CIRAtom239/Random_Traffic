from fake_useragent import UserAgent
import threading
import requests
import json
import time


def random_traffic():
    while True:
        with open('config.json') as f:
            templates = json.load(f)

            ua = UserAgent()
            agent = ua.random
            headers = {"User-Agent": agent}

            for j in templates['root_urls']:
                url = j
                try:
                    response = requests.get(url, headers=headers)
                    print(f"{response.status_code} Запрос отправлен на сайт - {url} с таким  User-Agent - {agent}")
                except:
                    print('Ошибка')


def main():
    count = int(input('Введите кол-во: '))

    for i in range(count):
        threading.Thread(target=random_traffic).start()


if __name__ == '__main__':
    main()