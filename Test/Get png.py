import os

for item in os.listdir(r"D:\★en\Course\experiment\数字图像处理\sy4"):
    item_u = item.upper()
    if item_u.endswith(".PNG"):
        print(item)