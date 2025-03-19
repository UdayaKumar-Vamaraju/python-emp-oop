class PermanentEmployee(Employee):
    def __init__(self, employee_id, name, department, basic_salary, bonus):
        super().__init__(employee_id, name, department)
        self._basic_salary = basic_salary
        self._bonus = bonus
    
    def calculate_sal(self):
        return self._basic_salary + self._bonus
    
    def display_details(self):
        super().display_details()
        print(f"Basic Salary: ${self._basic_salary:.2f}")
        print(f"Bonus: ${self._bonus:.2f}")
        print(f"Total Salary: ${self.calculate_sal():.2f}\n")
