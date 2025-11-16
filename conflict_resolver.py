class ConflictResolver:
    def resolve(self, matched_rules):
        raise NotImplementedError

class PriorityConflictResolver(ConflictResolver):
    def resolve(self, matched_rules):
        return max(matched_rules, key=lambda r: r.priority)

class SpecificityConflictResolver(ConflictResolver):
    def resolve(self, matched_rules):
        # Сначала по приоритету, затем по специфичности (как в CLIPS)
        return max(matched_rules, key=lambda r: (r.priority, r.specificity()))