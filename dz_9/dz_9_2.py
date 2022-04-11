class Road:
    _length = 0
    _width = 0

    def __init__(self, length: int, width: int):

        self._length = length
        self._width = width

    def calculate(self, hight: int = 5, mass_m_2: int = 25) -> int:
        return mass_m_2 * hight * self._width * self._length // 1000


if __name__ == '__main__':
    road = Road(5000, 20)
    print(f'Для изготовления покрытия дороги нужно {road.calculate()} тонн.')