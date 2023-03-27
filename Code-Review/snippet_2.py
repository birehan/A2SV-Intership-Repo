def is_valid_parenthesis(input_string):
    # Map opening parentheses to their corresponding closing parentheses
    parentheses_map = {
        '(': ')',
        '{': '}',
        '[': ']'
    }

    # Use a stack to keep track of opening parentheses
    stack = []

    # Iterate over each character in the input string
    for char in input_string:
        if char in parentheses_map.keys():
            # If the character is an opening parenthesis, push it onto the stack
            stack.append(char)
        elif len(stack) == 0 or parentheses_map[stack.pop()] != char:
            # If the character is a closing parenthesis, pop the top element from the stack
            # and check if it matches the corresponding opening parenthesis
            return False

    # If the stack is not empty, there are unmatched opening parentheses
    return len(stack) == 0