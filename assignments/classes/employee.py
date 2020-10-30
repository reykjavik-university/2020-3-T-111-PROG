class Employee:
    def __init__(self, name):
        self._name = name
    
    def get_name(self):
        return self._name

class HourlyEmployee(Employee):
    OVERTIME_RATE = 1.5
    HOURS_WEEK = 40

    def __init__(self, name, wage):
        super().__init__(name)
        self._hourly_wage = wage

    def weekly_pay(self, hours_worked):
        if hours_worked <= self.HOURS_WEEK:
            pay = hours_worked * self._hourly_wage
        else:
            pay = self.HOURS_WEEK * self._hourly_wage
            pay = pay + ((hours_worked - self.HOURS_WEEK) * self.OVERTIME_RATE * self._hourly_wage)
        return pay

class SalariedEmployee(Employee):
    WEEKS_PER_YEAR = 52

    def __init__(self, name, salary):
        super().__init__(name)
        self._annual_salary = salary

    def weekly_pay(self, hours_worked):
        return self._annual_salary / self.WEEKS_PER_YEAR
        
class Manager(SalariedEmployee):
    def __init__(self, name, salary, bonus):
        super().__init__(name, salary)
        self._weekly_bonus = bonus

    def weekly_pay(self, hours_worked):
        return super().weekly_pay(hours_worked) + self._weekly_bonus
