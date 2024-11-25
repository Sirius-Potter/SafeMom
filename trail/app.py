from flask import Flask, render_template, request, redirect, url_for, session
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Required for session management

# Route for index page (home page)
@app.route('/')
def index():
    return render_template('index.html')

# Route for information page
@app.route('/information')
def information():
    return render_template('information.html')

# Route for prediction form page
@app.route('/prediction', methods=['GET', 'POST'])
def prediction():
    if request.method == 'POST':
        # Collect form data (this would be more extensive in your actual app)
        age = request.form['age']
        blood_pressure = request.form['blood_pressure']
        blood_sugar = request.form['blood_sugar']
        weight = request.form['weight']
        lifestyle = request.form['lifestyle']
        
        # Here, you would integrate your prediction model
        # This is a placeholder result
        risk_score = "Low Risk"  # Replace with actual prediction model output
        
        # Redirect to the prediction result page with the risk score
        return redirect(url_for('prediction_result', risk_score=risk_score))

    return render_template('prediction.html')

# Route for showing prediction result
@app.route('/prediction_result')
def prediction_result():
    # Get the risk score from the query parameters
    risk_score = request.args.get('risk_score', 'Unknown Risk')
    
    # Render the result page with the risk score
    return render_template('prediction_result.html', risk_score=risk_score)

# Route for tracker page
@app.route('/tracker', methods=['GET', 'POST'])
def tracker():
    if 'entries' not in session:
        session['entries'] = []  # Initialize empty list if it doesn't exist

    if request.method == 'POST':
        # Collect form data
        blood_pressure = request.form['blood_pressure']
        sugar_level = request.form['sugar_level']
        weight = request.form['weight']
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')  # Current date and time

        # Store the new entry in the session
        session['entries'].append({
            'blood_pressure': blood_pressure,
            'sugar_level': sugar_level,
            'weight': weight,
            'timestamp': timestamp
        })

        # Save session
        session.modified = True

        # Redirect back to the tracker page
        return redirect(url_for('tracker'))

    return render_template('tracker.html', entries=session['entries'])

# Route for profile page
@app.route('/profile')
def profile():
    return render_template('profile.html')

if __name__ == "__main__":
    app.run(debug=True)
