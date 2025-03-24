

# 🌟 Digital Twin for a Personal Life Simulator

## 📖 Overview
The **Digital Twin for a Personal Life Simulator** provides personalized insights and actionable recommendations for users based on various personal data points. By simulating financial growth, career progress, health status, and lifestyle choices, this tool offers users a **digital twin** of their future life trajectory and helps them make informed decisions. The simulator incorporates machine learning models and gamification to empower users in achieving their career, financial, and health goals.

---

## 🛠️ Features

- **Personalized Career and Financial Insights**: Get customized recommendations for career growth and financial planning.
- **Health and Lifestyle Suggestions**: Receive health and wellness advice based on your personal status.
- **Financial Growth Prediction**: Predict your financial growth based on current salary, savings, risk tolerance, and health.
- **Gamification**: Earn points based on your financial habits and health actions.
- **Visualization**: Track your projected growth through a visual chart.
- **User-friendly Input**: Easy-to-use inputs for age, salary, health, risk tolerance, and more.

---

## 🚀 Installation & Setup

### 1️⃣ Install Dependencies
Ensure you have Python installed and install the required libraries:

```bash
pip install numpy pandas matplotlib scikit-learn
```

### 2️⃣ Run the Program
Once dependencies are installed, you can run the program by executing the script:

```bash
python personal_life_simulator.py
```

---

## 👨‍💻 How It Works

### 1. User Input Fields

The program collects data from the user, including:

- **Age** (18-65)
- **Current Salary**
- **Savings Rate** (as a decimal, e.g., 0.2 for 20%)
- **Health Status** (1 = Good, 2 = Average, 3 = Poor)
- **Risk Tolerance** (1 = Low, 2 = Medium, 3 = High)
- **Weekly Exercise Hours**
- **Diet Quality** (1 = Poor, 2 = Average, 3 = Excellent)

### 2. Predictive Model for Financial and Career Growth
The program uses a **Random Forest** machine learning model to predict the user's financial growth in the next 5 years based on their current salary, savings rate, health, and risk tolerance.

### 3. Personalized Recommendations
The program generates **personalized recommendations** based on the user's inputs in the following areas:
- **Career Growth**: Tailored advice based on the user's age and career stage.
- **Health & Wellness**: Suggestions to improve mental and physical well-being.
- **Financial Planning**: Advice on savings and investment strategies based on risk tolerance.

### 4. Gamification & Rewards
The program includes a gamification feature that rewards users with points based on their actions and behaviors:
- Users can earn points for maintaining a higher savings rate and being risk-tolerant.

### 5. Data Visualization
The program generates a graph that shows the **projected financial growth** over the next 5 years, based on the predicted growth model.

---

## 📈 Example Output

Upon running the program, the user will be asked to enter their data, and the program will provide recommendations like:

```
Enter your age (18-65): 44
Enter your current salary: 500000
Enter your savings rate (as a decimal, e.g., 0.2 for 20%): 0.5
Enter your health status (1=Good, 2=Average, 3=Poor): 1
Enter your risk tolerance (1=Low, 2=Medium, 3=High): 1
Enter average weekly exercise hours: 9
Rate your diet quality (1=Poor, 2=Average, 3=Excellent): 3

Personalized Recommendations:
- Explore opportunities for leadership roles and salary increases.
- Maintain a balanced diet and regular exercise.
- Keep up the good work with your savings!
- Consider safer investments such as bonds or index funds.

Predicted Financial Growth (5 years): $131600.00
```

---

## ⚙️ License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
```

