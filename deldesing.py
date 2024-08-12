emp={
    "id":"1",
    "name":"John Doe",
   "designation":"software engineer",
    "salary":50000
}
print("original Dictionary:")
print(emp)

del emp["designation"]

emp["name"]="John Doe"

print("\n Updated Dictionary:")
print(emp)
