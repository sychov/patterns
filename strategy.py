#-----------------------------------------------------------------------------#
# Name:         strategy.py
# Author:       Ryoga
# Created:      01.05.2019
# Description:  Strategy pattern demo.
#               Main idea: exclude algorithms varies to extra classes
#               with generic intergface.
#-----------------------------------------------------------------------------#


import abc


class Strategy(abc.ABC):
    """Generic strategy interface.
    Uses callable objects, for simplicity.
    """
    @abc.abstractmethod
    def __call__(self, value: int) -> int:
        pass


class IncrementStrategy(abc.ABC):
    """Incrementing algorithm.
    """
    def __call__(self, value: int) -> int:
        return value + 1


class DecrementStrategy(abc.ABC):
    """Decrementing algorithm.
    """
    def __call__(self, value: int) -> int:
        return value - 1


class Counter:
    """Counter class, just for demo.
    """
    def __init__(self, init_value: int):
        self._value = init_value
        self._strategy = None

    def set_strategy(self, strategy: Strategy):
        self._strategy = strategy

    def tick(self):
        if self._strategy:
            self._value = self._strategy(self._value)

    def __repr__(self):
        return 'Counter: %d' % self._value


# --------------------------- TEST --------------------------------

if __name__ == '__main__':
    counter = Counter(0)
    counter.set_strategy(IncrementStrategy())
    print('Incrementing:')
    for q in range(5):
        counter.tick()
        print(counter)

    counter = Counter(6)
    counter.set_strategy(DecrementStrategy())
    print('Decrementing:')
    for q in range(5):
        counter.tick()
        print(counter)


