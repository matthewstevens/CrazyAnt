from util import load

DATA_MAP = {}
RESOURCE_TO_ID = {}
RESOURCE_COUNTER = 0

def get_resource(resource_name):
	if RESOURCE_TO_ID.has_key(resource_name):
		return DATA_MAP[RESOURCE_TO_ID[resource_name]]
	resource_data = load(resource_name)
	resurouce_id = RESOURCE_COUNTER
	RESOURCE_COUNTER += 1
	RESOURCE_TO_ID[resource_name] = resurouce_id
	DATA_MAP[resurouce_id] = resource_data
	return resource_data
