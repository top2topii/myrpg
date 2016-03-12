
# NONAME RPG Project

  - 먼저 Combat Simulator를 만드는 것이 목표.

##1. Character

###1.1 Stats

####1.1.1

  - HP: VIT * 10
  - MP: WIL * 10
  - 상수(X): 300
  - Physical Damage: STR + Weapon Damage
  - Magical Damage: WIL(?)
  - Critical Damage: Damage * 1.5
  - Critical Rate: 일정상수
  - Dodge Rate: 일정상수
  - Physical Resist point: 일정상수

####1.1.2 

  - Strength(힘): STR
  - Will(정신): WIL
  - Vitality(활력): VIT

###1.2 Equipment

  - 무기: 단검, 검(1H,2H), 도끼, 둔기, 창, 활, 석궁, 총, 대포, 방패
  - 방어구: 머리, 상의, 하의, 신발, 허리
  - 장신구: 반지(2개), 목걸이


###1.3 Level Up

####1.3.1 Experience

  - n에서 n+1의 level로 level up 하기위한 획득 경험치
  - (1.1^n) * 1000 : n은 시작 level

##2. Item

###2.1 소비류
  - 소모성 아이템
  - 물약, 스크롤, 투척 무기


###2.2 장비류
  - 무기, 방어구, 장신구
  - 닳아 사용 불능이 된다.
  - 수리 가능.(옵션에 수리 불능이 있을 수 있다.)
  - 강화: 어떤 장비도 강화가 가능. 강화하는 데 강화석이 필요. 실패 확율 존재.(-,0,+,장비파괴)
  - 장비레벨: 장비의 가치 결정.(일반, 마법, 희귀, 유니크, 전설, 에픽)
  - 착용 제한:(ex: STR100, WIL80, LEVEL20)

###2.3 기타류
  - 부적(charm), 재료, 퀘스트 아이템, 기타(ex: 열쇠) ...

##3. Skill


##4. Monster

  - 각 몬스터는 고유 EXP(경험치)를 가지고 있다.
  - ex) 고블린 110

##5. Combat

###5.1 판정 절차

  - 회피, 치명타, 데미지, 방어



##6. 모험

###6.1 탐색
  - 몬스터 조우
  - 보물 발견
  - 휴식

###6.2 지역
  
  - 마을: 대장장이, 마법상점, 잡화점, 여관.
  - 필드: 탐색 가능
  - 던전: 휴식 불가능, 연속 몬스터 출현. 보물 많음.
  - 이동: .필드...필드...마을.
