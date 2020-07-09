from PyQt5.QtChart import QChartView, QChart, QPieSeries, QLineSeries, QValueAxis, QCategoryAxis
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QWidget
from PyQt5 import QtWidgets, Qt

# 本文件的代码部分参考了 https://github.com/PyQt5/PyQt/tree/master/QtChart 的自定义坐标轴

class statistic(QWidget):
    def __init__(self, *args, **kwargs):
       super(statistic, self).__init__(*args, **kwargs)

       self.resize(1500,700)

    def get_line_series(self):
        """
        TODO:订单管理界面点击统计调用该函数，计算订单管理界面当前搜索范围内 每天 的订单销售总额，
             然后范围内 第一天 作为 第0天 即 i=0 按顺序以以下格式放入 series 和 category 中，series.append(i, 第 i 天销售额)
             category.append('20-7-07') <- 那天具体的日期
        """
        totals, category = self.database.stat_1(*self.data)
        series = QLineSeries()
        for i in range(len(category)):
            series.append(i,totals[i])

        return series, category

    def get_pie_series(self):
        """
        TODO:订单管理界面点击统计调用该函数，计算订单管理界面当前搜索范围内所有订单 各大类 书的销售额
             按以下格式放入 series.append('类别x%', 销售额)
        """
        totals, classes = self.database.stat_2(*self.data)
        all_total = sum(totals)
        if all_total:
            series = QPieSeries()
            for i in range(len(totals)):
                if totals[i]:
                    word = (classes[i] + ' %.2f' % (totals[i]))
                    series.append(word, totals[i])
        else:
            series = QPieSeries()
            series.append('无销售', 1)
        series.setLabelsVisible()
        series.setPieSize(0.7)

        return series

    def customAxisX(self, chart, category):
        series = chart.series()
        if not series:
            return
        axisx = QCategoryAxis(
            chart, labelsPosition=QCategoryAxis.AxisLabelsPositionOnValue)
        axisx.setGridLineVisible(False)  # 隐藏网格线条
        minx = chart.axisX().min()
        maxx = chart.axisX().max()
        if len(category) == 1:
            axisx.append(category[0], (minx + maxx) / 2)
        else:
            num_step = len(category) // 10 + 1  # 每到10的倍数多跳一天 s为每次跳的天数
            residue = (len(category) - 1) % num_step  # 1+sk恰大于n
            real_consider = len(category) - residue  # 最后一个刻度所在位置
            num_tick = ((real_consider - 1) // num_step) + 1  # 刻度数量

            axisx.setTickCount(num_tick)  # 设置刻度个数
            step_len = ((maxx - minx) * ((len(category) - residue - 1) / (len(category) - 1))) / (num_tick - 1)
            # step = (maxx - minx) / (tickc - 1)  # tickc>=2
            for i in range(0, num_tick):
                axisx.append(category[i*num_step], minx + i * step_len)
        series[-1].attachAxis(axisx)  # 附加到series上
        chart.setAxisX(axisx, series[-1])

    def get_line_chart(self):
        chart = QChart(title = '每日销售额')
        series, category = self.get_line_series()
        chart.addSeries(series)
        chart.createDefaultAxes()
        self.customAxisX(chart, category)

        return chart

    def get_pie_chart(self):
        chart = QChart(title = '分类销售额')
        chart.addSeries(self.get_pie_series())

        return chart

    def makeup(self):
        layout = QtWidgets.QHBoxLayout(self)

        linechart = QChartView(self.get_line_chart())
        linechart.setRenderHint(QPainter.Antialiasing)
        layout.addWidget(linechart)

        piechart = QChartView(self.get_pie_chart())
        piechart.setRenderHint(QPainter.Antialiasing)
        layout.addWidget(piechart)