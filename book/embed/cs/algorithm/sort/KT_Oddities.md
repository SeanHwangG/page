{% tabs %}
{% tab title='KT_Oddities.md' %}

* n 이 짝수이면 n is even 홀수이면 n is odd 라고 출력하라.

{% endtab %}
{% tab title='KT_Oddities.py' %}

```py
n_test = int(input())
for _ in range(n_test):
  n = int(input())
  if n % 2 == 0:
    print(f"{n} is even")
  else:
    print(f"{n} is odd")
```

{% endtab %}
{% endtabs %}