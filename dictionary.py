# type data of dictionary, seems like objec, have key properties and value , this type data is mutable
# could add new data in dictionary

customer = {"name":"marimas", "age": 20}

customer["office"] = "Xbruh"
customer["name"] = "bijiah"

print(customer["name"])

for key in customer: 
    value = customer[key]
    print(f"{key}: {value}")


del customer["age"]
#dictionarya have items metdhod, result of items method is the form of tuppple 
for key, value in customer.items(): 
    print(f"{key}: {value}")