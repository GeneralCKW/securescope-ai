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
        
    return total_score, level