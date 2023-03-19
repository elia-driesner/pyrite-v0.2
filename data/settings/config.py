from pyrite.json_loader import JsonLoader

class Config:
    def __init__(self):
        self.json_loader = JsonLoader()
        
    def load_settings(self):
        """loads the settings from many diffrent files, linked in the dest.json file"""
        self.files = self.json_loader.read('dest.json')
        self.settings = {}
        
        for file in self.files:
            try:
                self.settings[file] = self.json_loader.read(self.files[file])
            except:
                print(f'Settings file not found: {file}')
        return self.settings