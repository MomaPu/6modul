import requests
from threading import Thread
import time  # Импортируем модуль time

def get_html(link):
    response = requests.get(link)
    page_text = response.text
    print(f"Длина текста страницы {link}: {len(page_text)}")

urls = ['https://www.google.com', 'https://yandex.ru', 'https://ru.wikipedia.org', 'https://vk.com', 'https://ok.ru/']

def parallel_run():
    start_time = time.time()

    threads = [Thread(target=get_html, args=(i,)) for i in urls]

    for t in threads:
        t.start()

    for t in threads:
        t.join()

    parallel_time = time.time() - start_time  
    print(f"Время параллельного выполнения: {parallel_time:.2f} секунд")

def consistently_run():
    start_time = time.time()

    for i in urls:
        get_html(i)

    consistently_time = time.time() - start_time
    print(f"Время последовательного выполнения: {consistently_time:.2f} секунд")

parallel_run()
consistently_run()
