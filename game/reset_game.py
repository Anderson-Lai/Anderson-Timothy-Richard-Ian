from game.start_game import Enemy, Projectile, EnemyWaves
from gameResults.save_score import save_score
from time import sleep
from copy import deepcopy
from game.lives import num_lives

def reset_game(current_score: int, projectiles: list[Projectile], enemies: list[Enemy],
               enemy_kills: int, previous_kills: int, event_variables: dict, 
               waves_copy: list[EnemyWaves], spawn_rates_copy: list[int],
               waves: list[EnemyWaves], spawn_rates: list[int], difficulty: str, target_game_state: str) \
                -> tuple[int, int, int, int, list[EnemyWaves], list[int]]: 
        # enemy_kills, current_score, previous_kills, lives, waves_copy, spawn_rates_copy
        
        save_score(current_score)

        # delete all projectiles and enemies since the game is restarting
        projectiles.clear()
        enemies.clear()

        # reset kills, scores, and lives
        enemy_kills = 0
        current_score = 0
        previous_kills = 0
        lives = num_lives(difficulty)

        # break out of the if statement for the next iteration
        event_variables["restart"] = False
        event_variables["gameState"] = target_game_state
        event_variables["location"] = 260

        # reset the copies as they have been altered
        waves_copy = deepcopy(waves)
        spawn_rates_copy = deepcopy(spawn_rates)

        # give the program time to reset everything
        sleep(0.05)

        return (enemy_kills, current_score, previous_kills, lives, waves_copy, spawn_rates_copy)