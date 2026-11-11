import unittest
from compiler_checker.source_interpreter import evaluate_source
from compiler_checker.compiler import compile_expression, execute_target
from compiler_checker.validator import check_expression

class CompilerCheckerTests(unittest.TestCase):
    def test_interpreter(self):
        self.assertEqual(evaluate_source("a + 0", {"a": 5}), 5)
    def test_correct_compilation(self):
        self.assertEqual(execute_target(compile_expression("a + 0"), {"a": 5}), 5)
    def test_faulty_optimization_detected(self):
        result = check_expression("a + 0", [{"a": 5}], True)
        self.assertEqual(result["status"], "BUG FOUND")
        self.assertEqual(result["counterexample"], {"a": 5})
    def test_no_bug_within_scope(self):
        result = check_expression("a * 2", [{"a": 0}, {"a": 3}])
        self.assertEqual(result["status"], "NO BUG FOUND WITHIN TEST SCOPE")

if __name__ == "__main__":
    unittest.main()
