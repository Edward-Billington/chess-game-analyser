from time import sleep
from progressbar import progressbar
for i in progressbar(range(100), redirect_stdout=True):
    print('Some text', i)
    sleep(0.1)
