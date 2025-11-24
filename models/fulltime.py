from .employee import Employee

class FullTImeEmployee(Employee):
    def __init__(self,name,department,position,monthly_salary,bonus=0):
        super().__init__(name,department,position,bonus)
        self._salary=monthly_salary
        
    
    def compute_salary(self)->float:
        
        return self._salary+self.bonus