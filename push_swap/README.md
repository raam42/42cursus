_This project has been created as part of the 42 curriculum by roandres, rodrigoa._

# push_swap

### Description

This repository contains our implementation of **push_swap**, a 42 group project focused on algorithmic thinking and optimization.  
The goal is to sort a list of integers using:
- two stacks (a and b)
- a restricted set of operations (sa, pb, ra, etc.)

The program outputs a sequence of valid push_swap operations that sorts stack **a** in ascending order while aiming to minimise the number of operations.

In this version of the project, we implement multiple strategies with different complexity classes and an **adaptive strategy** driven by a mandatory **disorder index**.

---

### Instructions

#### Downloading the project

Clone the repository:

```bash
git clone <repository_url>
cd <repository_name>
````

#### Compilation

Requirements:

*   cc (or clang)
*   make

Compile:

```bash
make
```

This builds the executable:

```bash
./push_swap
```

#### Execution

##### Basic usage

The first argument is the top of stack **a**:

```bash
./push_swap 2 1 3 6 5 8
```

##### Strategy selection flags

If no strategy flag is provided, the program runs in `--adaptive` mode by default.

```bash
./push_swap --simple 2 1 3 6 5 8
./push_swap --medium 2 1 3 6 5 8
./push_swap --complex 2 1 3 6 5 8
./push_swap --adaptive 2 1 3 6 5 8
```

##### Benchmark mode (`--bench`)

`--bench` prints extra metrics to **stderr** while the operations remain in **stdout**.

Example (count operations via stdout):

```bash
ARG="4 67 3 87 23"
./push_swap --bench --adaptive $ARG | wc -l
```

Example (validate correctness with checker):

```bash
ARG="4 67 3 87 23"
./push_swap --medium $ARG | ./checker_linux $ARG
```

#### Cleaning

Remove object files:

```bash
make clean
```

Remove all compiled files (including the binary):

```bash
make fclean
```

Rebuild:

```bash
make re
```

***

### Algorithms

#### Allowed operations (push\_swap model)

Our strategies generate sequences of the allowed operations:

    sa sb ss pa pb ra rb rr rra rrb rrr

All complexity discussions in this project are expressed in terms of the **number of push\_swap operations produced**, as required by the subject.

***

#### Mandatory: Disorder index (`compute_disorder`)

Before performing any move, we compute a disorder index in the range **\[0, 1]**.

It measures how far the initial stack is from being sorted by counting out-of-order pairs `(i, j)` such that `i < j` but `a[i] > a[j]`.

This metric is used by the adaptive strategy and is also displayed in benchmark mode.

***

#### Strategy 1 — Simple (O(n²))

**Goal:** provide a correct baseline algorithm in the O(n²) class (push\_swap model).  
**Implementation idea:** selection‑like approach (extract min/max by rotations and pushes).  
**Flag:** `--simple`

This quadratic strategy is executed **only when explicitly selected** and is **not used by the adaptive strategy**.

***

#### Strategy 2 — Medium (O(n√n))

**Goal:** improve operation count on medium‑sized inputs.  
**Implementation idea:** chunk / range‑based approach using node indices (`set_node_index`), pushing ranges from **a** to **b**, then restoring **a** by retrieving maximum indices efficiently.  
**Flag:** `--medium`

***

#### Strategy 3 — Complex (O(n log n))

**Goal:** provide an O(n log n) strategy for large inputs.  
**Implementation:** radix sort (LSD) based on node indices, implemented exclusively using push\_swap operations.  
**Flag:** `--complex`

***

#### Strategy 4 — Adaptive (custom)

**Flag:** `--adaptive` (default)

The adaptive strategy selects an internal algorithm depending on the disorder index:

*   **Low disorder:** disorder < 0.2 → uses a dedicated **Linear strategy (O(n))**
*   **Medium disorder:** 0.2 ≤ disorder < 0.5 → uses the Medium strategy
*   **High disorder:** disorder ≥ 0.5 → uses the Complex strategy

##### Linear strategy (O(n))

For nearly sorted inputs, the adaptive strategy uses a dedicated **linear‑time algorithm**, distinct from the quadratic `--simple` strategy.

This algorithm performs a bounded number of single‑pass traversals over stack **a**, correcting only local inversions using swap and rotation operations. Stack **b** is not used in this case.

Because both the number of passes and corrective operations are strictly bounded, the total number of push\_swap operations grows linearly with respect to the input size.

If the input is found to be more disordered than expected for linear processing, the adaptive strategy safely falls back to the Medium strategy to guarantee correctness.

##### Threshold justification

*   0.2 and 0.5 were selected to separate inputs that are nearly sorted, partially disordered, and highly disordered.
*   These values were validated through benchmarking random and partially sorted distributions.

***

### Benchmark mode (`--bench`)

When `--bench` is enabled, after sorting we print to **stderr**:

*   Disorder index (percentage, two decimals)
*   **Actual strategy used and its complexity class**
*   Total number of operations
*   Count per operation type:
    *   sa sb ss pa pb ra rb rr rra rrb rrr

This mode does not change the operations emitted on stdout, so the output can still be piped into a checker.

***

### Project organisation

*   `inc/` headers
*   `src/` core logic (main, parsing, disorder, indexing, strategy dispatcher)
*   `src/moves/` allowed push\_swap operations
*   `utils/` helpers and sorting strategies
*   `libft/` local libft

***

### Resources

#### References

*   42 push\_swap subject
*   Big‑O notation references
*   Chunk‑based sorting strategies
*   Radix sorting in constrained models

#### Use of Artificial Intelligence

Artificial Intelligence was used strictly as a **supporting and learning tool** to:

*   clarify theoretical concepts (complexity, strategy design),
*   generate testing ideas and edge cases,
*   assist with documentation drafting.

All final code was reviewed, understood, and validated by both team members.
*   42 push\_swap subject
*   Algorithm complexity analysis (Big‑O)
*   Chunk‑based sorting strategies
*   Radix sorting on constrained models
