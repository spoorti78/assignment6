import json

indian_states = {
    "karnataka":"bengaluru",
    "maharastra":"mumbai",
    "assam":"dispur",
    "tamilnadu":"chennai",
    "kerala":"thrivananthpuram",
    "goa":"panji",
    "sikkim":"gangtok"
}

# converting dict obj into json obj
json_obj = json.dumps(indian_states, indent=4)
print(json_obj)

