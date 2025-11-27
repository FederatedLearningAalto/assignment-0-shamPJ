from assignment import sum_of_3

# Test #1: basic positive numbers
assert sum_of_3(1, 2, 3) == 6, "Test #1 failed"

# Test #2: including zero
assert sum_of_3(0, 5, 7) == 12, "Test #2 failed"

# Test #3: negative numbers
assert sum_of_3(-1, -2, -3) == -6, "Test #3 failed"

# Test #4: mix of positive and negative
assert sum_of_3(-1, 5, -3) == 1, "Test #4 failed"

# Test #5: floating point numbers
assert sum_of_3(1.5, 2.5, 3.0) == 7.0, "Test #5 failed"

print("All tests passed!")
