from torch.utils.data import DataLoader, Subset
from torchvision import datasets, transforms

from utils.settings import BATCH_SIZE

trans = transforms.Compose([
    transforms.ToTensor()
])



def get_data():

    # CIFAR10
    # train_set = datasets.CIFAR10("./data", train=True, transform=trans, download=True)
    # test_set = datasets.CIFAR10("./data", train=False, transform=trans, download=True)  

    # MINST
    train_set = datasets.MNIST("./data", train=True, transform=trans, download=True)
    test_set = datasets.MNIST("./data", train=False, transform=trans, download=True)  

    # 从训练集中取出一部分作为验证集
    train_len = len(train_set)
    eval_len = int(0.1*train_len)

    eval_set = Subset(train_set, range(eval_len))
    train_set = Subset(train_set, range(eval_len, train_len))

    train_load = DataLoader(train_set, batch_size=BATCH_SIZE)
    eval_load = DataLoader(eval_set, batch_size=BATCH_SIZE)
    test_load = DataLoader(test_set, batch_size=BATCH_SIZE)

    return train_load, eval_load, test_load
