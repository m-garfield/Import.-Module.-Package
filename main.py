
from aplication import salary
from aplication.db import people
import datetime

def main():
    salary.calculate_salary()
    people.get_employees()
    print(datetime.date.today())

main()
