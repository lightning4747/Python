import numpy as np

# Create multiple arrays
features = np.random.rand(100, 10) # 100 samples, 10 features each
labels = np.random.randint(0, 2, size=100) # 100 binary labels

# Save them into a single .npz file
np.savez('training_data.npz', features=features, targets=labels)

# Load the .npz archive
with np.load('training_data.npz') as archived_data:
    # It behaves like a dictionary-like object
    loaded_features = archived_data['features']
    loaded_labels = archived_data['targets']

print(loaded_features.shape) # Output: (100, 10)