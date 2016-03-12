

# 다음에는 무얼 할까?

 - 장비
 - tick system
 - room(field)


## 데미지 계산 공식

 - 적중/회피를 계산
 - 적중시 데미지 계산
 - A.데미지 - B.물리방어력 포인트

## 장비
 - 무기
 - 방어구
 - 장신구


### 무기
 - 착용하는 무기에 따라 공격성공율, 데미지, 치명타율을 조정하게 된다.
 - ex) 재빠른 검: 공성: +0.0, 뎀: +10.0, 치명: +5.0  

### 방어구
 - 물리 방어력 조정
 - 데미지 포인트: A.데미지 - B.물리방어력 포인트
 - 단 A.데미지의 최소치는 1
 - ex) A가 재빠른 검으로 B(방어력포인트: 2.0)을 공격하면
 - 데미지 = 0 + 10.0 - 2.0 = 8.0


### 장신구
 - 마법 방어력 조정



### Room

'''
  A | B
  C | D
  E | F
  G | H
'''

  - 앞열: B, D, F, H
  - 뒷열: A, C, E, G
  - 앞열의 캐릭터가 모두 죽을 때 뒷열을 캐릭터들이 앞열로 온다.
  - 지형 지물이 있을경우를 고려하자. (파괴 or 없애고 뒷열이 앞열로 옮겨짐)
