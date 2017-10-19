# MNIST Data Set Problem Sheet
> Module: Emerging Technologies / 4th Year  
> Lecturer: Dr Ian McLoughlin  
Solutions to the [Read Digits Image Files problem sheet](https://github.com/w326004741/MNIST-Data-Set-Problem-Sheet/wiki/MNIST-Data-Problem-Sheet)

These files work with the famous [MNIST](http://yann.lecun.com/exdb/mnist/) data set. Please download the four data files from that [website](http://yann.lecun.com/exdb/mnist/) and place them (as gz files) in a subfolder called `data/`.

## How to use this repository
1. You must be have [Python 3.x](https://www.python.org/downloads/) and `Git` installed in your local.

2. Enter your `cmd` or [cmder](http://cmder.net/), mac should be `Terminal`, and following below:
```bash
# Change directory to anywhere just you like put
cd anywhere......

# Clone this repository 
git clone https://github.com/w326004741/MNIST-Data-Set-Problem-Sheet.git
&
cd your folder(MNIST-Data-Set-Problem-Sheet)

# You can run any .py file between the three files
python ReadDataFiles.py
python OutputimageToConsole.py
python OutputimageAsPNGs.py
```
#### Run python file before, you need to install in cmd/cmder/terminal: PIL.Image, numpy following below:
- `$ pip install pil`
- `$ pip install numpy`

## What is MNIST?
The MNIST database (Modified National Institute of Standards and Technology database) is a large database of handwritten digits that is commonly used for training various image processing systems. The database is also widely used for training and testing in the field of machine learning. It was created by "re-mixing" the samples from NIST's original datasets. 

The MNIST database of handwritten digits, available from this page, has a training set of 60,000 examples, and a test set of 10,000 examples. It is a subset of a larger set available from NIST. The digits have been size-normalized and centered in a fixed-size image.


