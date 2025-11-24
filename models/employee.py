from abc import ABC, abstractmethod

class Employee(ABC):
    """base class"""
    _id_counter =1 
    
    def __init__(self,name,department,position,bonus:float=0):
        
        self._name=name
        self._employee_id=Employee._id_counter
        Employee._id_counter+=1
        self.department=department
        self.position=position
        self.bonus=bonus if bonus else 0
        self._salary=0
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self,value):
        if not value.strip():
            raise ValueError("name is require")
        self._name=value
    
    @property
    def salary(self):
        return self._salary
    
    @salary.setter
    def salary(self,value):
        if value<0:
            raise ValueError("salary is always negative")
        self._salary=value
        
    @property
    def employee_id(self):
        return self._employee_id
    
   

    
    def update_salary(self,value):
        self._salary=value
        
    
    
    def update_bonus(self,value):
        self.bonus=value
    
    def __str__(self):
        return f"{self.name} (ID: {self._employee_id})"

    def __repr__(self):
        return f"Employee(emp_id='{self._employee_id}', name='{self.name}')"

    def __eq__(self, other):
        if isinstance(other, Employee):
            return self._employee_id == other.employee_id
        return False
    
    @abstractmethod 
    def compute_salary(self): 
        return self._salary+self.bonus
    
    def generate_payslip(self):
        print(f"Pay Slip for {self.name} (ID: {self.employee_id})")
        print("-"*40)
        print(f"Department: {self.department} | Position: {self.position}")
        print(f"Base Salary: ${self._salary:.2f}")
        print(f"Bonus: ${self.bonus:.2f}")
        print(f"Total Salary: ${self.compute_salary():.2f}")
        print("-" * 40)
    
     
