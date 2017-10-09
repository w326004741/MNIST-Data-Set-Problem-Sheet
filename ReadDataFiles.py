
# Adapted from: https://stackoverflow.com/questions/12902540/read-from-a-gzip-file-in-python
# Also here: https://stackoverflow.com/questions/2872381/how-to-read-a-file-byte-by-byte-in-python-and-how-to-print-a-bytelist-as-a-binar

 #读取4个文件
# this prints : b'\x00\x00\x08\x03'
#In binary this is : 00000000 00000000 00001000 00000011


# function to read labels from .gz file
def read_labels_from_file(filename):
    import gzip
    
    with gzip.open(filename, 'rb') as f:
        magic = f.read(4)   # read first 4 bytes
        # magic = int.from_bytes(magic,'big')
        print("Magic Number is: " +str(int.from_bytes(magic,'big')))  # invoke magic
        
        nolab = f.read(4) # read next 4 bytes
        nolab = int.from_bytes(nolab,'big')
        print("Number of labels is : ", nolab) # invoke nolab
        #savae labels to a list
        #labels = []
        #for i in range(nolab):
        #labels.append(f.read(1))
        
        labels = [f.read(1) for i in  range(nolab)]
        labels = [int.from_bytes(label,'big') for label in labels]
        #print(labels)
    return labels 

test_labels = read_labels_from_file('/Users/weichenwang/Year4/Read-Digits-Image-Files-Problem-sheet/Data/t10k-labels-idx1-ubyte.gz')
train_labels = read_labels_from_file('/Users/weichenwang/Year4/Read-Digits-Image-Files-Problem-sheet/Data/train-labels-idx1-ubyte.gz')
#print(train_labels[4999]) #print out the number of picture

# function to read images from .gz file
def read_images_from_file(filename):
    import gzip # use python open a file
    #import numpy as np
    with gzip.open(filename, 'rb') as f:
        magic = f.read(4)   # read first 4 bytes
        # magic = int.from_bytes(magic,'big')
        print("Magic is: " +str(int.from_bytes(magic,'big')))  # invoke magic
        
        noimg = f.read(4)   # read next 4 bytes
        noimg = int.from_bytes(noimg,'big')
        print("Number of images: ", noimg) # invoke noimg

        # read next 4 byte, the number of rows for each image-读取下一个4字节，显示每个图片占多少行
        norow = f.read(4)
        norow = int.from_bytes(norow,'big')
        print("Number of rows: ", norow)

        # read next 4 byte, the number of column for each image-读取下一个4字节，显示每个图片占多少列
        nocol = f.read(4)
        nocol = int.from_bytes(nocol,'big')
        print("Number of columns: ", nocol)
        #labels = []
        #for i in range(nolab):
        #     labels.append(f.read(1))
        
        # save images to a list
        
        #buffer = f.read(norow * nocol * noimg)
        #images = np.frombuffer(buffer, dtype= np.uint8).astype(np.float32)
        #images = images.reshape(noimg, norow, nocol,1) 


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

test_images = read_images_from_file('/Users/weichenwang/Year4/Read-Digits-Image-Files-Problem-sheet/Data/t10k-images-idx3-ubyte.gz')
train_images = read_images_from_file('/Users/weichenwang/Year4/Read-Digits-Image-Files-Problem-sheet/Data/train-images-idx3-ubyte.gz')
#print(train_images[4999])

#should be a 2.
#for row in train_images[4999]:
    #for col in row:
       #print('.' if col <= 127 else '#', end='')
    #print()

#import PIL.Image as pil
#import numpy as np
#img = pil.fromarray(np.array(train_images[4999]))
#img = img.convert('RGB')
#img.show()
#img.save('2.png')