{% tabs %}
{% tab title='HR_text-processing-tr-2.md' %}

* delete all the lowercase characters

{% endtab %}
{% tab title='HR_text-processing-tr-2.sh' %}

```sh
# tr -d [:lower:]
tr -d a-z
```

{% endtab %}
{% endtabs %}