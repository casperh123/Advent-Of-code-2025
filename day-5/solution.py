import os

def apply(char, a, b):
    if char == "+":
        return a + b
    elif char == "*":
        return a * b


# def solve(lines):
    
#     operators = lines.pop().split()
#     sum = 0

#     for numbers in lines:
#         for index, number in enumerate(numbers):
#             results[index] = apply(operators[index], results[index], int(number))
    
#     for numbers in results:
#         sum = sum + numbers

#     return sum

def collect_digit(char, number):
    return (int(number) * 10) + int(char)
    
def solve_2(lines):
    operators_line = lines.pop()
    
    # Remove newlines
    lines = [line for line in lines]
    
    # Find max width
    max_width = max(len(line) for line in lines)
    
    # Pad lines to same width
    lines = [line.ljust(max_width) for line in lines]
    
    problems = []
    current_problem = []
    
    # Process columns RIGHT-TO-LEFT
    for col_idx in range(max_width - 1, -1, -1):
        # Get all characters in this column
        column_chars = [line[col_idx] for line in lines]
        
        # Check if column is all spaces
        if all(c == ' ' for c in column_chars):
            if current_problem:
                problems.append(current_problem)
                current_problem = []
        else:
            # Build number from this column (top to bottom)
            number_str = ''.join(column_chars).replace(' ', '')
            if number_str:
                current_problem.append(int(number_str))
    
    if current_problem:
        problems.append(current_problem)
    
    # Calculate grand total
    grand_total = 0
    operators = [c for c in operators_line if c in ['+', '*']]
    
    for prob_idx, problem in enumerate(problems):
        if prob_idx < len(operators):
            op = operators[prob_idx]
            result = problem[0]
            for num in problem[1:]:
                result = apply(op, result, num)
            grand_total += result
    
    return grand_total
        
    

path = os.path.dirname(os.path.abspath(__file__))
lines = [list(x) for x in open(path + '/day-5.txt').readlines()]

count = solve_2(lines)

print(lines)
print(count)