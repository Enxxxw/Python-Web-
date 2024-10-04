class UserInfo:
    def __init__(self, a1, a2):
        self.username = a1
        self.password = a2


user_list = []
while True:
    user = input('用户名(Q/q)：')
    if user.upper() == 'Q':
        break
    pwd = input('密码：')

    obj = UserInfo(user, pwd)
    user_list.append(obj)

for item in user_list:
    msg = "{}-{}".format(item.username, item.password)
    print(msg)
