{% tabs %}
{% tab title='KT_lostlineup.md' %}

* 첫 줄에 사람 수 N이 주어진다.
* 1은 항상 줄 앞에 선다.
* 둘째 줄에 2 .. N과 1과의 거리가 주어진다.
* 이때 원래 줄을 순서를 출력하라.

{% endtab %}
{% tab title='KT_lostlineup.py' %}

```py
n = int(input())
ret = [1] * n
li = list(map(int, input().split()))
for i, n in enumerate(li):
    ret[n + 1] = i + 2
print(*ret)
```

{% endtab %}
{% endtabs %}