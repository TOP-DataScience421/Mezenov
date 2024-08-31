from numpy import array, linspace
from numpy import dot
from numpy import set_printoptions
from csv import reader
from pathlib import Path
from sys import path
from pandas import read_csv



# Абсолютный путь к файлу с хранящимиси данными
data_path = Path(path[0]) / 'science_investetions.csv'
invests = read_csv(data_path, comment='#')

data_path = Path(path[0]) / 'early_malignancy.csv'
malignancy = read_csv(data_path, comment='#')


def dataframe_to_ndarrays_parser(data: 'DataFrame') -> (array,):
    data_arrays = []
    for j in range(len(data.iloc[0][0].split())):
        data_arrays.append([])
        for i in range (len(data)):
            if i:
                data_arrays[j].append(float(data.iloc[i][0].split()[j]))
            else:
                data_arrays[j].append(float(str(data.iloc[0]).split()[j]))
                data_arrays[j].append(float(data.iloc[i][0].split()[j]))
    
    result = []
    
    for array_i in data_arrays:
        result.append(array(array_i))
    
    return tuple(result)
    
def var_constructor(main_data_array: array, main_dates_array: array, sec_data_array: array, sec_dates_array: array, bias: int = 0, freq: 'int|array' = 1) -> dict:
    
    result_dict = {}
    
    for m_i in range(len(main_data_array)):
        for s_i in range(len(sec_data_array)):
            try:
                if main_dates_array[m_i] + bias == sec_dates_array[s_i]:
                    result_dict.setdefault((
                    main_data_array[m_i],
                    sec_data_array[s_i],
                    f'Инвестиции в {int(main_dates_array[m_i])} году',
                    bias,),
                    freq)
            except:
                continue
      
        
    return result_dict
        

# Функция вычисления коэффициента корреляции между данными   
def corr_calc(data_dict: dict,):
    """
    Вычисляет все необходимые статистические величины для расчета коэффициента корреляции для переданных в функцию данных
    Возвращает сами данные, сдвиг между данными в годах, коэфициент корреляции
    """
    
    
    # Объем переданной выборки:
    N = len(data_dict)
    
    
    # Выделим вектора данных для корреляции
    X_array = []
    Y_array = []
    
    for data in data_dict.keys():
        X_array.append(data[0])
        Y_array.append(data[1])
        bias = data[3]
    
    
    X_array = (array(X_array))
    Y_array = (array(Y_array))
   
    
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
    for i in range(N):
        XY_norm_prod += X_norm[i] * Y_norm[i]
        
    # корреляционный момент
    XY_corr_moment = XY_norm_prod/N - X_norm_mean*Y_norm_mean
    # коэффициент корреляции
    XY_corr_coeff = XY_corr_moment / (X_norm_std * Y_norm_std)
    
  
    return f'Входные данные:\n {X_array.T} \n {Y_array.T} \n Сдвиг между данными в годах: {bias} \n коэффициент корреляции данных: {XY_corr_coeff.round(4)}'
        

    
invests_dates_array, invests_data_array = dataframe_to_ndarrays_parser(invests)
malignancy_dates_array, malignancy_data_array = dataframe_to_ndarrays_parser(malignancy)

invests_data_norm = ((invests_data_array - invests_data_array.mean()) / invests_data_array.std()).round(3)
malignancy_data_norm = ((malignancy_data_array - malignancy_data_array.mean()) / malignancy_data_array.std()).round(1)

# Сопоставление величин со всеми возможными смещениями
var_dicts_list = []
for i in range(len(invests_data_norm)):
    var_dicts_list.append(var_constructor(invests_data_array, invests_dates_array, malignancy_data_array, malignancy_dates_array, i))

# Вывод расчетов для всех полученных сопоставлений данных по смещениям
for data in var_dicts_list:
    print(corr_calc(data))

# Некоторые выходные результаты:
# Входные данные:
 # [6.55061743e+08 6.99948879e+08 7.95407851e+08 8.54288044e+08
 # 8.73778706e+08 9.50257085e+08 9.60689437e+08 1.06056038e+09
 # 1.09133347e+09 1.19357851e+09 1.32256392e+09]
 # [50.5 50.8 52.  53.7 54.7 55.6 56.4 57.4 56.3 57.9 59.3]
 # Сдвиг между данными в годах: 0
 # коэффициент корреляции данных: 0.9638
# Входные данные:
 # [5.68386750e+08 6.55061743e+08 6.99948879e+08 7.95407851e+08
 # 8.54288044e+08 8.73778706e+08 9.50257085e+08 9.60689437e+08
 # 1.06056038e+09 1.09133347e+09 1.19357851e+09 1.32256392e+09]
 # [50.5 50.8 52.  53.7 54.7 55.6 56.4 57.4 56.3 57.9 59.3 60.5]
 # Сдвиг между данными в годах: 1
 # коэффициент корреляции данных: 0.9756
# Входные данные:
 # [4.89450799e+08 5.68386750e+08 6.55061743e+08 6.99948879e+08
 # 7.95407851e+08 8.54288044e+08 8.73778706e+08 9.50257085e+08
 # 9.60689437e+08 1.06056038e+09 1.09133347e+09 1.19357851e+09]
 # [50.5 50.8 52.  53.7 54.7 55.6 56.4 57.4 56.3 57.9 59.3 60.5]
 # Сдвиг между данными в годах: 2
 # коэффициент корреляции данных: 0.9883
# Входные данные:
 # [4.61006216e+08 4.89450799e+08 5.68386750e+08 6.55061743e+08
 # 6.99948879e+08 7.95407851e+08 8.54288044e+08 8.73778706e+08
 # 9.50257085e+08 9.60689437e+08 1.06056038e+09 1.09133347e+09]
 # [50.5 50.8 52.  53.7 54.7 55.6 56.4 57.4 56.3 57.9 59.3 60.5]
 # Сдвиг между данными в годах: 3
 # коэффициент корреляции данных: 0.9836
# Входные данные:
 # [4.10864984e+08 4.61006216e+08 4.89450799e+08 5.68386750e+08
 # 6.55061743e+08 6.99948879e+08 7.95407851e+08 8.54288044e+08
 # 8.73778706e+08 9.50257085e+08 9.60689437e+08 1.06056038e+09]
 # [50.5 50.8 52.  53.7 54.7 55.6 56.4 57.4 56.3 57.9 59.3 60.5]
 # Сдвиг между данными в годах: 4
 # коэффициент корреляции данных: 0.9828
# Входные данные:
 # [3.52917701e+08 4.10864984e+08 4.61006216e+08 4.89450799e+08
 # 5.68386750e+08 6.55061743e+08 6.99948879e+08 7.95407851e+08
 # 8.54288044e+08 8.73778706e+08 9.50257085e+08 9.60689437e+08]
 # [50.5 50.8 52.  53.7 54.7 55.6 56.4 57.4 56.3 57.9 59.3 60.5]
 # Сдвиг между данными в годах: 5
 # коэффициент корреляции данных: 0.9684
# Входные данные:
 # [2.77784757e+08 3.52917701e+08 4.10864984e+08 4.61006216e+08
 # 4.89450799e+08 5.68386750e+08 6.55061743e+08 6.99948879e+08
 # 7.95407851e+08 8.54288044e+08 8.73778706e+08 9.50257085e+08]
 # [50.5 50.8 52.  53.7 54.7 55.6 56.4 57.4 56.3 57.9 59.3 60.5]
 # Сдвиг между данными в годах: 6
 # коэффициент корреляции данных: 0.9655
