import numpy as np

print("a. Help on np.add function:")
help(np.add)

print("\nb. Check if none of the elements are zero:")
arr1 = np.array([1, 2, 3, 4])
print("Array:", arr1)
print("None of the elements is zero:", np.all(arr1)) 

print("\nc. Element-wise comparisons:")
arr2 = np.array([1, 2, 3, 4])
arr3 = np.array([2, 2, 2, 2])

print("Array 1:", arr2)
print("Array 2:", arr3)

print("Greater:", np.greater(arr2, arr3))
print("Greater Equal:", np.greater_equal(arr2, arr3))
print("Less:", np.less(arr2, arr3))
print("Less Equal:", np.less_equal(arr2, arr3))
print("Equal:", np.equal(arr2, arr3))
print("Equal within a tolerance (allclose):", np.allclose(arr2, arr3, atol=1.0))

print("\nAdditional Examples:")


zeros_array = np.zeros((2, 3))
print("Zeros array:\n", zeros_array)


ones_array = np.ones((2, 3))
print("Ones array:\n", ones_array)


linspace_array = np.linspace(0, 1, 5)
print("Linspace array:", linspace_array)

list_from_array = linspace_array.tolist()
print("Converted to list:", list_from_array)
