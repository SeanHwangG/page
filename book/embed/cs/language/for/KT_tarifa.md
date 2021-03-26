{% tabs %}
{% tab title='KT_tarifa.md' %}

* 첫 줄에는 데이터 한도(한 달에 사용 가능 한 데이터), 두번째 줄에는 N이 주어진다.
* 각 N줄에는 각 달에 사용한 데이터 량이 주어지는데, 이 때 한도보다 적게 쓸 시 다음달로 이월된다.
* 이때 N + 1번째 달에 사용할 수 있는 데이터 양을 출력하라.

{% endtab %}
{% tab title='KT_tarifa.py' %}

```py
add = int(input())
n_line = int(input())
cur = 0
for n in range(n_line):
  cur += add
  cur = max(0, cur - int(input()))
print(cur + add)
```

{% endtab %}
{% endtabs %}