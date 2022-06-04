from die import Die
import pygal
# 创建两个D6
die_1 = Die()
die_2 = Die()
# 掷几次骰子，并将结果存储在一个列表中
results =[die_1.roll()*die_2.roll() for x in range(1000)]
# 分析结果
frequencies = [results.count(value) for value in range(1,die_1.num_sides*die_2.num_sides+1)]
# 对结果进行可视化
hist = pygal.Bar()
hist.title = 'Results of rolling two D6 dice 1000 times.'
hist.x_labels = [str(x) for x in range(1,die_1.num_sides*die_2.num_sides+1)]
hist.x_title = 'Result'
hist.y_title = 'Frequency of Result'
hist.add('D6*D6',frequencies)
hist.render_to_file('die_visual.svg')
