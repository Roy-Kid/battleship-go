"""Day 2: predict each result, then run this file. No Pygame required.
Coordinates in this lesson are zero-based board columns and rows.
"""
# Tuple: an ordered sequence whose entries cannot be replaced.
position = (2, 3)
print('Tuple:', position, 'x:', position[0], 'y:', position[1])
# position[0] = 4 would raise TypeError. Create a new tuple instead.
position = (4, position[1])
print('New tuple:', position)

# List: an ordered sequence whose entries can be changed, added or removed.
names = ['Scout', 'Cruiser']
# OPTIONAL L — PPT 15. Edit the appended name.
names.append('Carrier')
print('List:', names, 'first:', names[0], 'count:', len(names))

# Dictionary: values accessed by unique keys, rather than numbered positions.
ship = {'name': 'Scout', 'x': 2, 'y': 3, 'vertical': False}
ship['x'] = ship['x'] + 1
print('Dictionary:', ship, 'x:', ship['x'])

# A list can hold dictionaries. It stores references to those records.
fleet = [ship, {'name': 'Cruiser', 'x': 5, 'y': 6, 'vertical': False}]
# OPTIONAL R — PPT 16. Predict both references after this update.
fleet[0]['x'] = 6
print('Nested access:', fleet[0]['name'], fleet[0]['x'])
print('Same record:', ship['x'])  # 6: ship refers to fleet[0]'s dictionary.

# Optional: a set stores distinct values, with no positional order.

# OPTIONAL S — PPT 17. Add a new target tuple.
targets = {(2, 3), (2, 3), (4, 1)}
print('Unique target count:', len(targets))  # 2; do not rely on print order.
print('Already tried (2, 3):', (2, 3) in targets)
print('Empty dictionary:', type({}).__name__, 'empty set:', type(set()).__name__)
