#-----------------------------------------------------------------------------#
# Name:        singleton.py
# Author:      Ryoga
# Created:     18.04.2019
# Description: Singleton pattern.
#              Aim: class with one and only one possible instance.
#              (IMHO, the best singleton is trivial python module,
#              but here I tried to do this more or less usual way)
#-----------------------------------------------------------------------------#


class Singleton(type):
    """Singleton metaclass. Not my idea, to be honest.
    """
    _inst = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._inst:
            cls._inst[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._inst[cls]


# --------------------------- TEST --------------------------------


import uuid


class TestCase(metaclass=Singleton):
    """Singleton realization
    """
    def __init__(self):
        """Just for test.
        """
        self.id = str(uuid.uuid4())


class TestCaseA(TestCase):
    pass


class TestCaseB(TestCase):
    pass


test_A_1, test_A_2, test_A_3 = TestCaseA(), TestCaseA(), TestCaseA()
test_B_1, test_B_2, test_B_3 = TestCaseB(), TestCaseB(), TestCaseB()

if test_A_1.id == test_A_2.id == test_A_3.id and \
        test_B_1.id == test_B_2.id == test_B_3.id and \
        test_A_1.id != test_B_1.id:
    print('Ok')
else:
    print('FAIL')

