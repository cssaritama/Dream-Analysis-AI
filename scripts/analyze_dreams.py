import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from collections import Counter
import logging
import ast
import numpy as np

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

plt.style.use('default')
sns.set_palette("husl")

def load_data(file_path: str) -> pd.DataFrame:
    logger.info(f"Loading data from {file_path}")
    return pd.read_csv(file_path)

def analyze_emotions(dreams: pd.DataFrame) -> dict:
    logger.info("Analyzing emotions...")
    
    all_emotions = []
    for emotions_list in dreams['emotions']:
        emotions = ast.literal_eval(emotions_list)
        all_emotions.extend(emotions)
    
    emotion_counts = Counter(all_emotions)
    
    plt.figure(figsize=(10, 6))
    plt.bar(emotion_counts.keys(), emotion_counts.values(), color='skyblue')
    plt.title('Emotion Distribution in Dreams')
    plt.xlabel('Emotions')
    plt.ylabel('Frequency')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
    
    return dict(emotion_counts)

def analyze_symbols(dreams: pd.DataFrame) -> dict:
    logger.info("Analyzing symbols...")
    
    all_symbols = []
    for symbols_list in dreams['symbols']:
        symbols = ast.literal_eval(symbols_list)
        all_symbols.extend(symbols)
    
    symbol_counts = Counter(all_symbols)
    
    plt.figure(figsize=(12, 6))
    plt.bar(symbol_counts.keys(), symbol_counts.values(), color='lightcoral')
    plt.title('Symbol Distribution in Dreams')
    plt.xlabel('Symbols')
    plt.ylabel('Frequency')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
    
    return dict(symbol_counts)

def generate_insights(dreams: pd.DataFrame, emotion_counts: dict, symbol_counts: dict) -> None:
    logger.info("Generating insights...")
    
    most_common_emotion = max(emotion_counts.items(), key=lambda x: x[1])
    most_common_symbol = max(symbol_counts.items(), key=lambda x: x[1])
    
    print("\n🔍 KEY INSIGHTS:")
    print(f"• Most common emotion: {most_common_emotion[0]} ({most_common_emotion[1]} occurrences)")
    print(f"• Most common symbol: {most_common_symbol[0]} ({most_common_symbol[1]} occurrences)")
    print(f"• Total dreams analyzed: {len(dreams)}")
    print(f"• Average emotional intensity: {dreams['emotional_intensity'].mean():.1f}/10")
    print(f"• Average sleep quality: {dreams['sleep_quality'].mean():.1f}/10")

if __name__ == "__main__":
    print("🔍 STARTING DREAM ANALYSIS...")
    
    dreams = load_data("data/processed/cleaned_dreams.csv")
    emotion_counts = analyze_emotions(dreams)
    symbol_counts = analyze_symbols(dreams)
    generate_insights(dreams, emotion_counts, symbol_counts)
    
    print("✅ ANALYSIS COMPLETE!")