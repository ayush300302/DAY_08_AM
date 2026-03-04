# Difference Between `elif` and Multiple `if`

## Explanation
`elif` is used when conditions are mutually exclusive. Once one condition becomes true, the remaining conditions are skipped.
Multiple `if` statements evaluate every condition independently.

## Example

Input:
score = 85

### Using multiple if
```python
score = 85

if score >= 60:
    print("D")
if score >= 70:
    print("C")
if score >= 80:
    print("B")
```

Output:
D
C
B

### Using elif
```python
score = 85

if score >= 60:
    print("D")
elif score >= 70:
    print("C")
elif score >= 80:
    print("B")
```

Output:
D

## Why the difference happens
In multiple `if` statements every condition is checked even if a previous one is true.
In `elif`, once a condition becomes true, the remaining conditions are skipped.