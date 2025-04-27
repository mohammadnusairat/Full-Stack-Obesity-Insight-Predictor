# Full-Stack Obesity Insight Predictor

## Project Structure
- `/frontend` — React + Vite TypeScript frontend
- `/backend` — Flask API backend with machine learning model

## How to Run
### Backend

### Developer Notes:
1. Turn it into a Web App (Full-stack / Cloud)
Instead of just a local ML notebook, make a small web app where users input their lifestyle details and get a real-time obesity risk prediction!

Frontend: React.js

Simple form: age, gender, physical activity, food habits, etc.

POSTs user inputs to backend.

Display prediction result dynamically (low/medium/high risk).

Backend: Flask or Node.js/Express

Serve a RESTful API endpoint (/predict) that takes in user input and returns obesity risk.

Deploy: Host backend on AWS EC2 or Render.

Dockerize the backend for easy deployment and scaling.

→ This immediately hits web development, full-stack, cloud, REST API, Docker, and AWS skills.

2. Add Authentication (Security skills)
Add JWT authentication so users can optionally create accounts and save their obesity risk history.

Users create an account (simple username/password).

After login, they can track their previous submissions.

JWT used to authorize API requests.

→ This demonstrates understanding of user security, authentication, JWT, session management.

3. Use a Database (Backend skills)
Store user predictions and information in MongoDB or PostgreSQL.

Schema could be simple:

text
Copy
Edit
Users: { id, username, hashed_password }
Predictions: { user_id, input_features, predicted_risk, timestamp }
Use MongoDB Atlas (cloud MongoDB) or AWS RDS (PostgreSQL) for hosting the database.

→ Shows off database design, SQL or NoSQL, cloud database hosting.

4. API Documentation (Professionalism)
Write Swagger/OpenAPI documentation for your Flask or Express API.

It shows a professional-level API design practice.

Easy for employers to see you know how to make and document APIs.

5. Testing and TDD (Agile best practices)
Implement:

Unit tests (Pytest if Flask, Jest if Node.js)

Integration tests (test full prediction flow)

Setup a basic CI/CD pipeline if you want (like GitHub Actions).

→ Even a few basic tests will demonstrate knowledge of TDD and Agile.

6. More Machine Learning Improvements (Optional)
Add a feature importance chart to the output, so users see why they got their risk score.

Explore using a lightweight TensorFlow or PyTorch model if you want deep learning flavor.

🚀 Obesity Risk Predictor Upgrade Plan
Week 1: Backend API + Docker
Goal: Turn your notebook into a real REST API.

 Refactor your ML model code into a Flask (or FastAPI) backend:

Endpoint: POST /predict that accepts JSON input (age, gender, etc.) and returns predicted obesity risk.

 Dockerize the Flask app (write a Dockerfile).

 Test locally with Postman or curl.

 Save the model (.pkl file) and load it dynamically inside the API.

⚡ Tip: Use sklearn's joblib or pickle to save/load models.

Week 2: Frontend + Local Full Stack Integration
Goal: Build a simple React.js frontend that interacts with your backend.

 Build a React.js form:

Inputs for user lifestyle info.

Button to submit the form to /predict.

Display the obesity risk prediction on the page.

 Make API calls to your Flask backend using Axios or Fetch.

 Implement basic form validation (ex: no negative ages).

 Polish simple UI/UX (TailwindCSS or basic CSS).

 Run frontend and backend together locally.

Week 3: Authentication + Database
Goal: Add user accounts + store predictions.

 Add JWT Authentication:

Register and login endpoints (/register, /login).

Protect /predict so only logged-in users can call it.

 Set up a MongoDB Atlas or PostgreSQL database:

Users table/collection (id, username, password_hash).

Predictions table/collection (user_id, features, prediction, timestamp).

 Update the backend to store each prediction in the database.

⚡ Tip: You can hash passwords using libraries like bcrypt!

Week 4: Cloud Deployment + Testing + Polish
Goal: Deploy and polish everything for your portfolio.

 Deploy your backend API on AWS EC2 (or Render/Vercel for quick start).

 Deploy your frontend React app (Netlify or Vercel).

 Connect frontend to the deployed backend (update API URLs).

 Write basic unit tests:

Backend: test model loading, test /predict API.

Frontend: form validation tests.

 Optional: Write Swagger/OpenAPI docs for your API.

 Final polish:

Mobile responsiveness (basic).

404 page or error message for invalid API calls.

Loading spinners when waiting for prediction.

Clean up repo: update README.md with deployment links and usage instructions.

📜 Final Result (Resume Version)
Once done, you can write on your resume something like:

Obesity Risk Predictor | Flask, React, MongoDB, AWS
Built a full-stack ML web app predicting obesity risk based on lifestyle/demographic factors. Developed a RESTful API in Flask, containerized with Docker, deployed to AWS. Designed a React frontend for user interaction, secured with JWT authentication, and persisted user predictions on MongoDB Atlas. Implemented unit tests, API documentation (Swagger), and CI/CD (GitHub Actions). Achieved 98% model accuracy using Ensemble ML methods.

🛠 Tech Stack Covered:
React (frontend)

Flask / Express (backend API)

MongoDB / PostgreSQL (database)

AWS EC2 (deployment)

Docker (containerization)

JWT Authentication (security)

Swagger / OpenAPI (API docs)

Pytest / Jest (testing)

GitHub Actions (optional CI/CD)