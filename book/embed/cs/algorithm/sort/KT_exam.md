{% tabs %}
{% tab title='KT_exam.md' %}

* 첫줄에는 친구가 맞은 문제 수가, 둘째 줄 세째 줄에는 나와 친구의 답안이 주어진다.
* 내가 맞을 수 있는 최대 문제 수를 출력하라.

{% endtab %}
{% tab title='KT_exam.py' %}

```py
correct = int(input())
my = input()
fr = input()
total = len(my)
same = 0
for m, f in zip(my, fr):
    if m == f:
        same += 1

if same > correct:
    print(correct + (total - same))
else:
    print(same + (total - correct))
```

{% endtab %}
{% endtabs %}