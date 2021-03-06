# 导入模块
import pandas as pd  # 导入数据统计模块
import matplotlib  # 导入图表模块
import matplotlib.pyplot as plt  # 导入绘图模块

# 避免中文乱码
matplotlib.rcParams['font.sans-serif'] = ['SimHei']  # 设置字体为SimHei显示中文
matplotlib.rcParams['axes.unicode_minus'] = False  # 设置正常显示字符，使用rc配置文件来自定义
# 简单清洗
data = pd.read_csv('DataShow\data.csv')  # 读取csv数据
del data['Unnamed: 0']  # 将索引列删除
data.dropna(axis=0, how='any', inplace=True)  # 删除data数据中的所有空值
data['单价'] = data['单价'].map(lambda d: d.replace('元/平米', ''))  # 将单价“元/平米”去掉
data['单价'] = data['单价'].astype(float)  # 将房子单价转换为浮点类型，float（data['',单价]）

data['总价'] = data['总价'].map(lambda d: d.replace('万', ''))  # 将总价“万”去掉
data['总价'] = data['总价'].astype(float)  # 将房子总价转换为浮点类型，float（data['',单价]）

data['建筑面积'] = data['建筑面积'].map(lambda p: p.replace('平米', ''))  # 将建筑面积“平米去掉”
data['建筑面积'] = data['建筑面积'].astype(float)  # 将将建筑面积转换为浮点类型


# 获取各区二手房均价分析，根据需求，，进一步处理数据，如果要写相应算法，需要根据算法所需求的数据处理
def get_average_price():
    group = data.groupby('区域')  # 将房子区域分组
    average_price_group = group['单价'].mean()  # 计算每个区域的均价，average_price_group字典
    x = average_price_group.index  # 区域
    y = average_price_group.values.astype(int)  # 区域对应的均价a =['t':'123'] a.keys()
    return x, y  # 返回区域与对应的均价，region二关 average_price均价


# 显示均价条形图
def average_price_bar(x, y, title):
    plt.figure()  # 图形画布
    plt.bar(x, y, alpha=0.8)  # 绘制条形图
    plt.xlabel("区域")  # 区域文字
    plt.ylabel("均价")  # 均价文字
    plt.title(title)  # 表标题文字
    # 为每一个图形加数值标签
    for x, y in enumerate(y):
        plt.text(x, y + 100, y, ha='center')
    plt.show()


if __name__ == '__main__':
    x, y = get_average_price()
    title = '各区均价分析'
    average_price_bar(x, y, title)
