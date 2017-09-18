
# Adapted from: https://stackoverflow.com/questions/12902540/read-from-a-gzip-file-in-python
# Also here: https://stackoverflow.com/questions/2872381/how-to-read-a-file-byte-by-byte-in-python-and-how-to-print-a-bytelist-as-a-binar

import gzip

f = gzip.open('/Users/weichenwang/Year4/Read-Digits-Image-Files-Problem-sheet/Data/t10k-images-idx3-ubyte.gz', 'rb')

magic = f.read(4) #读取4个文件

# this prints : b'\x00\x00\x08\x03'
#In binary this is : 00000000 00000000 00001000 00000011

print(int.from_bytes(magic,'big'))


111