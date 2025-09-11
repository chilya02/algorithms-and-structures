import time
import matplotlib.pyplot as plt
from circdeque import CircularDeque

def benchmark_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        return execution_time
    return wrapper

@benchmark_decorator
def push_front_operations(size):
    deque = CircularDeque(size, True)
    for _ in range(size):
        deque.push_front(52)

@benchmark_decorator
def push_back_operations(size):
    deque = CircularDeque(size, True)
    for _ in range(size):
        deque.push_back(52)

@benchmark_decorator
def pop_front_operations(size):
    deque = CircularDeque(size, True)
    for _ in range(size):
        deque.push_back(52)

@benchmark_decorator
def pop_front_operations_on_deque(size, deque):
    for _ in range(size):
        deque.pop_front()
    return pop_front_operations_on_deque(size, deque)

@benchmark_decorator
def pop_back_operations(size):
    deque = CircularDeque(size, True)
    for _ in range(size):
        deque.push_back(52)

@benchmark_decorator
def pop_back_operations_on_deque(size, deque):
    for _ in range(size):
        deque.pop_back()
    return pop_back_operations_on_deque(size, deque)

@benchmark_decorator
def mixed_operations(size):
    deque = CircularDeque(size, True)
    for i in range(size):
        if i % 4 == 0:
            deque.push_front(i)
        elif i % 4 == 1:
            deque.push_back(i)
        elif i % 4 == 2 and not deque.empty():
            deque.pop_front()
        elif not deque.empty():
            deque.pop_back()

def run_benchmarks():
    sizes = [2**10, 2**12, 2**14, 2**16, 2**18, 2**20, 2**22]
    operations = {
        'push_front': push_front_operations,
        'push_back': push_back_operations,
        'pop_front': pop_front_operations,
        'pop_back': pop_back_operations,
        'mixed': mixed_operations
    }

    bench_results = {op: {'sizes': [], 'times': []} for op in operations}
    print("=== Running CircularDeque Benchmarks ===\n")
    for size in sizes:
        print(f"Testing size : {size:<8} elements")
        for op_name, op_func in operations.items():
            execution_time = op_func(size)
            bench_results[op_name]['sizes'].append(size)
            bench_results[op_name]['times'].append(execution_time)
            print(f" {op_name:11}: {execution_time:} seconds")
    return bench_results

def plot_results(results):
    fig1, ax1 = plt.subplots(figsize=(10, 6))
    fig2, ax2 = plt.subplots(figsize=(10, 6))

    for op_name, data in results.items():
        ax1.plot(data['sizes'], data['times'], 'o-', label=op_name, markersize=6, linewidth=2)
    ax1.set_xlabel('Размер дека')
    ax1.set_ylabel('Время выполнения (секунды)')
    ax1.set_title('Время выполнения операций в зависимости от размера дека')
    ax1.set_xscale('log')
    ax1.set_yscale('log')
    ax1.legend()
    ax1.grid(True, linestyle='--', alpha=0.7)
    fig1.savefig('all_operations_comparison.png', bbox_inches='tight', dpi=600)

    for op_name, data in results.items():
        times_per_op = [(time_val / size) * 10**6 for time_val, size in zip(data['times'], data['sizes'])]
        ax2.plot(data['sizes'], times_per_op, 'o-', label=op_name, markersize=4, linewidth=2)
    ax2.set_xlabel('Размер дека')
    ax2.set_ylabel('Время выполнения одной операции (микросекунды)')
    ax2.set_title('Анализ времени выполнения операций')
    ax2.set_xscale('log')
    ax2.legend()
    ax2.grid(True, linestyle='--', alpha=0.7)
    fig2.savefig('time_per_operation_analysis.png', bbox_inches='tight', dpi=600)
    plt.show()
    plt.close(fig1)
    plt.close(fig2)

if __name__ == "__main__":
    res = run_benchmarks()
    plot_results(res)
