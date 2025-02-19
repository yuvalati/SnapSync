from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Dummy data for demonstration
users = [
    {"id": 1, "name": "Alice", "age": 29, "location": "Tel Aviv", "image": "/static/images/alice.jpg"},
    {"id": 2, "name": "Bob", "age": 25, "location": "Tel Aviv", "image": "/static/images/bob.jpg"},
    {"id": 3, "name": "Messi", "age": 24, "location": "Tel Aviv", "image": "/static/images/messi.jpg"},
    {"id": 4, "name": "adele", "age": 27, "location": "Tel Aviv", "image": "/static/images/adele.jpg"},
]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/profile', methods=['GET', 'POST'])
def profile():
    if request.method == 'POST':
        # Simulate creating a profile
        name = request.form['name']
        age = request.form['age']
        location = request.form['location']
        users.append({"id": len(users)+1, "name": name, "age": age, "location": location})
        return redirect(url_for('connections'))
    return render_template('profile.html')

@app.route('/connections')
def connections():
    return render_template('connections.html', users=users)

if __name__ == '__main__':
    app.run(debug=True)
