class Police:
    """ 警察类 """
    def __init__(self, name, age, hit_points):
        self.name = name
        self.age = age
        self.hit_points = hit_points

    def catch(self):
        """ 抓小偷 """
        self.hit_points = self.hit_points + 100

    def smoking(self):
        """ 抽烟 """
        self.hit_points = self.hit_points - 50

    def shoot(self, user):
        """ 开枪 """
        user.hit_points = user.hit_points - 100
        self.hit_points = self.hit_points - 10


class Terriorist:
    """ 恐怖分子 """
    def __init__(self, name, hit_points):
        self.name = name
        self.hit_points = hit_points

    def shoot(self, user):
        """ 射击 """
        user.hit_points = user.hit_points - 200

    def strafe(self, user_list):
        """ 扫射 """
        for user in user_list:
            user.hit_points = user.hit_points - 200

    def bomb(self, user_list):
        """ 炸弹 """
        for user in user_list:
            user.hit_points = user.hit_points - 300
            self.hit_points = self.hit_points - 100


p1 = Police("张三", 22, 1000)
p2 = Police("李四", 22, 200)
p3 = Police("马五", 22, 8000)

t1 = Terriorist("牛六", 800)
t2 = Terriorist("赵七", 1000)

p3.shoot(t2)  # Police.shoot方法 -> p3=7990    t2=900

t2.bomb([p3, p1])  # Terriorist.bomb方法 -> t2=800  p1=700  p3=p690

t2.bomb([t1])  # Terriorist.bomb方法 -> t2=700  t1=500

t1.strafe([t2, t2])  # Terriorist.strafe方法 -> t2=100 t1=500