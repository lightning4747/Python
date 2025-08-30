# Define a custom exception for your AI application
class TrainingDataError(Exception):
    """Exception raised for errors in the training data."""
    def __init__(self, message, missing_features=None):
        super().__init__(message)
        self.missing_features = missing_features # You can add custom attributes!

# A function that validates data
def validate_training_data(data):
    required_features = ['age', 'salary']
    missing = [feature for feature in required_features if feature not in data]
    
    if missing:
        # Raise our custom exception with helpful context
        raise TrainingDataError(
            message="Training data is missing required features.",
            missing_features=missing
        )

# Using the custom exception
try:
    user_data = {'age': 30} # Missing 'salary'
    validate_training_data(user_data)
except TrainingDataError as e:
    print(f"Validation failed: {e}")
    print(f"Please add the following features: {e.missing_features}")
    # You could log this, send an alert, or use a default dataset.