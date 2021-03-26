{% tabs %}
{% tab title='HR_matching-ending-items.md' %}

* should consist of only lowercase and uppercase letters (no numbers or symbols).
* should end in s.

{% endtab %}
{% tab title='HR_matching-ending-items.py' %}

```py
import re
pattern = r'^[a-zA-Z]*s$'	# Do not delete 'r'.
print(str(bool(re.search(pattern, input()))).lower())
```

{% endtab %}
{% endtabs %}