import csv

csv.register_dialect('empDialect', skipinitialspace=True, strict=True)
def read_employees(csv_file_location):
    with open(csv_file_location) as f:
        reader = csv.DictReader(f,dialect='empDialect')
        employee_list = []
        for data in reader:
            employee_list.append(dict(data))
        return employee_list

def process_data(employees_list):
    dept_list = []
    for emp in employee_list:
        dept_list.append(emp["Department"])
    dept_dict = {}
    for dept in set(dept_list):
        dept_dict[dept] = dept_list.count(dept)
    return dept_dict

def write_report(dictionary,report_file):
    with open(report_file,"w+") as f:
        for k in sorted(dictionary):
            f.write(str(k)+':'+str(dictionary[k])+'\n')

#"/home/student-04-c9c27188fa69/data/report.txt"
employee_list = read_employees("employees.csv")
dictionary = process_data(employee_list)
print(employee_list)
print(dictionary)
write_report(dictionary,"report.txt")
