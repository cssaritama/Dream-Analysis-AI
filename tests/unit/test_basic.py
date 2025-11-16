import pytest
import sys
import os
sys.path.append('../scripts')

def test_imports():
    try:
        from preprocess import DreamPreprocessor
        from train_models import train_emotion_classifier
        assert True
    except ImportError:
        assert False

def test_data_loading():
    import pandas as pd
    try:
        data = pd.read_csv('../data/raw/dream_descriptions.csv')
        assert len(data) > 0
        assert 'dream_description' in data.columns
    except:
        assert False

if __name__ == '__main__':
    pytest.main([__file__, '-v'])