class Character:
    def __init__(self, name: str, max_hp: int):
        self.name = name
        self.max_hp = max_hp
        self.__hp = max_hp

    def take_damage(self, amount: int) -> None:
        self.__hp = max(0, self.__hp - amount)

    def heal(self, amount: int) -> None:
        self.__hp = min(self.max_hp, self.__hp + amount)

    def is_alive(self) -> bool:
        return self.__hp > 0