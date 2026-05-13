from src.tools.complexity_checker import ComplexityChecker


def test_complexity_analysis():

    checker = ComplexityChecker()

    sample_code = """
def calculate(x):
    if x > 0:
        return x
    return -x
"""

    result = checker.check_complexity(sample_code)

    assert len(result) > 0
