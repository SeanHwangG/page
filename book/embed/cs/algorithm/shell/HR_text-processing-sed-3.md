{% tabs %}
{% tab title='HR_text-processing-sed-3.md' %}

* highlight all the occurrences of 'thy' by wrapping them up in brace brackets

{% endtab %}
{% tab title='HR_text-processing-sed-3.sh' %}

```sh
# & is captured group
sed -e 's/thy/{&}/gi'
```

{% endtab %}
{% endtabs %}