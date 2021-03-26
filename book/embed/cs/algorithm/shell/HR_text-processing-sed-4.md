{% tabs %}
{% tab title='HR_text-processing-sed-4.md' %}

* Each line contains a credit card number in the form dddd dddd dddd dddd
* mask first 12 character

{% endtab %}
{% tab title='HR_text-processing-sed-4.sh' %}

```sh
sed 's/[0-9]\+ /**** /g'
```

{% endtab %}
{% endtabs %}