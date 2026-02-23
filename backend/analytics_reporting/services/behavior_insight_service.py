# Epic Title: Track and Analyze User Behavior

from sqlalchemy.orm import Session
from backend.database.config import get_db
from backend.analytics_reporting.models.user_behavior import UserBehavior

def generate_behavior_insights() -> dict:
    db: Session = next(get_db())
    behavior_data = db.query(UserBehavior).all()
    insights = analyze_behavior_data(behavior_data)
    return insights

def analyze_behavior_data(behavior_data: list) -> dict:
    behavior_patterns = {"common_actions": {}, "action_details": {}}
    for data in behavior_data:
        behavior_patterns["common_actions"][data.action] = behavior_patterns["common_actions"].get(data.action, 0) + 1
        if data.detail:
            behavior_patterns["action_details"][data.action] = behavior_patterns["action_details"].get(data.action, {})
            behavior_patterns["action_details"][data.action][data.detail] = behavior_patterns["action_details"][data.action].get(data.detail, 0) + 1
    return behavior_patterns