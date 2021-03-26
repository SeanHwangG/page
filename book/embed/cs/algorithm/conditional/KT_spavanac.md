{% tabs %}
{% tab title='KT_spavanac.md' %}

* 아침에 일찍 일어나고자 알람을 45분 일찍 맞춘다.
* h, m이 주어지면 맞춰야 되는 알람시간 h, m을 출력하라.

{% endtab %}
{% tab title='KT_spavanac.py' %}

```py
h, m = map(int, input().split())
total = h * 60 + m - 45
if total < 0:
  total += 1440
print(total // 60, total % 60)
```

{% endtab %}
{% endtabs %}