"""An example of how to represent a group of acquaintances in Python."""

# Your code to go here...
import numpy as np
my_group = [
    {"Yitian Xu": {"age": 23, "job": None, "connection": [{"Zicong Peng": "friend"}]}},
    [
        {
            "Zicong Peng": {
                "age": 22,
                "job": None,
                "connection": [{"Yitian Xu": "friend"}],
            }
        }
    ],
]
example_group = {
    "Jill": {
        "age": 26,
        "job": "biologist",
        "connection": {"Zalika": "friend", "John": "partner"},
    },
    "Zalika": {"age": 28, "job": "artist", "connection": {"Jill": "friend"}},
    "John": {"age": 27, "job": "writer", "connection": {"Jill": "partner"}},
    "Nash": {
        "age": 34,
        "job": "chef",
        "connection": {"John": "cousin", "Zalika": "landlord"},
    },
}

# for person in my_group:
# if person[*arg["connection"]]=="none":
# my_group.remove(person)

print(example_group["Jill"]["connection"]["John"])
for person in example_group:
    print(
        f"{person} is {example_group[person]["age"]}, a {example_group[person]["job"]} "
    )

ages = []
relation_number = []
one_age = []
for person in example_group:
    ages.append(example_group[person]["age"])
    if example_group[person]["connection"].value == "cousin" or "partner":
        one_age.append(example_group[person]["age"])
    relation_number.append(len(example_group[person]["connection"]))
print(np.max(ages))
print(np.mean(relation_number))

print(example_group[person]["connection"].value)

