class Three_Vecter:
    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, n):
        r = Three_Vecter()
        r.x = self.x + n.x
        r.y = self.y + n.y
        r.z = self.z + n.z
        return r

    def __sub__(self, n):
        r = Three_Vecter()
        r.x = self.x - n.x
        r.y = self.y - n.y
        r.z = self.z - n.z
        return r

    def __mul__(self, n):
        r = Three_Vecter()
        r.x = self.x * n
        r.y = self.y * n
        r.z = self.z * n
        return r

    def __truediv__(self, n):
        r = Three_Vecter()
        r.x = self.x / n
        r.y = self.y / n
        r.z = self.z / n
        return r

    def __floordiv__(self, n):
        r = Three_Vecter()
        r.x = self.x // n
        r.y = self.y // n
        r.z = self.z // n
        return r

    def show(self):
        print((self.x, self.y, self.z))


if __name__ == '__main__':
    v1 = Three_Vecter(1, 2, 3)
    v2 = Three_Vecter(4, 5, 6)
    v3 = v1+v2
    v3.show()
    v4 = v1-v2
    v4.show()
    v5 = v1*3
    v5.show()
    v6 = v1/2
    v6.show()

'''三要素： 封装继承和多态'''
