{% tabs %}
{% tab title='HR_text-processing-sed-2.md' %}

* transform all the occurrences of the word 'thy' with 'your'

{% endtab %}
{% tab title='HR_text-processing-sed-2.sh' %}

```sh
# g : global
# i : insensitive
sed 's/thy/your/ig'
```

{% endtab %}
{% endtabs %}