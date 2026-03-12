# AI-Powered Construction Cost & Delay Prediction System

An intelligent system for contractors to predict construction project costs and potential delays using machine learning.

## Features

- **Cost Prediction**: Estimate total project costs based on parameters like area, location, materials, etc.
- **Delay Prediction**: Predict potential delays and delay probability
- **Risk Assessment**: Get a comprehensive risk score with identified risk factors
- **Scenario Comparison**: Compare different project configurations to find optimal approaches
- **Project Management**: Save and track projects with prediction history

## Tech Stack

- **Backend**: Python, Flask, SQLAlchemy
- **ML Models**: XGBoost, Scikit-learn, Gradient Boosting
- **Database**: SQLite
- **Frontend**: HTML, CSS, JavaScript

## Installation

1. **Create a virtual environment** (recommended):
   ```bash
   cd construction_predictor
   python -m venv venv

   # Windows
   venv\Scripts\activate

   # macOS/Linux
   source venv/bin/activate
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Train the ML models** (optional - the system works with rule-based predictions without trained models):
   ```bash
   python train_models.py
   ```

4. **Run the application**:
   ```bash
   python run.py
   ```

5. **Open your browser** and go to: `http://localhost:5000`

## Project Structure

```
construction_predictor/
├── app/
│   ├── __init__.py          # Flask app factory
│   ├── models/
│   │   ├── __init__.py
│   │   └── database.py      # SQLAlchemy models
│   ├── routes/
│   │   ├── __init__.py
│   │   ├── main.py          # Main routes
│   │   ├── predictions.py   # Prediction API endpoints
│   │   └── projects.py      # Project management endpoints
│   ├── ml/
│   │   ├── __init__.py
│   │   └── predictor.py     # ML prediction engine
│   └── utils/
│       └── __init__.py
├── static/
│   ├── css/
│   │   └── style.css        # Dashboard styles
│   └── js/
│       └── main.js          # Frontend JavaScript
├── templates/
│   └── index.html           # Dashboard template
├── data/
│   └── sample_data.csv      # Training data
├── trained_models/          # Saved ML models (after training)
├── config.py                # Configuration settings
├── run.py                   # Application entry point
├── train_models.py          # Model training script
├── requirements.txt         # Python dependencies
└── README.md
```

## API Endpoints

### Predictions

- `POST /api/predictions/predict` - Get a prediction for a project
- `POST /api/predictions/quick-estimate` - Quick estimate without saving
- `POST /api/predictions/compare` - Compare multiple scenarios
- `GET /api/predictions/history` - Get prediction history
- `GET /api/predictions/<id>` - Get specific prediction

### Projects

- `GET /api/projects` - List all projects
- `POST /api/projects` - Create a new project
- `GET /api/projects/<id>` - Get project details
- `PUT /api/projects/<id>` - Update a project
- `DELETE /api/projects/<id>` - Delete a project
- `POST /api/projects/<id>/complete` - Mark project complete with actual values
- `GET /api/projects/stats` - Get overall statistics

## Input Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| project_type | string | residential, commercial, industrial, infrastructure |
| location | string | City/State location |
| total_area_sqft | float | Total area in square feet |
| num_floors | int | Number of floors |
| num_workers | int | Number of workers assigned |
| planned_duration_days | int | Planned project duration |
| material_quality | string | economy, standard, premium |
| complexity_level | string | low, medium, high |
| has_basement | bool | Whether project includes basement |
| weather_risk_zone | string | low, moderate, high |
| contractor_experience_years | int | Years of contractor experience |

## Prediction Output

```json
{
  "predicted_cost": 2500000.00,
  "predicted_delay_days": 15.5,
  "delay_probability": 0.45,
  "risk_score": 42.5,
  "cost_lower_bound": 2125000.00,
  "cost_upper_bound": 2875000.00,
  "delay_lower_bound": 5.0,
  "delay_upper_bound": 26.0,
  "risk_factors": [...],
  "recommendations": [...]
}
```

## Training Custom Models

To train models on your own data:

1. Prepare a CSV file with the same columns as `data/sample_data.csv`
2. Update the `DATA_PATH` in `train_models.py`
3. Run `python train_models.py`

The more historical data you provide, the more accurate the predictions will be.

## License

MIT License
