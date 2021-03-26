{% tabs %}
{% tab title='KT_zamka.md' %}

* determine the minimal integer 𝑁 such that 𝐿≤𝑁≤𝐷 and the sum of its digits is 𝑋
* determine the maximal integer 𝑀 such that 𝐿≤𝑀≤𝐷 and the sum of its digits is 𝑋

{% endtab %}
{% tab title='KT_zamka.py' %}

```py
mn = int(input())
mx = int(input())
sm = int(input())
def match(n, sm):
  while n != 0:
    sm -= n % 10
    n //= 10
  return sm == 0
for i in range(mn, mx + 1):
  if match(i, sm):
    print(i)
    break
for i in range(mx, mn - 1, -1):
  if match(i, sm):
    print(i)
    break
```

{% endtab %}
{% endtabs %}