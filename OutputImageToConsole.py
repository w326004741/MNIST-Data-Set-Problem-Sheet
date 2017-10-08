# Adapted from: https://stackoverflow.com/questions/12902540/read-from-a-gzip-file-in-python
# Also here: https://stackoverflow.com/questions/2872381/how-to-read-a-file-byte-by-byte-in-python-and-how-to-print-a-bytelist-as-a-binar

#import ReadDateFiles.py and numpy
import ReadDataFiles
import numpy as np

# using training set image  
# train_images[4999] ＝ 2 and train_labels[4999] = 2
# print(train_labels[4999]) output value is 2
for row in ReadDataFiles.train_images[4999]:
    for col in row:
        #da ying
       print('.' if col <128 else '#', end='')
    print()

