from knowledge_base import KnowledgeBase
from working_memory import WorkingMemory
from conflict_resolver import PriorityConflictResolver, SpecificityConflictResolver
from inference_engine import InferenceEngine
from explanation import ExplanationModule


def ask_int(prompt, min_val, max_val) -> int:
    while True:
        try:
            value = int(input(prompt))
            if min_val <= value <= max_val:
                return value
        except ValueError:
            pass
        prompt = "Неверный ввод. Введите повторно: "

def ask_choice(prompt, options):
    while True:
        ans = input(prompt).strip().lower()
        if ans in options:
            return ans
        prompt = "Неверный ввод. Введите повторно: "

if __name__ == "__main__":
    wm = WorkingMemory()
    kb = KnowledgeBase('knowledge_base.json')

    labs = ask_int("Введите количество сданных лабораторных работ (0–5): ", 0, 5)
    wm.assert_fact("labs_count", labs)
    if labs >= 3:
        att = ask_int("Введите посещаемость лекций (0–100%): ", 0, 100)
        wm.assert_fact("attendance_percent", att)

        # Запускаем МЛВ для вывода 'attendance'
        engine = InferenceEngine(kb, wm, PriorityConflictResolver())
        engine.run_forward_chaining()

        # Если после вывода есть auto_grade — спрашиваем экзамен
        if wm.get_fact("auto_grade") is not None:
            exam = ask_choice("Как сдан экзамен? (уд/неуд): ", ['уд', 'неуд', '1', '0'])
            if exam == "1": exam='уд'
            elif exam == "0": exam='неуд'
            print(exam)
            wm.assert_fact("exam_answer", exam)

    # Финальный запуск МЛВ с более точной стратегией разрешения конфликтов
    final_engine = InferenceEngine(kb, wm, SpecificityConflictResolver())
    final_engine.run_forward_chaining()

    grade = wm.get_fact("grade") or "не определена"
    print(f"\nИтоговая оценка: **{grade}**")

    expl = ExplanationModule(final_engine.execution_log)
    print("\n" + expl.explain())