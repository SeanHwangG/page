{% tabs %}
{% tab title='KT_parking.md' %}

* 직선으로 되어있는 시장에서 모든 n개의 가게에서 장을 본다.
* 이때 총 이동거리를 최소화 시키는 시작점에서 모든 장을 보고 돌아오는 데까지 걸리는 거리를 출력하라.

{% endtab %}
{% tab title='KT_parking.py' %}

```py
n_test = int(input())
for i in range(n_test):
  N = int(input())
  li = list(map(int, input().split()))
  print((max(li) - min(li)) * 2)
```

{% endtab %}
{% endtabs %}