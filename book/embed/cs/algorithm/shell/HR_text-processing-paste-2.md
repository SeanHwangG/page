{% tabs %}
{% tab title='HR_text-processing-paste-2.md' %}

* Restructure the file so that three consecutive rows are folded into one line and are separated by semicolons.

{% endtab %}
{% tab title='HR_text-processing-paste-2.sh' %}

```sh
paste - - - -d ';'
```

{% endtab %}
{% endtabs %}