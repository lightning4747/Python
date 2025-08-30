import pickle

# A complex Python object common in AI
complex_data = {
    'model_name': 'AwesomeClassifier',
    'hyperparameters': {'C': 1.0, 'kernel': 'linear'},
    'accuracy': 0.95,
    'feature_list': ['age', 'salary', 'department']
}

# Serialize and write the object to a file
with open('model_config.pkl', 'wb') as file:
    pickle.dump(complex_data, file) # dump() writes to a file
    # You can also use pickle.dumps() to get the bytes directly.

# Read and deserialize the object from the file
with open('model_config.pkl', 'rb') as file:
    loaded_data = pickle.load(file) # load() reads from a file
    # pickle.loads() takes bytes directly.

print(loaded_data)
# Output: The entire dictionary is perfectly restored.
print(loaded_data['feature_list'][1]) # Output: 'salary'