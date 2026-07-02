memory_store = {}

def save_decision(request_id, data):
    memory_store[request_id] = data

def get_decision(request_id):
    return memory_store.get(request_id)