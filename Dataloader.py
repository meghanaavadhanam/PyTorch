import torchvision
import torch
import os
import matplotlib.pyplot as plt
import numpy as np

train_dataset_path = "C:/Users/HP/Documents/meghana-laptop-stuff/downloads+imp/work/W2/AllImageFiles/1"
test_dataset_path = "C:/Users/HP/Documents/meghana-laptop-stuff/downloads+imp/work/W2/AllImageFiles/2"

train_dataset = torchvision.datasets.ImageFolder(root = train_dataset_path, transform = None)
test_dataset = torchvision.datasets.ImageFolder(root = test_dataset_path, transform = None)

train_loader = torch.utils.data.DataLoader(train_dataset, batch_size=1, shuffle= False)
test_loader = torch.utils.data.DataLoader(test_dataset, batch_size=1, shuffle= False)
