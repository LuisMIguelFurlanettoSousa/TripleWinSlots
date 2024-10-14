import itertools
import random
from time import sleep
import os


class Player:
    def __init__(self, balance=0):
        self.balance = balance

class CassaNiquel:

    def __init__(self, level=1, balance=0):
        self.SIMBOLOS = {
            'money_mouth_face': '1F911',
            'cold_face': '1F976',
            'alien': '1F47D',
            'heart_on_fire': '2764',
            'collision': '1F4A5'
        }
        self.level = level
        self.permutations = self._gen_permutations()
        self.balance = balance
        self.initial_balance = self.balance

    def _gen_permutations(self):
        permutations = list(itertools.product(self.SIMBOLOS.keys(), repeat=3))
        for j in range(self.level):
            for i in self.SIMBOLOS.keys():
                permutations.append((i, i, i))
        return permutations

    def _get_final_result(self):
        if not hasattr(self, 'permutations'):
            self.permutations = self._gen_permutations()

        result = list(random.choice(self.permutations))
        
        if len(set(result)) == 3 and random.randint(0, 5) >= 2:
            result[1] = result[0]
        
        return result

    def _display(self, amount_bet, result):
        rolos = [[random.choice(list(self.SIMBOLOS.keys())) for _ in range(3)] for _ in range(3)]
        
        for i in range(3):
            self._spin_reel(rolos, i, result[i])
            sleep(0.5) 
        
        print(self._emojize(result))
        if self._check_result_user(result):
            print(f'Você venceu e recebeu: {amount_bet * 3}')
        else:
            print('Foi quase, tente novamente')

    def _spin_reel(self, rolos, reel_index, final_symbol):
        steps = random.randint(10, 20)
        delay = 0.1 

        for _ in range(steps):
            rolos[reel_index] = [random.choice(list(self.SIMBOLOS.keys())) for _ in range(3)]
            self._print_rolos(rolos)
            sleep(delay)
            os.system('cls' if os.name == 'nt' else 'clear')

            delay += 0.05 

        rolos[reel_index] = [final_symbol] * 3
        self._print_rolos(rolos)
        sleep(0.5)

    def _print_rolos(self, rolos):
        """Exibe os símbolos em formato de caça-níquel."""
        for row in range(3):
            print(f'{self._emojize([rolos[col][row] for col in range(3)])}')
        print('-' * 15)

    def _emojize(self, emojis):
        return ''.join(tuple(chr(int(self.SIMBOLOS[code], 16)) for code in emojis))
    
    def _check_result_user(self, result):
        return all([result[0] == x for x in result])
    
    def _update_balance(self, amount_bet, result, player: Player):
        if self._check_result_user(result):
            self.balance -= (amount_bet * 3)
            player.balance += (amount_bet * 3)
        else:
            self.balance += amount_bet
            player.balance -= amount_bet

    def play(self, amount_bet, player: Player):
        result = self._get_final_result()
        self._display(amount_bet, result)
        self._update_balance(amount_bet, result, player)


maquina1 = CassaNiquel(level=5)
jogador1 = Player()
maquina1.play(10, jogador1)