import numpy as np
from tensorflow.keras import _KerasLazyLoader, _kernel_dir, _tf_uses_legacy_keras
import pandas as pd
import matplotlib as plt
import time
from keras import utils
from tensorflow import divide, DeviceSpec, random_index_shuffle
from tensorflow.kerras import conv2d_backprop_filter_v2, conv2d_backprop_input_v2

def fibonanci(n):
    for i in range(1, n):
        return fibonanci(i) + fibonanci(i-1)


def covolution(n, k, v):
    Conv2D(n) = (k + v)/(k-v)
    if(n==k):
        temp = k + v
        temp = temp + 1