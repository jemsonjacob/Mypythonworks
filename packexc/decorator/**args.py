

employees = {
    1000: {"eid": 1000, 'ename': 'ajay', 'salary': 34000, "designation": "devoleper"},
    1001: {"eid": 1001, 'ename': 'arun', 'salary': 38000, "designation": "devoleper"},
    1002: {"eid": 1002, 'ename': 'akhil', 'salary': 21000, "designation": "hr"},
    1003: {"eid": 1003, 'ename': 'anu', 'salary': 45000, "designation": "analyst"}
}
eid = int(input("enter the eid"))
prop = input("enter the property eid,ename,salary,designation")
if eid  in employees and prop in employees:
    print(employees[eid][prop])
else:
    print("invalid")