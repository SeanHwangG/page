{% tabs %}
{% tab title='HR_text-processing-awk-2.md' %}

* A student is considered to have passed if (s)he has a score  or more in each of the three subjects.
* display the following for each student: `[Identifier] : [Pass/Fail]`

{% endtab %}
{% tab title='HR_text-processing-awk-2.sh' %}

```sh
awk '{print $1,":", ($2<50||$3<50||$4<50) ? "Fail" : "Pass"}'
```

{% endtab %}
{% endtabs %}