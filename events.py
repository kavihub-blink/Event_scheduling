from flask import Blueprint, request
from database import get_db

events_bp = Blueprint("events", __name__)

@events_bp.route("/create_event", methods=["POST"])
def create_event():
    data = request.json
    db = get_db()

    db.execute("""
        INSERT INTO events(title,date,time,duration,participants,status,created_by)
        VALUES(?,?,?,?,?,'PENDING',?)
    """, (data["title"], data["date"], data["time"],
          data["duration"], data["participants"], data["user_id"]))

    db.commit()
    return {"message": "Event Created"}
@events_bp.route("/test_event")
def test_event():
    return {"status":"events module working"}

