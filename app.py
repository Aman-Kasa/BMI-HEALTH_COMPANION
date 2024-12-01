from flask import Flask, request, render_template
from decouple import config
import http.client
import json

app = Flask(__name__)

# API Configuration
API_KEY = "5d4bf58fe9msh26860649e4a334ep179efbjsnfa5d03ded9aa"  # Your API key
API_HOST = "body-mass-index-bmi-calculator.p.rapidapi.com"  # API host

# Sample workout and meal plans data (mock data based on BMI category)
workout_plans = {
    "underweight": [
        "Strength training exercises",
        "Bodyweight exercises like squats, push-ups, lunges"
    ],
    "normal": [
        "Cardio workout: Running, swimming, cycling",
        "Strength training: Weight lifting, squats, push-ups"
    ],
    "overweight": [
        "Low-impact cardio exercises: Walking, swimming",
        "Strength training with moderate intensity"
    ]
}

meal_plans = {
    "underweight": [
        "High-calorie foods: Avocados, nuts, protein-rich meals",
        "5-6 smaller meals throughout the day"
    ],
    "normal": [
        "Balanced diet with lean proteins, vegetables, and healthy fats",
        "Eat 3 main meals and 2 snacks daily"
    ],
    "overweight": [
        "Low-calorie foods: Vegetables, lean proteins",
        "Cut down on processed carbs, sugar, and unhealthy fats"
    ]
}

health_tips = {
    "underweight": [
        "Focus on nutrient-dense foods",
        "Incorporate healthy fats in your meals"
    ],
    "normal": [
        "Stay hydrated",
        "Maintain regular exercise routines"
    ],
    "overweight": [
        "Focus on portion control",
        "Include more fiber-rich foods"
    ]
}

# Function to call Health API using http.client
def get_health_data(weight, height):
    bmi = weight / (height / 100) ** 2  # Calculate BMI
    if bmi < 18.5:
        category = "underweight"
    elif 18.5 <= bmi <= 24.9:
        category = "normal"
    else:
        category = "overweight"

    return {
        "bmi": round(bmi, 1),
        "category": category,
        "workout": workout_plans.get(category, []),
        "meal": meal_plans.get(category, []),
        "tips": health_tips.get(category, [])
    }

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        try:
            weight = float(request.form["weight"])
            height = float(request.form["height"])
            health_data = get_health_data(weight, height)

            # Debug the data passed to the template
            print("Data Passed to Template:", health_data)

            if "error" in health_data:
                return render_template("index.html", error=health_data["error"])

            return render_template(
                "index.html",
                bmi=health_data.get("bmi", "N/A"),
                category=health_data.get("category", "N/A"),
                tips=health_data.get("tips", []),
                workout=health_data.get("workout", []),
                meal=health_data.get("meal", [])
            )
        except ValueError:
            return render_template("index.html", error="Invalid input. Please enter valid numbers.")
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True, port=5001)  # Run on port 5001


