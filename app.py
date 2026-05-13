from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

from flask_mail import Mail, Message
from dotenv import load_dotenv

from groq import Groq

import os

# ==========================================
# APP SETUP
# ==========================================

app = Flask(__name__)

load_dotenv()

# ==========================================
# GROQ AI CONFIGURATION
# ==========================================

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

# ==========================================
# DATABASE CONFIGURATION
# ==========================================

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///leads.db"

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# ==========================================
# MAIL CONFIGURATION
# ==========================================

app.config["MAIL_SERVER"] = "smtp.gmail.com"

app.config["MAIL_PORT"] = 587

app.config["MAIL_USE_TLS"] = True

app.config["MAIL_USERNAME"] = os.getenv("EMAIL_USER")

app.config["MAIL_PASSWORD"] = os.getenv("EMAIL_PASS")

# ==========================================
# INITIALIZE EXTENSIONS
# ==========================================

db = SQLAlchemy(app)

mail = Mail(app)

# ==========================================
# DATABASE MODEL
# ==========================================

class Lead(db.Model):

    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(100), nullable=False)

    email = db.Column(db.String(100), nullable=False)

    phone = db.Column(db.String(20), nullable=False)

    business = db.Column(db.String(100), nullable=False)

    message = db.Column(db.Text, nullable=False)

    status = db.Column(db.String(50), default="New")

# ==========================================
# HOME PAGE
# ==========================================

@app.route("/", methods=["GET", "POST"])
def home():

    if request.method == "POST":

        # ==========================================
        # GET FORM DATA
        # ==========================================

        name = request.form["name"]

        email = request.form["email"]

        phone = request.form["phone"]

        business = request.form["business"]

        message = request.form["message"]

        # ==========================================
        # CREATE LEAD OBJECT
        # ==========================================

        new_lead = Lead(
            name=name,
            email=email,
            phone=phone,
            business=business,
            message=message
        )

        # ==========================================
        # SAVE TO DATABASE
        # ==========================================

        db.session.add(new_lead)

        db.session.commit()

        print("Lead Saved Successfully!")

        # ==========================================
        # AI GENERATED EMAIL RESPONSE
        # ==========================================

        try:

            response = client.chat.completions.create(

                model="llama-3.1-8b-instant",

                messages=[

                    {
                        "role": "system",

                        "content": """
You are a professional business assistant for LeadFlow CRM.

Generate a professional and friendly customer reply email.

IMPORTANT:
- Do NOT use placeholders.
- Do NOT write things like [Your Name].
- Do NOT write [Company Name].
- End every email with:

Regards,
LeadFlow CRM Team
"""
                    },

                    {
                        "role": "user",

                        "content": f"""
Customer Name: {name}

Business Type: {business}

Customer Message:
{message}
"""
                    }

                ]

            )

            email_body = response.choices[0].message.content

            print("AI Email Generated Successfully!")

        except Exception as e:

            print("Groq AI Error:", e)

            # ==========================================
            # FALLBACK EMAIL
            # ==========================================

            email_body = f"""
Hello {name},

Thank you for contacting us regarding your {business} business.

We have successfully received your inquiry.

Our team will contact you shortly.

Regards,
LeadFlow CRM Team
"""

        # ==========================================
        # CREATE EMAIL MESSAGE
        # ==========================================

        msg = Message(

            subject="Thank You For Contacting Us",

            sender=os.getenv("EMAIL_USER"),

            recipients=[email]

        )

        msg.body = email_body

        # ==========================================
        # SEND EMAIL
        # ==========================================

        mail.send(msg)

        print("Email Sent Successfully!")

    return render_template("index.html")

# ==========================================
# DASHBOARD
# ==========================================

@app.route("/dashboard")
def dashboard():

    search = request.args.get("search")

    status = request.args.get("status")

    query = Lead.query

    # SEARCH FILTER

    if search:

        query = query.filter(
            Lead.name.contains(search)
        )

    # STATUS FILTER

    if status and status != "All":

        query = query.filter(
            Lead.status == status
        )

    leads = query.all()

    return render_template(
        "dashboard.html",
        leads=leads
    )

# ==========================================
# UPDATE STATUS
# ==========================================

@app.route("/update_status/<int:id>", methods=["POST"])
def update_status(id):

    lead = Lead.query.get(id)

    new_status = request.form["status"]

    lead.status = new_status

    db.session.commit()

    return redirect("/dashboard")

# ==========================================
# DELETE LEAD
# ==========================================

@app.route("/delete/<int:id>", methods=["POST"])
def delete_lead(id):

    lead = Lead.query.get(id)

    db.session.delete(lead)

    db.session.commit()

    return redirect("/dashboard")

# ==========================================
# RUN APPLICATION
# ==========================================

if __name__ == "__main__":

    with app.app_context():

        db.create_all()

    app.run(debug=True)