# 🌀 Day 37 - Rotate a Matrix by 90 Degrees Anti-Clockwise
## 🔍 Problem Statement:
Given a square matrix mat[][] of size n x n, rotate it 90 degrees anti-clockwise without using any extra space.

## 🧠 Approach:
#### We use two-step in-place transformation:
1. Transpose the matrix
- Swap mat[i][j] with mat[j][i]. This reflects elements across the main diagonal.

2. Reverse each column
- Swap top and bottom elements of each column to rotate the matrix 90° anti-clockwise.

## 📈 Complexity:
- Time Complexity: O(n²)

- Space Complexity: O(1) (In-place)

## 📌 Concepts Practiced:
- Matrix Transposition

- In-place Reversal

- 2D Array Manipulation

## 📚 Tags:
Matrix In-place Rotation 2D Arrays Coding Challenge Python Interview Problem
