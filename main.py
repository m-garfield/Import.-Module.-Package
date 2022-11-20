
from aplication import salary
from aplication.db import people
import datetime
import matplotlib
def main():
    salary.calculate_salary()
    people.get_employees()
    print(datetime.date.today())
if __name__ == '__main__':
    main()
