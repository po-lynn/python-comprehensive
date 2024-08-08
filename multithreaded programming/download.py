import random
import time


def download(filename):
    start = time.time()
    print(f'start download {filename}.')
    time.sleep(random.randint(3, 6))
    print(f'{filename} Download completed.')
    end = time.time()
    print(f'time consuming to download: {end - start:.3f}Second.')


def main():
    start = time.time()
    download(filename='Python.pdf')
    download(filename='PostgreSQL Database.avi')
    download(filename='Linux.mp4')
    end = time.time()
    print(f'total time spent: {end - start:.3f}Second.')


if __name__ == '__main__':
    main()