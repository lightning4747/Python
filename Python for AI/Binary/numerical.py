import numpy as np

# Create a large array (common in AI)
large_array = np.random.rand(1000, 1000) # 1,000,000 random numbers

# Save the array to a .npy file
np.save('large_dataset.npy', large_array) # Notice no 'wb' needed. NumPy handles it.

# Load the array back into memory
loaded_array = np.load('large_dataset.npy')

print(np.array_equal(large_array, loaded_array)) # Output: True