#!/usr/bin/env python3


class Employee(object):

    def __init__(self, first_name, second_name, salary, experiance, manager):    
        self.first_name = first_name
        self.second_name = second_name
        self.salary = salary
        self.experiance = experiance
        self.manager = manager

    def __repr__(self):
        return self.first_name + ' ' + self.second_name + ' manager: ' + self.manager.first_name + ' ' + self.manager.second_name + ' experiance: ' + str(self.experiance)

    def get_salary(self):
        final_salary = self.salary
        if self.experiance > 3:
            final_salary *= 1.2
            final_salary += 500
        elif self.experiance > 2:
            final_salary += 200
        return final_salary

class Developer(Employee):

    pass


class Designer(Employee):

    def __init__(self, first_name, second_name, salary, experiance, manager, effec_coef):
        super().__init__(first_name, second_name, salary, experiance, manager)
        self.effec_coef = effec_coef
    
    def get_salary(self):
        return self.salary * self.effec_coef

class Manager(Employee):
    
    def __init__(self, first_name, second_name, salary, experiance, manager, employees=None):
        super().__init__(first_name, second_name, salary, experiance, manager)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def get_employees(self):
        return self.employees

    def man_salary(self):
        final_salary = self.get_salary()
        if len([filter(lambda emp: type(emp) is Developer, self.employees)])  > len(self.employees) / 2:
            final_salary *= 1.1
        if len(self.employees) > 5:
            final_salary += 200
        elif len(self.employees) > 10:
            final_salary += 500
        return final_salary


    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, *emp):
        if emp not in self.employees:
            self.employess.remove(emp)

class Department(object):
    def __init__(self, *managers):
        self.managers = managers

    def provide_salary(self):
        for i in self.managers:
            for j in i.employees:
                print(j.first_name + " " + j.second_name + ": got salary:" + str(j.get_salary()))

man1 = Manager('Big', 'Bos', 3000, 10, None)
des1 = Designer('Petya', 'Vasin', 2000, 6, man1, 1.1)
dev1 = Developer('Vasya', 'Petrov', 1000, 4, man1)
dev2 = Developer('Maxim', 'Pupkin', 1500, 4, man1)
man1.add_emp(des1)
man1.add_emp(dev1)
man1.add_emp(dev2)
dep1 = Department(man1)
dep1.provide_salary()
print(man1.man_salary())
print(dev1)