def simulate_attack(responses):
    triggered_paths = []
    
    if responses["no_mfa"] and responses["weak_password_policy"]:
        triggered_paths.append({
            "entry_point": "Credential Stuffing",
            "lateral_+movement": True,
            "impact": "PHI Database Access",
            "estimated_costs": 275000
        })
        
    return triggered_paths