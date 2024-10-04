def func(*a1):
    # 用户传来的参数统一会被打包为元组
    print(a1)
func(1)
func(11,22,33)
func(11,22,33,"xxx",True,[44,55,66])