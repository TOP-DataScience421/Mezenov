from matplotlib import pyplot as plt
from matplotlib import rcParams
from numpy import array, linspace
from numpy import dot
from numpy import set_printoptions
from csv import reader
from pathlib import Path
from sys import path
from pandas import read_csv
from datetime import datetime, date, timedelta
from dateutil import parser
from pprint import pprint

rcParams['toolbar'] = 'None'
rcParams['font.size'] = 14
rcParams['axes.titlesize'] = 18
set_printoptions(suppress=True)

# Абсолютный путь к файлу с хранящимиси данными
data_path = Path(path[0]) / 'urals_oil_rus_export_prices.csv'
export_prices = read_csv(data_path, comment='#')

data_path = Path(path[0]) / 'dizel_fuel_rus_prices.csv'
rus_prices = read_csv(data_path, comment='#')

# Разбивает DataFrame на ndarray
def dataframe_to_ndarrays_parser(data: 'DataFrame') -> (array,):
    data_arrays = []
    for j in range(len(data.iloc[0][0].split())):
        data_arrays.append([])
        for i in range (len(data)):
            if i:
                data_arrays[j].append(data.iloc[i][0].split()[j])
            else:
                data_arrays[j].append(str(data.iloc[0]).split()[j])
                data_arrays[j].append(data.iloc[i][0].split()[j])
    
    result = []
    
    for array_i in data_arrays:
        result.append(array(array_i))
            
    return tuple(result)

def DatesParser(Date: str) -> datetime:
    """
    Возвращает дату в формате datetime.date
    """
    Monthes = {
        'янв': 1, 
        'фев': 2, 
        'мар': 3, 
        'апр': 4, 
        'май': 5, 
        'июн': 6, 
        'июл': 7, 
        'авг': 8, 
        'сен': 9, 
        'окт': 10, 
        'ноя': 11, 
        'дек': 12}
    
    for m, n in Monthes.items():
        if m in Date:
            result = Date.replace(m, str(n))
            result = result.split('.')
            result = date(year = int('20' + result[2]), month = int(result[1]), day = 1)
            
    return result
    
# Функция вычисления коэффициента корреляции между данными   
def corr_calc(main_data_array: array, main_dates_array: list, sec_data_array: array, sec_dates_array: list, bias: int = 0):
    """
    Делает сдвиг между данными, составляет вариационные ряды для статистической оценки
    Вычисляет все необходимые статистические величины для расчета коэффициента корреляции для переданных в функцию данных
    Возвращает сами данные, сдвиг между данными в месяцах, коэфициент корреляции
    """
    
    data_lists = [[],[],[],[]]
    
    for m_i in range(len(main_data_array)):
        for s_i in range(len(sec_data_array)):
            try:
                if main_dates_array[m_i] + timedelta(0, bias, 0) == sec_dates_array[s_i]:
                    data_lists[0].append(float(main_data_array[m_i - bias]))
                    data_lists[1].append(float(sec_data_array[s_i]))
                    data_lists[2].append(main_dates_array[m_i])
                    data_lists[3].append(bias)
            except IndexError:
                break
    # Объем переданной выборки:
    N = len(main_data_array)
    
    
    # Выделим вектора данных для корреляции
    X_array = array(data_lists[0].copy())
    Y_array = array(data_lists[1].copy())
    
    # Вычислим мат. ожидания и среднеквдратичные отклонения:
    X_mean, X_std = X_array.mean(), X_array.std()
    Y_mean, Y_std = Y_array.mean(), Y_array.std()
    
    # Проведем нормировку данных
    X_norm = (X_array - X_mean) / X_std
    Y_norm = (Y_array - Y_mean) / Y_std
    
    # Мат. ожидания и среднеквдратичные отклонения нормированных величин:
    X_norm_mean, X_norm_std = X_norm.mean(), X_norm.std()
    Y_norm_mean, Y_norm_std = Y_norm.mean(), Y_norm.std()
    
    XY_norm_prod = 0
    for i in range(len(X_norm)):
        XY_norm_prod += X_norm[i] * Y_norm[i]
        
    # корреляционный момент
    XY_corr_moment = XY_norm_prod/N - X_norm_mean*Y_norm_mean
    # коэффициент корреляции
    XY_corr_coeff = XY_corr_moment / (X_norm_std * Y_norm_std)
    
    X_std_bias = X_norm_std * X_std
    Y_std_bias = Y_norm_std * Y_std

    # y = kx + b
    k = XY_corr_coeff * Y_std_bias / X_std_bias
    b = Y_mean - k * X_mean
    
    return X_array.T, Y_array.T, bias, XY_corr_coeff.round(4), k, b
    
export_dates_array, export_prices_array = dataframe_to_ndarrays_parser(export_prices)
rus_dates_array, rus_prices_array = dataframe_to_ndarrays_parser(rus_prices)
export_dates_list, rus_dates_list = [], []

for ind in range(len(export_dates_array)):
    export_dates_list.append(DatesParser(export_dates_array[ind]))

for ind in range(len(rus_dates_array)):
    rus_dates_list.append(DatesParser(rus_dates_array[ind]))

# Сопоставление величин со всеми возможными смещениями
var_lists = []
for i in range(len(rus_prices_array)):
    var_lists.append(corr_calc(export_prices_array, export_dates_list, rus_prices_array, rus_dates_list, i))

# Находим при каком смещении будет максимальный коэффициент корреляции 
max_corr_ind = 0   
max_corr_coef = 0
for ind in range(len(var_lists)):
    if var_lists[ind][3] > max_corr_coef:
        max_corr_coef = var_lists[ind][3]
        max_corr_ind = ind
        
plt.scatter(var_lists[max_corr_ind][0], var_lists[max_corr_ind][1])
plt.scatter(var_lists[max_corr_ind][0].mean(), var_lists[max_corr_ind][1].mean(), s=45, c='#000')
# plt.text(X_mean, Y_mean, ' A')

plt.axline((var_lists[max_corr_ind][0].mean(), var_lists[max_corr_ind][1].mean()), slope=var_lists[max_corr_ind][4], c='#f21', linewidth=3)

data_path = Path(path[0]) / 'regression_fig.png'

plt.savefig(data_path, dpi=300)

# plt.show()

    
