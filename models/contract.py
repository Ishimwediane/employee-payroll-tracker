from .employee import Employee

class ContractEmployee(Employee):
 
    def __init__(self, name,  department, position, hours_worked, hourly_rate, salary,bonus=0):
        super().__init__(name, department, position, salary)
        self.hours_worked = hours_worked
        self.hourly_rate = hourly_rate
        self._salary = self.hours_worked * self.hourly_rate


    def compute_salary(self) -> float:
        self._salary = self.hours_worked * self.hourly_rate
        return self._salary + self.bonus
