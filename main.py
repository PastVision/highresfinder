import sys
from tqdm import tqdm
import os


class HighRev:
    def __init__(self, folder: str) -> None:
        self.folder = folder
        self.__begin()

    def __begin(self):
        for image in tqdm(next(os.walk(self.folder), (None, None, []))[2]):
            with open(image, 'rb')


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('No path specified!')
    else:
        bot = HighRev(sys.argv[-1])
