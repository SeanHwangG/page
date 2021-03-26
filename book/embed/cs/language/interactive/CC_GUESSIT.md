{% tabs %}
{% tab title='CC_COOK127B.md' %}

* guess random square number under 1e6

{% endtab %}
{% tab title='CC_COOK127B.py' %}

```py
import sys
for _ in range(int(input())):
  for n in range(1, int(1e3) + 1):
    print(n ** 2)
    sys.stdout.flush()
    ret = int(input())
    if ret == -1:
      exit()
    elif ret == 1:
      break
```

{% endtab %}
{% endtabs %}