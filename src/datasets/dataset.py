import torch

from torch.utils.data import Dataset, DataLoader


class FunctionHistoryDataset(Dataset):
    """ torch dataset """

    def __init__(self):
        pass

    def __len__(self):
        pass

    def __getitem__(self, idx):
        if torch.is_tensor(idx):
            idx = idx.tolist()

