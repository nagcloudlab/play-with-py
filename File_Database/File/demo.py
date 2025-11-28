

"""
Empployee,Department,Salary
A,IT,1000
B,HR,1500
C,IT,2000
D,Finance,2500
"""

"""
find total salary by department
"""

import csv
from collections import defaultdict

# way-1
department_salary = defaultdict(int)
with open("report.csv", newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        department = row['Department']
        salary = int(row['Salary'])
        department_salary[department] += salary

for department, total_salary in department_salary.items():
    print(f"{department}: {total_salary}")

print("-----")

# way-2
import pandas as pd
df = pd.read_csv("report.csv")
total_salary_by_department = df.groupby('Department')['Salary'].sum()
print(total_salary_by_department)

