# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import csv
import helper
import hr_02

#import hr
#import polygons
#import polygons_final


# TEST 1
# salary_employee = hr.SalaryEmployee(1, 'John Smith', 1500)
# sr = hr.SalaryEmployee(4, "Patty", 2000)
# hourly_employee = hr.HourlyEmployee(2, 'Jane Doe', 40, 15)
# commission_employee = hr.CommissionEmployee(3, 'Kevin Bacon', 1000, 250)
# disgruntled_employee = hr.DisgruntledEmployee(20000, 'Anonymous')
# payroll_system = hr.PayrollSystem()
# payroll_system.calculate_payroll([
#     salary_employee,
#     hourly_employee,
#     commission_employee,
#     disgruntled_employee
# ])


# # TEST 2
# manager = hr.Manager(1, 'Mary Poppins', 3000)
# secretary = hr.Secretary(2, 'John Smith', 1500)
# sales_guy = hr.SalesPerson(3, 'Kevin Bacon', 1000, 250)
# factory_worker = hr.FactoryWorker(2, 'Jane Doe', 40, 15)
# employees = [
#     manager,
#     secretary,
#     sales_guy,
#     factory_worker,
# ]
# productivity_system = hr.ProductivitySystem()
# productivity_system.track(employees, 40)
# payroll_system = hr.PayrollSystem()
# payroll_system.calculate_payroll(employees)

# TEST 3


salary_employee = hr_02.EmployeeSalary(1, "Tom", 3000)
hourly_employee = hr_02.HourlySalary(4, "Paty", 40, 20)
commission_employee = hr_02.ComissionSalary(4)
payroll_system = hr_02.Calculate_Payroll()
payroll_system.calculatePay()
