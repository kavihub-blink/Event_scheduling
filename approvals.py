from flask import Blueprint, request
from database import get_db

approvals_bp = Blueprint("approvals", __name__)

@approvals_bp.route("/approve", methods=["POST"])
def approve():
    data = request.json
    db = get_db()

    if data["action"] == "approve":
        db.execute("UPDATE events SET status=? WHERE event_id=?",
                   (data["next_status"], data["event_id"]))
    else:
        db.execute("UPDATE events SET status='REJECTED' WHERE event_id=?",
                   (data["event_id"],))

    db.commit()
    return {"status": "updated"}
