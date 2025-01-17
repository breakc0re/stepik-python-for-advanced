def chunked(text, n):
    return [text[i:i+n] for i in range(0, len(text), n)]


text = input().split()
n = int(input())

result = chunked(text, n)
print(result)
