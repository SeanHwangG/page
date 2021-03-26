{% tabs %}
{% tab title='HR_capturing-non-capturing-groups.md' %}

* should have or more consecutive repetitions of ok.

{% endtab %}
{% tab title='HR_capturing-non-capturing-groups.py' %}

```py
import re
pattern = r'(ok){3,}'
print(str(bool(re.search(pattern, input()))).lower())
```

{% endtab %}
{% endtabs %}