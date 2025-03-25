import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from statsmodels.tsa.arima.model import ARIMA
from sklearn.metrics import mean_squared_error

df = pd.read_csv("synthetic_stock_data.csv")

# Преобразуем даты
df["Date"] = pd.to_datetime(df["Date"])

# Выбираем Tesla
company = "Tesla"
df_company = df[df["Company"] == company].copy()

# Сортируем по дате (если вдруг не отсортировано)
df_company = df_company.sort_values(by="Date")
# Рассчитываем скользящее среднее (например, 5-дневное)
df_company["SMA_5"] = df_company["Close"].rolling(window=5).mean()

# Создаем график
plt.figure(figsize=(14, 7))

# График цены закрытия
plt.plot(df_company["Date"], df_company["Close"], label="Цена закрытия", marker="o", linestyle="-", color="blue")

# График скользящего среднего
plt.plot(df_company["Date"], df_company["SMA_5"], label="Скользящее среднее (5)", linestyle="dashed", color="red")

# Заголовок и подписи
plt.title(f"Динамика цен акций {company}", fontsize=14, fontweight="bold")
plt.xlabel("Дата", fontsize=12)
plt.ylabel("Цена закрытия (USD)", fontsize=12)

# Улучшение читаемости осей
plt.xticks(rotation=45)
plt.grid(True, linestyle="--", alpha=0.5)

# Добавление легенды
plt.legend()

# Отображение графика
plt.show()