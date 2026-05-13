from src.agent.review_agent import ReviewAgent


def test_review_agent():

    agent = ReviewAgent()

    sample_code = """
def hello():
    return 'hello'
"""

    result = agent.review_code(sample_code)

    assert "syntax" in result
    assert "complexity" in result
