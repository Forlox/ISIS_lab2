class ExplanationModule:
    def __init__(self, log):
        self.log = log

    def explain(self):
        if not self.log:
            return "Вывод не был осуществлён."

        lines = ["=== Цепочка вывода ==="]
        for step in self.log:
            lines.append(f"Правило '{step['rule_name']}' (ID={step['rule_id']})")
            for action in step['actions']:
                lines.append(f"   • {action}")
        return "\n".join(lines)