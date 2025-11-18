import operator

# Маппинг операторов
OPS = {
    '==': operator.eq,
    '!=': operator.ne,
    '<': operator.lt,
    '<=': operator.le,
    '>': operator.gt,
    '>=': operator.ge,
}

class Rule:
    def __init__(self, id, name, priority, conditions, actions):
        self.id = id
        self.name = name
        self.priority = priority
        self.conditions = conditions  # [{fact, operator, value}, ...]
        self.actions = actions        # [{fact, value}, ...]

    def matches(self, working_memory):
        for cond in self.conditions:
            fact_name = cond['fact']
            op = OPS.get(cond['operator'])
            if op is None:
                raise ValueError(f"Неизвестный оператор: {cond['operator']}")

            # Если факт неизвестен — правило не срабатывает (ждём ввода позже)
            if not working_memory.has_fact(fact_name):
                return False

            fact_value = working_memory.get_fact(fact_name)
            expected = cond['value']
            if not op(fact_value, expected):
                return False
        return True

    def execute(self, working_memory):
        log = []
        for act in self.actions:
            name = act['fact']
            value = act['value']
            working_memory.assert_fact(name, value)
            log.append(f"- Утверждён факт: {name} = {value!r}")
        return log

    def specificity(self):
        return len(self.conditions)

    def __repr__(self):
        return f"Rule(id={self.id}, name='{self.name}')"