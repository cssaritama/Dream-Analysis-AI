import pandas as pd
import re
import logging
from typing import List, Dict
import ast

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class DreamPreprocessor:
    def __init__(self):
        self.emotion_keywords = {
            'joy': ['happy', 'joy', 'euphoric', 'peaceful', 'content', 'free', 'laughing', 'smiling'],
            'fear': ['scared', 'afraid', 'fear', 'terrified', 'anxious', 'worried', 'panic', 'frightened'],
            'sadness': ['sad', 'depressed', 'unhappy', 'mournful', 'melancholy', 'alone', 'crying', 'lost'],
            'anger': ['angry', 'mad', 'furious', 'enraged', 'frustrated', 'annoyed'],
            'surprise': ['surprised', 'shocked', 'amazed', 'astonished', 'unexpected'],
            'neutral': ['neutral', 'calm', 'normal', 'fine', 'okay']
        }
        
        self.symbol_keywords = {
            'ocean': ['ocean', 'sea', 'water', 'waves', 'beach', 'shore'],
            'forest': ['forest', 'woods', 'trees', 'jungle', 'wilderness'],
            'city': ['city', 'building', 'skyscraper', 'urban', 'street'],
            'animals': ['animal', 'dog', 'cat', 'bird', 'dolphin', 'lion'],
            'people': ['person', 'people', 'friend', 'family', 'stranger'],
            'flying': ['flying', 'fly', 'air', 'sky', 'floating']
        }
    
    def clean_text(self, text: str) -> str:
        if not isinstance(text, str):
            return ""
        text = text.lower().strip()
        text = re.sub(r'[^\w\s]', '', text)
        text = re.sub(r'\s+', ' ', text)
        return text
    
    def extract_emotions(self, text: str) -> List[str]:
        emotions = []
        for emotion, keywords in self.emotion_keywords.items():
            if any(keyword in text for keyword in keywords):
                emotions.append(emotion)
        return emotions if emotions else ['neutral']
    
    def extract_symbols(self, text: str) -> List[str]:
        symbols = []
        for symbol, keywords in self.symbol_keywords.items():
            if any(keyword in text for keyword in keywords):
                symbols.append(symbol)
        return symbols if symbols else ['none']
    
    def process_dataframe(self, df: pd.DataFrame) -> pd.DataFrame:
        logger.info("Processing dream data...")
        df['cleaned_text'] = df['dream_description'].apply(self.clean_text)
        df['emotions'] = df['cleaned_text'].apply(self.extract_emotions)
        df['symbols'] = df['cleaned_text'].apply(self.extract_symbols)
        df['word_count'] = df['dream_description'].str.split().str.len()
        return df

def preprocess_dreams(input_path: str, output_path: str) -> None:
    try:
        logger.info(f"Loading data from {input_path}")
        dreams_df = pd.read_csv(input_path)
        
        preprocessor = DreamPreprocessor()
        processed_df = preprocessor.process_dataframe(dreams_df)
        
        processed_df.to_csv(output_path, index=False)
        logger.info(f"Successfully processed {len(processed_df)} dreams")
        
        print("\n📊 PREPROCESSING SUMMARY:")
        print(f"Total dreams: {len(processed_df)}")
        print(f"Average word count: {processed_df['word_count'].mean():.1f}")
        
    except Exception as e:
        logger.error(f"Error in preprocessing: {str(e)}")
        raise

if __name__ == "__main__":
    preprocess_dreams(
        input_path="data/raw/dream_descriptions.csv",
        output_path="data/processed/cleaned_dreams.csv"
    )