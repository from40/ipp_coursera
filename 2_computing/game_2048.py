

"""
Merge function for 2048 game.
"""

def merge(line):
    """
    Function that merges a single row or column in 2048.
    """
    # replace with your code
    merged_list = [0 for index in range(len(line))]
    update_index = 0
    for index in range(len(line)):
        if line[index] != 0:
            if merged_list[update_index] == 0:
                merged_list[update_index] += line[index]
            else:
                if merged_list[update_index] == line[index]:
                    merged_list[update_index] += line[index]
                    update_index += 1 
                else:
                    update_index += 1
                    merged_list[update_index] += line[index]     
    return merged_list
