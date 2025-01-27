class test:
    def __init__(self, x, y):
        self.x = float(x)
        self.y = float(y)

    def print_pos(self):
        print(self.x, self.y)

    def tate(self, y):
        self.y += y

    def yoko(self, x):
        self.x += x

if __name__ == "__main__":
    aaa = test(5, 3)
    aaa.print_pos()
    aaa.tate(3)
    aaa.yoko(4)
    aaa.print_pos()