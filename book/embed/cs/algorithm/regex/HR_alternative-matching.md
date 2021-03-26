{% tabs %}
{% tab title='HR_alternative-matching.md' %}

* must start with Mr., Mrs., Ms., Dr. or Er..
* The rest of the string must contain only one or more English alphabetic letters (upper and lowercase).

{% endtab %}
{% tab title='HR_alternative-matching.py' %}

```py
import re
pattern = r'^(Mr|Mrs|Ms|Dr|Er)\.[A-Za-z]+$'	# Do not delete 'r'.

print(str(bool(re.search(pattern, input()))).lower())
```

{% endtab %}
{% endtabs %}