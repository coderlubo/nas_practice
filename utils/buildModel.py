from torch import nn

from utils.settings import CONV_LAYER, CONV_LAYER_LEN, DEVICE, LINEAR_LAYER, LINEAR_LAYER_LEN, POOLING_LAYER, POOLING_LAYER_LEN

def build_model(code):
    model = nn.Sequential()

    i = 0
    length = len(code)
    last_neurons = 0

    while i < length:
        if code[i] == CONV_LAYER:
            
            if i == 0:
                model.append(nn.Conv2d(in_channels=1, out_channels=code[i+1], kernel_size=code[i+2]))
            else:
                model.append(nn.Conv2d(in_channels=last_neurons, out_channels=code[i+1], kernel_size=code[i+2]))
        
            last_neurons = code[i+1]
            model.append(nn.ReLU())

            i += CONV_LAYER_LEN

        elif code[i] == POOLING_LAYER:

            model.append(nn.MaxPool2d(kernel_size=code[i+1], stride=1))
            i += POOLING_LAYER_LEN
        
        elif code[i] == LINEAR_LAYER:
            model.append(nn.Flatten())
            # model.append(nn.Linear(in_features=size*size*channel, out_features=code[i+1]))
            model.append(nn.LazyLinear(out_features=code[i+1]))
            model.append(nn.ReLU())

            i += LINEAR_LAYER_LEN

    model.append(nn.Linear(in_features=code[-1], out_features=10))
    model.to(DEVICE)

    return model
