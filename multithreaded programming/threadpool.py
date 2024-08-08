import random
import time
from concurrent.futures import ThreadPoolExecutor
from threading import Thread


def download(*, filename):
    start = time.time()
    print(f'start download {filename}.')
    time.sleep(random.randint(3, 6))
    print(f'{filename} Download completed.')
    end = time.time()
    print(f'time consuming to download: {end - start:.3f}Second.')


def main():
    with ThreadPoolExecutor(max_workers=4) as pool:
        filenames = ['Python from entry to hospitalization.pdf', 'MySQL from deleting the database to running away.avi', 'Linux from proficiency to abandonment.mp4']
        start = time.time()
        for filename in filenames:
            pool.submit(download, filename=filename)
    end = time.time()
    print(f'total time spent: {end - start:.3f}Second.')


if __name__ == '__main__':
    main()