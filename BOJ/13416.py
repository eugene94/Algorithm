# BOJ 13413 문제
# https://www.acmicpc.net/problem/13413

# 문제

# 회사명	1일	2일	3일	4일
# A사	500	300	-100	600
# B사	800	0	-200	200
# C사	200	300	-400	300
# 위 표에서 양수는 이익을, 음수는 손해를 나타내며, 0은 이익도, 손해도 없음을 의미한다.
# 예를 들어 1일째에 A사의 주식을 장이 열릴 때 사고, 장이 닫힐 때 팔면 500의 이익을 얻을 수 있었다.
# 만약 3일째에 C사의 주식을 장이 열릴 때 사고, 장이 닫힐 때 판다면 400의 손해가 생겼을 것이다.

# 데이터를 분석하던 환규는 자신이 정리한 데이터를 이용해서 N일 동안 규칙을 지키면서 매일 최적의 투자를 할 경우 최대 얼마를 벌 수 있었는지 궁금해졌다.
# 예를 들어 위 표에서 1일째에는 B사의 주식을 사면 가장 많은 이익을 남길 수 있다. 2일째에는 A사, 또는 C사의 주식을 사면 가장 많은 이익을 남길 수 있다.
# 3일째에는 어떤 주식을 사도 손해가 나므로 주식을 사지 않는다. 4일째에는 A사의 주식을 사면 된다.
# 이렇게 주식 투자를 할 경우 환규는 800 + 300 + 0 + 600 = 1700으로, 최대 1700의 이익을 남길 수 있다.
# N일 동안 A사, B사, C사의 주식을 장이 열릴 때 사고, 장이 닫힐 때 모두 팔았을 경우의 손익을 정리한 데이터가 주어질 때,
# 환규가 N일간 규칙을 지키며 최적의 투자를 했을 경우 얻을 수 있었을 최대 이윤을 출력하는 프로그램을 작성하시오.

# 입력값
# 4
# 500 800 200
# 300 0 300
# -100 -200 -400
# 600 200 300

# 출력값
# 1700

# ===========================================================================

testLen = int(input())

for _ in range(testLen):
    days = int(input())
    sumVal = 0
    for _ in range(days):
        maxVal = max(list(map(int, input().split(" "))))
        sumVal += maxVal if (maxVal > 0) else 0
    print(sumVal)
