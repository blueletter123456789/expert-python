class Weirdint(int):
    def __add__(self, other):
        return int.__add__(self, other) + 1

    def __repr__(self) -> str:
        return "<weirdo %d>" % self

    def do_this(self):
        print("this")

    def do_that(self):
        print("that")


if __name__ == "__main__":
    a = Weirdint(10)
    b = 20
    print(a + b)
    print(a)
