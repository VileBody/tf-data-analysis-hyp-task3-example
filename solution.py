import pandas as pd
import numpy as np


chat_id = 345534690 # Ваш chat ID, не меняйте название переменной

import numpy as np
from scipy.stats import ttest_ind

def solution(control: np.array, test: np.array) -> bool:
    """
    Функция принимает две выборки показателей NPV (контроль и тест) и возвращает bool-значение,
    отвечая на вопрос: "Отклонить ли нулевую гипотезу" на заданном уровне значимости.
    
    Параметры:
    - control (np.array): Контрольная выборка показателей NPV.
    - test (np.array): Тестовая выборка показателей NPV.
    
    Возвращаемое значение:
    - bool: True, если нулевая гипотеза отклонена на уровне значимости 0.07, иначе False.
    """
    # Уровень значимости
    alpha = 0.07
    
    # Проведение t-теста для независимых выборок
    stat, p_value = ttest_ind(control, test, equal_var=False)
    
    # Проверка, отклоняется ли нулевая гипотеза на уровне значимости 0.07
    return p_value < alpha
