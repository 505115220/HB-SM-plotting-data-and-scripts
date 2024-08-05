import pandas as pd
from upsetplot import from_indicators, UpSet
import matplotlib.pyplot as plt
import warnings



warnings.simplefilter(action='ignore', category=FutureWarning)
data = pd.read_excel(r"C:\Users\Zhang Shuai\OneDrive\upset_data.xlsx")
# 创建一个空字典来存储集合和对应的元素
contents = {}
for column in data.columns:                    # 遍历数据框的每一列
    elements = data[column].dropna().tolist()  # 获取当前列的所有非空值
    contents[column] = elements                # 将这些元素添加到字典中，列名作为键
# 找出所有唯一的对象
all_elements = set()
for values in contents.values():
    all_elements.update(values)
# 创建布尔矩阵
data = []
for element in sorted(all_elements):
    row = {set_name: (element in values) for set_name, values in contents.items()}
    row['Element'] = element
    data.append(row)
df = pd.DataFrame(data)  # 将布尔矩阵转换为DataFrame
df = df[[col for col in df.columns if col != 'Element'] + ['Element']]  # 将'Element'列移动到最后一列
df = df.astype({col: bool for col in df.columns if col != 'Element'})   # 将布尔矩阵中的数据类型转换为布尔类型、
# 绘制图像
upset_data = from_indicators(df.columns[:-1], df[df.columns[:-1]])      # 将数据转换为UpSet格式
# 在upset中有几个参数
'''
sort_by='cardinality' # 排序
show_counts=True # 显示柱状图的数值
'''
upset = UpSet(upset_data, show_counts=True)   # 绘制UpSet图，不排序
upset.plot()
plt.suptitle("Five Major Dominant Mononuclear Evaluation Criteria")
plt.show()  # 显示图像
