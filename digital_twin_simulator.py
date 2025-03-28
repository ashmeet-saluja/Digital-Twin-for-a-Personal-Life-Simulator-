# -*- coding: utf-8 -*-
"""digital_twin_simulator.py

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/13JY54HnrCMT0EjcbjfdJOwm0eU6Z7Jq2
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
import random

# Step 1: Define User Input Fields
def get_user_input():
    while True:
        age = int(input("Enter your age (18-65): "))
        if 18 <= age <= 65:
            break
        print("Invalid age. Please enter a value between 18 and 65.")

    user_data = {
        "age": age,
        "current_salary": float(input("Enter your current salary: ")),
        "savings_rate": float(input("Enter your savings rate (as a decimal, e.g., 0.2 for 20%): ")),
        "health_status": int(input("Enter your health status (1=Good, 2=Average, 3=Poor): ")),
        "risk_tolerance": int(input("Enter your risk tolerance (1=Low, 2=Medium, 3=High): ")),
        "exercise_hours": int(input("Enter average weekly exercise hours: ")),
        "diet_quality": int(input("Rate your diet quality (1=Poor, 2=Average, 3=Excellent): "))
    }
    return user_data

# Step 2: Predictive Model for Financial and Career Growth (Refined)
def predict_growth(user_data):
    base_growth_rate = 0.03  # Base annual growth rate (3%)
    risk_multiplier = {1: 1.0, 2: 1.2, 3: 1.5}  # Higher risk tolerance = higher potential growth
    savings_multiplier = min(1 + user_data["savings_rate"], 2.0)  # Capped multiplier for savings
    health_bonus = {1: 1.05, 2: 1.02, 3: 0.98}  # Good health slightly boosts earnings
    experience_factor = 1 + (user_data["age"] / 100)  # More experience = slightly higher returns

    adjusted_growth_rate = (
        base_growth_rate * risk_multiplier[user_data["risk_tolerance"]] * savings_multiplier * health_bonus[user_data["health_status"]] * experience_factor
    )

    predicted_salary = user_data["current_salary"] * ((1 + adjusted_growth_rate) ** 5)  # 5-year growth
    return max(predicted_salary, user_data["current_salary"] * 1.05)  # Ensure at least 5% growth

# Step 3: Personalized Career, Health, and Financial Recommendations
def provide_recommendations(user_data, predicted_growth):
    print("\nPersonalized Recommendations:")

    # Career Recommendations
    if user_data["age"] < 30:
        print("- Focus on career growth, consider upskilling or learning new technologies.")
    elif user_data["age"] < 50:
        print("- Explore opportunities for leadership roles and salary increases.")
    else:
        print("- Consider retirement planning or semi-retirement options.")

    # Health Recommendations
    if user_data["health_status"] == 1:
        print("- Maintain a balanced diet and regular exercise.")
    elif user_data["health_status"] == 2:
        print("- Consider consulting a health professional for a wellness plan.")
    else:
        print("- Prioritize mental and physical health; consider therapy or medical checkups.")

    # Financial Recommendations
    if user_data["savings_rate"] < 0.2:
        print("- Increase your savings rate for long-term security.")
    else:
        print("- Keep up the good work with your savings!")

    # Investment Recommendations
    if user_data["risk_tolerance"] == 3:
        print("- Consider higher-risk, high-reward investments like stocks or crypto.")
    else:
        print("- Consider safer investments such as bonds or index funds.")

    # Health & Lifestyle Suggestions
    if user_data["exercise_hours"] < 3:
        print("- Increase your weekly exercise to improve health and energy levels.")
    if user_data["diet_quality"] == 1:
        print("- Improve your diet by including more balanced, nutritious meals.")

    # Financial Growth Prediction
    print(f"Predicted Financial Growth (5 years): ${predicted_growth:.2f}")

# Step 4: Data Visualization (Progress Tracking)
def plot_growth(user_data, predicted_growth):
    years = np.arange(1, 6)
    initial_salary = user_data["current_salary"]
    growth = [initial_salary * ((1 + (predicted_growth / initial_salary - 1) / 5) ** i) for i in years]

    plt.figure(figsize=(10, 6))
    plt.plot(years, growth, marker='o', linestyle='-', color='b', label="Projected Salary Growth")
    plt.title('Projected Financial Growth Over the Next 5 Years')
    plt.xlabel('Years')
    plt.ylabel('Salary ($)')
    plt.legend()
    plt.grid(True)
    plt.show()

# Step 5: Gamification - Points and Rewards
def gamify_user_experience(user_data):
    points = 0
    if user_data["savings_rate"] >= 0.2:
        points += 10
    if user_data["risk_tolerance"] == 3:
        points += 5
    if user_data["exercise_hours"] >= 5:
        points += 5
    if user_data["diet_quality"] == 3:
        points += 5
    return points

# Main Execution Flow
def main():
    # Get user input
    user_data = get_user_input()

    # Predict future financial growth
    predicted_growth = predict_growth(user_data)

    # Provide personalized recommendations
    provide_recommendations(user_data, predicted_growth)

    # Plot financial growth over the next 5 years
    plot_growth(user_data, predicted_growth)

    # Gamify the user's experience and show points
    points = gamify_user_experience(user_data)
    print(f"\nYou have earned {points} reward points!")

# Run the main function
if __name__ == "__main__":
    main()