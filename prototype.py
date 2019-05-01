#-----------------------------------------------------------------------------#
# Name:        prototype.py
# Author:      Ryoga
# Created:     18.04.2019
# Description: "Prototype" pattern.
#              Main idea: copying object using it's own method.
#-----------------------------------------------------------------------------#


import abc
from dataclasses import dataclass


RED = '#ff0000'
GREEN = '#00ff00'


class Prototype(abc.ABC):
    """Interface.
    Declares clone() method.
    """
    @abc.abstractmethod
    def clone(self):
        """Create object's copy.
        """
        pass


@dataclass
class Monster(Prototype):
    """Monster, generic clonable class.
    """
    name: str
    color: str
    coord_x: int
    coord_y: int

    def clone(self):
        return Monster(self.name, self.color, self.coord_x, self.coord_y)

    def show(self):
        print('%s at (%d:%d), color %s' %
              (self.name, self.coord_x, self.coord_y, self.color))


class RedMonster(Monster):
    """Red Monster prototype.
    """
    def __init__(self, coord_x, coord_y):
        super().__init__('red_monster', RED, coord_x, coord_y)

    def clone(self):
        return RedMonster(self.coord_x, self.coord_y)


# --------------------------- TEST --------------------------------


if __name__ == '__main__':
    monster_1 = Monster('TestMonster', GREEN, 0, 0)
    monster_2 = monster_1.clone()
    monster_2.coord_x = 1
    monster_1.show()
    monster_2.show()

    red_1 = RedMonster(7, 7)
    red_2 = red_1.clone()
    red_2.coord_x = 8
    red_1.show()
    red_2.show()
