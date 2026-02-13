from flask import Blueprint, request
from database import get_db

auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.json
    db = get_db()

    user = db.execute(
        "SELECT * FROM users WHERE name=? AND password=?",
        (data["name"], data["password"])
    ).fetchone()

    if user:
        return {
            "status": "success",
            "user_id": user["user_id"],
            "role": user["role"],
            "department": user["department"]
        }

    return {"status": "fail", "message": "Invalid login"}


@auth_bp.route("/test")
def test():
    return {"status": "auth working"}
