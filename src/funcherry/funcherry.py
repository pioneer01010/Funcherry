import json

from funcherry.generator import Generator
class Funcherry:
    def __init__(self, sample):
        self.sample = sample
        self.positive = Generator.gen_positive(sample)
        self.negatives = Generator.gen_negatives(sample)
    
    def __repr__(self):
        return json.dumps(self, default=lambda o: o.__dict__)

    @classmethod
    def from_str(cls, str):
        return Funcherry(str)
    
    @classmethod
    def from_json(cls, json_dict):
        return Funcherry(json_dict['function'])

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
