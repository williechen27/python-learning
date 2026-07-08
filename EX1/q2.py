import math

r = 6371.01

x1 = float(input('輸入第一點的緯度：'))
y1 = float(input('輸入第一點的經度：'))
x2 = float(input('輸入第二點的緯度：'))
y2 = float(input('輸入第二點的經度：'))

x1 = math.radians(x1)
y1 = math.radians(y1)
x2 = math.radians(x2)
y2 = math.radians(y2)

d = r * math.acos(math.sin(x1) * math.sin(x2) + \
                  math.cos(x1) * math.cos(x2) * math.cos(y1-y2))

print('兩點間的大圓距離為 %.2f 公里' %d)
