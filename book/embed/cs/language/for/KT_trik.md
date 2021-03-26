{% tabs %}
{% tab title='KT_trik.md' %}

* 처음에는 1번에 구슬이 놓여있고 ABC는 위와 같이 정의 된다.
* 주어진 인풋과 같이 돌을 옮겼을때 최종적인 돌의 위치를 출력하라.

{% endtab %}
{% tab title='KT_trik.py' %}

```py
moves = input()
cur = 1
for move in moves:
  if move == 'A':
    if cur == 1:
      cur = 2
    elif cur == 2:
      cur = 1
  elif move == 'B':
    if cur == 2:
      cur = 3
    elif cur == 3:
      cur = 2
  else:
    if cur == 1:
      cur = 3
    elif cur == 3:
      cur = 1
print(cur)
```

{% endtab %}
{% endtabs %}