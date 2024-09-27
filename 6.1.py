import time # Импортируем для работы с временем
from threading import Thread # импорт для параллельной работы

def get_thread(thread_name): 
	
	time.sleep(1)
	print(thread_name)

def run_parallel(): # параллельный запуск
	
	start_time = time.time()
	threads = [Thread(target = get_thread, args=(i,)) for i in ['First', 'Second', 'Third','Fourth','Fifth' ]]
	
	for t in threads:
		t.start()

	for t in threads:
		t.join()
	
	parallel_time = time.time() - start_time
	print(f"Время параллельного выполнения: {parallel_time:.2f} секунд")

def run_consistently(): # поочередный запуск
	start_time = time.time()
	
	for i in ['First', 'Second', 'Third','Fourth','Fifth' ]:
		get_thread(i)
	
	consistently_time = time.time() - start_time
	print(f"Время последовательного выполнения: {consistently_time:.2f} секунд")

run_parallel()
run_consistently()