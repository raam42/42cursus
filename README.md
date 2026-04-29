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
