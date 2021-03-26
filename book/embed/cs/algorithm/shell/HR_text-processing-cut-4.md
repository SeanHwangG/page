{% tabs %}
{% tab title='HR_text-processing-cut-4.md' %}

```txt
1   New York, New York[10]  8,244,910   1   New York-Northern New Jersey-Long Island, NY-NJ-PA MSA  19,015,900  1   New York-Newark-Bridgeport, NY-NJ-CT-PA CSA 22,214,083
2   Los Angeles, California 3,819,702   2   Los Angeles-Long Beach-Santa Ana, CA MSA    12,944,801  2   Los Angeles-Long Beach-Riverside, CA CSA    18,081,569
```

* first three tab seperated columns

```txt
1   New York, New York[10]  8,244,910
2   Los Angeles, California 3,819,702
```

{% endtab %}
{% tab title='HR_text-processing-cut-4.sh' %}

```sh
# by default seperator is tab
cut -f-3
```

{% endtab %}
{% endtabs %}