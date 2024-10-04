class Base:
    def do(self):
        print("base.do")


class Son(Base):

    def do(self):
        print("do")

    def show(self):
        print("show")
        self.do()


s1 = Son()
s1.show()