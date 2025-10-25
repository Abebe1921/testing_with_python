"""
Input an integer and number of shift positions.

Show results of left shift and right shift.

Print the binary form before and after.
"""

num = int(input("Enter an integer: "))
shift = int(input("Enter number of shift positions: "))

binary_before = bin(num)

left_shift = num << shift
right_shift = num >> shift

binary_left = bin(left_shift)
binary_right = bin(right_shift)

print(f"Original number: ",num)
print(f"Binary (before): ",binary_before)

print("Bitwise Shift Results")

print(f"Left Shift by ",shift,":")
print(f"Result: ",left_shift)
print(f"Binary: ",binary_left)

print(f"Right Shift by: ",shift)
print(f"Result: ",right_shift)
print(f"Binary: ",binary_right)
