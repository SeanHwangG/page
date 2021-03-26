{% tabs %}
{% tab title='KT_licensetolaunch.md' %}

* N개의 숫자가 주어질 때 최소인 index를 출력하라

{% endtab %}
{% tab title='KT_licensetolaunch.py' %}

```py
N = int(input())
mn, mn_idx = float('inf'), -1
for i, e in enumerate(map(int, input().split())):
  if e < mn:
    mn_idx = i
    mn = e
print(mn_idx)
```

{% endtab %}
{% endtabs %}