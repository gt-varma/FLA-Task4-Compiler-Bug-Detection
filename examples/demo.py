from compiler_checker.validator import check_expression

expr = "a + 0"
inputs = [{"a": n} for n in (-2, 0, 5, 12)]
print("Correct compiler:")
print(check_expression(expr, inputs))
print("\nDeliberately faulty optimization:")
print(check_expression(expr, inputs, faulty_optimization=True))
