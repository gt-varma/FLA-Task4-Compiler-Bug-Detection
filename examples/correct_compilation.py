from compiler_checker.compiler import compile_expression, execute_target
print(execute_target(compile_expression("a + 0"), {"a": 5}))  # 5
