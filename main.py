list_1 = [
    {"id": "1", "name": "Shrey", "age": 25},
    {"id": "3", "age": 10, "name": "Hello"},
    {"id": "2", "name": "World", "age": 24},
]

list_2 = [
    {"id": "1", "marks": 100},
    {
        "id": "3",
        "marks": 90,
        "roll_no": 11,
        "extra_info": {
            "hello": "world",
        },
    },
]

def merge_lists(list_1, list_2):
    # Creating an empty dictionary to store the merged information
    merged_dict = {}
    
    # Looping through each student in the combined list of list_1 and list_2
    for student in list_1 + list_2:
        # Checking if the student's ID is already in the merged_dict
        if student['id'] in merged_dict:
            # If the ID already exists, update the existing dictionary with the current student's information
            merged_dict[student['id']].update(student)
        else:
            # If the ID does not exist, create a new entry in the merged_dict with the student's information
            merged_dict[student['id']] = student
    
    # Convert the dictionary of merged information into a list and return it
    return list(merged_dict.values())

list_3 = merge_lists(list_1, list_2)

print(list_3)