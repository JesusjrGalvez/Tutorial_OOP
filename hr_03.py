class Employee:
    def __init__(self, id, name):
        self.id = id
        self.name = name


class MonthlySalary(Employee):
    def __init__(self, id, name, monthly_salary):
        super().__init__(id, name)
        self.monthly_salary = monthly_salary

    def calculate_pay(self):
        return self.monthly_salary

class HourlySalary(Employee):
    def __init__(self, id, name, hours, hourly_salary):
        super().__init__(id, name)
        self.hours = hours
        self.hourly_salary = hourly_salary

    def calculate_pay(self):
        return self.hours * self.hourly_salary


class CommissionSalary(MonthlySalary):
    def __init__(self, id, name, monthly_salary, commission):
        super().__init__(id, name, monthly_salary)
        self.commission = commission

    def calculate_pay(self):
        return self.monthly_salary + self.commission


class IPayRollCalculator():
    def calculate_payroll(self, employees):
        print("Calculating Payroll")
        print("===================")
        print("")
        for employee in employees:
            print(f"Employee id:{employee.id}, name {employee.name}")
            print(f"Check amounts to {employee.calculate_pay()}")
            print("")


salary_employee = MonthlySalary(1, 'John Smith', 1500)
hourly_employee = HourlySalary(2, 'Jane Doe', 40, 15)
commission_employee = CommissionSalary(3, 'Kevin Bacon', 1000, 250)
payroll_system = IPayRollCalculator()
payroll_system.calculate_payroll([
     salary_employee,
    hourly_employee,
    commission_employee
 ])