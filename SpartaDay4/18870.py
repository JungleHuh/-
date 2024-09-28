# 입력 받기
n = int(input())
zip_list = list(map(int, input().strip().split()))
# 오름차순 정리 + 인덱스 부여를 위한 Set(집합)처리
sorted_zip_list = sorted(set(zip_list))
# 다시 Zip_list에 있는 순서대로 Set(집합)의 인덱스 부여 -> Dict 사용
zip_dict = {zip: idx for idx, zip in enumerate(sorted_zip_list)}

changed_zip_list = [zip_dict[zip] for zip in zip_list]
print(" ".join(map(str, changed_zip_list)))



'''
소트를 해주면 인덱스 값이 낮은 상태로 유지되지
그러면 어떻게 해야할까?
왜 그렇게 해야할까?
-10 -9 2 4 4 인덱스가 만들어지는데 중복 제거하기 위해서 
set으로 바꿔줌 그래서 인덱스 부여: 딕셔너니로
그 후에 다시 처음 집리스트로 돌아와 인덱스 부여
이게 풀이 방식


여기서 내가 부족한 것이: 딕셔너리 선언하고 그 인덱스 배열하는 것 잘 모름
이에 대해서 블로그에 정리하고 문제 풀기

골드 상위도 어렵지 않다는 말이 약간이나마 이해가 간다.
'''