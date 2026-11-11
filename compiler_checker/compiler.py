"""Compiler and executor for a tiny stack-machine target."""
import ast
from .source_interpreter import UnsupportedExpression

def compile_expression(expression: str, faulty_optimization: bool = False):
    try:
        root = ast.parse(expression, mode="eval").body
    except SyntaxError as exc:
        raise UnsupportedExpression(str(exc)) from exc
    code = []
    def emit(node):
        if isinstance(node, ast.Constant) and isinstance(node.value, int) and not isinstance(node.value, bool):
            code.append(("PUSH", node.value))
        elif isinstance(node, ast.Name):
            code.append(("LOAD", node.id))
        elif isinstance(node, ast.UnaryOp) and isinstance(node.op, ast.USub):
            emit(node.operand); code.append(("NEG", None))
        elif isinstance(node, ast.BinOp) and isinstance(node.op, (ast.Add, ast.Sub, ast.Mult)):
            # Deliberate demonstration bug: a + 0 is incorrectly changed to a + 1.
            if faulty_optimization and isinstance(node.op, ast.Add) and isinstance(node.right, ast.Constant) and node.right.value == 0 and isinstance(node.left, ast.Name):
                code.extend([("LOAD", node.left.id), ("PUSH", 1), ("ADD", None)])
                return
            emit(node.left); emit(node.right)
            op = "ADD" if isinstance(node.op, ast.Add) else "SUB" if isinstance(node.op, ast.Sub) else "MUL"
            code.append((op, None))
        else:
            raise UnsupportedExpression(f"Unsupported syntax: {type(node).__name__}")
    emit(root)
    return code

def execute_target(code, env):
    stack = []
    for op, arg in code:
        if op == "PUSH": stack.append(arg)
        elif op == "LOAD":
            if arg not in env: raise UnsupportedExpression(f"Missing variable: {arg}")
            stack.append(env[arg])
        elif op == "NEG": stack.append(-stack.pop())
        elif op in ("ADD", "SUB", "MUL"):
            right, left = stack.pop(), stack.pop()
            stack.append(left + right if op == "ADD" else left - right if op == "SUB" else left * right)
        else: raise UnsupportedExpression(f"Unknown instruction: {op}")
    if len(stack) != 1: raise RuntimeError("Invalid target stack state")
    return stack[0]
