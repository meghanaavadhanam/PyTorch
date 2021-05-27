import torchvision
import torch
import numpy as np
from PIL import Image

#image to tensor 

image = Image.open("C:/Users/HP/Documents/meghana-laptop-stuff/downloads+imp/work/W2/AllImageFiles/1/Training/DAT W2-1.jpg")
print(image)
#image.show()


img2np = np.asarray(image)
print(np.shape(img2np))
print('the shape of loaded image transformed into numpy array: {}'.format(np.shape(img2np)))
print('transformed image: {}'.format(img2np))


np2tensor = torchvision.transforms.ToTensor()(img2np)
print('the shape of numpy array transformed into tensor: {}'.format(np.shape(np2tensor)))
print('transformed numpy array: {}'.format(np2tensor))


np2image = torchvision.transforms.ToPILImage("RGB")(np2tensor)
print(np2image)
npArray_2_image.save('datw21_recovery.jpg')
Image._show(np2image)
