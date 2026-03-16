"""
Script to train the ML models for construction cost and delay prediction.

Usage:
    python train_models.py

This script will:
1. Load training data from data/sample_data.csv
2. Train cost prediction model (XGBoost)
3. Train delay prediction model (Gradient Boosting)
4. Train delay probability model (Random Forest Classifier)
5. Save trained models to trained_models/
"""

import os
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.ensemble import GradientBoostingRegressor, RandomForestClassifier
from xgboost import XGBRegressor
import joblib

# Configuration
DATA_PATH = 'data/sample_data.csv'
MODEL_DIR = 'trained_models'

# Feature definitions
CATEGORICAL_FEATURES = ['project_type', 'location', 'material_quality',
                       'complexity_level', 'weather_risk_zone',
                       'soil_type', 'water_table_level', 'site_accessibility',
                       'foundation_type', 'finishing_level', 'site_topography']
NUMERICAL_FEATURES = ['total_area_sqft', 'num_floors', 'num_workers',
                     'planned_duration_days', 'contractor_experience_years',
                     'distance_from_city_km', 'floor_height_ft',
                     'num_bathrooms', 'electrical_load_kw']
BOOLEAN_FEATURES = ['has_basement']


def load_and_prepare_data(data_path):
    """Load and preprocess training data"""
    print(f"Loading data from {data_path}...")
    df = pd.read_csv(data_path)
    print(f"Loaded {len(df)} records")

    # Initialize encoders
    encoders = {}
    for feat in CATEGORICAL_FEATURES:
        encoders[feat] = LabelEncoder()
        df[f'{feat}_encoded'] = encoders[feat].fit_transform(df[feat].fillna('unknown'))

    # Convert boolean
    df['has_basement'] = df['has_basement'].astype(int)

    # Calculate delay (actual - planned duration)
    df['delay_days'] = df['actual_duration_days'] - df['planned_duration_days']
    df['has_delay'] = (df['delay_days'] > 0).astype(int)

    return df, encoders


def prepare_features(df):
    """Prepare feature matrix"""
    feature_cols = (
        NUMERICAL_FEATURES +
        BOOLEAN_FEATURES +
        [f'{feat}_encoded' for feat in CATEGORICAL_FEATURES]
    )

    X = df[feature_cols].values
    y_cost = df['actual_cost'].values
    y_delay = df['delay_days'].values
    y_delay_binary = df['has_delay'].values

    return X, y_cost, y_delay, y_delay_binary, feature_cols


def train_cost_model(X_train, y_train, X_test, y_test):
    """Train cost prediction model"""
    print("\n" + "="*50)
    print("Training Cost Prediction Model (XGBoost)")
    print("="*50)

    model = XGBRegressor(
        n_estimators=300,
        max_depth=8,
        learning_rate=0.05,
        subsample=0.8,
        colsample_bytree=0.8,
        min_child_weight=3,
        reg_alpha=0.1,
        reg_lambda=1.0,
        random_state=42,
        verbosity=0
    )

    model.fit(X_train, y_train)

    # Evaluate
    train_pred = model.predict(X_train)
    test_pred = model.predict(X_test)

    print(f"\nTraining Metrics:")
    print(f"  MAE: ${mean_absolute_error(y_train, train_pred):,.2f}")
    print(f"  RMSE: ${np.sqrt(mean_squared_error(y_train, train_pred)):,.2f}")
    print(f"  R2: {r2_score(y_train, train_pred):.4f}")

    print(f"\nTest Metrics:")
    print(f"  MAE: ${mean_absolute_error(y_test, test_pred):,.2f}")
    print(f"  RMSE: ${np.sqrt(mean_squared_error(y_test, test_pred)):,.2f}")
    print(f"  R2: {r2_score(y_test, test_pred):.4f}")

    return model


def train_delay_model(X_train, y_train, X_test, y_test):
    """Train delay prediction model"""
    print("\n" + "="*50)
    print("Training Delay Prediction Model (Gradient Boosting)")
    print("="*50)

    model = GradientBoostingRegressor(
        n_estimators=300,
        max_depth=6,
        learning_rate=0.05,
        subsample=0.8,
        min_samples_split=5,
        min_samples_leaf=3,
        random_state=42
    )

    model.fit(X_train, y_train)

    # Evaluate
    train_pred = model.predict(X_train)
    test_pred = model.predict(X_test)

    print(f"\nTraining Metrics:")
    print(f"  MAE: {mean_absolute_error(y_train, train_pred):.2f} days")
    print(f"  RMSE: {np.sqrt(mean_squared_error(y_train, train_pred)):.2f} days")
    print(f"  R2: {r2_score(y_train, train_pred):.4f}")

    print(f"\nTest Metrics:")
    print(f"  MAE: {mean_absolute_error(y_test, test_pred):.2f} days")
    print(f"  RMSE: {np.sqrt(mean_squared_error(y_test, test_pred)):.2f} days")
    print(f"  R2: {r2_score(y_test, test_pred):.4f}")

    return model


def train_delay_probability_model(X_train, y_train, X_test, y_test):
    """Train delay probability (classification) model"""
    print("\n" + "="*50)
    print("Training Delay Probability Model (Random Forest)")
    print("="*50)

    model = RandomForestClassifier(
        n_estimators=300,
        max_depth=10,
        min_samples_split=5,
        min_samples_leaf=2,
        random_state=42
    )

    model.fit(X_train, y_train)

    # Evaluate
    train_acc = model.score(X_train, y_train)
    test_acc = model.score(X_test, y_test)

    print(f"\nTraining Accuracy: {train_acc:.4f}")
    print(f"Test Accuracy: {test_acc:.4f}")

    return model


def save_models(cost_model, delay_model, delay_prob_model, encoders, scaler, model_dir):
    """Save all trained models"""
    print("\n" + "="*50)
    print(f"Saving models to {model_dir}/")
    print("="*50)

    os.makedirs(model_dir, exist_ok=True)

    joblib.dump(cost_model, os.path.join(model_dir, 'cost_model.joblib'))
    joblib.dump(delay_model, os.path.join(model_dir, 'delay_model.joblib'))
    joblib.dump(delay_prob_model, os.path.join(model_dir, 'delay_prob_model.joblib'))
    joblib.dump(encoders, os.path.join(model_dir, 'encoders.joblib'))
    joblib.dump(scaler, os.path.join(model_dir, 'scaler.joblib'))

    print("Models saved successfully!")
    print(f"  - cost_model.joblib")
    print(f"  - delay_model.joblib")
    print(f"  - delay_prob_model.joblib")
    print(f"  - encoders.joblib")
    print(f"  - scaler.joblib")


def main():
    print("="*60)
    print("  Construction Cost & Delay Prediction - Model Training")
    print("="*60)

    # Load data
    df, encoders = load_and_prepare_data(DATA_PATH)

    # Prepare features
    X, y_cost, y_delay, y_delay_binary, feature_cols = prepare_features(df)

    # Scale features
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    # Split data
    X_train, X_test, y_cost_train, y_cost_test, y_delay_train, y_delay_test, y_bin_train, y_bin_test = \
        train_test_split(X_scaled, y_cost, y_delay, y_delay_binary, test_size=0.2, random_state=42)

    print(f"\nTraining set size: {len(X_train)}")
    print(f"Test set size: {len(X_test)}")
    print(f"Features: {len(feature_cols)}")

    # Train models
    cost_model = train_cost_model(X_train, y_cost_train, X_test, y_cost_test)
    delay_model = train_delay_model(X_train, y_delay_train, X_test, y_delay_test)
    delay_prob_model = train_delay_probability_model(X_train, y_bin_train, X_test, y_bin_test)

    # Save models
    save_models(cost_model, delay_model, delay_prob_model, encoders, scaler, MODEL_DIR)

    print("\n" + "="*60)
    print("  Training Complete!")
    print("="*60)
    print("\nYou can now run the application with: python run.py")


if __name__ == '__main__':
    main()
