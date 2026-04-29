_This project has been created as part of the 42 curriculum by **roandres** and **rodrigoa**._

# push_swap

## Description

**push_swap** is a constrained sorting project from the 42 core curriculum.  
The goal is to sort a list of integers stored in **stack A**, using an empty auxiliary **stack B** and a **restricted set of operations**, while producing the **shortest possible sequence of valid push_swap instructions**.

This implementation focuses on:
- algorithmic reasoning,
- complexity analysis in a constrained model,
- and strategy selection based on the **initial disorder of the input**.

The project implements **four different strategies** with distinct complexity classes, including a mandatory **adaptive strategy** that selects the most appropriate internal algorithm at runtime.

---

## Allowed operations (push_swap model)

The program generates sequences made exclusively of the following operations:

- `sa` `sb` `ss`
- `pa` `pb`
- `ra` `rb` `rr`
- `rra` `rrb` `rrr`

All complexity analysis in this project is expressed in terms of the **number of push_swap operations produced**, as required by the subject.

---

## Compilation

Requirements:
- `cc` (or `clang`)
- `make`

Compile the project:

```bash
make
````

This produces the executable:

```bash
./push_swap
```

***

## Usage

### Basic usage

The first argument corresponds to the **top of stack A**:

```bash
./push_swap 2 1 3 6 5 8
```

The program prints, to **stdout**, the list of push\_swap operations required to sort stack A in ascending order.

***

## Strategy selection

If **no strategy flag** is provided, the program runs in **adaptive mode** by default.

You can explicitly force a strategy using the following flags:

```bash
./push_swap --simple   2 1 3 6 5 8
./push_swap --medium   2 1 3 6 5 8
./push_swap --complex  2 1 3 6 5 8
./push_swap --adaptive 2 1 3 6 5 8
```

Only one strategy flag may be provided. Using multiple or invalid flags results in an error.

***

## Benchmark mode (`--bench`)

When `--bench` is enabled, the program prints **additional metrics to `stderr`**, while keeping the push\_swap operations in `stdout` (so the output can still be piped into `checker`).

Metrics printed:

*   Disorder index (percentage, two decimals)
*   Total number of operations
*   Count per operation type (`sa`, `pb`, `ra`, etc.)

Example (count operations):

```bash
ARG="4 67 3 87 23"
./push_swap --bench --adaptive $ARG | wc -l
```

Example (validate correctness):

```bash
ARG="4 67 3 87 23"
./push_swap --medium $ARG | ./checker_linux $ARG
```

***

## Algorithms

### Mandatory preprocessing — Indexing

Each node is assigned an **index** representing its final sorted position (`0` to `n - 1`).
All sorting strategies operate on indices rather than raw values, allowing simpler comparisons and consistent behaviour across strategies.

***

### Mandatory metric — Disorder index

Before performing any move, the program computes a **disorder index** in the range **\[0.0, 1.0]**.

The disorder index represents the proportion of out‑of‑order pairs:

    mistakes / total_pairs,
    where a[i] > a[j] for i < j

*   `0.0` → already sorted
*   `1.0` → maximally disordered

This metric is used exclusively by the **adaptive strategy** and is also shown in benchmark mode.

***

## Strategy 1 — Simple (`O(n²)`)

**Flag:** `--simple`  
**Complexity (push\_swap model):** `O(n²)`

A selection‑style algorithm that repeatedly:

*   rotates stack A to bring the smallest index to the top,
*   pushes it to stack B,
*   and finally rebuilds stack A.

This strategy prioritises correctness and clarity and serves as a baseline.

***

## Strategy 2 — Medium (`O(n√n)`)

**Flag:** `--medium`  
**Complexity (push\_swap model):** `O(n√n)`

A chunk‑based algorithm:

*   the range of indices is divided into √n chunks,
*   elements are pushed from A to B by range,
*   the largest elements are efficiently restored from B to A.

This approach significantly reduces operations compared to quadratic methods on medium‑sized inputs.

***

## Strategy 3 — Complex (`O(n log n)`)

**Flag:** `--complex`  
**Complexity (push\_swap model):** `O(n log n)`

A **binary radix sort (LSD)** implemented **exclusively with push\_swap operations**:

*   each bit of the index is processed from least significant to most significant,
*   elements are distributed using `pb` / `ra`,
*   and restored using `pa`.

This strategy is designed for large and highly disordered inputs (e.g. 500+ numbers).

***

## Strategy 4 — Adaptive (default)

**Flag:** `--adaptive` (default)

The adaptive strategy selects an internal algorithm based on the disorder index:

| Disorder range | Strategy used | Complexity   |
| -------------- | ------------- | ------------ |
| `< 0.2`        | Simple        | `O(n)`       |
| `< 0.5`        | Medium        | `O(n√n)`     |
| `≥ 0.5`        | Complex       | `O(n log n)` |

### Threshold justification

*   **0.2** separates nearly sorted inputs, where linear corrections are sufficient.
*   **0.5** distinguishes moderately disordered data from highly random distributions.
*   These thresholds were chosen to balance operation count and algorithmic overhead.

The adaptive strategy performs **no sorting itself**; it only selects the appropriate strategy **once**, before any move is executed.

***

## Project structure

*   `main.c` — program entry point
*   `parser.c` — argument parsing and validation
*   `index.c` — index assignment
*   `disorder.c` — disorder metric computation
*   `strategy.c` — strategy selection (dispatcher)
*   `simple_sort.c` — `O(n²)` strategy
*   `medium_sort.c` — `O(n√n)` strategy
*   `complex_sort.c` — `O(n log n)` strategy (radix sort)
*   `pushing.c`, `swapping.c`, `rotating.c`, `rrotating.c` — allowed operations
*   `print_bench.c` — benchmark output
*   `libft/` — local libft dependency

***

## Team contributions

*   **roandres**: parsing, validation, disorder metric, indexing, medium strategy, dispatcher, benchmarking
*   **rodrigoa**: complex strategy design, optimisation, algorithm validation

***

## Use of Artificial Intelligence

Artificial Intelligence tools were used **only as a support**, for:

*   clarifying theoretical concepts (complexity, algorithm classes),
*   generating testing ideas and edge‑case scenarios,
*   helping structure and review documentation.

All code was fully reviewed, understood, and validated by both team members.

***

## Resources

*   42 push\_swap subject
*   Algorithm complexity analysis (Big‑O)
*   Chunk‑based sorting strategies
*   Radix sorting on constrained models

```

---

```
