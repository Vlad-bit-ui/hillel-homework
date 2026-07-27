class CandyStash:
    MAX_CAPACITY = 50

    @staticmethod
    def validate_amount(value):
        if not isinstance(value, int):
            raise ValueError("Amount must be an int")
        if value < 0:
            raise ValueError("Amount must not be negative")
        return value

    def __init__(self, count):
        self.validate_amount(count)
        self._count = min(count, self.MAX_CAPACITY)

    @classmethod
    def full_stash(cls):
        return cls(cls.MAX_CAPACITY)

    @property
    def count(self):
        return self._count

    @count.setter
    def count(self, value):
        self.validate_amount(value)
        self._count = min(value, self.MAX_CAPACITY)

    def __str__(self):
        return f"CandyStash ( {self._count} / {self.MAX_CAPACITY} )"

    def __repr__(self):
        return f"CandyStash ( {self._count} / {self.MAX_CAPACITY} )"

    def __add__(self, other):
        if isinstance(other, CandyStash):
            other = other.count
        self.validate_amount(other)
        return CandyStash(min(self._count + other, self.MAX_CAPACITY))

    def __sub__(self, other):
        if isinstance(other, CandyStash):
            other = other.count
        self.validate_amount(other)
        return CandyStash(max(self._count - other, 0))

    def __eq__(self, other):
        if isinstance(other, CandyStash):
            return self._count == other.count
        if isinstance(other, int):
            return self._count == other
        return NotImplemented