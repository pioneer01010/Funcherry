import json
import os

from utils.parser import FunctionParser


def test_load_config_file(resource_path, config_path):
    with open(config_path, 'r') as config_file:
        config = json.load(config_file)
        assert "sample_file" in config
        for file in config['sample_file']['python']:
            assert os.path.isfile(resource_path + "/" + file)


class TestFunctionParser:
    def test_parse_functions_from_file(self, resource_path, config_path):
        with open(config_path, 'r') as config_file:
            config = json.load(config_file)
            for file in config['sample_file']['python']:
                filepath = resource_path + "/" + file
                result = FunctionParser.parse_functions_from_file(filepath)
                assert result
