"""Module for bodyweight calculations and advice."""

def compute_bmi(weight, height):
    """Calculate BMI."""
    return weight / (height ** 2)

def healthy_weight_range(height):
    """Return the healthy weight range for a given height."""
    min_w = 18.5 * height ** 2
    max_w = 24.9 * height ** 2
    return min_w, max_w

def weight_status(weight, min_w, max_w):
    """Determine if weight is below, within, or above healthy range."""
    if weight < min_w:
        return "Below healthy range ⚠️"
    elif weight > max_w:
        return "Above healthy range ⚠️"
    else:
        return "Within healthy range ✅"

def compute_bmr(weight, height_cm, age, gender, pregnancy="No"):
    """Calculate BMR with optional pregnancy adjustment."""
    if gender == "Male":
        bmr = 10 * weight + 6.25 * height_cm - 5 * age + 5
    else:
        bmr = 10 * weight + 6.25 * height_cm - 5 * age - 161
        if pregnancy == "Yes":
            bmr += 300
    return bmr

def compute_tdee(bmr, activity_level):
    """Calculate TDEE based on activity level."""
    activity_factors = {"Low": 1.2, "Moderate": 1.375, "High": 1.55, "Extreme": 1.725}
    return bmr * activity_factors.get(activity_level, 1.2)

def weight_tips(current_weight, desired_weight, tdee):
    """Generate simple advice to reach the desired weight."""
    if desired_weight > current_weight:
        return f"To gain weight: ~{int(tdee + 500)} kcal/day, focus on strength training & protein-rich diet."
    elif desired_weight < current_weight:
        return f"To lose weight: ~{int(tdee - 500)} kcal/day, focus on cardio & balanced diet."
    else:
        return "Maintain your weight by keeping calories around your TDEE."

def estimate_progress_graph(current_weight, desired_weight, days=90):
    """Return X and Y values for a simple linear weight graph."""
    return [0, days], [current_weight, desired_weight]

def evaluate_weight(height, current_weight, desired_weight, age, gender, activity_level, pregnancy="No"):
    """Main function returning all outputs as a dictionary."""
    height_cm = height * 100
    current_bmi = compute_bmi(current_weight, height)
    desired_bmi = compute_bmi(desired_weight, height)
    min_w, max_w = healthy_weight_range(height)

    return {
        "current_bmi": current_bmi,
        "desired_bmi": desired_bmi,
        "current_status": weight_status(current_weight, min_w, max_w),
        "desired_status": weight_status(desired_weight, min_w, max_w),
        "healthy_range": (min_w, max_w),
        "bmr": compute_bmr(current_weight, height_cm, age, gender, pregnancy),
        "tdee": compute_tdee(compute_bmr(current_weight, height_cm, age, gender, pregnancy), activity_level),
        "tips": weight_tips(current_weight, desired_weight, compute_tdee(compute_bmr(current_weight, height_cm, age, gender, pregnancy), activity_level)),
        "graph_data": estimate_progress_graph(current_weight, desired_weight)
    }
