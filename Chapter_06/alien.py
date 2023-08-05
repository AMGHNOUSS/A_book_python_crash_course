alien_0 = {'color': 'green', 'points': 5}

print(alien_0['color'])
print(alien_0['points'])

# Add a new key
alien_0['x_position'] = 0
alien_0['y_position'] = 25
alien_0['speed'] = 'medium'
print(alien_0)

# Modifying value in dictionary
alien_0['color'] = 'yellow'
print(alien_0)

# Move the alien to the right.
# Determine how far to move the alien based on its current sp
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    # This must be a fast alien.
    x_increment = 3
    #The new position is the old position plus the increment.
alien_0['x_position'] = alien_0['x_position'] + x_increment
print(alien_0)

# Removing key 'pointers'
del alien_0['points']
print(alien_0)

# using get() method to find value of key
point_value = alien_0.get('points', 'No point value assigned.')
print(point_value)