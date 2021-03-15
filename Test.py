class Test:

    def __init__(self):
        self.__user__ = 'gaofeng'

    def test2(self, b, w):
        c = b + w
        return c

    def test1(self):
        a = 10
        r = self.__user__
        return self.test2(r + str(a), str(a))


def main():
    t = Test()
    t1 = t.test1()
    print(t1)


if __name__ == '__main__':
    main()
