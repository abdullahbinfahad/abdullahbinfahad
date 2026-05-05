from flask import Flask, render_template

app = Flask(__name__)

profile = {
    "name": "Abdullah Bin Fahad",
    "age": "19 (approx)",
    "dob": "14 August 2006",
    "gender": "Male",
    "religion": "Islam",
    "blood_group": "A+",
    "height": "166 cm",
    "weight": "57.1 kg",

    "education": {
        "university": "Nanjing Tech University",
        "major": "Automation",
        "scholarship": "20,000 RMB",
        "hsc": "GPA 4.58",
        "ssc": "GPA 5.00"
    },

    "skills": [
        "Python", "HTML", "Marketing Strategy",
        "Research & Analysis", "Public Speaking",
        "Creative Writing", "Video Editing"
    ],

    "personality": [
        "Introverted", "Overthinker",
        "Ambitious", "Philosophical",
        "Emotionally intense"
    ],

    "goals": [
        "Become Billionaire",
        "Master Chinese (HSK 1–4)",
        "Build Smart Calculator",
        "Develop AI-based systems"
    ]
}

@app.route("/")
def home():
    return render_template("index.html", profile=profile)

if __name__ == "__main__":
    app.run(debug=True)

