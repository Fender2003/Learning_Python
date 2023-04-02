customer={
    "name": "Dhruv Thakkar",
    "age": 17,
    "is_verified": True
}
print(customer["name"])
print(customer.get("name"))
print(customer.get("birthday"))
print(customer.get("birthday","Nov 25 2003"))
print(customer.get("age"))
customer["name"]="Jack Smith"
print(customer["name"])

