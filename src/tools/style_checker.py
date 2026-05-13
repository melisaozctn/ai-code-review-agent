from pylint.lint import Run
from pylint.reporters.text import TextReporter
from io import StringIO


class StyleChecker:

    def check_style(self, file_path):

        output = StringIO()
        reporter = TextReporter(output)

        Run(
            [file_path],
            reporter=reporter,
            exit=False
        )

        result = output.getvalue()

        return {
            "tool": "Pylint",
            "result": result
        }
