import os
from flask import Flask, render_template, request, redirect, url_for, jsonify
from checkPaths import process_photos_and_check_paths_2directories
import markdown

app = Flask(__name__)

# Dummy data for demonstration
users = [
    {"id": 1, "name": "Alice", "age": 29, "location": "United Kingdom", "image": "/static/images/alice.jpg",
     "gallery": "SnapUsers/Alice"},
    {"id": 2, "name": "Bob", "age": 25, "location": "United Kingdom", "image": "/static/images/bob.jpg",
     "gallery": "SnapUsers/Bob"},
    {"id": 3, "name": "Messi", "age": 24, "location": "United Kingdom", "image": "/static/images/messi.jpg",
     "gallery": "SnapUsers/Messi"},
    {"id": 4, "name": "adele", "age": 27, "location": "United Kingdom", "image": "/static/images/adele.jpg",
     "gallery": "SnapUsers/Adele"},
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
        users.append({
            "id": len(users) + 1,
            "name": name,
            "age": age,
            "location": location,
            "image": "/static/images/default.jpg",
            "gallery": "SnapUsers/User"
        })
        return redirect(url_for('connections'))
    return render_template('profile.html')


@app.route('/connections')
def connections():
    # Assume the newest user in the list is "my profile"
    if users:
        my_profile = users[-1]
        other_users = users[:-1]
    else:
        my_profile = None
        other_users = []
    return render_template('connections.html', my_profile=my_profile, users=other_users)


@app.route('/add_friend/<int:friend_id>', methods=['POST'])
def add_friend(friend_id):
    """
    Approve friend, check crossing paths immediately, return the results in JSON.
    (But we won't show an alert on the frontend—just the "Approved" button)
    """
    current_user = users[-1]
    friend_user = next((u for u in users if u['id'] == friend_id), None)
    if not friend_user:
        return jsonify({"error": "Friend not found"}), 404

    # Check crossing paths (though not displayed here unless user goes to "Cross Paths" tab)
    crossed_paths = process_photos_and_check_paths_2directories(
        current_user['gallery'],
        friend_user['gallery']
    )

    return jsonify({
        "message": "Friend approved.",
        "crossed_paths": crossed_paths
    })


@app.route('/cross_paths/<int:friend_id>', methods=['GET'])
def cross_paths(friend_id):
    """
    On demand: re-check or fetch cross path data for this friend and the current user.
    """
    current_user = users[-1]
    friend_user = next((u for u in users if u['id'] == friend_id), None)
    if not friend_user:
        return jsonify({"error": "Friend not found"}), 404

    crossed_paths = process_photos_and_check_paths_2directories(
        current_user['gallery'],
        friend_user['gallery']
    )

    return jsonify({
        "crossed_paths": crossed_paths
    })


@app.route('/privacy')
def show_privacy():
    md_path = os.path.join(app.root_path, 'PRIVACY.md')
    with open(md_path, 'r', encoding='utf-8') as f:
        md_text = f.read()

    # Convert Markdown to HTML
    html_content = markdown.markdown(md_text)

    # Render a template that displays the HTML content
    return render_template('privacy.html', content=html_content)

if __name__ == '__main__':
    app.run(debug=True)
