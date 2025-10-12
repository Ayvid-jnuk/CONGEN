def hydration_estimator(weight_kg, age, gender, activity_level):
    if weight_kg <= 0 or age <= 0:
        return {"error": "Weight and age must be positive values."}
    
    if gender.lower() == "male":
        base_water_intake = 35 * weight_kg
    elif gender.lower() == "female":
        base_water_intake = 31 * weight_kg

    activity_levels = {
        "Low": 1.0,
        "Moderate (some physical activity)": 1.2,
        "High (intense physical activity)": 1.4
    }
    if activity_level not in activity_levels:
        return {"error": "Invalid activity level. Choose from Low, Moderate, High."}
    
    water_intake_ml = base_water_intake * activity_levels[activity_level]
    water_intake_liters = round(water_intake_ml / 1000, 2)

    return {"water_intake_liters": water_intake_liters}

    