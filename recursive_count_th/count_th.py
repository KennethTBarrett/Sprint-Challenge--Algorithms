'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):  
    if len(word) == 0:  # If there's no word left (base case)...
        return 0  # Return 0.
    if word[:2] == 'th':  # If 'th' is in our first 2 characters...
        # We need to use recursion, slicing to take off the first letter, basically
        # traversing down the list counting each time. 
        return count_th(word[1:]) + 1  # Slice off, add 1 to the count.
    else:  # If it's not...
        return count_th(word[1:])  # Just slice, don't add 1 to the count.