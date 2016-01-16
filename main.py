
# -*- coding: utf-8 -*-

'''
    RPG
'''

'''
설정값
기본 공격 100 tick

player가 쓰러지면 일정한 시간 만큼은 쉬어야 한다.
일정한 시간을 어떻게 할까? 이동하는  거리 대비 게임 시간을 생각해 보자.


'''

g_attack_speed = 100        # 100 tick

from threading import Timer
from time import sleep
import random

class RepeatedTimer(object):
    def __init__(self, interval, function, *args, **kwargs):
        self._timer     = None
        self.interval   = interval
        self.function   = function
        self.args       = args
        self.kwargs     = kwargs
        self.is_running = False
        self.start()

    def _run(self):
        self.is_running = False
        self.start()
        self.function(*self.args, **self.kwargs)

    def start(self):
        if not self.is_running:
            self._timer = Timer(self.interval, self._run)
            self._timer.start()
            self.is_running = True

    def stop(self):
        self._timer.cancel()
        self.is_running = False

class  Character():
    def __init__(self, name):
        self.stats = {
            'str': 30,              # 힘
            'dex': 30,              # 민첩
            'wil': 30,              # 정신
            'vit': 30,              # 활력
            'hp':30,                # 체력
            'mp':30,                # 마나
            'damage': 0,            # 공격력 보너스
            'physical_defense_rate': 0.0,  # 물리 방어력 보너스
            'magic_defense_rate': 0.0,    # 마법 방어력 보너스
            'critical_rate': 0.0,     # 치명타율
            'dodge_rate': 0.0,        # 회피율
            'attack_speed': g_attack_speed,       # 공속, 단위는 tick
        }

        self.stats_point = 7        # level up시 얻어지는 stats 포인트
        self.experience = 1100      # level up을 하려면 필요한 경험치
        self.critical_damage_rate = 1.5     # 치명타 피해는 보통 공격의 1.5배

        self.level = 0
        self.name = name
        self.stats['damage'] = self.stats['str']
        self.stats['physical_defense_rate'] = self.stats['vit'] / float(self.stats['vit'] + 300.0)
        self.stats['magic_defense_rate'] = self.stats['wil'] / float(self.stats['wil'] + 300.0)
        '''
        self.stats['critical_rate'] = self.stats['dex'] / float(self.stats['dex'] + 300.0)
        self.stats['dodge_rate'] = self.stats['dex'] / float(self.stats['dex'] + 300.0)
        self.stats['attack_speed'] -= g_attack_speed * self.stats['dex'] / float(self.stats['dex'] + 300.0)
        '''

        ''' 강이 결정 사항: dex를 없앤다. 그래서 아래의 수치는 현재 고정값'''
        self.stats['critical_rate'] = 0.1
        self.stats['dodge_rate'] = 0.1
        self.stats['attack_speed'] = g_attack_speed

        self.rt = None

    def skill_on(self):
        pass

    def skill_off(self):
        pass

    def Equip_on(self):
        pass

    def Equip_off(self):
        pass

    def print_stats(self, item):
        print "%s(%s): %0.2f" % (self.name, item, self.stats[item])

    def attack_start(self, aTarget):

        print self.name + " attack " + aTarget.name
        print "%s[hp]: %0.2f" % (aTarget.name, aTarget.stats['hp'])

        aTarget.stats['hp'] -= 5.0
        if aTarget.stats['hp'] <= 0.0:
            self.attack_stop()

        self.rt = RepeatedTimer(1, self.attacking, aTarget)


    def attacking(self, aTarget):
        print self.name + " attack " + aTarget.name
        print "%s[hp]: %0.2f" % (aTarget.name, aTarget.stats['hp'])

        aTarget.stats['hp'] -= 5.0

        if aTarget.stats['hp'] <= 0.0:
            print "%s killed." % aTarget.name
            self.attack_stop()


    # 한번의 공격
    #
    def attack(self, aTarget):
        print self.name + " attack " + aTarget.name

        this_damage = random.randrange(1,6)
        aTarget.stats['hp'] -= this_damage

        print "%s have damage(%0.2f), [hp]: %0.2f" % (aTarget.name, this_damage, aTarget.stats['hp'])

        if aTarget.stats['hp'] <= 0.0:
            print "%s is killed." % aTarget.name
            return True

        return False




    def attack_stop(self):

        self.rt.stop()


class Room():

    def __init__(self, teamA, teamB):
        self.teamA = teamA
        self.teamB = teamB
        self.current_tick = 1


    # 상대 고르기, 현재는 무작위
    # teamB에 Character가 없다면 -1을 돌려준다.
    def pick_one_target(self, team):
        no_player = len(team)


        print "living player(s): %d" % no_player
        if no_player == 0:
            return -1
        elif no_player == 1:
            return 1

        return random.randrange(1, no_player)



    # 모든 싸움이 끝나면 True를 돌려준다.
    def fight(self, this_turn):

        current_attack = 'B'
        team_attack = self.teamB
        team_defense = self.teamA
        is_killed = None

        if this_turn %2 == 1:
            team_attack = self.teamA
            team_defense = self.teamB
            current_attack = 'A'


        print "team(%s) attack" %  current_attack

        for a_man in team_attack:
            # 상대팀 살아 있는 상대 고르기.
            a_target_no = self.pick_one_target(team_defense)
            a_target = team_defense[a_target_no-1]
            is_killed = a_man.attack(a_target)

            if is_killed:
                del team_defense[a_target_no-1]

                # 살아 있는 팀원이 없다면
                if self.pick_one_target(team_defense) == -1:
                    print "%s is win!" % current_attack
                    return True

        return False


if __name__ == '__main__':

    a = Character('Joseph')
    b = Character('Moria')
    c = Character('Crea')

    monster_a = Character('Snake')
    monster_b = Character('Lion')
    monster_c = Character('Skeleton')

    '''
    player나 monster group은 공격 순서가 정해져 있다.
    공격 순서는 민첩순. 민첩이 같을 경우 주사위.

    같은 tick에서도 민첩순으로 공격. 같은 방법으로 민첩이 같을 경우는 주사위.

    타이머는 직선형으로 구현한다.

    '''

    a.print_stats('damage')
    a.print_stats('physical_defense_rate')
    a.print_stats('magic_defense_rate')
    a.print_stats('critical_rate')
    a.print_stats('attack_speed')

    #a.attack_start(b)
    teamA = [a, b, c]
    teamB = [monster_a, monster_b, monster_c]

    myroom = Room(teamA, teamB)

    i = 1
    while True:

        print "This Turn: %d" % i
        is_done = myroom.fight(i)

        if is_done:
            break
        i += 1