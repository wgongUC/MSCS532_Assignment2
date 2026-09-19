# MSCS532_Assignment2 by Weevern Gong

## Description
This project implements the Merge Sort and Quick Sort divide-and-conquer algorithms using Python. Both programs sort a list of integers in monotonically increasing order, from smallest to largest. A performance comparison program tests both algorithms using sorted, reverse-sorted, and random data and records execution time and peak Python-traced memory.

## Requirements
- Python 3.8 or higher
- Visual Studio Code or alternate IDE
- Python extension for Visual Studio Code
- Git (to clone repository)
- GitHub account (to fork repository to own GitHub account, etc.)
- Code Runner extension (optional requirement)

## Instructions
1. Go to the GitHub repository at https://github.com/wgongUC/MSCS532_Assignment2

2. Select either option 1 or option 2:

Option 1: Download ZIP File
- Click on the green button "Code" and select "Download ZIP".
- Extract the downloaded ZIP file, then open Visual Studio Code and select File > Open Folder.
- Select the folder containing merge_sort.py, quick_sort.py, and performance_comparison.py.

Option 2: Clone with Git
- Click on the green button "Code", and select the HTTPS tab. Click "Copy URL to clipboard" on the right to copy the URL https://github.com/wgongUC/MSCS532_Assignment2.git.
- In Windows, open a terminal window and run this command:
    ```bash
    git clone https://github.com/wgongUC/MSCS532_Assignment2.git
    ```
- A new project folder will be created in the current terminal location.
- In Visual Studio Code, select File > Open Folder and select the project folder that was created.

3. To run the Merge Sort program in Visual Studio Code, select Terminal > New Terminal and run the following command:
    ```bash
    python merge_sort.py
    ```

4. To run the Quick Sort program, run the following command:
    ```bash
    python quick_sort.py
    ```

The terminal will display the input list and the list sorted in monotonically increasing order.

5. To run the performance comparison, run the following command:
    ```bash
    python performance_comparison.py
    ```

The performance comparison tests sorted, reverse-sorted, and random inputs containing 100, 300, and 600 elements. Each execution-time test is run five times and the median is recorded. Peak Python-traced memory is measured separately. The complete results are displayed in the terminal and saved to results.csv.

6. To test Merge Sort or Quick Sort with custom inputs, edit the numbers in the numbers_arr array in merge_sort.py or quick_sort.py, then save the program file and run it.

## Example Input
[5, 2, 20, 9, 1, 5, 6, 3, 71, 8, 4, 56, 12]

## Example Output
[1, 2, 3, 4, 5, 5, 6, 8, 9, 12, 20, 56, 71]

## Time Complexity
Merge Sort has best-case, average-case, and worst-case time complexity of Θ(n log n).

Quick Sort has best-case and expected average-case time complexity of Θ(n log n). Its worst-case time complexity is Θ(n²).

## References
Bentley, J. L., & McIlroy, M. D. (1993). Engineering a sort function. *Software: Practice and Experience, 23*(11), 1249–1265. https://doi.org/10.1002/spe.4380231105

Hoare, C. A. R. (1962). Quicksort. *The Computer Journal, 5*(1), 10–16. https://doi.org/10.1093/comjnl/5.1.10

Katajainen, J., Pasanen, T., & Teuhola, J. (1996). Practical in-place mergesort. Nordic Journal of Computing, 3(1), 27–40. https://dl.acm.org/doi/10.5555/642136.642138
