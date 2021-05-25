class CustomData(Dataset):
    def __init__(self, data):
        self.data = torch.FloatTensor(data.values.astype('float'))
        
    def __len__(self):
        return len(self.data)
    
    def __getitem__(self, index):
        target = self.data[index][-1]
        data_val = self.data[index] [:-1]
        return data_val,target
