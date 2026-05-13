from radon.complexity import cc_visit


class ComplexityChecker:

    def check_complexity(self, code):

        results = cc_visit(code)

        complexity_data = []

        for item in results:
            complexity_data.append({
                "function": item.name,
                "complexity": item.complexity
            })

        return complexity_data
