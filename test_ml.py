import pytest
# TODO: add necessary import
import os
from numpy import load
import pytest
import pandas as pd
import sklearn
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from ml.data import process_data
from ml.model import load_model, train_model
from fastapi.testclient import TestClient
from main import app
from sklearn.metrics import accuracy_score
import unittest
from ml.model import train_model
from train_model import X_train, y_train

# TODO: implement the first test. Change the function name and input as needed
client = TestClient(app
def test_api():
    """
    # Tests if API request was successfull
    """
    r = client.get("/")
    assert r.status_code == 200
    pass


# TODO: implement the second test. Change the function name and input as needed
def test_used_algorithm():
    """
    Tests if the model is using the correct machine learning algorithm
    """
    model = train_model(X_train,y_train)  
    expected_algorithm = 'RandomForestClassifier' 
    assert type(model).__name__ == expected_algorithm, f"Expected {expected_algorithm}, {type(model).__name__} actual"


# TODO: implement the third test. Change the function name and input as needed
def compute_accuracy(y_true, y_pred):
    return accuracy_score(y_true, y_pred)

class TestMetricsFunctions(unittest.TestCase):
    def test_compute_accuracy(self):
        """
        Tests classification accuracy between two lists of labels.
        """
        
        y_true = [0, 1, 1, 0, 1, 0, 0, 0, 1, 1]
        y_pred = [0, 0, 1, 0, 1, 0, 1, 0, 0, 1]

        computed_accuracy = compute_accuracy(y_true, y_pred)
        
        expected_accuracy = 0.7          

        self.assertAlmostEqual(computed_accuracy, expected_accuracy, places=2, msg= "The computed accuracy did not meet the expected threshold of 0.7.")