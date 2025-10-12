#backend for calorie estimation
def calorie_estimator(weight_kg, height_cm, age, gender):
    if height_cm <= 0 or weight_kg <= 0 or age <= 0:
        return {"error": "Height, weight and age must be positive values..."}
    if gender.lower() == "male":
        bmr = 10 * weight_kg + 6.25 * height_cm - 5 * age + 5
    elif gender.lower() == "female":
        bmr = 10 * weight_kg + 6.25 * height_cm - 5 * age - 161
    
    bmr = round(bmr, 2)
    return {"bmr": bmr}
