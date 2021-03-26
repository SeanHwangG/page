{% tabs %}
{% tab title='KT_sodaslurper.md' %}

* 첫 줄에 e, f, c 가 주어진다.
* e와 f 를 합치면 가지고 있는 총 빈 병의 개수가 나오고,
* 병을 c개 가지고 오면 꽉 찬 음료수를 받을 수 있다. 이 때 총 마실 수 있는 음료수의 수를 출력하라.

{% endtab %}
{% tab title='KT_sodaslurper.py' %}

```py
e, f, c = map(int, input().split())
e += f
ret = 0
while e >= c:
  ret += e // c
  e = e % c + e // c

print(ret)
```

{% endtab %}
{% endtabs %}