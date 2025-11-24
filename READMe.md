# Employee Payroll Tracker

A **console-based Python application** for managing employees, payroll, and salary operations.  
Supports **Full-Time, Contract, and Intern employees**, calculates salaries automatically, generates payslips, and provides summary reports. Employee IDs are assigned automatically.

---

## Features

- **Add Employees**
  - Full-Time, Contract, or Intern
  - Automatic employee ID assignment
  - Bonus is optional

- **Update Salary and Bonus**
  - Update an employee's salary or bonus

- **Generate Payslips**
  - View individual or all employee payslips
  - Shows base salary, bonus, and total salary

- **Summary Report**
  - Lists all employees with total salary

- **Search Employee**
  - Search by employee ID and display the payslip

- **Remove Employee**
  - Remove an employee from the system

---

## Employee Types

1. **Full-Time Employee**
   - Fixed monthly salary + optional bonus

2. **Contract Employee**
   - Paid based on hours worked × hourly rate + optional bonus

3. **Intern**
   - Fixed stipend + optional bonus

---

## Folder Structure

```
Employee-Payroll-Tracker/
│
├── main.py                 # Main program (CLI interface)
├── payroll.py              # Payroll management class
├── models/
│   ├── __init__.py
│   ├── employee.py         # Abstract base Employee class
│   ├── fulltime.py         # Full-Time Employee class
│   ├── contract.py         # Contract Employee class
│   └── intern.py           # Intern class
├── requirements.txt        # Project dependencies (optional)
└── README.md               # Project documentation
```

---

## Installation

1. **Clone the repository:**
   ```bash
   git clone repo-name
   cd employee-payroll-tracker
   ```

2. **Create and activate a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Linux/Mac
   venv\Scripts\activate      # On Windows
   ```

3. **Install dependencies (if any):**
   ```bash
   pip install -r requirements.txt
   ```

---

## Usage

1. **Run the application:**
   ```bash
   python main.py
   ```

2. **Select options from the menu:**
   ```
   ---- Employee Payroll Tracker Menu ----
   1. Add Employee
   2. Update Salary
   3. Update Bonus
   4. Generate All Payslips
   5. Summary Report
   6. Search Employee by ID
   7. Remove Employee
   8. Exit
   ```

3. **Follow prompts** to add employees, update salaries/bonuses, generate payslips, or view reports.

---

## How It Works

### Adding Employees

When adding an employee, you'll be prompted for:
- **Employee Type**: FullTime, Contract, or Intern
- **Name**: Employee's full name
- **Department**: Department they belong to
- **Position**: Job title or role
- **Salary Details**:
  - Full-Time: Monthly salary
  - Contract: Hourly rate and hours worked
  - Intern: Monthly stipend
- **Bonus** (optional): Additional compensation

### Salary Calculation

- **Full-Time Employee**: `Total = Monthly Salary + Bonus`
- **Contract Employee**: `Total = (Hours Worked × Hourly Rate) + Bonus`
- **Intern**: `Total = Stipend + Bonus`

---

## Example Usage

### Adding an Intern

```
---- Employee Payroll Tracker Menu ----
Enter your choice: 1

Enter type (FullTime/Contract/Intern): Intern
Name: Alice
Department: HR
Position: Intern
Stipend: 500
Bonus (press Enter to skip): 

✔ Employee Alice added successfully with ID: 1
```

### Generating All Payslips

```
Enter your choice: 4

========================================
          PAYROLL PAYSLIPS
========================================

----------------------------------------
Employee ID: 1
Name: Alice
Type: Intern
Department: HR | Position: Intern
Stipend: $500.00
Bonus: $0.00
Total Pay: $500.00
----------------------------------------
```

### Summary Report

```
Enter your choice: 5

========================================
        PAYROLL SUMMARY REPORT
========================================

ID | Name           | Type      | Department | Total Pay
----|----------------|-----------|------------|-----------
1   | Alice          | Intern    | HR         | $500.00

Total Payroll: $500.00
Total Employees: 1
========================================
```

---

## Notes

- Employee IDs are automatically generated sequentially starting from 1
- Bonus can be left empty (defaults to 0)
- Interns only have a stipend; no base salary
- Contract employees' salary is calculated as: `hours_worked × hourly_rate + bonus`
- Full-time employees' salary is: `monthly_salary + bonus`
- All monetary values are displayed with two decimal places

---

## Requirements

- Python 3.6 or higher
- No external dependencies required (uses only Python standard library)

---

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a new branch (`git checkout -b feature/your-feature`)
3. Commit your changes (`git commit -m 'Add some feature'`)
4. Push to the branch (`git push origin feature/your-feature`)
5. Open a Pull Request

---



## Future Enhancements

- Export payslips to PDF or CSV
- Database integration for persistent storage
- Tax calculation and deductions
- Employee attendance tracking
- GUI interface using tkinter or PyQt
- Email payslips to employees
- Generate monthly/yearly reports
- Multi-currency support

---

## Contact

For questions or suggestions, please open an issue on GitHub or contact the maintainer.
email:ishimwediane400@gmail.com

---

## Acknowledgments

- Built with Python
- Inspired by real-world payroll management systems
- Thanks to all contributors

---
## link to demo screen recording
 - https://drive.google.com/file/d/1dHrpulBMSqZZ9H6AKG_VCfSylEfWU9xT/view?usp=sharing