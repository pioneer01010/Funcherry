import json
from pathlib import Path

from funcherry.generator import Generator
from metric.complexity.evaluator import Cyclomatic
from utils.gitc import GitClient
from utils.parser import FunctionParser

class Funcherry:
    def __init__(self, sample):
        self.sample = sample
        self.positive = Generator.gen_positive(sample)
        self.negatives = Generator.gen_negatives(sample)
    
    def __repr__(self):
        return json.dumps(self, default=lambda o: o.__dict__)
    
    def to_dict(self):
        return {
            "sample": self.sample,
            "positive": self.positive,
            "negatives": self.negatives
        }

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
        return json.dumps(self, default=lambda o: o.__dict__)\
    
    def to_list(self):
        json_list = []
        for fc in self.funcherrys:
            json_list.append(fc.to_dict())
        return json_list

    def export_json(self):
        try:
            with open("sample.json", "w") as file:
                json.dump(self.to_list(), file)
        except Exception as e:
            print("Export error:", e)
    
    @classmethod
    def from_repo(cls, repo, dir):
        GitClient.clone(repo, dir)
        return cls.from_dir(dir)

    @classmethod
    def from_dir(cls, dir):
        func_dict = []
        files = [f for f in Path(dir).rglob('*.py') if not f.name.startswith("__init__")]
        for file in files:
            functions = FunctionParser.parse_functions_from_file(file)
            for function in functions:
                cyclomatic = Cyclomatic().calculate(function.get('block'))
                function["cyclomatic"] = cyclomatic
                if cyclomatic > 3:
                    func_dict.append(function)

        manager = cls()
        manager.funcherrys = [Funcherry.from_str(function['block']) for function in func_dict]
        return manager
