import torch
from torch import nn
from torch.utils.data import DataLoader
from torch.utils.data import Dataset



class data_set_maker(Dataset):
    device = 'cuda' if torch.cuda.is_available() else 'cpu'
    def __init__(self,a,b):
        self.a = a
        self.b = b
        self.a_ten = torch.tensor(a, dtype=torch.float32,device=device, requires_grad=True)
        self.b_ten = torch.tensor(b, dtype=torch.float32,device=device, requires_grad=True)
    
    def __len__(self):
        return len(self.a_ten)
    
    def __getitem__(self,i):
        return self.a_ten[i], self.b_ten[i]




def data_loader(X, batch, shuf):
    data_set = DataLoader(X, batch, shuffle=shuf)
    
    return data_set







