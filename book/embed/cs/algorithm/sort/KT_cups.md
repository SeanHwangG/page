{% tabs %}
{% tab title='KT_cups.md' %}

* n개 줄에 색 반지름 / 지름 색
* 둘 중 하나의 포맷으로 주어진다. 이 색들을 작은 반지름 순서대로 출력하라.

{% endtab %}
{% tab title='KT_cups.py' %}

```py
n_line = int(input())
li = []
for _ in range(n_line):
  a, b = input().split()
  if a.isdigit():
    li.append((int(a), b))
  else:
    li.append((int(b) * 2, a))
for _, color in sorted(li):
  print(color)
```

{% endtab %}
{% endtabs %}