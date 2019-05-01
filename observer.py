#-----------------------------------------------------------------------------#
# Name:         observer.py
# Author:       Ryoga
# Created:      24.04.2019
# Description:  Observer pattern demo.
#               Main idea: realize subscription, when some objects
#               ("subscriber") should know and react to changes in other
#               objects ("publishers").
#               All links beetween them may change dynamically.
#-----------------------------------------------------------------------------#


import abc


# -------------------- INTERFACES ------------------------- #

class Publisher(abc.ABC):
    """Abstract Publisher class.

    Let's make it simple, so we will use single string value
    as a whole state of publisher class.
    """
    @abc.abstractmethod
    def subscribe(self, subscriber: 'Subscriber'):
        """Add subcriber to subscribers list.
        """
        pass

    @abc.abstractmethod
    def unsubscribe(self, subscriber: 'Subscriber'):
        """Remove subcriber from subscribers list.
        """
        pass

    @property
    @abc.abstractmethod
    def value(self) -> str:
        """Return current value.
        """
        pass


class Subscriber(abc.ABC):
    """Abstract Subscriber class.

    In this realization subscriber will get publisher instance to
    get value from it. But in other implementations it may be varied.
    """
    @abc.abstractmethod
    def update(self, publisher: 'Publisher'):
        """Update subscriber according to publisher changes.
        """
        pass


# -------------------- REALIZATION ------------------------- #

class TextElementGUI(Subscriber):
    """Particular realization of subscriber - some text
    element, shown in GUI.
    """
    def __init__(self, source: Publisher):
        """Init. Subscribe to variable when created.
        """
        source.subscribe(self)
        self.update(source)

    def _draw(self):
        """Just for demonstration.
        """
        print('Redraw text element with value "%s"' % self._value)

    def update(self, source: Publisher):
        """Update text element according to source.
        """
        self._value = source.value
        self._draw()


class TextElementInModalGui(TextElementGUI):
    """Another realization of subscriber - some text
    element, shown in GUI in some modal window.
    """
    def _draw(self):
        """Just for demonstration.
        """
        print('Redraw text element in modal with value "%s"' % self._value)


class TextVariable(Publisher):
    """Particular realization of publisher - some text
    variable, ued as source for GUI view.
    """
    def __init__(self, value: str):
        """Initialize by value.
        """
        self._value = value
        self._subscribers = []

    def subscribe(self, subscriber: Subscriber):
        """Add subcriber to subscribers list.
        """
        self._subscribers.append(subscriber)

    def unsubscribe(self, subscriber: Subscriber):
        """Remove subcriber from subscribers list.
        """
        if subscriber in self._subscribers:
            self._subscribers.remove(subscriber)

    @property
    def value(self) -> str:
        """Return current value of variable.
        """
        return self._value

    @value.setter
    def value(self, value: str):
        """Set current value of variable.
        """
        self._value = value
        for subscriber in self._subscribers:
            subscriber.update(self)


# --------------------------- TEST --------------------------------

if __name__ == '__main__':
    variable = TextVariable('Welcome to application!')
    t1 =TextElementGUI(variable)
    t2 = TextElementInModalGui(variable)
    variable.value = 'Hope you enjoy it!'
    variable.unsubscribe(t2)
    variable.value = 'Good bye, pal!'


