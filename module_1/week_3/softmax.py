import torch
import torch.nn as nn


data = torch.Tensor([1, 2, 3])
softmax_function = nn.Softmax(dim=0)
output = softmax_function(data)
print(output)

class SoftmaxStable(nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x:torch.Tensor):
        exp_x = torch.exp(x)
        return exp_x / exp_x.sum()

data = torch.Tensor([1,2,3])
my_softmax = SoftmaxStable()
output = my_softmax(data)
print(output)