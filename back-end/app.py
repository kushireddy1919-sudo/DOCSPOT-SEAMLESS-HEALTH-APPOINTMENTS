from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Hospital Data (AP & TS)
hospital_data = {
    "hyderabad": [
        "Apollo Hospitals, Jubilee Hills",
        "Yashoda Hospitals, Somajiguda",
        "Care Hospitals, Banjara Hills",
        "NIMS, Punjagutta",
        "Medicover Hospitals, Hitech City"
    ],
    "vizag": [
        "Seven Hills Hospital",
        "KIMS-Icon Hospital",
        "Apollo Hospitals, Arilova",
        "Care Hospitals, Waltair",
        "MGH Vizag"
    ],
    "vijayawada": [
        "Manipal Hospital",
        "Ayush Hospitals",
        "Ramesh Hospitals",
        "Andhra Hospitals",
        "Rainbow Children's Hospital"
    ],
    "tirupati": [
        "SVRR Government Hospital",
        "Sankara Netralaya",
        "Amara Hospital",
        "Apollo Clinic",
        "Lotus Hospital"
    ],
    "warangal": [
        "MGM Hospital",
        "St. Ann's Hospital",
        "Maxcare Hospital",
        "Ajara Hospital",
        "Rohini Hospital"
    ]
}


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/find_hospitals', methods=['POST'])
def find_hospitals():
    area = request.json.get("area", "").lower()

    for city in hospital_data:
        if city in area:
            return jsonify(hospital_data[city])

    # fallback
    return jsonify([
        f"{area.title()} Government Hospital",
        f"{area.title()} Multi-Specialty Clinic",
        f"Suraksha Hospital, {area.title()}",
        "LifeLine Medical Center",
        "People's Choice Hospital"
    ])


if __name__ == '__main__':
    app.run(debug=True)
