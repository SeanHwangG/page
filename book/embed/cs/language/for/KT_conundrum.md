{% tabs %}
{% tab title='KT_conundrum.md' %}

* 주어진 문자를 PERPERPER로 바꾸는데 몇 번 문자를 바꿔야 하는가

{% endtab %}
{% tab title='KT_conundrum.py' %}

```py
st = input()
ret = 0
for i, ch in enumerate(st):
  if i % 3 == 0 and ch != 'P':
    ret+=1
  if i % 3 == 1 and ch != 'E':
    ret+=1
  if i % 3 == 2 and ch != 'R':
    ret+=1
print(ret)
```

{% endtab %}
{% endtabs %}