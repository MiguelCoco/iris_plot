import pandas as pd
import seaborn as sn
import matplotlib.pyplot as plt

iris = pd.read_csv('iris.csv')


#根据species分别统计计数的条形图
#countplot = sn.countplot('species',data=iris)

#根据species及petal_length的条形图
#barplot = sn.barplot(x='species',y='petal_length',data=iris)

#根据species及petal_length的箱型图
#boxplot = sn.boxplot(x='species',y='petal_length',data=iris)

#根据petal_length绘制的直方图
#distplot = sn.distplot(iris['petal_length'])

#根据X轴为species分类，Y轴为petal_length的直方图,add_legend()方法显示图例
#sn.FacetGrid(iris,hue='species').map(sn.distplot,'petal_length').add_legend()

#散点图
#sn.regplot(x='petal_length',y='petal_width',data=iris)

#根据species分类，散点图
sn.FacetGrid(iris,hue='species').set (xlim=(0,2.5)).map(sn.regplot,'petal_width','petal_length').add_legend()
plt.show()
