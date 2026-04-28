from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Temporary storage (no DB)
requests_list = []
volunteers = []

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/add_request', methods=['POST'])
def add_request():
    data = request.json
    requests_list.append(data)
    return jsonify({"message": "Request added!"})

@app.route('/add_volunteer', methods=['POST'])
def add_volunteer():
    data = request.json
    volunteers.append(data)
    return jsonify({"message": "Volunteer added!"})

@app.route('/match', methods=['GET'])
def match():
    matches = []

    for req in requests_list:
        for vol in volunteers:
            if req['location'].lower() == vol['location'].lower():
                matches.append({
                    "task": req['task'],
                    "volunteer": vol['name'],
                    "location": req['location']
                })

    return jsonify(matches)

if __name__ == '__main__':
    app.run(debug=True)