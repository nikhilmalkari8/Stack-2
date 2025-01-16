def isValid(s):
    # Mapping of closing to opening brackets
    bracket_map = {')': '(', '}': '{', ']': '['}
    stack = []

    for char in s:
        if char in bracket_map:  # If it's a closing bracket
            # Check the top of the stack or use a dummy value
            top_element = stack.pop() if stack else '#'
            if bracket_map[char] != top_element:
                return False
        else:  # It's an opening bracket
            stack.append(char)

    return not stack
