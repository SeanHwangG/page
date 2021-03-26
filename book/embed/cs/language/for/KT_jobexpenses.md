{% tabs %}
{% tab title='KT_jobexpenses.md' %}

* 첫줄에 N이 주어진다.
* 다음 줄에 N개의 숫자가 주어지는데, 이 때 0보다 작은 수의 절대값의 합을 구하여라.

{% endtab %}
{% tab titlepyT_jobexpenses.md'' %}

```py
N = int(input())
ret = 0
for a in map(int, input().split()):
  if a < 0:
    ret -= a
print(ret)
```

{% endtab %}
{% endtabs %}