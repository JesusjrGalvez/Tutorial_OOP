class Employee:
    def __init__(self, id, name):
        self.id = id
        self.name = name


class EmployeeSalary(Employee):
    def __init__(self, id, name, weekly_salary):
        # This means that __init__ is taken from Employee
        super().__init__(id, name)
        self.weekly_salary = weekly_salary

    def calculate_payroll(self):
        return self.weekly_salary



class EmployeeSalary1(Employee):
    def __init(self, id, name, monthly_salary):
        super().__init__(id, name)
        self.monthly_salary = monthly_salary

    def calculate_pay(self):
        return self.monthly_salary


class HourlySalary(Employee):
    def __init__(self, id, name, hours, hourly_pay):
        super().__init__(id, name)
        self.hours = hours
        self.hourly_pay = hourly_pay

    def calculate_pay(self):
        return self.hours * self.hourly_pay


def ComissionSalary(Employee):
    def __init__(self, id, name, monthly_salary, comission):
        super().__init__(id, name)
        self.monthly_salary = monthly_salary
        self.comission = comission

    def calculate_pay(self):
        return self.monthly_salary + self.comission


class Calculate_Payroll:
    print("Payroll for this month)")
    print("=======================")
    print("")
    def calculate(self, employees):
        for employee in employees:
            print(f'Payroll for: {employee.id} - {employee.name}')
            print(f'- Check amount: {employee.calculate_payroll()}')
            print('')
















        super().__init__(id, name)
        self.monthly_salary = monthly_salary

    def calculatePay(self):
        return self.monthly_salary
