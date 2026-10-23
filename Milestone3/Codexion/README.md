*This project has been created as part of the 42 curriculum by rodrigoa.*

# Codexion

## Description
Codexion is a multi-threaded concurrency simulation built in C. The project models a shared co-working space where multiple coders must compete for limited resources (USB dongles) to compile their quantum code. The goal is to orchestrate these coders using POSIX threads, mutexes, condition variables, and smart scheduling algorithms (FIFO and Earliest Deadline First) to ensure fair resource allocation and prevent any coder from burning out before the simulation completes.

## Instructions

### Compilation
The project includes a `Makefile` that compiles the source code strictly with `-Wall -Wextra -Werror` and `-pthread`.

To compile the simulation, run:
```bash
make
```

### Execution
Run the executable with the following 8 mandatory arguments:
```bash
./codexion <number_of_coders> <time_to_burnout> <time_to_compile> <time_to_debug> <time_to_refactor> <number_of_compiles_required> <dongle_cooldown> <scheduler>
```

**Example:**
```bash
./codexion 5 800 200 200 200 5 100 edf
```

*   **number_of_coders:** Total coders (and total dongles).
*   **time_to_burnout (ms):** Maximum time a coder can go without starting a compilation before they burn out.
*   **time_to_compile (ms):** Duration of the compiling phase (requires holding 2 dongles).
*   **time_to_debug (ms):** Duration of the debugging phase.
*   **time_to_refactor (ms):** Duration of the refactoring phase.
*   **number_of_compiles_required:** The simulation successfully stops if all coders reach this quota.
*   **dongle_cooldown (ms):** Wait time required before a dropped dongle can be picked up again.
*   **scheduler:** Arbitration policy for the dongles (`fifo` or `edf`).

## Blocking cases handled

*   **Deadlock Prevention (Breaking Circular Wait):** If all coders reach for their left dongle simultaneously, the system freezes in a classic circular wait deadlock (The Dining Philosophers problem). This implementation breaks Coffman's symmetry by enforcing a strict lock hierarchy based on coder IDs. Even-numbered coders acquire their left dongle first, while odd-numbered coders acquire their right dongle first. This asymmetry guarantees at least one coder will be blocked on their first attempt, leaving a dongle free for a neighbor to successfully secure a matching pair.
*   **Starvation Prevention (Priority Queues):** Standard POSIX mutexes do not guarantee FIFO or priority-based access order. To prevent starvation—especially under the EDF (Earliest Deadline First) scheduler—each dongle maintains a dedicated Min-Heap priority queue. Coders push their request (timestamp or burnout deadline) into the heap and sleep until they sit at index `0` and the dongle becomes free.
*   **The "Lost Wakeup" Trap:** When the monitor thread halts the simulation due to a burnout or quota completion, coders suspended deep inside `pthread_cond_wait` will sleep forever, hanging the main thread's `pthread_join`. The monitor explicitly iterates through every dongle and issues a `pthread_cond_broadcast` during the shutdown sequence, forcefully waking all threads to evaluate the `simulation_active = 0` escape hatch and exit cleanly.
*   **Cooldown Enforcement:** To simulate hardware limits, dongles cannot be instantly re-acquired. Upon release, the dongle's `available_at` timestamp is pushed forward by `dongle_cooldown` milliseconds. Threads woken by a broadcast must verify this timestamp in their conditional acquisition loop; if the hardware is still cooling down, they immediately drop back to sleep.

## Thread synchronization mechanisms

*   **Dongle Isolation (`pthread_mutex_t` & `pthread_cond_t`):** Every shared dongle is isolated behind a dedicated mutex. This lock protects both the hardware's `is_held` binary state and the memory of its priority queue array. Instead of busy-waiting (which spikes CPU usage and disrupts the monitor's precision timing), coders suspend execution via `pthread_cond_wait`. They are exclusively woken by `pthread_cond_broadcast` when the previous owner drops the hardware or the cooldown expires.
*   **State Integrity (`state_lock`):** The monitor thread continuously scans the coders' `last_compile_start` timestamps to detect burnouts within a strict 10ms tolerance. If a coder updates this timestamp at the exact microsecond the monitor reads it, a data race corrupts the calculation. A centralized `state_lock` mutex temporarily freezes the simulation state during these read/write operations, guaranteeing the monitor always evaluates pristine data.
*   **Output Serialization (`write_lock`):** Terminal output is inherently thread-unsafe. If two coders transition states simultaneously, their `printf` buffers will interleave and garble the text. A dedicated `write_lock` mutex wraps every logging action, ensuring that each state change is printed atomically to standard output and guaranteeing clean execution logs.

## Resources

*   **POSIX Threads (pthreads) Documentation:** Standard reference for thread creation, joining, and mutex/condition variable management.
*   **Dijkstra's Dining Philosophers Problem:** Foundational computer science concepts regarding resource allocation and deadlock prevention.
*   **Min-Heap Array Architecture:** Algorithms for building priority queues using flattened arrays to manage scheduling.
*   **AI Usage:** AI was used during the development of this project as a conceptual sparring partner to structure the Min-Heap priority queue math, brainstorm deadlock prevention strategies (Even/Odd locking), and refine the precision timing loop of the monitor thread.