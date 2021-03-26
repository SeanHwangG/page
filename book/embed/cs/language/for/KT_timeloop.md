{% tabs %}
{% tab title='KT_timeloop.md' %}

* 첫 줄에는 N이 주어진다
* 다음 N줄에
* 1 Abracadabra … N Abracadabra 을 출력하라

{% endtab %}
{% tab title='KT_timeloop.py' %}

```py
n_line = int(input())
for i in range(1, n_line + 1):
  print(f"{i} Abracadabra")
```

{% endtab %}
{% endtabs %}