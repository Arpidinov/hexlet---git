
# a = 97
# z = 122
a = int(input())
ans = []
for x in range(a):
  b = input()
  for y in range(len(b) - 1):
    if (b[y] == 'z' and b[y + 1] == 'a') or ord(b[y]) + 1 == ord(b[y + 1]) or ord(b[y]) + 1 == ord(b[y + 1]):
      ans.append('YES')
      break
    else:
      ans.append('NO')
      break
for x in ans:
  print(x)
