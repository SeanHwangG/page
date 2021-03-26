{% tabs %}
{% tab title='HR_saying-hi.md' %}

* The first character must be the letter H or h.
* The second character must be the letter I or i.
* The third character must be a single space.
* The fourth character must not be the letter D or d.

{% endtab %}
{% tab title='HR_saying-hi.py' %}

```py
import re
regex = r"^[Hh][Ii]\s[^Dd]"
n= int(input())
for _ in range(n):
  s = input()
  res = re.match(regex,s)
  if res:
    print(s)
  else:
    pass
```

{% endtab %}
{% endtabs %}