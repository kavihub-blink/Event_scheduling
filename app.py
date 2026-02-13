from flask import Flask,jsonify
from auth import auth_bp
from events import events_bp
from approvals import approvals_bp
from resources import resources_bp
from venues import venues_bp

app = Flask(__name__)
app.secret_key = "hackathon_secret"
@app.route("/")
def home():
    return "Event Resource Management System Running!"
if __name__ == "__main__":
    app.run(debug=True)
app.register_blueprint(auth_bp)
app.register_blueprint(events_bp)
app.register_blueprint(approvals_bp)
app.register_blueprint(resources_bp)
app.register_blueprint(venues_bp)


