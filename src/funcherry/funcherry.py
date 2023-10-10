import json
class Funcherry:
    def __init__(self, anchor, positive, negatives):
        self.anchor = anchor
        self.positive = positive
        self.negatives = negatives
    
    def __repr__(self):
        return json.dumps(self, default=lambda o: o.__dict__)

    @classmethod
    def from_json(cls, json_dict):
        return Funcherry(json_dict['anchor'], json_dict['positive'], json_dict['negatives'])

class FCManager:
    def __init__(self):
        self.funcherrys = []

    def __repr__(self):
        return json.dumps(self, default=lambda o: o.__dict__)
    
    @classmethod
    def from_repo(cls, repo_url):
        pass

    @classmethod
    def from_dir(cls, dir):
        pass
    
    @classmethod
    def from_json(cls, json_str):
        json_dict = json.loads(json_str)

        new_instance = cls()
        new_instance.funcherrys = [Funcherry.from_json(function) for function in json_dict['functions']]
        return new_instance
