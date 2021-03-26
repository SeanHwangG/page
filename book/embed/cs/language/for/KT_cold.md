{% tabs %}
{% tab title='KT_cold.md' %}

* 첫줄에는 N이, 그 다음 줄에는 N개의 숫자가 주어진다.
* N개의 수 중 0보다 작은 수를 출력하라.

{% endtab %}
{% tab title='KT_cold.py' %}

```py
N = int(input())
count = 0
for n in map(int, input().split()):
  if n < 0:
    count += 1
print(count)
```

{% endtab %}
{% endtabs %}