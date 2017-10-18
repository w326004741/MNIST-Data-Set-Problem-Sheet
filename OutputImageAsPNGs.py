#import OutputImageToConsole, python imaging library, numpy
import OutputImageToConsole as out
import PIL.Image as pil
import numpy as np
#defined function
def outImages(type):
    #set if loop
    if(type == 'test'):
        #using len() return the length of an object(char,list,tuple,etc.) or number of items
        for i in range(len(out.ReadDataFiles.test_images)):
           #Convert PIL image.img is a PIL image
           img = pil.fromarray(np.array(out.ReadDataFiles.test_images[i]))
           lab = out.ReadDataFiles.test_labels[i]
           #convert RGB mode
           img = img.convert('RGB')
           #save image as RGB mode and output specific file name.
           imgname = '/Gitrepository/Read-Digits-Image-Files-Problem-sheet/test_images/test-'+str(i)+'-'+str(lab)+'.png'
           #save imgname
           img.save(imgname)
    #set if loop
    if(type == 'train'):
        #using len() return the length of an object(char,list,tuple,etc.) or number of items
        for i in range(len(out.ReadDataFiles.train_images)):
            #Convert PIL image.img is a PIL image
            img = pil.fromarray(np.array(out.ReadDataFiles.train_images[i]))
            lab = out.ReadDataFiles.train_labels[i]
            #convert RGB mode
            img = img.convert('RGB')
            #save image as RGB mode and output specific file name.
            imgname = '/Gitrepository/Read-Digits-Image-Files-Problem-sheet/train_images/train-'+str(i)+'-'+str(lab)+'.png'
            #save imgname
            img.save(imgname)
#output images for specific file          
outImages('test')
outImages('train')