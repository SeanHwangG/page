{% tabs %}
{% tab title='KT_lineup.md' %}

* 첫줄에 N 그 다음 N 줄에 사람 이름이 주어진다.
* 이 때 사람 이름이 알파벳 순서 일시 INCREASING,
* 알파벳 역순 일시 DECREASING, 둘 다 아니면 NEITHER을 출력하라.

{% endtab %}
{% tab title='KT_lineup.py' %}

```py
n = int(input())
li = []
for _ in range(n):
  li.append(input())
if li == sorted(li):
  print("INCREASING")
elif li == sorted(li, reverse=True):
  print('DECREASING')
else:
  print('NEITHER')
```

{% endtab %}
{% endtabs %}