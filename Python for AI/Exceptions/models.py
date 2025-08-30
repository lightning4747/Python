import numpy as np
import pickle 
import logging as logger

try:
    # Try to load a pre-trained model
    with open('trained_model.pkl', 'rb') as f:
        model = pickle.load(f)
    # Try to load the new data
    data = np.load('new_data.npy')
except FileNotFoundError as e:
    logger.error(f"Required file not found: {e}. Please run the training script first.")
    exit(1) # Exit gracefully with an error code
except Exception as e:
    logger.error(f"An unexpected error occurred during loading: {e}")
    exit(1)
else:
    # Only predict if loading succeeded
    predictions = model.predict(data)