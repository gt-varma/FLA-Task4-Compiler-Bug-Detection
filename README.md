# Formal Language and Automata-Based Analysis of Compiler Bug Detection

## Team Details

| Role | Team member | Register number |
|---|---|---|
| Team member | K Neeraj | RA2411026050023 |
| Team member | G Tarun Varma | RA2411026050037 |
| Team member | N Bennu Durgesh | RA2411026050065 |

**Course:** 21CSC301T – Formal Language and Automata  
**Assignment:** Task 4 – Formal Language and Automata-Based Real-World Problem Solving and System Design  
**Project topic:** Compiler Bug Detection

## Problem

A compiler translates a source program into a target program. A compiler bug occurs when the compiled program behaves differently from the source program under the same input and observation model.

Let P be a source program, C a compiler, and x an input. Let Obs(P,x) record termination and, if it terminates, the observable output.

A mismatch exists if there is an input x such that Obs(P,x) != Obs(C(P),x). Universal correctness asks whether the observations agree for every supported program and input. For sufficiently expressive programs, general semantic equivalence and universal correctness are undecidable.

## Computational model mapping

| Real-world concept | Computational formulation |
|---|---|
| Source program | Program / Turing-machine description |
| Compiler | Translation function C |
| Compiled output | Target program C(P) |
| Input | Input string or value x |
| Execution | Computation |
| Observable result | Termination and output |
| Bug witness | Input producing different observations |
| General correctness | Equivalence for all supported inputs |

## Worked example

Source expression: a + 0. Input: a = 5. Correct output: 5. A faulty optimization may translate this into a + 1, producing 6. The input a = 5 is a concrete counterexample.

## Restricted-case engineering approach

This repository implements a tiny integer expression language and compares a source interpreter with a stack-machine target. The supported operators are addition, subtraction, and multiplication.

Possible outcomes:
- **BUG FOUND** – at least one tested input produced a mismatch.
- **NO BUG FOUND WITHIN TEST SCOPE** – all selected tests agreed.
- **INCONCLUSIVE** – unsupported syntax or a validation issue prevented a conclusion.

A finite test suite is decidable over its stated finite scope, but passing it does not prove universal correctness. A timeout in a more general executor would be inconclusive, not proof of nontermination.

## Undecidability perspective

General program equivalence is undecidable for sufficiently expressive programs. A standard reduction relates equivalence to the halting problem: compare a program that loops forever with one that simulates a chosen machine on a chosen input and halts only if that simulation halts. Deciding equivalence would decide the halting problem.

Practical tools therefore restrict the language and input domain, use bounded execution, differential testing, static analysis, and/or bounded symbolic execution. Their conclusions must state their scope.

## Run

Requires Python 3.10 or later. No third-party packages are required.

```bash
python -m unittest discover -s tests -v
python examples/demo.py
```

## Repository structure

- `compiler_checker/source_interpreter.py` – reference semantics for the source language.
- `compiler_checker/compiler.py` – translates expressions into stack-machine instructions and executes them.
- `compiler_checker/validator.py` – compares source and compiled observations over selected test inputs.
- `compiler_checker/equivalence.py` – compares observable results.
- `compiler_checker/computability.py` – short theory notes.
- `examples/` – correct and deliberately faulty compilation demonstrations.
- `tests/` – automated unit tests.
- `CONTRIBUTIONS.md` – individual contribution statements.

## Limitations

This is an educational prototype, not a production compiler verifier. It supports integer constants, variables, unary minus, addition, subtraction, and multiplication. It does not model loops, functions, pointers, I/O, concurrency, undefined behavior, or machine-width overflow. Conclusions apply only to this model and tested inputs.

## References

1. Michael Sipser, *Introduction to the Theory of Computation*.
2. John E. Hopcroft, Rajeev Motwani, and Jeffrey D. Ullman, *Introduction to Automata Theory, Languages, and Computation*.
3. Alfred V. Aho et al., *Compilers: Principles, Techniques, and Tools*.
