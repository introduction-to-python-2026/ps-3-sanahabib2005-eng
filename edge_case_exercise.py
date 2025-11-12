def move(my_list, direction=None):
    # Finds the index of the one in the list
    index_of_one = my_list.index(1)
    # Move right if possible
    if direction == 'right':
       if index_of_one < len(my_list) - 1:
          my_list[index_of_one], my_list[index_of_one + 1] = 0, 1
        # else: do nothing (already at far right)

    # Move left if possible
    elif direction == 'left':
       if index_of_one > 0:
          my_list[index_of_one], my_list[index_of_one - 1] = 0, 1
        # else: do nothing (already at far left)

    return my_list
