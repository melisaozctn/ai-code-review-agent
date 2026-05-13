from src.tools.syntax_checker import SyntaxChecker
from src.tools.complexity_checker import ComplexityChecker


class ReviewAgent:

    def __init__(self):

        self.syntax_checker = SyntaxChecker()
        self.complexity_checker = ComplexityChecker()

    def review_code(self, code):

        syntax_result = self.syntax_checker.check_syntax(code)

        complexity_result = self.complexity_checker.check_complexity(code)

        return {
            "syntax": syntax_result,
            "complexity": complexity_result
        }
