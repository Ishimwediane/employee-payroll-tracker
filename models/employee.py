from abc import ABC
class Employee(ABC):
    """base class"""
    
    def __init__(self,name,employee_id,salary):
        self.employee_id=employee_id
        self._name=name
        self._salary=salary
    
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

    