# Matrix Multiplication with Test Suite (Python)

This project implements matrix multiplication in Python along with a comprehensive automated test suite using pytest. It focuses on correctness, robustness, and validation of edge cases.

## Features
- Matrix multiplication for arbitrary dimensions
- Input validation and error handling
- Automated testing using pytest
- Scoring system based on test case performance

## Files
- `matmul.py` → implementation of matrix multiplication
- `test_matmul.py` → test suite with multiple test cases and scoring system

## Test Coverage
The test suite validates multiple scenarios:

- Basic matrix multiplication (2x2)
- Different compatible dimensions
- Single element matrices (1x1)
- Larger matrices with identity behavior
- Zero matrix multiplication
- Incompatible dimensions (error handling)
- Empty matrix inputs
- Non-numeric input handling

## Example Test Case
```python
matrix1 = [[1, 2], [3, 4]]
matrix2 = [[5, 6], [7, 8]]

# Expected Output
[[19, 22], [43, 50]]
