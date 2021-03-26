{% tabs %}
{% tab title='KT_harshadnumbers.md' %}

* harshad 수는 각 자리 수를 다 더한 수로 나누어 떨어지는 수이다.
* n이 주어질 때 n보다 크거나 같은 가장 작은 harshad 수를 출력하라.

{% endtab %}
{% tab title='KT_harshadnumbers.py' %}

```py
def is_harshad(num):
  digit_sum = 0
  cur = num
  while cur != 0:
    digit_sum += cur % 10
    cur //= 10
  return num % digit_sum == 0
n = int(input())
while True:
  if is_harshad(n):
    print(n)
    break
  n = n + 1
```

{% endtab %}
{% endtabs %}