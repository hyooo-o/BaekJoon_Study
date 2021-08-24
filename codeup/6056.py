a, b = input().split()
_a = bool(int(a))
_b = bool(int(b))
print((_a and not _b) or (not _a and _b))