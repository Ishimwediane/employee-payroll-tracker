from models.employee import Employee
from models.contract import ContractEmployee
from models.intern import Intern
from models.fulltime import FullTImeEmployee
from payroll import Payroll


def main():
    tracker=Payroll()
    
    while True:
        print("----Employee payroll tracker menu----")
        print("1.Add Employee")
        print("2.update salary")
        print("3.update bonus")
        print("4.generate all payslips")
        print("5.summary report")
        print("6.search employee by id")
        print("7.Exit")
        
        choice=input("Enter your choice: ")
        
        if choice =="1":
            emp_type=input("enter type(FulltTime/Contract/Intern:)").strip().lower()
            name=input("Name:")
        
            dept=input("Department:")
            pos=input("position:")
            
            if emp_type =="fulltime":
                salary=float(input("monthly salary:"))
                bonus=float(input("Bonus:") or 0)
                tracker.add_employee(FullTImeEmployee(name,dept,pos,salary,bonus))
                
            elif emp_type=="contract":
                hours=float(input("hours worked:"))
                rate=float(input("hourly rate:"))
                bonus=float(input("Bonus:") or 0)
                tracker.add_employee(ContractEmployee(name,dept,pos,hours,rate,bonus))
            
            elif emp_type == "intern":
                stipend = float(input("Stipend: "))
                bonus = float(input("Bonus: ") or 0)
                tracker.add_employee(Intern(name,  dept, pos, stipend))
            else:
                print("Invalid employee type!")
                
        elif choice == "2":
            emp_id=int(input("enter employee id:"))
            new_salary=float(input("enter new salary:"))
            tracker.update_salary(emp_id,new_salary)
            
        elif choice == "3":
            emp_id=int(input("enter employee id:"))
            new_bonus=float(input("enter new bonus:"))
            tracker.update_bonus(emp_id,new_bonus)
            
        elif choice == "4":
            tracker.generate_all_payslips()
            
        elif choice == "5":
            tracker.summary_report()
            
        elif choice == "6":
            emp_id=int(input("enter employee id:"))
            emp=tracker.get_employee(emp_id)
            if emp:
                emp.generate_payslip()
            else:
             print("Employee not found")
            
        elif choice == "7":
            print("exiting payroll")
            break
        else:
            print("invalid choice try again")
            
if __name__ == "__main__":
    main()