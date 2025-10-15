import numpy as np

arr = np.array([3, 7, 1, 9, 2, 7, 4, 3, 7, 5])

specified_num = 5

less_than = arr[arr < specified_num]

greater_than = arr[arr > specified_num]

max_val = np.max(arr)
min_val = np.min(arr)

argmax_index = np.argmax(arr)
argmin_index = np.argmin(arr)

unique_elements, counts = np.unique(arr, return_counts=True)

bin_count = np.bincount(arr)

array_repr = repr(arr)

print("Original array:", arr)
print("Array representation:", array_repr)

print("\nPart (a):")
print(f"Numbers less than {specified_num}:", less_than)
print(f"Numbers greater than {specified_num}:", greater_than)

print("\nPart (b):")
print("Max value:", max_val)
print("Min value:", min_val)
print("Index of max value (argmax):", argmax_index)
print("Index of min value (argmin):", argmin_index)

print("Unique elements:", unique_elements)
print("Counts of unique elements:", counts)
print("Bincount (frequency of each integer index):", bin_count)
