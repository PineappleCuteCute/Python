def calculate_hash(s, m):
    k = len(s)
    hash_code = 0
    for i in range(k):
        hash_code = (hash_code * 256 + ord(s[i])) % m
    return hash_code

n, m = map(int, input().split())

for _ in range(n):
    s = input().strip()
    hash_code = calculate_hash(s, m)
    print(hash_code)
    print()
