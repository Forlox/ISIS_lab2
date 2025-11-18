class InferenceEngine:
    def __init__(self, kb, wm, resolver):
        self.kb = kb
        self.wm = wm
        self.resolver = resolver
        self.execution_log = []

    def run_forward_chaining(self):
        fired = set()
        while not self.wm.get_fact("final"):
            matched = [r for r in self.kb.get_all_rules() if r.matches(self.wm) and r.id not in fired]
            if not matched:
                break
            selected = self.resolver.resolve(matched)
            log = selected.execute(self.wm)
            self.execution_log.append({
                'rule_id': selected.id,
                'rule_name': selected.name,
                'actions': log
            })
            fired.add(selected.id)