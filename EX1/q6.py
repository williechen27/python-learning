s = "   蘋果 , 香蕉, 鳳梨 , 水蜜桃  "

lst = s.split(",")

for i in range(len(lst)):
    lst[i] = lst[i].strip()

s = "-".join(lst)

print("整理後的串列：", lst)
print("整理後的字串：", s)
