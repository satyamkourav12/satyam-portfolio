# app.py

from flask import Flask, render_template, request, redirect, url_for, flash
from data import PROFILE, SKILLS, PROJECTS, CERTIFICATES, INITIATIVE

app = Flask(__name__)
app.secret_key = "satyam-kaurav-aiml-portfolio-key"

@app.route("/", methods=["GET"])
def home():
    return render_template(
        "index.html",
        profile=PROFILE,
        skills=SKILLS,
        projects=PROJECTS,
        certificates=CERTIFICATES,
        initiative=INITIATIVE,
    )

@app.route("/contact", methods=["POST"])
def contact():
    name = request.form.get("name", "").strip()
    email = request.form.get("email", "").strip()
    message = request.form.get("message", "").strip()

    if not name or not email or not message:
        flash("Please complete all fields before submitting.", "error")
        return redirect(url_for("home") + "#contact")

    # In production, write this to SQLite or a CSV
    print(f"Portfolio Inbound -> Name: {name} | Email: {email} | Msg: {message}")

    flash("Thank you! Your message was received successfully.", "success")
    return redirect(url_for("home") + "#contact")

if __name__ == "__main__":
    app.run(debug=True, port=5000)