# Variables
name = "Jonas"
age = 38
price = 3000
is_active = True

print("name:", name)
print("age:", age)
print("price:", price)
print("is_active:", is_active)

# List
numbers = [1, 2, 3, 4, 5]
print("First number:", numbers[0])

# Loop
for num in numbers:
    print("Number:", num)

# Dictionar
user = {
    "name": "Jonas",
    "email": "jonas@email.com",
    "is_admin": False
}
print("User name:", user["name"])

# Add new key
user["age"] = 38
print("Updated user:", user)

# Condition
if user["is_admin"]:
    print("Admin user")
else:
    print("Regular user")

# None (null equivalent)
token = None

if token is None:
    print("No token found")
    