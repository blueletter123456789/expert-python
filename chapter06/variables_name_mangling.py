class Base:
    def __secret(self):
        print("秘密です")

    def public(self):
        self.__secret()


class Derived(Base):
    def __secret(self):
        print("参照されません")


if __name__ == '__main__':
    try:
        Base.__secret()
    except Exception as ex:
        print(ex)

    print(dir(Base))

    Base().public()

    Derived().public()
