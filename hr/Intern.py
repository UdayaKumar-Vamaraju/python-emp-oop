class Intern(Employee):
    def __init__(self, employee_id, name, department, stipend):
        super().__init__(employee_id, name, department)
        self._stipend = stipend
    
    def calculate_sal(self):
        return self._stipend
    
    def display_details(self):
        super().display_details()
        print(f"Stipend: ${self._stipend:.2f}")
        print(f"Total Salary: ${self.calculate_sal():.2f}\n")
