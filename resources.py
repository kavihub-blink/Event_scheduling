from flask import Blueprint, request
from database import get_db

resources_bp = Blueprint("resources", __name__)

@resources_bp.route("/allocate", methods=["POST"])
def allocate():
    data = request.json
    db = get_db()

    db.execute("""
        INSERT INTO allocations(event_id,resource_id,qty)
        VALUES(?,?,?)
    """, (data["event_id"], data["resource_id"], data["qty"]))

    db.execute("""
        UPDATE resources SET available_qty = available_qty - ?
        WHERE resource_id = ?
    """, (data["qty"], data["resource_id"]))

    db.commit()
    return {"status": "allocated"}
