'''
task 1 recursive
'''
def sum_nested_recursive(lst):
    total = 0
    for element in lst:
        if isinstance(element, list):
            total += sum_nested_recursive(element)
        else:
            total += element
    return total

nested_list = [1, [2, [3, 4, [5]]]]
result_recursive = sum_nested_recursive(nested_list)
print(result_recursive)

'''
not recursive
'''
def sum_nested_iterative(lst):
    total = 0
    stack = [lst]

    while stack:
        current = stack.pop()
        for element in current:
            if isinstance(element, list):
                stack.append(element)
            else:
                total += element

    return total

nested_list = [1, [2, [3, 4, [5]]]]
result_iterative = sum_nested_iterative(nested_list)
print(result_iterative)

'''
task 2 recursive
'''
import math
def recursive_sequence(n):
    if n == 1:
        return 1
    else:
        return 0.5 * (math.sqrt(recursive_sequence(n - 1)) + 0.5 * math.sqrt(recursive_sequence(n - 1)))

n_value = 4
result_recursive = recursive_sequence(n_value)
print(f"a{n_value} =", result_recursive)

'''
not recursive
'''
def non_recursive_sequence(n):
    a = [0] * (n + 1)
    a[1] = 1

    for i in range(2, n + 1):
        a[i] = 0.5 * (math.sqrt(a[i - 1]) + 0.5 * math.sqrt(a[i - 1]))

    return a[n]

n_value = 2
result_non_recursive = non_recursive_sequence(n_value)
print(f"a{n_value} =", result_non_recursive)