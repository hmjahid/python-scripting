import json

employee_data = '''
{
    "people" :[
{
"name" : "Jahid",
"email" : "jahid@gmail.com",
"married" :true
},
{
"name" : "Osman",
"email" : "osman@gmail.com",
"married" :true
}
]
}
'''
print(employee_data)

data = json.loads(employee_data)

print(data)