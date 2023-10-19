from funcherry import Funcherry
from funcherry.funcherry import FCManager

repo = "https://github.com/pioneer01010/Funcherry.git"
path = "C:\\/workspace\\/Funcherry"
sample = "def foo():\n        for i in range(0, 5):\n            a = 3\n        return a"

class TestFuncherry:
    def test_funcherry(self):
        fc = Funcherry.from_str(sample)
        print(fc.__repr__)

    def test_fc_manager(self):
        manager = FCManager().from_repo(repo, path)
        manager.export_json()