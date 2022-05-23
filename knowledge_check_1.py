greeting = "hello world!"
mixed_list = ["while it's", True, f"that I just printed {greeting}, it's not ", False, "that I'm about to print a dictionary value", {
    "porridge": 39.3, "chimichangas": "good"}]
requested_dictionary = {
    "my_first_value": (4234.43, 85.64),
    "not_my_first_value": (4324.45, 85.40)}
your_tuple = (43, 32, 49, 40)

print(greeting)
print(your_tuple[0])
print(list(mixed_list[5])[1])
print(requested_dictionary["my_first_value"])
 