import yaml
from yaml.loader import SafeLoader
from factories import EasyLevel, MediumLevel, HardLevel

levels = """
levels:
        - !easy_level {}
        - !medium_level
            enemy: ['rat']
        - !hard_level
            enemy:
                - rat
                - snake
                - dragon
            enemy_count: 10
"""

SafeLoader.add_constructor('!easy_level', EasyLevel.from_yaml)
SafeLoader.add_constructor('!medium_level', MediumLevel.from_yaml)
SafeLoader.add_constructor('!hard_level', HardLevel.from_yaml)
obj = yaml.load(levels, Loader=SafeLoader)
