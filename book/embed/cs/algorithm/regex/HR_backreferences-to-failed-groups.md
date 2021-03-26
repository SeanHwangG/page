{% tabs %}
{% tab title='HR_backreferences-to-failed-groups.md' %}

* consists of 8 digits.
* - separator such that string S gets divided in 4 parts, with each part having exactly two digits

{% endtab %}
{% tab title='HR_backreferences-to-failed-groups.py' %}

```py
pattern = r"^((\d{8})|(\d{2}-\d{2}-\d{2}-\d{2}))$"
import re
print(str(bool(re.search(pattern, input()))).lower())
```

{% endtab %}
{% endtabs %}