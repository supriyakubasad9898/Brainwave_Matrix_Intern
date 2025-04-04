from flask import Flask, request, jsonify, render_template
import re

app = Flask(__name__)

class PasswordStrengthChecker:
    def __init__(self):
        self.common_passwords = {
            "123456", "password", "123456789", "12345678", "12345", "1234567",
            "qwerty", "abc123", "football", "monkey", "letmein", "111111",
            "iloveyou", "admin", "welcome", "123123", "1234", "1q2w3e4r",
            "qwertyuiop", "password1", "123321", "passw0rd", "123", "qwerty123"
        }

    def check_length(self, password):
        return len(password) >= 8

    def check_complexity(self, password):
        has_upper = re.search(r'[A-Z]', password) is not None
        has_lower = re.search(r'[a-z]', password) is not None
        has_digit = re.search(r'\d', password) is not None
        has_special = re.search(r'[!@#$%^&*(),.?":{}|<>]', password) is not None
        return has_upper and has_lower and has_digit and has_special

    def check_uniqueness(self, password):
        return password not in self.common_passwords

    def assess_password_strength(self, password):
        score = 0
        feedback = []

        if self.check_length(password):
            score += 1
        else:
            feedback.append("Password should be at least 8 characters long.")

        if self.check_complexity(password):
            score += 1
        else:
            feedback.append("Password should include uppercase, lowercase, digits, and special characters.")

        if self.check_uniqueness(password):
            score += 1
        else:
            feedback.append("Password is too common. Choose a more unique password.")

        if score == 3:
            feedback.append("Password is strong!")
            if len(password) >= 12:
                feedback.append("Password is the strongest!")
        elif score == 2:
            feedback.append("Password is moderate. Consider improving it.")
        else:
            feedback.append("Password is weak. Choose a stronger password.")

        return {"feedback": feedback, "score": score}

checker = PasswordStrengthChecker()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/check-password', methods=['POST'])
def check_password():
    data = request.json
    password = data.get('password', '')
    result = checker.assess_password_strength(password)
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)