class Employee:
    def __init__(self, emp_id, name, age, salary):
        self.emp_id = emp_id
        self.name = name
        self.age = age
        self.salary = salary

    def __str__(self):
        return f"Employee ID: {self.emp_id}, Name: {self.name}, Age: {self.age}, Salary: {self.salary}"


class EmployeeManager:
    def __init__(self, employees):
        self.employees = employees

    def display_employees(self):
        for emp in self.employees:
            print(emp)

    def sort_employees(self, sort_param):
        if sort_param == 1:
            self.employees.sort(key=lambda x: x.age)
        elif sort_param == 2:
            self.employees.sort(key=lambda x: x.name)
        elif sort_param == 3:
            self.employees.sort(key=lambda x: x.salary)
        else:
            print("Invalid sorting parameter. Please choose 1, 2, or 3.")


if __name__ == "__main__":
    employees_data = [
        Employee("161E90", "Ramu", 35, 59000),
        Employee("171E22", "Tejas", 30, 82100),
        Employee("171G55", "Abhi", 25, 100000),
        Employee("152K46", "Jaya", 32, 85000)
    ]

    employee_manager = EmployeeManager(employees_data)

    employee_manager.display_employees()

    sort_parameter = int(
        input("Choose sorting parameter (1. Age, 2. Name, 3. Salary): "))
    employee_manager.sort_employees(sort_parameter)

    employee_manager.display_employees()
