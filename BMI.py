def bmi_estimator(weight_kg, height_cm):
    if height_cm <=0 or weight_kg <=0:
        return {"error": "Height and weight must be positive values."}
    
    height_m = height_cm / 100
    bmi = weight_kg / (height_m ** 2)
    bmi = round(bmi, 2)

    if bmi < 18.5:
        category = "Underweight"
    elif 18.5 <= bmi < 24.9:
        category = "Normal weight"
    elif 25 <= bmi < 29.9:
        category = "Overweight"
    else:
        category = "Obesity"

    return {"bmi": bmi, "category": category}