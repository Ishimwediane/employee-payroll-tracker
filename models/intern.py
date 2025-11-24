from .employee import Employee

class Intern(Employee):
   
    def __init__(self, name,  department, position, stipend):
        super().__init__(name, department, position)
        self.stipend = stipend
        self._salary=stipend
    
    def compute_salary(self):
        return self.stipend
    
    def generate_payslip(self):
        print("----------------------------------------")
        print(f"Intern: {self.name}")
        print(f"Department: {self.department} | Position: {self.position}")
        print(f"Stipend: ${self.stipend:.2f}")
        print(f"Total Pay: ${self.compute_salary():.2f}")
        print("----------------------------------------")