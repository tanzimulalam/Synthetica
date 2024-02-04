from stix2 import Bundle

def create_bundle(stix_objects, relationships):
    all_objects = stix_objects + relationships
    return Bundle(objects=all_objects).serialize(pretty=True)
