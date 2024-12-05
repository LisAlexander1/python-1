import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.svm import SVR
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error
import matplotlib.pyplot as plt
import numpy as np


# Загрузка данных
data = pd.read_csv('./5/MSPUS.csv')

# 2. Исследуем данные
print(data.head())
print(data.info())
#----------------------------------------------------------------------------------------


# 3. выполнить предварительную обработку данных 

# Преобразование столбца DATE в формат datetime
data['DATE'] = pd.to_datetime(data['DATE'])

# Проверка пропущенных значений
print(data.isnull().sum())

# Удаление или заполнение пропущенных значений (например, методом заполнения медианой)
data.fillna(data.median(), inplace=True)
#----------------------------------------------------------------------------------------

# Создадим новый столбец для числового представления даты
data['DATE_numeric'] = (data['DATE'] - data['DATE'].min()).dt.days


X = data[['DATE_numeric']]  # Признаки
y = data['MSPUS']  # Целевая переменная

# Маштабирование
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Разделим данные на обучающую и тестовую выборки
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)
#----------------------------------------------------------------------------------------


'''
Линейная регрессия - Простая и быстрая модель для анализа тренда.

Случайный лес: Работает с нелинейными зависимостями

Градиентный бустинг: Предоставляет более точные прогнозы для сложных, нелинейных данных
'''

# Линейная регрессия
linear_model = LinearRegression()
linear_model.fit(X_train, y_train)

# Случайный лес
rf_model = RandomForestRegressor(n_estimators=100, random_state=42)
rf_model.fit(X_train, y_train)

# Градиентный бустинг
gb_model = GradientBoostingRegressor(n_estimators=100, random_state=42)
gb_model.fit(X_train, y_train)

'''
Средняя абсолютная ошибка (MAE) — оценивает, насколько близки предсказания к реальным значениям.
Среднеквадратическая ошибка (MSE) —  чувствительна к выбросам.
R² — показывает, насколько хорошо модель объясняет изменения в целевой переменной.
'''

# Предсказания для тестовых данных
y_pred_linear = linear_model.predict(X_test)
y_pred_rf = rf_model.predict(X_test)
y_pred_gb = gb_model.predict(X_test)

# Оценка качества моделей
print("Linear Regression - R²:", r2_score(y_test, y_pred_linear), "MAE:", mean_absolute_error(y_test, y_pred_linear))
print("Random Forest - R²:", r2_score(y_test, y_pred_rf), "MAE:", mean_absolute_error(y_test, y_pred_rf))
print("Gradient Boosting - R²:", r2_score(y_test, y_pred_gb), "MAE:", mean_absolute_error(y_test, y_pred_gb))


future_dates = pd.DataFrame({'DATE_numeric': [max(data['DATE_numeric']) + i for i in range(1, 365*2)]})
future_dates_scaled = scaler.transform(future_dates)
future_predictions = rf_model.predict(future_dates_scaled)

print("Прогноз на будущее:")
print(future_predictions)