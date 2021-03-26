{% tabs %}
{% tab title='KT_batterup.md' %}

* 첫번째 줄 n개의 타석이 주어지고, 다음줄에는 n개 타석에서의 각 정수가 주어진다.
* N개의 정수가 주어질 때, 볼넷,스트라이크,1루타, 2루타, 3루타, 홈런은 각 -1,0,1,2,3,4 점수를나타냄
* 볼넷 -1의 경우 타석으로 고려하지 않음
* 선수의 장타율을 출력하라(장타율은 모든 타석에서의 점수를 더한 값에 n타석으로 나눈 값)

{% endtab %}
{% tab title='KT_batterup.py' %}

```py
n_hit = int(input())
li = list(map(int, input().split()))
miss = li.count(-1)
print((sum(li) + miss) / (n_hit - miss))
```

{% endtab %}
{% endtabs %}