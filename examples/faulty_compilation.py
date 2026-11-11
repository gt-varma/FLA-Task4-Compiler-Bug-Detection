from compiler_checker.compiler import compile_expression, execute_target
print(execute_target(compile_expression("a + 0", True), {"a": 5}))  # Deliberately wrong: 6
