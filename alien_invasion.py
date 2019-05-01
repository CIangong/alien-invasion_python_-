import sys
import pygame
from settings import Settings
from game_stats import GameStats
from scoreboard import Scoreboard
from button import Button
from ship import Ship
from alien import Alien
import game_functions as gf
from pygame.sprite import Group

def run_game():
    # 初始化游戏并创建一个屏幕对象
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    # 创建Play按钮
    play_button = Button(ai_settings, screen, "Play")
    # 创建一个用于存储游戏统计信息的实例，并创建记分牌
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)
    ship = Ship(ai_settings,screen)
    bullets = Group()
    aliens = Group()
    alien = Alien(ai_settings, screen)
    gf.create_fleet(ai_settings, screen,ship, aliens)
    # 开始游戏的主循环
    while True:
    # 监视键盘和鼠标事件
        gf.check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets)
        if stats.game_active:
            ship.update(ai_settings)
            gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets)
            gf.update_aliens(ai_settings, screen, stats, sb, ship, aliens, bullets)
            for bullet in bullets.copy():
                if bullet.rect.bottom <= 0:
                    bullets.remove(bullet)
            print(len(bullets))
        gf.update_screen(ai_settings, screen, stats, sb, ship, aliens,bullets, play_button)

if __name__ == '__main__':
    run_game()
