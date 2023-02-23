from collections import deque

dq = deque(['a', 'b', 'c'])
print(dq)

dq.append('e')
print(dq)

x = dq.popleft()
print(dq)
print(x)