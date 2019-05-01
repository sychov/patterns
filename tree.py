#-----------------------------------------------------------------------------#
# Name:         .py
# Author:       Ryoga
# Created:      30.04.2019
# Description:  Tree (Composite) pattern.
#               Main idea: simple tree structure realization.
#               Two clases, for single node and group of nodes, with
#               same interface.
#               Group node may include groups and singles both.
#-----------------------------------------------------------------------------#


import abc
from dataclasses import dataclass


class WorkUnit(abc.ABC):
    """Work unit interface.
    """
    @abc.abstractmethod
    def get_bill(self) -> int:
        """Get bill for a month.
        """
        pass


class Department(WorkUnit):
    """Group of work units.
    """
    def __init__(self, title: str):
        self._title = title
        self._work_units = []

    def get_bill(self) -> int:
        """Get department bill for a month.
        """
        return sum(q.get_bill() for q in self._work_units)

    def add_work_unit(self, work_unit: WorkUnit):
        self._work_units.append(work_unit)

    def remove_work_unit(self, work_unit: WorkUnit):
        if work_unit in self._work_units:
            self._work_units.remove(work_unit)

    def __repr__(self):
        """Represent as XML.
        """
        _content = '\n'.join(str(q) for q in self._work_units)
        result = f'<department title="{self._title}">\n' + _content + \
                  '\n</department>'
        return result


@dataclass
class Employer(WorkUnit):
    """Single work unit - employer.
    """
    _name: str
    _job: str
    _salary: int

    def get_bill(self) -> int:
        """Get employer bill for a month.
        """
        return self._salary

    def __repr__(self):
        """Represent as XML.
        """
        return '<employer job="%s" salary="%d">%s</employer>' % (
                self._job, self._salary, self._name)


# --------------------------- TEST --------------------------------

if __name__ == '__main__':
    firm = Department('Some Business Ltd')
    firm.add_work_unit(Employer('John', 'CEO', 10000))
    firm.add_work_unit(Employer('Mary', 'Account', 5000))

    sales = Department('Sales')
    firm.add_work_unit(sales)
    sales.add_work_unit(Employer('Bob', 'Manager', 2000))
    sales.add_work_unit(Employer('Ted', 'Manager', 2000))

    programmers = Department('Programmers')
    firm.add_work_unit(programmers)

    programmers_python = Department('Pythonists')
    programmers.add_work_unit(programmers_python)
    programmers_python.add_work_unit(Employer('Alex', 'Senior', 3000))

    programmers_cpp = Department('C++')
    programmers.add_work_unit(programmers_cpp)
    programmers_cpp.add_work_unit(Employer('Eugene', 'Senior', 3000))
    programmers_cpp.add_work_unit(Employer('Victoir', 'Junior', 800))

    print(firm)



