"""Reference interpreter for a small integer expression language."""
import ast
from collections.abc import Mapping

class UnsupportedExpression(ValueError):
    pass

def evaluate_source(expression: str, env: Mapping[str, int]) -> int:
    try:
        root = ast.parse(expression, mode="eval").body
    except SyntaxError as exc:
        raise UnsupportedExpression(str(exc)) from exc

    def visit(node):
        if isinstance(node, ast.Constant) and isinstance(node.value, int) and not isinstance(node.value, bool):
            return node.value
        if isinstance(node, ast.Name):
            if node.id not in env or not isinstance(env[node.id], int) or isinstance(env[node.id], bool):
                raise UnsupportedExpression(f"Invalid or missing integer variable: {node.id}")
            return env[node.id]
        if isinstance(node, ast.UnaryOp) and isinstance(node.op, ast.USub):
            return -visit(node.operand)
        if isinstance(node, ast.BinOp) and isinstance(node.op, (ast.Add, ast.Sub, ast.Mult)):
            left, right = visit(node.left), visit(node.right)
            if isinstance(node.op, ast.Add): return left + right
            if isinstance(node.op, ast.Sub): return left - right
            return left * right
        raise UnsupportedExpression(f"Unsupported syntax: {type(node).__name__}")
    return visit(root)
