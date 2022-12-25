import json

class Employees:
    def __init__(self,Name,DOB,height,city,state):
        self.name = Name
        self.dob = DOB
        self.height = height
        self.city = city
        self.state = state

# Open a json file
with open('C:\\Users\\DELL\\Desktop\\DS\\ds_class_1.py\\assignment_s.py\\employee.json','r') as file :
    data = json.load(file)
    
# Create a list of Employee object from the dict
employees = [Employees(e['Name'], e['DOB'], e['height'], e['city'] , e['state']) for e in data['Employees']]
print(employees)
# Printing the list
for employee in employees:
    print(employee.name, employee.dob, employee.height, employee.city, employee.state)
