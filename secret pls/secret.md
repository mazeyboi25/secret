# 1. Which concurrency tool did you use?
# threading

# 2. Why did you select this approach?
# Threading is simple and works well for tasks with waiting time like simulated delays.

# 3. Is your program using task parallelism or data parallelism?
# Task parallelism because different tasks (orders) run at the same time.

# 4. Is this example primarily CPU-bound or I/O-bound?
# I/O-bound because the program mostly waits (time.sleep).

# 5. How does the simulated delay (time.sleep) represent real-world system behavior?
# It simulates waiting time for operations like payment verification or packaging.

# 6. Explain how processing orders concurrently improves system performance.
# Multiple orders are processed at the same time instead of waiting for one to finish first.

# 7. If the system needed to process thousands of orders, what improvement could be made?
# Use a thread pool or multiprocessing to better manage large numbers of tasks.
