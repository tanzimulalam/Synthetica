from faker import Faker
from stix2 import ThreatActor, Identity, Malware, Tool, Indicator, AttackPattern, Campaign, IntrusionSet, Vulnerability, CourseOfAction, Location, MalwareAnalysis
import random

fake = Faker()


def create_threat_actors(count):
    templates = [
        "{} Bear",
        "{} Panda",
        "{} Group",
        "{} Squad",
        "{} Collective",
        "{} APT",
        "{} Brigade",
        "{} Syndicate"
    ]
    return [ThreatActor(name=random.choice(templates).format(fake.word().capitalize()),
                        description="Generated fake Threat Actor") for _ in range(count)]

def create_identities(count):
    templates = [
        "{} Analyst",
        "{} Researcher",
        "{} Operator",
        "{} Developer",
        "{} Admin"
    ]
    return [Identity(name=random.choice(templates).format(fake.word().capitalize()),
                     identity_class="individual",
                     description="Generated fake Identity") for _ in range(count)]

def create_malware(count):
    templates = [
        "{} Virus",
        "{} Worm",
        "{} Trojan",
        "{} Ransomware",
        "{} Botnet",
        "{} Spyware",
        "{} Rootkit",
        "{} FilelessMalware",
        "{} Adware",
        "{} Keylogger",
        "{} Cryptojacker",
        "{} Wiper"
    ]
    return [Malware(name=random.choice(templates).format(fake.word().capitalize()),
                    description="Generated fake Malware",
                    malware_types=[fake.word()],
                    is_family=False) for _ in range(count)]

def create_indicators(count):
    templates = [
        "{} PhishingActivity",
        "{} MalwareSignature",
        "{} AnomalousTraffic",
        "{} SuspiciousLogin",
        "{} DataExfiltrationSignal"
    ]
    return [Indicator(pattern="[file:hashes.'SHA-256' = '{}']".format(fake.sha256()),
                      pattern_type="stix",
                      name=random.choice(templates).format(fake.word().capitalize())) for _ in range(count)]

def create_attack_patterns(count):
    templates = [
        "{} Phishing",
        "{} SpearPhishing",
        "{} DriveByCompromise",
        "{} ExploitPublicFacingApplication"
    ]
    return [AttackPattern(name=random.choice(templates).format(fake.word().capitalize()),
                          description="Generated fake Attack Pattern") for _ in range(count)]

def create_campaigns(count):
    templates = [
        "Operation {}",
        "{} Threat",
        "Project {}",
        "{} Offensive",
        "{} Maneuver",
        "{} Wave",
        "{} Blitz"
    ]
    return [Campaign(name=random.choice(templates).format(fake.word().capitalize()),
                     description="Generated fake Campaign") for _ in range(count)]

def create_intrusion_sets(count):
    templates = [
        "{} Recon",
        "{} Domination",
        "{} Exploitation",
        "{} Disruption",
        "{} Theft"
    ]
    return [IntrusionSet(name=random.choice(templates).format(fake.word().capitalize()),
                         description="Generated fake Intrusion Set") for _ in range(count)]

def create_vulnerabilities(count):
    templates = [
        "{} Misconfiguration",
        "{} UnsecuredAPI",
        "{} OutdatedSoftware",
        "{} ZeroDay",
        "{} CredentialLeak",
        "{} AccessControlIssue",
        "{} SharedResponsibilityFlaw"
    ]
    return [Vulnerability(name=random.choice(templates).format(fake.word().capitalize()),
                          description="Generated fake Vulnerability") for _ in range(count)]

def create_tools(count):
    templates = [
        "{} Scanner",
        "{} Firewall",
        "{} Encryptor",
        "{} Analyzer",
        "{} Protector"
    ]
    return [Tool(name=random.choice(templates).format(fake.word().capitalize()),
                 description="Generated fake Tool") for _ in range(count)]

def create_course_of_actions(count):
    templates = [
        "Mitigate {} Vulnerability",
        "Prevent {} Attack",
        "Respond to {} Incident",
        "Improve {} Security Posture",
        "Patch {} Software"
    ]
    return [CourseOfAction(name=random.choice(templates).format(fake.word().capitalize()),
                           description="Generated fake Course of Action") for _ in range(count)]

def create_locations(count):
    templates = [
        "{} Headquarters",
        "{} Datacenter",
        "{} Office",
        "{} Facility",
        "{} Building",
        "{} Room",
        "{} Lab",
        "{} Department",
        "{} Company",
        "{} Campus"
    ]


    return [Location(name=random.choice(templates).format(fake.word().capitalize()), latitude=fake.latitude(), longitude=fake.longitude(), city=fake.city(), country=fake.country(), street_address=fake.street_address(), postal_code=fake.postcode(), region=fake.state()) for _ in range(count)]

def create_malware_analysis(count):
    
    templates = ["{} VirusTotal",
                     "{} Hybrid Analysis", 
                     "{} Malwarebytes", 
                     "{} Kaspersky Lab", 
                     "{} McAfee"]
    
    return [MalwareAnalysis(product=random.choice(templates).format(fake.word).capitalize(),
                            version=fake.random_element(elements=("1.0", "2.0", "3.0", "4.0")),
                            analysis_engine_version=fake.random_element(elements=("1.0", "2.0", "3.0", "4.0")),
                            analysis_definition_version=fake.random_element(elements=("1.0", "2.0", "3.0", "4.0")),
                            result=fake.random_element(elements=("malicious", "suspicious", "clean")),
                            ) for _ in range(count)]