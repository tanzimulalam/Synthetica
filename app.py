from flask import Flask, render_template, request, jsonify
from stix_object_builder import (
    create_threat_actors, create_identities, create_malware,
    create_indicators, create_attack_patterns, create_tools,
    create_campaigns, create_intrusion_sets, create_vulnerabilities, 
    create_course_of_actions, create_malware_analysis
)
from relationship_builder import randomly_connect_objects
from stix_bundler import create_bundle
app = Flask(__name__, static_folder='static')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/select-objects', methods=['GET'])
def select_objects():
    return render_template('select_objects.html')

@app.route('/generate-graph', methods=['POST'])
def generate_graph():
    data = request.form
    threat_actor_count = int(data.get('threat-actor-count', 0))
    identity_count = int(data.get('identity-count', 0))
    malware_count = int(data.get('malware-count', 0))
    indicators_count = int(data.get('indicator-count', 0))
    attack_patterns_count = int(data.get('attack-pattern-count', 0))
    tools_count = int(data.get('tool-count', 0))
    campaigns_count = int(data.get('campaign-count', 0))
    intrusion_sets_count = int(data.get('intrusion-set-count', 0))
    vulnerabilities_count = int(data.get('vulnerability-count', 0))
    course_of_actions_count = int(data.get('course-of-action-count', 0))

    threat_actors = create_threat_actors(threat_actor_count) if threat_actor_count > 0 else []
    identities = create_identities(identity_count) if identity_count > 0 else []
    malwares = create_malware(malware_count) if malware_count > 0 else []
    indicators = create_indicators(indicators_count) if indicators_count > 0 else []
    attack_patterns = create_attack_patterns(attack_patterns_count) if attack_patterns_count > 0 else []
    tools = create_tools(tools_count) if tools_count > 0 else []
    campaigns = create_campaigns(campaigns_count) if campaigns_count > 0 else []
    intrusion_sets = create_intrusion_sets(intrusion_sets_count) if intrusion_sets_count > 0 else []
    vulnerabilities = create_vulnerabilities(vulnerabilities_count) if vulnerabilities_count > 0 else []
    course_of_actions = create_course_of_actions(course_of_actions_count) if course_of_actions_count > 0 else []

    stix_objects = threat_actors + identities + malwares + indicators + attack_patterns + tools + campaigns + intrusion_sets + vulnerabilities + course_of_actions


    for obj in stix_objects:
        print(obj)

    relationships = randomly_connect_objects(stix_objects)

    stix_bundle = create_bundle(stix_objects, relationships)

    return jsonify({"stix_bundle": stix_bundle})

if __name__ == '__main__':
    app.run(debug=True)
