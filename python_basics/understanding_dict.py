sample_dict = {"name":"john"}

user_data = {"name":"jane","experience":5,"location":"USA"}

user_data_extra = {
    "name": "jane",
    "experience": 5,
    "location": "USA",
    "job": "developer",
    "permissions": ["read","write"]
}
print(user_data_extra['permissions'][1])