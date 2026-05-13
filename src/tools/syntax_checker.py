import ast


class SyntaxChecker:

    def check_syntax(self, code):
        try:
            ast.parse(code)
            return {
                "success": True,
                "message": "No syntax errors found."
            }

        except SyntaxError as e:
            return {
                "success": False,
                "message": f"Syntax Error: {e}"
            }
