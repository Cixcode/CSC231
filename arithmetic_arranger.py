def arithmetic_arranger(operations:list, with_answer=False):
    display_stack = []
    def logger(key, error): # An helper function that log the errors to the screen
        # print(f"Error in {key+1}: {error}")
        print(f"Error: {error}")

    if len(operations) > 7:
        logger('Too many problems.')
        return;
    for i, ops in enumerate(operations):
        # Find the index of the operator (-,+)
        operator_index = max(ops.find('+'), ops.find('-'))
        if operator_index == -1: # Log error if no operator in (-,+) is found
            logger(i, "Operator must be '+' or '-'.")
            continue
        operator = ops[operator_index]
        ops = ops.split(operator) # Split the input string with the operator
        if len(ops) != 2:
            logger(i, 'The operation has to be 2.')
            continue
        # Remove unnecessary empty space around the operands and assign to variable 
        ops1, ops2 = (i.strip() for i in ops)
        ops1_len, ops2_len = len(ops1), len(ops2)
        if not ops1.isdigit() or not ops2.isdigit(): # Log error if any of the operands is not a number
            logger(i, "Numbers must only contain digits.")
            continue
        if ops1_len > 6 or ops2_len > 6:
            logger(i, "Number cannot be more than six digits.")
            continue
        # The width of the display is sum of the longest operand, length of operator, length of an empty space
        # length of operator = 1
        # length of empty space = 1
        # length of operator + length of empty space = 2
        width = max(ops1_len, ops2_len) + 2
        solution = eval(ops1+operator+ops2) # Solving the arithmetic with builtin eval function
        # Each result is added to the display stack
        display_stack.append([f"{ops1}".rjust(width),
              f"{operator} "+f"{ops2}".rjust(width-2),#subtract length of operator and empty space
              f"{'-'*width}",
              f"{solution}".rjust(width) if with_answer else '',
              f"{'-'*width}" if with_answer else ''])
    # Display all the arithmetic in display stack side by side separated with 4 empty space
    for i in zip(*display_stack):
        print(*i, sep=' '*4)


if __name__ == '__main__':
    arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])
    arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"], True)
