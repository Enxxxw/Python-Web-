class Message:
    # 特殊的方法，Python内部会自动调用？ 实例化话对象时自动调用。
    def __init__(self, city):
        self.company = "联通"
        self.city = city

    def send_email(self, to):
        msg = "给{}的{}发送了一封邮件".format(self.company, to)
        print(msg)

    def send_dingding(self, to):
        msg = "给{}的{}发送了钉钉消息".format(self.city, to)
        print(msg)

    def send_wechat(self, to):
        msg = "给{}的{}发送了微信消息".format(self.city, to)
        print(msg)


# 1.创建空对象 & 空对象和类关联起来。
# 2.自动执行 __init__ 方法。
obj1 = Message("广西")    # obj1.__init__("广西")
obj2 = Message("河南")    # obj2.__init__("河南")

obj1.send_email("张三")   # 给联通的张三发送了一封邮件
obj1.send_email("李四")   # 给联通的李四发送了一封邮件
obj2.send_wechat("马五")  # 给河南的马五发送了微信消息