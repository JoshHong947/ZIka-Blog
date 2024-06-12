import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm

# 读取数据
data = pd.read_excel('graduation demo/Final_Cleaned_Data.xlsx')
data['Year'] = pd.to_datetime(data['Year'], format='%Y')
data.set_index('Year', inplace=True)

# 提取需要的列
gdp_growth = data['GDP growth (annual %)']
population_growth = data['Population growth (annual %)']

# 绘制数据
plt.figure(figsize=(10, 6))
plt.plot(gdp_growth, label='GDP Growth')
plt.plot(population_growth, label='Population Growth')
plt.legend()
plt.title('GDP and Population Growth Rates Over Time')
plt.show()

# 门限自回归模型
# 创建门限自回归模型
class ThresholdAutoregressiveModel:
    def __init__(self, data, threshold):
        self.data = data
        self.threshold = threshold
        self.model_low = None
        self.model_high = None

    def fit(self):
        low_data = self.data[self.data <= self.threshold]
        high_data = self.data[self.data > self.threshold]
        self.model_low = sm.tsa.AR(low_data).fit()
        self.model_high = sm.tsa.AR(high_data).fit()

    def predict(self, steps):
        pred_low = self.model_low.predict(start=len(self.data), end=len(self.data) + steps - 1)
        pred_high = self.model_high.predict(start=len(self.data), end=len(self.data) + steps - 1)
        return pred_low, pred_high

# 设置门限值（根据前文数据分析选择）
threshold = data['Male labor participation rate (15-64)'].mean()
tar_model = ThresholdAutoregressiveModel(population_growth, threshold)
tar_model.fit()

# 预测未来几年的人口增长率
steps = 10
pred_low, pred_high = tar_model.predict(steps)

# 打印预测结果
print("Predictions (low regime):", pred_low)
print("Predictions (high regime):", pred_high)

# 绘制预测结果
plt.figure(figsize=(10, 6))
plt.plot(population_growth, label='Observed Population Growth')
plt.plot(pd.date_range(start=population_growth.index[-1], periods=steps + 1, freq='A')[1:], pred_low, label='Predicted (Low Regime)')
plt.plot(pd.date_range(start=population_growth.index[-1], periods=steps + 1, freq='A')[1:], pred_high, label='Predicted (High Regime)')
plt.legend()
plt.title('Population Growth Rate Predictions')
plt.show()
