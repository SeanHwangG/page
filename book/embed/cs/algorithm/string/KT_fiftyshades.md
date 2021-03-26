{% tabs %}
{% tab title='KT_fiftyshades.md' %}

* 첫줄엔 N 이 그 다음 N 줄엔 문자가 주어진다.
* 이 때 rose나 pink를 포함한 문자의 수를 구하라. (단 대문자 / 소문자는 무시한다.)

{% endtab %}
{% tab title='KT_fiftyshades.py' %}

```py
N = int(input())
count = 0
for _ in range(N):
    st = input().lower()
    if st.find('pink') != -1 or st.find('rose') != -1:
        count += 1

print(count if count != 0 else "I must watch Star Wars with my daughter")
```

{% endtab %}
{% endtabs %}