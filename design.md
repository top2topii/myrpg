
# NONAME RPG Project

  - 먼저 Combat Simulator를 만드는 것이 목표.

##1. Character

###1.1 Stats

####1.1.1

  - HP: 상수(100)
  - MP: 상수
  - Resource: 뭔가 소모되는 것들(stamina, magazine, mana, ...)
  - Damage(DA): + Weapon Damage
  - Critical Damage(CD): Damage * 1.5
  - Critical Rate(CR): 일정상수
  - Dodge Rate(GR): 일정상수
  - Defense point(DP): 일정상수, 데미지 경감
  - Defense Rate(DR): 일정비, 데미지 경가 비율
  - Accuracy(AC): 공격 성공률, 1.0

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
  - 닳지 않는다.
  - 수리 가능.(옵션에 수리 불능이 있을 수 있다.)
  - 강화: 어떤 장비도 강화가 가능. 강화하는 데 강화석이 필요. 실패 확율 존재.(-,0,+,장비파괴)
  - 장비레벨: 장비의 가치 결정.(일반, 고급, 희귀, 유니크, 전설, 에픽)
  - 착용 제한:(ex: STR100, WIL80, LEVEL20)

###2.3 기타류
  - 부적(charm), 재료, 퀘스트 아이템, 기타(ex: 열쇠) ...

##3. Skill


##4. Monster

  - 각 몬스터는 고유 EXP(경험치)를 가지고 있다.
  - ex) 고블린 110

##5. Combat

###5.1 판정 절차(적은 순서대로 계산)

  - 회피, 치명타, 데미지, 방어(DR, DP)의 순서로 계산



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


##7. Euipment 예제

  - 머리
  - 몸통
  - 신발
  - 허리
  - 반지2개
  - 목걸이
  - 무기
  - 보조장비(방패)
  
##8. Item 예제
  - 무기: 철검(Iron Sword): 데미지+25
  - 보조장비: 철방패(Iron Shield): DR+20(데미지 경감이 20%)
  - 머리: 철모(Iron Helm): DP+2(데미지 2경감)
  - 몸통: 철갑(Iron Mail): DP+3(데미지 3경감)
  - 신발: 아이언부츠(Iron Boots): DP+1
  - 벨트: 아이언벨트(Iron Belt):DP+1
  - 부적(Charm): Inventory에 있지만 캐릭터의 속성에 영향을 준다: AC+0.1
  - 회복물약:  HP+30 회복, Quick Slot에 장착.
  
##9. Inventory
  - 모든 아이템은 1칸에 1개
  - 이미지는 http://smite.gamepedia.com/Elixir_of_Power 를 봐라.
  - 
##10. Quick Slot(소모성 또는 기타 장비)
  - 기본 1칸을 가지고 있다.
  - 벨트를 차면 기본 1칸, 좋은 벨트는 더 많이 착용 가능.
  
##11. 주의사항
  - 회복 관련 아이템 사용시 원래의 체력을 초과해서 회복될 수는 없다.
  - 데미지가 (-)의 값을 가질 수 없다.
