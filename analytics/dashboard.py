from analytics.performance_analyzer import identify_low_performers
from analytics.dropout_predictor import predict_dropout_risk
from analytics.engagement_scorer import calculate_engagement_scores
from analytics.intervention_engine import generate_interventions
from analytics.anomaly_detector import detect_anomalies


def generate_dashboard():

    return {
        "low_performers": identify_low_performers(),
        "dropout_risks": predict_dropout_risk(),
        "engagement_scores": calculate_engagement_scores(),
        "interventions": generate_interventions(),
        "anomalies": detect_anomalies()
    }