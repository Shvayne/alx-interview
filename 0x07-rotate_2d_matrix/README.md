### 0x07-Rotate 2D Matrix

## Overview
This project implements an in-place algorithm to rotate an n x n 2D matrix 90 degrees clockwise.

## Features
- Rotate square matrices of any size
- O(n²) time complexity
- O(1) space complexity
- Modifies matrix directly without creating a copy

## Usage
```python
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
rotate_2d_matrix(matrix)
print(matrix)  # Output: [[7, 4, 1], [8, 5, 2], [9, 6, 3]]
```

## Rotation Algorithm
1. Transpose the matrix
2. Reverse each row