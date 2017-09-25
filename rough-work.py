
# Adapted from: https://stackoverflow.com/questions/12902540/read-from-a-gzip-file-in-python
# Also here: https://stackoverflow.com/questions/2872381/how-to-read-a-file-byte-by-byte-in-python-and-how-to-print-a-bytelist-as-a-binar

 #读取4个文件
# this prints : b'\x00\x00\x08\x03'
#In binary this is : 00000000 00000000 00001000 00000011
import gzip
def read_labels_from_file(filename):
    with gzip.open(filename, 'rb') as f:
        magic = f.read(4)
        magic = int.from_bytes(magic,'big')
        print("Magic is: ", magic)
        
        nolab = f.read(4)
        nolab = int.from_bytes(nolab,'big')
        print("Number of labels: ", nolab)

        #labels = []
        #for i in range(nolab):
        #     labels.append(f.read(1))
        


        labels = [f.read(1) for i in  range(nolab)]
        labels = [int.from_bytes(label,'big') for label in labels]
    return labels

test_labels = read_labels_from_file('/Users/weichenwang/Year4/Read-Digits-Image-Files-Problem-sheet/Data/t10k-labels-idx1-ubyte.gz')
train_labels = read_labels_from_file('/Users/weichenwang/Year4/Read-Digits-Image-Files-Problem-sheet/Data/train-labels-idx1-ubyte.gz')
print(train_labels[4999])


def read_images_from_file(filename):
    with gzip.open(filename, 'rb') as f:
        magic = f.read(4)
        magic = int.from_bytes(magic,'big')
        print("Magic is: ", magic)
        
        noimg = f.read(4)
        noimg = int.from_bytes(noimg,'big')
        print("Number of images: ", noimg)


        norow = f.read(4)
        norow = int.from_bytes(norow,'big')
        print("Number of rows: ", norow)

        nocol = f.read(4)
        nocol = int.from_bytes(nocol,'big')
        print("Number of columns: ", nocol)
        #labels = []
        #for i in range(nolab):
        #     labels.append(f.read(1))
        
        images = []
        for i in range(noimg):
            rows = []
            for r in range(norow):
                cols = []
                for c in range(nocol):
                    cols.append(int.from_bytes(f.read(1), 'big'))
                rows.append(cols)
            images.append(rows)
        #labels = [f.read(1) for i in  range(nolab)]
        #labels = [int.from_bytes(label,'big') for label in labels]
    return images


train_images = read_images_from_file('/Users/weichenwang/Year4/Read-Digits-Image-Files-Problem-sheet/Data/train-images-idx3-ubyte.gz')
test_images = read_images_from_file('/Users/weichenwang/Year4/Read-Digits-Image-Files-Problem-sheet/Data/t10k-images-idx3-ubyte.gz')
#print(train_images[4999])

#should be a 2.
for row in train_images[4999]:
    for col in row:
        print('.' if col <= 127 else '#', end='')
    print()

import PIL.Image as pil
import numpy as np
img = pil.fromarray(np.array(train_images[4999]))
img = img.convert('RGB')
img.show()
img.save('2.png')