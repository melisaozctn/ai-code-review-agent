from src.tools.syntax_checker import SyntaxChecker


def test_valid_syntax():

    checker = SyntaxChecker()

    code = "print('Hello World')"

    result = checker.check_syntax(code)

    assert result["success"] == True


def test_invalid_syntax():

    checker = SyntaxChecker()

    code = "print('Hello World'"

    result = checker.check_syntax(code)

    assert result["success"] == False
