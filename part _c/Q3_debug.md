# Bug Analysis

```python
score = 85

if score >= 60:
    grade = 'D'
if score >= 70:
    grade = 'C'
if score >= 80:
    grade = 'B'
if score >= 90:
    grade = 'A'

print(grade)
```

## What is the bug?
The program uses multiple `if` statements instead of `elif`.

## Why does this give the wrong output?
All conditions are checked sequentially. For score = 85:
- 60 condition → True → grade = D
- 70 condition → True → grade = C
- 80 condition → True → grade = B

Final grade becomes **B**.

## Correct fix
```python
score = 85

if score >= 90:
    grade = 'A'
elif score >= 80:
    grade = 'B'
elif score >= 70:
    grade = 'C'
elif score >= 60:
    grade = 'D'

print(grade)
```