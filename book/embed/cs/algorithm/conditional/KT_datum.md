{% tabs %}
{% tab title='KT_datum.md' %}

* 정수 m, d가 주어진다.
* 2009년 m월 d일이 무슨 요일인지 출력하라.

{% endtab %}
{% tab title='KT_datum.py' %}

```py
n_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
weeks = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
day, month = map(int, input().split())
nth = sum(n_days[:month - 1]) + day - 1
print(weeks[(nth + 3) % 7])
```

{% endtab %}
{% endtabs %}