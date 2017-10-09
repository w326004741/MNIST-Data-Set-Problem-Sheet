


import OutputImageToConsole as out
import PIL.Image as pil
import numpy as np


def outImages(type):
    if(type == 'test'):
        for i in range(len(out.ReadDataFiles.test_images)):
           img = pil.fromarray(np.array(out.ReadDataFiles.test_images[i]),mode='RGBA')
           lab = out.ReadDataFiles.test_labels[i]
           # convert image
           img = img.convert('RGB')
           # save image
           imgname = '/Users/weichenwang/Year4/Read-Digits-Image-Files-Problem-sheet/test_images/test-'+str(i)+'-'+str(lab)+'.png'
           img.save(imgname)
    if(type == 'train'):
        for i in range(len(out.ReadDataFiles.train_images)):
            img = pil.fromarray(np.array(out.ReadDataFiles.train_images[i]),mode='RGBA')
            lab = out.ReadDataFiles.train_labels[i]

            img = img.convert('RGB')

            imgname = '/Users/weichenwang/Year4/Read-Digits-Image-Files-Problem-sheet/train_images/train-'+str(i)+'-'+str(lab)+'.png'
            img.save(imgname)
outImages('test')
outImages('train')