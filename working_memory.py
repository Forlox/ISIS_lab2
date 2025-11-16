class WorkingMemory:
    def __init__(self):
        self.facts = {}

    def assert_fact(self, name, value):
        self.facts[name] = value

    def retract_fact(self, name):
        self.facts.pop(name, None)

    def get_fact(self, name):
        return self.facts.get(name)

    def has_fact(self, name):
        return name in self.facts

    def get_all_facts(self):
        return self.facts.copy()