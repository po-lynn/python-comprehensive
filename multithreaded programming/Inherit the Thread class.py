import random
import time
from threading import Thread


class DownloadThread(Thread):

    def __init__(self, filename):
        self.filename = filename
        super().__init__()

    def run(self):
        start = time.time()
        print(f'start download {self.filename}.')
        time.sleep(random.randint(3, 6))
        print(f'{self.filename} Download completed.')
        end = time.time()
        print(f'time consuming to download: {end - start:.3f}Second.')


def main():
    threads = [
        DownloadThread('Python from entry to hospitalization.pdf'),
        DownloadThread('MySQL from deleting the database to running away.avi'),
        DownloadThread('Linux from proficiency to abandonment.mp4')
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