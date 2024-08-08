import random
import time
from threading import Thread


def download(filename):
    start = time.time()
    print(f'start download {filename}.')
    time.sleep(random.randint(3, 6))
    print(f'{filename} Download completed.')
    end = time.time()
    print(f'time consuming to download: {end - start:.3f} Second.')


def main():
    threads = [
        Thread(target=download, kwargs={'filename': 'Python.pdf'}),
        Thread(target=download, kwargs={'filename': 'PostgresSQL Database.avi'}),
        Thread(target=download, kwargs={'filename': 'Linux.mp4'})
    ]
    start = time.time()
    # start three threads
    for thread in threads:
        thread.start()
    # wait for thread to finish
    for thread in threads:
        thread.join()
    end = time.time()
    print(f'total time spent: {end - start:.3f}Second.')


if __name__ == '__main__':
    main()