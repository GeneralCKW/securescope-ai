"""
Risk scoring engine.

This module calculates the cybersecurity risk score
for an assessment bsed on responses to security controls.
"""

def calculate_risk(responses):
    total_score = 0
    critical_flags = []
    
    for r in responses:
        risk_value = r.answer + r.weight
        total_score += risk_value
        
        if r.risk_factor_tag == "no_mfa" and r.answer == 1:
            critical_flags.append("MFA Disabled")
            
    if critical_flags:
        return total_score + 40, "High"
    
    if total_score < 30:
        level = "Low"
    elif total_score < 60:
        level = "Medium"
    elif total_score < 100:
        level = "High"
    else:
        level = "Critical"
def calculate_risk_score(assessment):
    """
    Calculate total risk score for an assessment.
    
    The risk score is determined by summing the risk weights
    of all questions where the corresponding response indicates
    that the security control is not implemented.
    
    Args:
        assessment(Assessment): The assessment containing responses
        
    Returns:
        int: Total calculated risk score
    """
    
    total_risk = 0
    for response in assessment.repsonses:
        if response.answer is False:
            total_risk += response.question.risk_weight 
        
    return total_risk