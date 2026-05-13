from src.agent.review_agent import ReviewAgent


sample_code = """
def add(a, b):
    return a + b
"""


agent = ReviewAgent()

results = agent.review_code(sample_code)

print(results)
