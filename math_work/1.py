from numpy import array, dot, exp, pi, sort, average
from matplotlib import pyplot as plt

# распределение Гаусса
def gauss(x, mean, std):
    return exp(-(x - mean)**2 / (2 * std**2)) / (std * (2*pi)**.5)


N = array([1864, 2472, 2123, 2621, 2202, 2701, 2364, 3035, 2386, 3373])
R = array([3043, 3332, 3091, 3338, 3184, 3365, 3244, 3436, 3242, 2461, 3242, 3783, 3311, 3610])

N_n = 10
R_n = 14
alpha = .05

N_mean_sample = dot(1, N) / N_n
R_mean_sample = dot(1, R) / R_n

N_C = N.mean()
N_D_2 = sum((N - N_C)**2) / (N_n - 1)
N_D = N_D_2**0.5

R_C = R.mean()
R_D_2 = sum((R - R_C)**2) / (R_n - 1)
R_D = R_D_2**0.5

N_intervals = {
    (1500,2000): 0,
    (2000,2500): 0,
    (2500,3000): 0,
    (3000,3500): 0,
    # (3000,3300): 0,
}

R_intervals = {
    (2400,2800): 0,
    (2800,3200): 0,
    (3200,3600): 0,
    (3600,4000): 0,
    # (3400,3600): 0,
    # (3600,3800): 0,
}

for N_i in N:
    for rng in N_intervals:
        l, r = rng
        if l <= N_i <= r:
            N_intervals[rng] += 1
            
for R_i in R:
    for rng in R_intervals:
        l, r = rng
        if l <= R_i <= r:
            R_intervals[rng] += 1


print('Вариант №6', end = '\n\n')

print('Данные к обработке:', f'N = {N}', f'R = {R}', sep = '\n', end = '\n\n')

print('Общие мат. ожидания выборок:', f'N_mean = {N_C.round(2)}', f'R_mean = {R_C.round(2)}', sep = '\n', end = '\n\n')

print('Общие среднеквадратичные отклонения выборок:', f'N_std = {N_D.round(3)}', f'R_std = {R_C.round(3)}', sep = '\n', end = '\n\n')

print('Разбивка на интервалы для N:', N_intervals, sep='\n', end='\n\n')
print('Разбивка на интервалы для R:', R_intervals, sep='\n', end='\n\n')

N_m_intervals = array([*N_intervals.values()])
N_intervals_means = array([(l+r)/2 for l, r in N_intervals])

R_m_intervals = array([*R_intervals.values()])
R_intervals_means = array([(l+r)/2 for l, r in R_intervals])

print('Таблица для N: медианы по интервалам - Кол-во значений в интервале:', array([N_intervals_means, N_m_intervals]), sep='\n', end='\n\n')
print('Таблица для R: медианы по интервалам - Кол-во значений в интервале:', array([R_intervals_means, R_m_intervals]), sep='\n', end='\n\n')

N_mean_sample = average(N)
N_var_sample = sum((N_i - N_mean_sample)**2 for N_i in N) / N_n
N_std_sample = N_var_sample ** 0.5

R_mean_sample = average(R)
R_var_sample = sum((R_i - R_mean_sample)**2 for R_i in R) / R_n
R_std_sample = R_var_sample ** 0.5

print('Вариационные ряды для N')
print(
    N_mean_sample,
    N_std_sample,
    sep='\n', 
    end='\n\n'
)
print('данные для R')
print(
    R_mean_sample,
    R_std_sample,
    sep='\n',
    end='\n\n'
)

N_p_intervals = gauss(N_intervals_means, N_mean_sample, N_std_sample)
R_p_intervals = gauss(R_intervals_means, R_mean_sample, R_std_sample)

print('данные для N')
print(array([N_intervals_means.round(4), N_m_intervals.round(4), N_p_intervals.round(4)]), end='\n\n')
print('данные для R')
print(array([R_intervals_means.round(4), R_m_intervals.round(4), R_p_intervals.round(4)]), end='\n\n')


N_Chi_observed = sum((N_m_intervals - N_n*N_p_intervals)**2 / N_n*N_p_intervals)
R_Chi_observed = sum((R_m_intervals - R_n*R_p_intervals)**2 / R_n*R_p_intervals)
N_Chi_Critical = R_Chi_Critical = 3.841

print('Расчитанное Хи для набора N =', N_Chi_observed.round(5), 'Хи критическое из таблицы =', N_Chi_Critical, end ='\n\n')
print('Расчитанное Хи для набора R =', R_Chi_observed.round(5), 'Хи критическое из таблицы =', R_Chi_Critical, end ='\n\n')


if N_Chi_observed < N_Chi_Critical:
    print('нулевая гипотеза для набора данных N принята')
else:
    print('нулевая гипотеза для набора данных N отвергнута')
print()
    
if R_Chi_observed < R_Chi_Critical:
    print('нулевая гипотеза для набора данных R принята')
else:
    print('нулевая гипотеза для набора данных R отвергнута')
print()


def calc(v_cur, v_mean, v_disp, v_n):
    
    return (v_cur - v_mean)/(v_disp * ((v_n-1)/v_n)**.5)
    

def general_hyp_check(v_to_check, v_mean, v_disp, v_n, r_Crit):
    
    r_cur = calc(v_to_check, v_mean, v_disp, v_n)
    
    if r_cur < r_Crit:
        print(f'Крайний член последовательности {v_to_check} с вероятностью {100 - alpha*100} % принадлежит генеральной совокупности')
    else:
        print(f'Крайний член последовательности {v_to_check} не принадлежит генеральной совокупности')
    
    
general_hyp_check(int(N[len(N)-1]), N_C, N_D, N_n, 2.294)
general_hyp_check(int(N[0]), N_C, N_D, N_n, 2.294)
general_hyp_check(int(R[len(R)-1]), R_C, R_D, R_n, 2.294)
general_hyp_check(int(R[0]), R_C, R_D, R_n, 2.294)


# Тестовый запуск
# Вариант №6

# Данные к обработке:
# N = [1864 2472 2123 2621 2202 2701 2364 3035 2386 3373]
# R = [3043 3332 3091 3338 3184 3365 3244 3436 3242 2461 3242 3783 3311 3610]

# Общие мат. ожидания выборок:
# N_mean = 2514.1
# R_mean = 3263.0

# Общие среднеквадратичные отклонения выборок:
# N_std = 443.36
# R_std = 3263.0

# Разбивка на интервалы для N:
# {(1500, 2000): 1, (2000, 2500): 5, (2500, 3000): 2, (3000, 3500): 2}

# Разбивка на интервалы для R:
# {(2400, 2800): 1, (2800, 3200): 3, (3200, 3600): 8, (3600, 4000): 2}

# Таблица для N: медианы по интервалам - Кол-во значений в интервале:
# [[1.75e+03 2.25e+03 2.75e+03 3.25e+03]
 # [1.00e+00 5.00e+00 2.00e+00 2.00e+00]]

# Таблица для R: медианы по интервалам - Кол-во значений в интервале:
# [[2.6e+03 3.0e+03 3.4e+03 3.8e+03]
 # [1.0e+00 3.0e+00 8.0e+00 2.0e+00]]

# Вариационные ряды для N
# 2514.1
# 420.6082381504195

# данные для R
# 3263.0
# 289.39641620843497

# данные для N
# [[1.75e+03 2.25e+03 2.75e+03 3.25e+03]
 # [1.00e+00 5.00e+00 2.00e+00 2.00e+00]
 # [2.00e-04 8.00e-04 8.00e-04 2.00e-04]]

# данные для R
# [[2.6e+03 3.0e+03 3.4e+03 3.8e+03]
 # [1.0e+00 3.0e+00 8.0e+00 2.0e+00]
 # [1.0e-04 9.0e-04 1.2e-03 2.0e-04]]

# Расчитанное Хи для набора N = 0.00236 Хи критическое из таблицы = 3.841

# Расчитанное Хи для набора R = 0.00627 Хи критическое из таблицы = 3.841

# нулевая гипотеза для набора данных N принята

# нулевая гипотеза для набора данных R принята

# Крайний член последовательности 3373 с вероятностью 95.0 % принадлежит генеральной совокупности
# Крайний член последовательности 1864 с вероятностью 95.0 % принадлежит генеральной совокупности
# Крайний член последовательности 3610 с вероятностью 95.0 % принадлежит генеральной совокупности
# Крайний член последовательности 3043 с вероятностью 95.0 % принадлежит генеральной совокупности