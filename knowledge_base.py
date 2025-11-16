import json
from rule import Rule

class KnowledgeBase:
    def __init__(self, filepath='knowledge_base.json'):
        self.rules = []
        self.load_from_json(filepath)

    def load_from_json(self, filepath):
        with open(filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)
        self.rules = [
            Rule(
                id=r['id'],
                name=r['name'],
                priority=r['priority'],
                conditions=r['conditions'],
                actions=r['actions']
            )
            for r in data['rules']
        ]

    def get_all_rules(self):
        return self.rules[:]