import time
from multiprocessing import Pool

def read_info(name):
    all_data = []
    with open(name, 'r', encoding='utf-8') as file:
         while True:
             line = file.readline()
             if not line:
                 break
             all_data.append(line)

if __name__ == '__main__':
    filenames = [f'./file {number}.txt' for number in range(1, 5)]

    # Линейный вызов
    start_time = time.time()
    for filename in filenames:
        read_info(filename)
    print(f'Линейный запуск занял: {time.time() - start_time:.6f} секунд')
    # Многопроцессный
    start_time = time.time()
    with Pool(4) as pool:
        map(read_info, filenames)
    print(f'Многопроцессный запуск занял: {time.time() - start_time:.6f} секунд')