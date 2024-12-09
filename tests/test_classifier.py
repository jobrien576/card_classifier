import os
import pytest
import numpy as np
from src.cropped_cards import preprocess_card_image  # Example function for preprocessing
from src.classifier import load_model, predict_card  # Example model-related functions

# Test 1: Test preprocessing of card images
def test_preprocess_card_image():
    # Assume we have a test image in a known location
    test_image_path = "tests/test_data/sample_card.jpg"
    assert os.path.exists(test_image_path), "Test image file not found"

    # Call the preprocessing function
    preprocessed_image = preprocess_card_image(test_image_path)

    # Check if the output is the correct size (e.g., 224x224 for a model like ResNet)
    assert preprocessed_image.shape == (224, 224, 3), "Preprocessed image shape is incorrect"

# Test 2: Test loading the model
def test_load_model():
    # Call the load_model function
    model = load_model()

    # Check if the model is loaded correctly (not None)
    assert model is not None, "Model failed to load"

# Test 3: Test model prediction
def test_predict_card():
    # Assume we have a test preprocessed image (random noise for simplicity here)
    test_image = np.random.rand(1, 224, 224, 3).astype(np.float32)

    # Load model and make a prediction
    model = load_model()
    prediction = predict_card(model, test_image)

    # Check that the prediction is not empty
    assert prediction is not None, "Prediction is empty"
    assert isinstance(prediction, str), "Prediction is not a string"
    assert prediction in ["A_club", "10_heart", "7_diamond"], "Unexpected card prediction result"
