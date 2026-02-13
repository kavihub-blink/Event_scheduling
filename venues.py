from flask import Blueprint, request
from database import get_db

venues_bp = Blueprint("venues", __name__)

@venues_bp.route("/book", methods=["POST"])
def book_venue():
    data = request.json
    db = get_db()

    db.execute("""
        INSERT INTO allocations(event_id,venue_id,time_slot)
        VALUES(?,?,?)
    """, (data["event_id"], data["venue_id"], data["time_slot"]))

    db.commit()
    return {"status": "venue booked"}
