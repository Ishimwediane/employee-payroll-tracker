from models.employee import Employee

class Payroll:
    """Manages a list of employees and salary operations."""
    def __init__(self):
        self.employees = {}

    def add_employee(self, employee: Employee):
        if employee.employee_id in self.employees:
            
            print(f" Employee {employee.name} already exixt.")
        else:
            self.employees[employee.employee_id]=employee
            print(f" Employee {employee.name} added.")

    def remove_employee(self, emp_id):
         if emp_id in self.employees:
             removed=self.employees.pop(emp_id)
             print(f" Employee {removed.name} removed.")
         else:
             print("employee not found")
        

    def get_employee(self,emp_id):
        return self.employees.get(emp_id)
    
    def update_employee(self,emp_id,**kwargs):
        emp=self.get_employee(emp_id)
        if not emp:
            print("employee not found")
            return
        
        for key,value in kwargs.items():
            if hasattr(emp,key):
                setattr(emp,key,value)
            else:
                print(f"'{key}' is not a valid field")
        print(f"Employee {emp.name} updated")

    def update_salary(self,emp_id,new_salary):
        emp=self.get_employee(emp_id)
        if not emp:
            print("employee not found")
            return
        emp.update_salary(new_salary)
    
    def update_bonus(self,emp_id,new_bonus):
        emp=self.get_employee(emp_id)
        if not emp:
            print("employee not found")
            return
        emp.update_bonus(new_bonus)
    
    
    
    def generate_all_payslips(self):
        if not self.employees:
            print("No employees to generate payslips for.")
            return
        for emp in self.employees.values():
            emp.generate_payslip()
            
   

    def summary_report(self):
        print("Payroll Summary Report")
        print("=" * 50)
        for emp in self.employees.values():
            print(f"{emp.employee_id} | {emp.name} | {emp.department} | {emp.position} | Total: ${emp.compute_salary():.2f}")
        print("=" * 50)