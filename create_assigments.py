import json
import random

def assign_secret_santa(participants):
    if len(participants) < 2:
        return "Need at least two participants."
    shuffled = participants[:]
    random.shuffle(shuffled)
    assignments = {}
    for i, participant in enumerate(shuffled):
        assignments[participant] = shuffled[(i + 1) % len(shuffled)]
    return assignments

def save_assignments(assignments, filename='assignments.json'):
    with open(filename, 'w') as f:
        json.dump(assignments, f)

# Run this script once to create and save the assignments
participants = ['Brian', 'Emmanuelle', 'Jonathan', 'Marie B.', 'Sammy', 'Thomas', 'Cyril', 'Marie P.', 'Lorenzo']
assignments = assign_secret_santa(participants)
save_assignments(assignments)
print("Assignments have been generated and saved.")