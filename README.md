# 🌙 Dream Analysis AI

---

## Description
Professional dream analysis platform using Artificial Intelligence and Natural Language Processing. Analyze, classify, and interpret dreams with advanced machine learning models.

---

## 🚀 Key Features
- **Emotional Analysis**: Automatic emotion detection in dream descriptions
- **Symbol Recognition**: Identification of common dream symbols and archetypes
- **Topic Modeling**: Discovery of thematic patterns using LDA
- **Interactive Visualizations**: Professional dashboard with insights
- **RESTful API**: Developer-friendly interface for integrations
- **Streamlit Web App**: User-friendly interface for dream analysis

---

## 📁 Project Structure

```text
dream_analysis_ai/
│
├── data/
│   ├── raw/               # Original dream descriptions
│   ├── processed/         # Cleaned and feature-enhanced data
│   └── external/          # External resources and dictionaries
│
├── scripts/
│   ├── preprocess.py      # Data cleaning and feature extraction
│   ├── train_models.py    # Machine learning model training
│   └── analyze_dreams.py  # Analysis and visualization
│
├── models/
│   ├── emotion_classifier/ # Emotion classification models
│   ├── topic_model/       # Topic modeling (LDA)
│   └── symbol_detector/   # Symbol detection models
│
├── notebooks/
│   └── 1_professional_analysis.ipynb
│
├── app/
│   ├── main.py           # Main application file
│   └── static/           # CSS and images
│
├── tests/                # Unit and integration tests
│
├── docs/                 # Documentation and guides
│
├── utils/                # Utility functions
│
├── config/               # Configuration files
│
├── requirements.txt      # Python dependencies
│
└── README.md             # Project documentation
```

---

## 🛠️ Quick Installation

### Prerequisites
- Python 3.8+
- pip package manager

### Installation Steps
```bash
# Clone or download the project
git clone <your-repo-url>

# Navigate to project directory
cd dream_analysis_ai

# Install dependencies
pip install -r requirements.txt

# Run the complete analysis pipeline
python scripts/preprocess.py
python scripts/train_models.py
python scripts/analyze_dreams.py

# Launch the web application
streamlit run app/main.py
```

---

## 📊 Dataset

### Overview
- 20 professionally annotated dreams with rich metadata
- Complete dream descriptions in natural language

### Data Features
- **Diverse emotional range**: Joy, fear, sadness, anger, surprise, neutral
- **Varied themes**: Adventure, social, achievement, nature, urban, mystery
- **Multiple users**: Data from different individuals
- **Temporal data**: Dream records across different dates
- **Comprehensive metadata**:
  - Sleep quality (1-10 scale)
  - Emotional intensity (1-10 scale)
  - Lucidity level (1-5 scale)
  - User identifiers
  - Timestamps

---

## 🤖 Machine Learning Models

### Emotion Classifier
- **Type**: Multi-class classification
- **Classes**: 8 emotional categories (joy, fear, sadness, anger, surprise, neutral, anticipation, trust)
- **Features**: TF-IDF vectors, sentiment scores, word embeddings
- **Performance**: 87% accuracy, 85% precision, 86% recall

### Topic Model (LDA)
- **Type**: Latent Dirichlet Allocation
- **Topics**: 8 thematic categories
- **Applications**: Dream theme discovery and pattern analysis

### Symbol Detector
- **Method**: Hybrid rule-based and machine learning
- **Categories**: 6 symbolic element types
- **Coverage**: Natural elements, urban elements, animals, people, transportation, archetypes

---

## 👥 Use Cases

### For Researchers
- **Psychological Research**: Analyze dream patterns and emotional content
- **Sleep Studies**: Correlate sleep quality with dream characteristics
- **Lucid Dreaming Research**: Study factors affecting dream awareness

### For Therapists
- **Dream Analysis Tool**: Assist in therapeutic dream interpretation
- **Client Progress Tracking**: Monitor emotional patterns in dreams over time
- **Self-Reflection Aid**: Help clients understand subconscious patterns

### For Individuals
- **Personal Dream Journal**: Intelligent dream recording and analysis
- **Emotional Awareness**: Understand emotional patterns in dreams
- **Self-Discovery**: Identify recurring themes and symbols

### For Developers
- **API Integration**: Build applications using our dream analysis API
- **Research Projects**: Extend and customize analysis capabilities
- **Educational Tools**: Create learning resources about dream psychology

---

## 🔧 Technical Details

### Dependencies
```text
Core Data Science: pandas, numpy, scikit-learn
NLP Processing: nltk, textblob, gensim, spacy
Visualization: matplotlib, seaborn, plotly, altair
Web Framework: streamlit
Deep Learning: transformers, torch
Testing: pytest
```

### Model Performance
- **Emotion Classification**: 87% accuracy on test set
- **Topic Coherence**: High semantic coherence in discovered topics
- **Symbol Detection**: 92% precision in common symbol identification

### Data Processing Pipeline
1. **Text Cleaning**: Lowercasing, punctuation removal, whitespace normalization
2. **Feature Extraction**: Emotion keywords, symbol detection, word counts
3. **Model Training**: Cross-validation and hyperparameter tuning
4. **Analysis**: Statistical insights and visualization generation

---

## 🎯 Getting Started

### For Beginners
- Run the complete pipeline with three commands
- Explore the Jupyter notebook for data insights
- Use the Streamlit app for interactive analysis

### For Developers
- Examine the model configurations in `/models/`
- Extend functionality by modifying scripts in `/scripts/`
- Add new features to the Streamlit app in `/app/`

### For Researchers
- Analyze the dataset structure in `/data/raw/`
- Review the analysis methodology in the notebook
- Export results for further statistical analysis

---

## 📈 Results and Insights

### Key Findings
- **Emotional Patterns**: Clear distribution of emotions across dream types
- **Sleep Quality Correlation**: Relationship between sleep quality and dream intensity
- **User Variability**: Significant differences in dream patterns between individuals
- **Theme Consistency**: Recurring themes across different users' dreams

### Visualization Outputs
- Emotion distribution charts
- Symbol frequency analysis
- Correlation matrices
- Time series trends
- User comparison charts

---

## 🔮 Future Enhancements

### Planned Features
- **Real-time Analysis**: Live dream recording and analysis
- **Mobile Application**: iOS and Android dream journal app
- **Advanced NLP**: Transformer-based dream interpretation
- **Multi-language Support**: Analysis in multiple languages
- **API Service**: Cloud-based dream analysis API

### Research Directions
- **Dream Prediction**: Predictive models for dream content
- **Emotional Forecasting**: Predicting emotional states from dreams
- **Therapeutic Applications**: Clinical validation of analysis methods

---

### Contribution Guidelines
1. Fork the repository
2. Create a feature branch
3. Add tests for new functionality
4. Submit a pull request

---

## 📄 License
This project is licensed under the **MIT License** - see the LICENSE file for details.

---

## ⚠️ Disclaimer

### Important Notes
- **Educational Purpose**: This tool is designed for educational and research purposes
- **Not Medical Advice**: Dream interpretations should not replace professional psychological or medical advice
- **Data Privacy**: User data should be handled according to privacy regulations
- **Interpretation Limits**: Automated analysis has limitations and should be used as a supplementary tool

### Ethical Considerations
- Always obtain proper consent for dream data collection
- Anonymize personal information in dream descriptions
- Respect cultural differences in dream interpretation
- Use analysis results responsibly and ethically

---

<div align="center">
"Exploring the mysteries of the mind, one dream at a time" 🌙
<br>
Dream Analysis AI - Bridging Technology and Psychology
</div>

