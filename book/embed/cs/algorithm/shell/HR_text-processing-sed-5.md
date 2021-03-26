{% tabs %}
{% tab title='HR_text-processing-sed-5.md' %}

* reverse the ordering of segments in each credit card number

{% endtab %}
{% tab title='HR_text-processing-sed-5.sh' %}

```sh
sed -r 's/(.... )(.... )(.... )(....)/\4 \3\2\1/'
```

{% endtab %}
{% endtabs %}