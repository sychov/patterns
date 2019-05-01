#-----------------------------------------------------------------------------#
# Name:         factory_method.py
# Author:       Ryoga
# Created:      19.04.2019
# Description:  "Factory method" pattern.
#               Main idea: to create instances of one class in another
#               through special method, that could be overloaded later.
#-----------------------------------------------------------------------------#


import abc


TEXT_INPUT = '~ some text ~'
TEXT_OUTPUT = '~ some anither text ~'


class UserInterface(abc.ABC):
    """Actually, Interface for user interfaces.
    Declares methods "input()" and "output()".
    """
    @abc.abstractmethod
    def input(self):
        pass

    @abc.abstractmethod
    def output(self):
        pass


class Console(UserInterface):
    """Console user interface.
    """
    def input(self):
        print('User enetered "%s" in console.' % TEXT_INPUT)
        return TEXT_INPUT

    def output(self, text):
        print('User see "%s" in console.' % text)


class GUI(UserInterface):
    """Graphics user interface.
    """
    def input(self):
        print('User enetered "%s" in GUI.' % TEXT_INPUT)
        return TEXT_INPUT

    def output(self, text):
        print('User see "%s" in GUI.' % text)


class Application(abc.ABC):
    """Main pattern's client class.
    """
    def __init__(self):
        """Do many stuff here:
        ...
        ...
        """
        self._interface = self._create_interface()

    @abc.abstractmethod
    def _create_interface(self):
        """Factory method.
        """
        pass

    def some_actions(self):
        """Just for test.
        """
        x = self._interface.input()
        self._interface.output(TEXT_OUTPUT)


class GUIApplication(Application):
    """Main pattern's client class.
    """
    def _create_interface(self):
        """Factory method.
        """
        return GUI()


class ConsoleApplication(Application):
    """Another pattern's client class.
    """
    def _create_interface(self):
        """Factory method.
        """
        return Console()


# --------------------------- TEST --------------------------------#


if __name__ == '__main__':
    print('GUI variant:')
    GUIApplication().some_actions()
    print('Console variant:')
    ConsoleApplication().some_actions()

