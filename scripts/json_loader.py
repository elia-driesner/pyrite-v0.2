import json

class JsonLoader:
    def __init__(self, path, folder_path='data/settings'):
        self.path = str(folder_path + path)
        
    def read(self):
        with open('self.path', 'r') as file:
            json_data = json.load(file)
        return json_data

    def write(self, prefix, data):
        with open('self.path', 'r') as file:
            json_data = json.load(file)
            json_data['prefix'] = data
                
        with open('self.path', 'w') as file:
            json.dump(json_data, file, indent=2)