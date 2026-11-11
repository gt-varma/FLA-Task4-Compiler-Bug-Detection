"""Finite-domain differential checker."""
from .compiler import compile_expression, execute_target
from .equivalence import Observation, equivalent
from .source_interpreter import evaluate_source, UnsupportedExpression

def check_expression(expression, environments, faulty_optimization=False):
    results = []
    try:
        target_code = compile_expression(expression, faulty_optimization)
    except UnsupportedExpression as exc:
        return {"status": "INCONCLUSIVE", "results": results, "reason": str(exc)}
    for env in environments:
        try:
            source = Observation("HALTED", evaluate_source(expression, env))
            target = Observation("HALTED", execute_target(target_code, env))
        except (UnsupportedExpression, RuntimeError, KeyError, ValueError, IndexError) as exc:
            return {"status": "INCONCLUSIVE", "results": results, "reason": str(exc)}
        match = equivalent(source, target)
        results.append({"input": dict(env), "source": source.value, "compiled": target.value, "match": match})
        if not match:
            return {"status": "BUG FOUND", "results": results, "counterexample": dict(env), "instructions": target_code}
    return {"status": "NO BUG FOUND WITHIN TEST SCOPE", "results": results, "instructions": target_code}
