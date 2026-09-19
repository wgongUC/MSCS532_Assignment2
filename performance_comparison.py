# Name: Weevern Gong
# Project Title: MSCS532_Assignment2
# Description: This program compares the performance of Merge Sort and Quick Sort using sorted, reverse-sorted, and random data.
# The program records the median execution time and peak traced memory usage for each algorithm and saves the results to a CSV file.

# Performance comparison explanation: This program tests both sorting algorithms with input sizes of 100, 300, and 600 elements.
# For each input size, the same values are arranged in sorted, reverse-sorted, and random order so that the effect of input order
# can be compared without changing the values being sorted. Each execution-time test is run five times, and the median time
# is recorded to reduce the effect of small timing differences between runs.
# Peak memory usage is measured separately with Python's tracemalloc module so that memory tracing does not affect the timing results.
# The program also checks each sorted result against Python's expected ascending order before recording the measurement.
# The completed performance results are displayed in the terminal and saved to results.csv.

import csv
import random
import statistics
import time
import tracemalloc

from merge_sort import merge_sort
from quick_sort import quick_sort


INPUT_SIZES = [100, 300, 600]
NUMBER_OF_TRIALS = 5
RANDOM_SEED = 532
OUTPUT_FILE = "results.csv"


def create_datasets(size, random_generator):

    # Create the same values in sorted order
    sorted_arr = list(range(size))

    # Create the same values in reverse-sorted order
    reverse_sorted_arr = list(reversed(sorted_arr))

    # Create the same values in random order
    random_arr = sorted_arr.copy()
    random_generator.shuffle(random_arr)

    return {
        "Sorted": sorted_arr,
        "Reverse Sorted": reverse_sorted_arr,
        "Random": random_arr,
    }


def verify_sorted_result(original_arr, sorted_arr):

    # Compare the algorithm result with Python's expected ascending order
    expected_arr = sorted(original_arr)

    if sorted_arr != expected_arr:
        raise ValueError("The sorting algorithm produced an incorrect result.")


def measure_execution_time(sort_function, input_arr):

    execution_times = []

    # Run the same test several times and record each execution time
    for i in range(NUMBER_OF_TRIALS):
        test_arr = input_arr.copy()

        start_time = time.perf_counter()
        sort_function(test_arr)
        end_time = time.perf_counter()

        verify_sorted_result(input_arr, test_arr)

        execution_time_ms = (end_time - start_time) * 1000
        execution_times.append(execution_time_ms)

    # Use the median execution time so one unusually fast or slow run has less effect
    return statistics.median(execution_times)


def measure_peak_memory(sort_function, input_arr):

    # Copy the input before memory tracing starts so the measurement focuses on the sorting algorithm
    test_arr = input_arr.copy()

    tracemalloc.start()

    sort_function(test_arr)

    current_memory, peak_memory = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    verify_sorted_result(input_arr, test_arr)

    # Convert peak traced memory from bytes to kibibytes
    return peak_memory / 1024


def run_performance_comparison():

    algorithms = {
        "Merge Sort": merge_sort,
        "Quick Sort": quick_sort,
    }

    random_generator = random.Random(RANDOM_SEED)
    results = []

    # Test each required input size
    for size in INPUT_SIZES:
        datasets = create_datasets(size, random_generator)

        # Test sorted, reverse-sorted, and random data for each size
        for dataset_name, input_arr in datasets.items():

            # Run both algorithms on the same input arrangement
            for algorithm_name, sort_function in algorithms.items():

                median_time_ms = measure_execution_time(sort_function, input_arr)
                peak_memory_kib = measure_peak_memory(sort_function, input_arr)

                results.append(
                    {
                        "Algorithm": algorithm_name,
                        "Dataset": dataset_name,
                        "Input Size": size,
                        "Median Execution Time (ms)": round(median_time_ms, 6),
                        "Peak Traced Memory (KiB)": round(peak_memory_kib, 3),
                    }
                )

    return results


def save_results(results):

    column_names = [
        "Algorithm",
        "Dataset",
        "Input Size",
        "Median Execution Time (ms)",
        "Peak Traced Memory (KiB)",
    ]

    # Write all performance results to results.csv
    with open(OUTPUT_FILE, "w", newline="", encoding="utf-8") as results_file:
        writer = csv.DictWriter(results_file, fieldnames=column_names)
        writer.writeheader()
        writer.writerows(results)


def print_results(results):

    # Print column headings for the performance results
    print(
        f"{'Algorithm':<12}"
        f"{'Dataset':<16}"
        f"{'Input Size':>12}"
        f"{'Median Time (ms)':>20}"
        f"{'Peak Traced Memory (KiB)':>25}"
    )

    print("-" * 85)

    # Print one row for each performance result
    for result in results:
        print(
            f"{result['Algorithm']:<12}"
            f"{result['Dataset']:<16}"
            f"{result['Input Size']:>12}"
            f"{result['Median Execution Time (ms)']:>20.6f}"
            f"{result['Peak Traced Memory (KiB)']:>25.3f}"
        )


def main():

    results = run_performance_comparison()

    print_results(results)

    save_results(results)

    print("\nPerformance comparison results saved to results.csv")


if __name__ == "__main__":
    main()
