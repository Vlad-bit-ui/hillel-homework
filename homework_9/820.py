class Buffer:
    def __init__(self):
        self.part = []

    def add(self, *a):
        self.part += list(a)
        while len(self.part) >= 5:
            print(sum(self.part[:5]))
            self.part = self.part[5:]

    def get_current_part(self):
        return self.part


if __name__ == "__main__":
    buf = Buffer()
    for line in [
        "1 2 3",
        "4 5 6",
        "7 8 9 10",
        "1 1 1 1 1 1 1 1 1 1 1",
    ]:
        buf.add(*map(int, line.split()))
        print(buf.get_current_part())