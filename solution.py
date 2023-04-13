import pandas as pd
import numpy as np

from scipy.stats import anderson_ksamp


chat_id = 376970407

def solution(x: np.array, y: np.array) -> bool:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    alpha = 0.06
    p_value = anderson_ksamp([x, y]).pvalue
    
    return p_value < alpha
