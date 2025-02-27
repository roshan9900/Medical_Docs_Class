# Medical Documents Classification - An End-to-End MLOps Project

## Overview
This project is an end-to-end MLOps pipeline for classifying medical documents using machine learning and deep learning techniques. It integrates data ingestion, preprocessing, model training, evaluation, and deployment, ensuring a seamless workflow with automation.

## Project Structure
```
roshan9900-medical_docs_class/
│── README.md            # Project Documentation
│── Dockerfile           # Containerization Setup
│── LICENSE              # Licensing Information
│── app.py               # Web Application Backend
│── kaggle.json          # Kaggle API Credentials
│── main.py              # Entry Point for Training and Evaluation
│── params.yaml          # Model Parameters and Configuration
│── requirements.txt     # Dependencies and Packages
│── schema.yaml          # Data Schema Definition
│── setup.py             # Package Setup
│── template.py          # Code Template for Reproducibility
│── config/              # Configuration Files
│   └── config.yaml      # Project Configuration
│── research/            # Research and Experimentation
│   ├── data_ingestion.ipynb  # Data Preprocessing
│   └── research.ipynb        # Model Experiments
│── src/Medical_Text_Classification/  # Core Source Code
│   ├── components/      # Data Ingestion, Processing, and Model Training Modules
│   ├── config/          # Configuration Management
│   ├── constants/       # Constant Variables
│   ├── entity/          # Entity Definitions
│   ├── pipeline/        # Complete ML Pipeline
│   ├── utils/           # Utility Functions
│   └── monitoring/      # Model Monitoring and Logging
│── templates/           # Frontend HTML Templates
│   └── index.html       # Web Interface
└── .github/workflows/   # CI/CD Workflows
```

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/roshan9900/Medical_Docs_Class.git
   cd Medical_Docs_Class
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Set up environment variables in `.env` if necessary.

## End-to-End MLOps Pipeline

### 1. Data Ingestion
- Fetch data from Kaggle or other sources.
- Perform data cleaning and preprocessing.

### 2. Data Validation
- Validate schema using `schema.yaml`.
- Check for missing values and inconsistencies.

### 3. Data Transformation
- Convert raw text into numerical representations (TF-IDF, Word Embeddings, etc.).
- Tokenization and vectorization for deep learning models.

### 4. Model Training
- Train traditional ML models like Random Forest (90% accuracy).
- Train deep learning models like BERT with superior performance.

### 5. Model Evaluation
- Evaluate models using metrics such as Accuracy, Precision, Recall, and F1-score.
- **BERT Model Performance:**
  - Accuracy: **98.94%**
  - Precision: **98.95%**
  - Recall: **98.94%**
  - F1 Score: **98.94%**

### 6. Model Deployment
- Deploy the best model using **Flask** in `app.py`.
- Serve predictions through an API endpoint.

### 7. CI/CD Integration
- Automate model training and deployment using GitHub Actions.
- Use **Docker** for containerization and deployment.

### 8. Monitoring and Logging
- Track model performance using monitoring tools.
- Log model predictions and retrain as needed.

## Running the Project
To train and evaluate the models:
```bash
python main.py
```

To run the web application locally:
```bash
python app.py
```

## Contributing
Feel free to fork the repository and submit pull requests for improvements.

## License
This project is licensed under the GPL-3.0 License.

