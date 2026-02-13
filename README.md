**AI-Based Institutional Event Resource Management System
Smart, Conflict-Free Event Planning with AI & Real-Time Resource Optimization**

**📌 Project Overview**
Large institutions conduct multiple events in parallel, sharing limited resources such as venues, equipment, food, IT services, and volunteers. Manual planning often leads to conflicts, overbooking, and inefficiency.
This project presents an AI-driven Event Resource Management System that ensures:
Conflict-free venue and resource allocation
Multi-level approval workflows
Real-time availability updates
Explainable AI-based decisions
Secure role-based access

**🚀 Key Features**
🔐 Role-Based Access Control
1.Event Coordinator
2.Head of Department (HOD)
3.Dean
4.Institutional Head
5.Admin / ITC Team
Each role sees only authorized data.

**🧠 AI-Driven Resource Allocation**
Smart venue selection
Capacity validation
Conflict detection
Resource demand prediction
Minimal disruption reallocation
Explainable rejection reasons

🔄** Dynamic Approval Workflow**
Event Coordinator → HOD → Dean → Institutional Head
Rejections include reasons

Modified requests re-enter workflow

No partial resource locking

📊 Real-Time Dashboards
Venue occupancy state

Resource availability

Approval status

Running / completed events

🔓 Clean Event Closure
Explicit resource release

Occupancy update

Audit logging

Availability restoration

🏗 System Architecture
Web / Mobile Dashboard
        ↓
Backend API (Flask / FastAPI)
        ↓
AI Allocation Engine
        ↓
Database (SQLite / PostgreSQL)
🛠 Technology Stack
Backend
Python

Flask / FastAPI

Database
SQLite (development)

PostgreSQL / MySQL (production)

AI / ML
Scikit-Learn

NumPy

Pandas

Frontend (Optional)
React / HTML-CSS

📂 Project Folder Structure
event-scheduling/
│
├── app.py                 # Main application
├── database.py            # Database connection
├── schema.sql             # Database schema
├── allocator.py           # AI allocation logic
├── auth.py                # Authentication & roles
├── requirements.txt       # Dependencies
├── event.db               # SQLite database
└── README.md

⚙️ Installation & Setup
1️⃣ Clone the Project
git clone <project-url>
cd event-scheduling
2️⃣ Create Virtual Environment (Recommended)
python -m venv venv
venv\Scripts\activate   # Windows
3️⃣ Install Dependencies
pip install -r requirements.txt
4️⃣ Create Database
sqlite3 event.db
.read schema.sql
.quit
5️⃣ Run Application
python app.py
Open browser:

http://127.0.0.1:5000
🧪 Synthetic Data Generation
Real institutional data is often unavailable.
This project uses synthetic datasets generated using:
1.Faker
2.NumPy
3.Pandas

This approach is industry-standard for prototyping AI systems.

🤖 AI Components Explained
✔ Conflict Detection
Time overlap detection

Capacity validation

Resource availability check

✔ Smart Allocation
Chooses feasible venues

Prevents overbooking

Minimizes disruption

✔ Explainability
Provides reasons for rejection

Identifies conflicting events/resources

🧠 Use Cases
College fests

University conferences

Workshops & seminars

Institutional scheduling systems

Hackathon event planning

🔒 Security & Reliability
Role-based visibility

No approval bypassing

No over-allocation

Transaction-safe resource updates

Real-time consistency

🏆 Competition / Evaluation Highlights
✔ AI-based decision engine
✔ Real-time resource tracking
✔ Multi-level approval logic
✔ Explainable outputs
✔ Scalable system design

📈 Future Enhancements
1.Mobile app (Flutter)

2.WebSockets for live updates

3.Cloud deployment

4.Reinforcement learning for scheduling

5.Notification system

6.Analytics dashboard

