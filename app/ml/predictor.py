import os
import numpy as np
import pandas as pd
import joblib
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from sklearn.preprocessing import LabelEncoder, StandardScaler
from xgboost import XGBRegressor


class CostDelayPredictor:
    """AI-powered predictor for construction cost and delays"""

    # Feature columns used for prediction
    CATEGORICAL_FEATURES = ['project_type', 'location', 'material_quality',
                           'complexity_level', 'weather_risk_zone',
                           'soil_type', 'water_table_level', 'site_accessibility',
                           'foundation_type', 'finishing_level', 'site_topography']
    NUMERICAL_FEATURES = ['total_area_sqft', 'num_floors', 'num_workers',
                         'planned_duration_days', 'contractor_experience_years',
                         'distance_from_city_km', 'floor_height_ft',
                         'num_bathrooms', 'electrical_load_kw']
    BOOLEAN_FEATURES = ['has_basement']

    def __init__(self, model_dir='trained_models'):
        self.model_dir = model_dir
        self.cost_model = None
        self.delay_model = None
        self.delay_prob_model = None
        self.encoders = {}
        self.scaler = None
        self.is_loaded = False

        # Try to load existing models
        self._load_models()

    def _load_models(self):
        """Load pre-trained models if they exist"""
        cost_path = os.path.join(self.model_dir, 'cost_model.joblib')
        delay_path = os.path.join(self.model_dir, 'delay_model.joblib')
        delay_prob_path = os.path.join(self.model_dir, 'delay_prob_model.joblib')
        encoders_path = os.path.join(self.model_dir, 'encoders.joblib')
        scaler_path = os.path.join(self.model_dir, 'scaler.joblib')

        if all(os.path.exists(p) for p in [cost_path, delay_path, encoders_path, scaler_path]):
            self.cost_model = joblib.load(cost_path)
            self.delay_model = joblib.load(delay_path)
            self.encoders = joblib.load(encoders_path)
            self.scaler = joblib.load(scaler_path)
            if os.path.exists(delay_prob_path):
                self.delay_prob_model = joblib.load(delay_prob_path)
            self.is_loaded = True
            print("Models loaded successfully!")
        else:
            print("No pre-trained models found. Please train the models first.")

    def _preprocess_features(self, data: dict) -> np.ndarray:
        """Convert input data to feature array for prediction"""
        features = []

        # Process numerical features
        for feat in self.NUMERICAL_FEATURES:
            features.append(float(data.get(feat, 0)))

        # Process boolean features
        for feat in self.BOOLEAN_FEATURES:
            features.append(1 if data.get(feat, False) else 0)

        # Process categorical features
        for feat in self.CATEGORICAL_FEATURES:
            value = data.get(feat, 'unknown')
            if feat in self.encoders:
                try:
                    encoded = self.encoders[feat].transform([value])[0]
                except ValueError:
                    # Handle unseen categories
                    encoded = 0
                features.append(encoded)
            else:
                features.append(0)

        features = np.array(features).reshape(1, -1)

        # Scale features
        if self.scaler:
            features = self.scaler.transform(features)

        return features

    def predict(self, project_data: dict) -> dict:
        """
        Make predictions for a construction project.

        Args:
            project_data: Dictionary containing project parameters

        Returns:
            Dictionary with predictions and risk analysis
        """
        if not self.is_loaded:
            # Use rule-based estimation if no model is trained
            return self._rule_based_prediction(project_data)

        features = self._preprocess_features(project_data)

        # Get predictions
        predicted_cost = float(self.cost_model.predict(features)[0])
        predicted_delay = float(self.delay_model.predict(features)[0])

        # Calculate delay probability
        if self.delay_prob_model:
            delay_probability = float(self.delay_prob_model.predict_proba(features)[0][1])
        else:
            delay_probability = min(1.0, max(0.0, predicted_delay / project_data.get('planned_duration_days', 100)))

        # Calculate confidence intervals (using ensemble variance if available)
        cost_std = predicted_cost * 0.15  # 15% standard deviation estimate
        delay_std = max(5, predicted_delay * 0.2)  # 20% standard deviation estimate

        # Calculate risk score (0-100)
        risk_score = self._calculate_risk_score(
            project_data, predicted_cost, predicted_delay, delay_probability
        )

        # Identify risk factors
        risk_factors = self._identify_risk_factors(project_data)

        return {
            'predicted_cost': round(predicted_cost, 2),
            'predicted_delay_days': round(max(0, predicted_delay), 1),
            'delay_probability': round(delay_probability, 3),
            'risk_score': round(risk_score, 1),
            'cost_lower_bound': round(predicted_cost - 1.96 * cost_std, 2),
            'cost_upper_bound': round(predicted_cost + 1.96 * cost_std, 2),
            'delay_lower_bound': round(max(0, predicted_delay - 1.96 * delay_std), 1),
            'delay_upper_bound': round(predicted_delay + 1.96 * delay_std, 1),
            'risk_factors': risk_factors,
            'recommendations': self._generate_recommendations(risk_factors, project_data)
        }

    def _rule_based_prediction(self, data: dict) -> dict:
        """Fallback rule-based prediction when no ML model is available"""
        # Base cost per sqft by project type (in Indian Rupees)
        base_costs = {
            'residential': 1800,      # ₹1,800 per sqft
            'commercial': 2500,       # ₹2,500 per sqft
            'industrial': 2200,       # ₹2,200 per sqft
            'infrastructure': 3000    # ₹3,000 per sqft
        }

        # Material quality multipliers
        material_multipliers = {
            'economy': 0.8,
            'standard': 1.0,
            'premium': 1.4
        }

        # Complexity multipliers
        complexity_multipliers = {
            'low': 0.9,
            'medium': 1.0,
            'high': 1.3
        }

        project_type = data.get('project_type', 'commercial')
        total_area = data.get('total_area_sqft', 10000)
        num_floors = data.get('num_floors', 1)
        material_quality = data.get('material_quality', 'standard')
        complexity = data.get('complexity_level', 'medium')
        has_basement = data.get('has_basement', False)
        weather_risk = data.get('weather_risk_zone', 'moderate')
        planned_duration = data.get('planned_duration_days', 180)
        num_workers = data.get('num_workers', 20)
        experience = data.get('contractor_experience_years', 5)
        soil_type = data.get('soil_type', 'normal')
        water_table = data.get('water_table_level', 'deep')
        distance_km = data.get('distance_from_city_km', 5)
        road_access = data.get('site_accessibility', 'easy')
        floor_height = data.get('floor_height_ft', 10)
        foundation_type = data.get('foundation_type', 'isolated')
        num_bathrooms = data.get('num_bathrooms', 2)
        electrical_load = data.get('electrical_load_kw', 10)
        finishing_level = data.get('finishing_level', 'standard')
        topography = data.get('site_topography', 'flat')

        # Calculate base cost
        base_cost_sqft = base_costs.get(project_type, 175)
        base_cost = total_area * base_cost_sqft

        # Apply multipliers
        base_cost *= material_multipliers.get(material_quality, 1.0)
        base_cost *= complexity_multipliers.get(complexity, 1.0)
        base_cost *= (1 + (num_floors - 1) * 0.1)  # 10% increase per additional floor

        if has_basement:
            base_cost *= 1.15  # 15% increase for basement

        # Soil type impact on excavation cost
        soil_multipliers = {'normal': 1.0, 'rocky': 1.25, 'sandy': 1.05, 'clay': 1.10, 'marshy': 1.30}
        base_cost *= soil_multipliers.get(soil_type, 1.0)

        # Water table impact (dewatering costs)
        water_multipliers = {'deep': 1.0, 'moderate': 1.05, 'shallow': 1.12, 'high': 1.20}
        base_cost *= water_multipliers.get(water_table, 1.0)

        # Distance from city (transport costs)
        if distance_km > 50:
            base_cost *= 1.15
        elif distance_km > 20:
            base_cost *= 1.08
        elif distance_km > 10:
            base_cost *= 1.04

        # Road access impact
        access_multipliers = {'easy': 1.0, 'moderate': 1.05, 'difficult': 1.15, 'remote': 1.25}
        base_cost *= access_multipliers.get(road_access, 1.0)

        # Floor height impact (scaffolding costs)
        if floor_height > 14:
            base_cost *= 1.12
        elif floor_height > 12:
            base_cost *= 1.06

        # Foundation type impact
        foundation_multipliers = {'isolated': 1.0, 'strip': 1.08, 'raft': 1.18, 'pile': 1.40}
        base_cost *= foundation_multipliers.get(foundation_type, 1.0)

        # Bathroom cost (plumbing fixtures)
        base_cost += num_bathrooms * 75000  # ~Rs.75K per bathroom

        # Electrical load impact
        if electrical_load > 100:
            base_cost += electrical_load * 800
        elif electrical_load > 50:
            base_cost += electrical_load * 500
        else:
            base_cost += electrical_load * 300

        # Finishing level impact
        finishing_multipliers = {'basic': 0.85, 'standard': 1.0, 'premium': 1.35, 'luxury': 1.80}
        base_cost *= finishing_multipliers.get(finishing_level, 1.0)

        # Topography impact
        topo_multipliers = {'flat': 1.0, 'gentle_slope': 1.08, 'steep_slope': 1.20, 'hilly': 1.30}
        base_cost *= topo_multipliers.get(topography, 1.0)

        # Calculate delay prediction
        base_delay = 0
        delay_probability = 0.3  # Base 30% chance of delay

        # Weather risk impact
        weather_delays = {'low': 0, 'moderate': 5, 'high': 15}
        base_delay += weather_delays.get(weather_risk, 5)

        # Complexity impact
        complexity_delays = {'low': 0, 'medium': 5, 'high': 15}
        base_delay += complexity_delays.get(complexity, 5)

        # Experience impact
        if experience < 3:
            base_delay += 10
            delay_probability += 0.15
        elif experience > 10:
            base_delay -= 5
            delay_probability -= 0.1

        # Worker efficiency
        optimal_workers = total_area / 500  # Rule of thumb
        if num_workers < optimal_workers * 0.7:
            base_delay += 10
            delay_probability += 0.1

        # Soil and topography delays
        if soil_type in ('rocky', 'marshy'):
            base_delay += 8
            delay_probability += 0.08
        if topography in ('steep_slope', 'hilly'):
            base_delay += 10
            delay_probability += 0.10
        if water_table in ('shallow', 'high'):
            base_delay += 5
            delay_probability += 0.05
        if road_access in ('difficult', 'remote'):
            base_delay += 7
            delay_probability += 0.07
        if foundation_type == 'pile':
            base_delay += 12
            delay_probability += 0.08

        delay_probability = min(0.95, max(0.05, delay_probability))

        # Calculate risk score
        risk_score = self._calculate_risk_score(
            data, base_cost, base_delay, delay_probability
        )

        risk_factors = self._identify_risk_factors(data)

        return {
            'predicted_cost': round(base_cost, 2),
            'predicted_delay_days': round(max(0, base_delay), 1),
            'delay_probability': round(delay_probability, 3),
            'risk_score': round(risk_score, 1),
            'cost_lower_bound': round(base_cost * 0.85, 2),
            'cost_upper_bound': round(base_cost * 1.25, 2),
            'delay_lower_bound': round(max(0, base_delay - 10), 1),
            'delay_upper_bound': round(base_delay + 20, 1),
            'risk_factors': risk_factors,
            'recommendations': self._generate_recommendations(risk_factors, data),
            'note': 'Using rule-based estimation. Train ML models for better accuracy.'
        }

    def _calculate_risk_score(self, data: dict, cost: float, delay: float,
                             delay_prob: float) -> float:
        """Calculate overall risk score (0-100)"""
        score = 0

        # Delay probability contributes 40%
        score += delay_prob * 40

        # Project complexity contributes 20%
        complexity_scores = {'low': 5, 'medium': 10, 'high': 20}
        score += complexity_scores.get(data.get('complexity_level', 'medium'), 10)

        # Weather risk contributes 15%
        weather_scores = {'low': 3, 'moderate': 8, 'high': 15}
        score += weather_scores.get(data.get('weather_risk_zone', 'moderate'), 8)

        # Experience factor contributes 15%
        experience = data.get('contractor_experience_years', 5)
        if experience < 3:
            score += 15
        elif experience < 5:
            score += 10
        elif experience < 10:
            score += 5
        else:
            score += 2

        # Size and duration factor contributes 10%
        area = data.get('total_area_sqft', 10000)
        if area > 50000:
            score += 10
        elif area > 20000:
            score += 5
        else:
            score += 2

        return min(100, score)

    def _identify_risk_factors(self, data: dict) -> list:
        """Identify key risk factors for the project"""
        risks = []

        # Check weather risk
        if data.get('weather_risk_zone') == 'high':
            risks.append({
                'factor': 'High Weather Risk Zone',
                'severity': 'high',
                'impact': 'Potential for significant weather-related delays'
            })

        # Check complexity
        if data.get('complexity_level') == 'high':
            risks.append({
                'factor': 'High Project Complexity',
                'severity': 'high',
                'impact': 'Increased likelihood of technical challenges and delays'
            })

        # Check experience
        experience = data.get('contractor_experience_years', 5)
        if experience < 3:
            risks.append({
                'factor': 'Limited Contractor Experience',
                'severity': 'medium',
                'impact': 'Less experienced contractors may face unforeseen challenges'
            })

        # Check worker allocation
        area = data.get('total_area_sqft', 10000)
        workers = data.get('num_workers', 20)
        optimal_workers = area / 500
        if workers < optimal_workers * 0.7:
            risks.append({
                'factor': 'Understaffed Project',
                'severity': 'medium',
                'impact': 'May lead to delays due to insufficient workforce'
            })
        elif workers > optimal_workers * 1.5:
            risks.append({
                'factor': 'Potential Overstaffing',
                'severity': 'low',
                'impact': 'May lead to coordination challenges and increased costs'
            })

        # Check duration vs size
        duration = data.get('planned_duration_days', 180)
        expected_duration = (area / 1000) * 10 + (data.get('num_floors', 1) * 15)
        if duration < expected_duration * 0.7:
            risks.append({
                'factor': 'Aggressive Timeline',
                'severity': 'high',
                'impact': 'Timeline may be too aggressive for project scope'
            })

        # Premium materials
        if data.get('material_quality') == 'premium':
            risks.append({
                'factor': 'Premium Materials',
                'severity': 'low',
                'impact': 'Higher costs but better quality and longevity'
            })

        # Basement construction
        if data.get('has_basement'):
            risks.append({
                'factor': 'Basement Construction',
                'severity': 'medium',
                'impact': 'Additional excavation and foundation work required'
            })

        return risks

    def _generate_recommendations(self, risk_factors: list, data: dict) -> list:
        """Generate recommendations based on risk factors"""
        recommendations = []

        for risk in risk_factors:
            factor = risk['factor']

            if 'Weather' in factor:
                recommendations.append(
                    'Consider seasonal planning and weather contingency buffers'
                )
            elif 'Complexity' in factor:
                recommendations.append(
                    'Engage specialized consultants for complex technical aspects'
                )
            elif 'Experience' in factor:
                recommendations.append(
                    'Consider partnering with experienced contractors or adding senior oversight'
                )
            elif 'Understaffed' in factor:
                recommendations.append(
                    'Consider increasing workforce to meet project demands'
                )
            elif 'Overstaffing' in factor:
                recommendations.append(
                    'Review workforce allocation to optimize efficiency'
                )
            elif 'Aggressive' in factor:
                recommendations.append(
                    'Re-evaluate timeline or increase resources to meet schedule'
                )
            elif 'Basement' in factor:
                recommendations.append(
                    'Conduct thorough soil analysis before excavation begins'
                )

        # Add general recommendations
        if not recommendations:
            recommendations.append('Project parameters look reasonable. Monitor progress regularly.')

        return list(set(recommendations))  # Remove duplicates

    def train(self, training_data: pd.DataFrame):
        """
        Train the prediction models on historical data.

        Args:
            training_data: DataFrame with historical project data including actual costs and delays
        """
        print("Preparing training data...")

        # Initialize encoders
        for feat in self.CATEGORICAL_FEATURES:
            self.encoders[feat] = LabelEncoder()
            training_data[f'{feat}_encoded'] = self.encoders[feat].fit_transform(
                training_data[feat].fillna('unknown')
            )

        # Prepare feature matrix
        feature_cols = (
            self.NUMERICAL_FEATURES +
            self.BOOLEAN_FEATURES +
            [f'{feat}_encoded' for feat in self.CATEGORICAL_FEATURES]
        )

        X = training_data[feature_cols].values
        y_cost = training_data['actual_cost'].values
        y_delay = (training_data['actual_duration_days'] - training_data['planned_duration_days']).values

        # Initialize and fit scaler
        self.scaler = StandardScaler()
        X_scaled = self.scaler.fit_transform(X)

        # Train cost prediction model
        print("Training cost prediction model...")
        self.cost_model = XGBRegressor(
            n_estimators=100,
            max_depth=6,
            learning_rate=0.1,
            random_state=42
        )
        self.cost_model.fit(X_scaled, y_cost)

        # Train delay prediction model
        print("Training delay prediction model...")
        self.delay_model = GradientBoostingRegressor(
            n_estimators=100,
            max_depth=5,
            learning_rate=0.1,
            random_state=42
        )
        self.delay_model.fit(X_scaled, y_delay)

        # Train delay probability model (classification)
        from sklearn.ensemble import RandomForestClassifier
        y_delay_binary = (y_delay > 0).astype(int)
        self.delay_prob_model = RandomForestClassifier(
            n_estimators=100,
            max_depth=6,
            random_state=42
        )
        self.delay_prob_model.fit(X_scaled, y_delay_binary)

        # Save models
        self._save_models()
        self.is_loaded = True
        print("Training complete! Models saved.")

    def _save_models(self):
        """Save trained models to disk"""
        os.makedirs(self.model_dir, exist_ok=True)

        joblib.dump(self.cost_model, os.path.join(self.model_dir, 'cost_model.joblib'))
        joblib.dump(self.delay_model, os.path.join(self.model_dir, 'delay_model.joblib'))
        joblib.dump(self.delay_prob_model, os.path.join(self.model_dir, 'delay_prob_model.joblib'))
        joblib.dump(self.encoders, os.path.join(self.model_dir, 'encoders.joblib'))
        joblib.dump(self.scaler, os.path.join(self.model_dir, 'scaler.joblib'))
