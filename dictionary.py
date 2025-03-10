states = {
	"CA": "California",
	"DE": "Delaware",
	"NY": "New York",
	"TX": "Texas",
	"WY": "Wyoming"
}
print(len(states))
print("CA" in states)
print("New York" in states)
print(states["CA"])
print(states["DE"])
print(states["TX"])
print(states["WY"])
""" Dictionary rules:
All keys in a dictionary are distinct (there can only be one value per key)
A key cannot be a list or dictionary (or any other mutable type)
The values can be any type, however!
"""
