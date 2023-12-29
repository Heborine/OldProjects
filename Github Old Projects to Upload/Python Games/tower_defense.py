import math
import pygame
import time


class Tower(pygame.sprite.Sprite):
    def __init__(self, height, width):
        super().__init__()
        self.r = 255
        self.g = 225
        self.b = 255
        self.width = width
        self.height = height
        self.color = (self.r, self.g, self.b)
        self.image = pygame.Surface([self.width, self.height])
        # this is divided by 1.4 later
        self.tower_range = 50

        # so it can shoot immediately when created, but then will need to start using timer again
        self.shot_time = 0
        self.since_shot = 2
        self.when_next_shot = 2
        self.can_shoot = True

        self.bullet_speed = 1
        self.amount_bullets = 1
        self.bullet_damage = 1

        pygame.draw.rect(self.image, self.color, pygame.Rect(0, 0, self.width, self.height))
        self.rect = self.image.get_rect()

    def placement(self, mouse_position):
        # Its position
        self.rect.x = mouse_position[0]
        self.rect.y = mouse_position[1]

    def clicked(self):
        return self.rect.x, self.rect.y, self.width, self.height, self.color, self.tower_range

    def give_center(self):
        return (self.rect.x + (self.width / 2)), (self.rect.y + (self.height / 2)), (self.tower_range)

    def upgrade(self):
        # max ten upgrades
        # allows for a more accurate range "circle" to be made while limited
        if self.tower_range <= 60:
            self.tower_range += 1
            if self.g > 0:
                self.g -= 50
            if self.g < 0:
                self.g += 60
            self.color = (self.r, self.g, self.b)
            # redraw the rectangle to have the new color
            pygame.draw.rect(self.image, self.color, pygame.Rect(0, 0, self.width, self.height))

    def upgrade2(self):
        # faster amount of time between shots
        if self.when_next_shot > 0:
            self.when_next_shot -= 0.2
            if self.b > 0:
                self.b -= 50
            if self.b < 0:
                self.b += 60
            self.color = (self.r, self.g, self.b)
            # redraw the rectangle to have the new color
            pygame.draw.rect(self.image, self.color, pygame.Rect(0, 0, self.width, self.height))

    def set_shot_time(self):
        self.shot_time = time.time()

    def count_since_shot(self):
        # change the since_shot time
        self.since_shot = time.time()

    def timer_shot(self):
        # subtract the running time from the static one that is taken
        if self.since_shot - self.shot_time < self.when_next_shot:
            self.can_shoot = False
        else:
            self.can_shoot = True


class Tower2(Tower):
    def __init__(self, width, height):
        super().__init__(width, height)
        self.tower_range = 45
        self.r = 225
        self.g = 255
        self.b = 255
        self.color = (self.r, self.g, self.b)
        pygame.draw.rect(self.image, self.color, pygame.Rect(0, 0, self.width, self.height))

    def upgrade(self):
        # max five upgrades -- bullet_speed = 6
        if self.bullet_speed <= 5:
            self.bullet_speed += 1
            if self.r > 0:
                self.r -= 50
            if self.r < 0:
                self.r += 60
            self.color = (self.r, self.g, self.b)
            # redraw the rectangle to have the new color
            pygame.draw.rect(self.image, self.color, pygame.Rect(0, 0, self.width, self.height))

    def upgrade2(self):
        if self.amount_bullets < 5:
            self.amount_bullets += 1
            if self.b > 0:
                self.b -= 50
            if self.b < 0:
                self.b += 60
            self.color = (self.r, self.g, self.b)
            # redraw the rectangle to have the new color
            pygame.draw.rect(self.image, self.color, pygame.Rect(0, 0, self.width, self.height))


class Tower3(Tower):
    def __init__(self, width, height):
        super().__init__(width, height)
        self.tower_range = 45
        self.r = 255
        self.g = 255
        self.b = 225
        self.color = (self.r, self.g, self.b)
        pygame.draw.rect(self.image, self.color, pygame.Rect(0, 0, self.width, self.height))

    def upgrade(self):
        # loses bullet speed as well
        if self.bullet_damage <= 3:
            self.bullet_damage += 1
            self.bullet_speed -= 1
            if self.b > 0:
                self.b -= 50
            if self.b < 0:
                self.b += 60
            self.color = (self.r, self.g, self.b)
            # redraw the rectangle to have the new color
            pygame.draw.rect(self.image, self.color, pygame.Rect(0, 0, self.width, self.height))

    def upgrade2(self):
        if self.bullet_speed < 2:
            self.bullet_speed += 1
            if self.g > 0:
                self.g -= 50
            if self.g < 0:
                self.g += 60
            self.color = (self.r, self.g, self.b)
            # redraw the rectangle to have the new color
            pygame.draw.rect(self.image, self.color, pygame.Rect(0, 0, self.width, self.height))


class Range(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, tower_color, tower_range):
        super().__init__()
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = (125, 125, 125)
        # color of inner box that shows original tower
        self.tower_color = tower_color
        # range of circle
        self.range_value = tower_range
        self.image = pygame.Surface([self.width + self.range_value, self.height + self.range_value])
        pygame.draw.rect(self.image, self.color,
                         pygame.Rect(0, 0, self.width + self.range_value, self.height + self.range_value), 20, 20, 20,
                         20)
        self.rect = self.image.get_rect()
        self.rect.x = self.x - (self.range_value / 2)
        self.rect.y = self.y - (self.range_value / 2)
        pygame.draw.rect(self.image, self.tower_color,
                         pygame.Rect((self.range_value / 2), (self.range_value / 2), self.width, self.height))


class Enemy(pygame.sprite.Sprite):
    def __init__(self, hp, starting_position):
        super().__init__()
        self.color = (255, 0, 0)
        self.width = 15
        self.height = 15
        self.image = pygame.Surface([self.width, self.height])
        self.hp = hp
        self.escaped = False

        pygame.draw.rect(self.image, self.color, pygame.Rect(0, 0, self.width, self.height))
        self.rect = self.image.get_rect()

        # starting position
        self.rect.x = starting_position
        self.rect.y = 0

        # speed per update
        # originally set to 0, and then when type is called, start moving when movement_speed is changed
        self.movement_speed = 0

    def moving(self):
        # movement along the current "map"
        if (self.rect.x < course_size_x_min) and (self.rect.y < course_size_y_min):
            self.rect.x += self.movement_speed
            self.rect.y += self.movement_speed
        elif (self.rect.x < course_size_x) and (self.rect.y == course_size_y_min):
            self.rect.x += self.movement_speed
        elif (self.rect.x == course_size_x) and (self.rect.y < course_size_y):
            self.rect.y += self.movement_speed
        elif (self.rect.x <= course_size_x) and (self.rect.y == course_size_y) and (not (self.rect.x <= off_map)):
            self.rect.x -= self.movement_speed
        elif self.rect.x <= off_map:
            # will remove object
            self.escaped = True
        else:
            pass
        # make sure it follows/does not jump over map guidelines for many more movement_speed values
        if self.rect.x > course_size_x:
            self.rect.x = course_size_x
        if self.rect.y > course_size_y:
            self.rect.y = course_size_y
        if (self.rect.x < course_size_x) and (self.rect.y > course_size_y_min and self.rect.y <= course_size_y_min + 7):
            self.rect.y = course_size_y_min

    def provide_center(self):
        return (self.rect.x + (self.width / 2)), (self.rect.y + (self.height / 2))

    def type(self):
        if self.hp > 3:
            self.color = (125, 125, 125)
            pygame.draw.rect(self.image, self.color, pygame.Rect(0, 0, self.width, self.height))
        elif self.hp > 2:
            self.color = (0, 0, 255)
            pygame.draw.rect(self.image, self.color, pygame.Rect(0, 0, self.width, self.height))
        elif self.hp > 1:
            self.color = (0, 255, 0)
            pygame.draw.rect(self.image, self.color, pygame.Rect(0, 0, self.width, self.height))
        elif self.hp > 0:
            self.color = (255, 0, 0)
            pygame.draw.rect(self.image, self.color, pygame.Rect(0, 0, self.width, self.height))
        else:
            self.kill()
        self.movement_speed = self.hp


class Bullet(pygame.sprite.Sprite):
    def __init__(self, which_enemy, bullet_speed, bullet_damage):
        super().__init__()
        self.width = 3
        self.height = 4
        self.color = (125, 255, 0)
        self.image = pygame.Surface([self.width, self.height])
        pygame.draw.rect(self.image, self.color, pygame.Rect(0, 0, self.width, self.height), 20, 20)
        self.rect = self.image.get_rect()
        self.enemy_follow = which_enemy
        self.enemy_follow_x = self.enemy_follow.rect.x
        self.enemy_follow_y = self.enemy_follow.rect.y
        self.hit_position = False
        self.last_x_greater = False
        self.last_y_greater = False
        self.change_x_not_broken = True
        self.change_y_not_broken = True
        self.bullet_speed = bullet_speed
        self.bullet_damage = bullet_damage

    def spawn(self, towerxcord, towerycord):
        self.rect.x = towerxcord
        self.rect.y = towerycord

    def move(self):
        if not self.hit_position:
            if self.change_x_not_broken:
                if self.rect.x > self.enemy_follow_x:
                    self.rect.x -= self.bullet_speed
                    self.last_x_greater = True
                elif self.rect.x == self.enemy_follow_x:
                    self.change_x_not_broken = False
                    if self.last_x_greater:
                        self.rect.x -= self.bullet_speed
                    else:
                        self.rect.x += self.bullet_speed
                else:
                    self.rect.x += self.bullet_speed
                    self.last_x_greater = False
            else:
                if self.last_x_greater:
                    self.rect.x -= self.bullet_speed
                else:
                    self.rect.x += self.bullet_speed
            if self.change_y_not_broken:
                if self.rect.y > self.enemy_follow_y:
                    self.rect.y -= self.bullet_speed
                    self.last_y_greater = True
                elif self.rect.y == self.enemy_follow_y:
                    self.change_y_not_broken = False
                    if self.last_y_greater:
                        self.rect.y -= self.bullet_speed
                    else:
                        self.rect.y += self.bullet_speed
                else:
                    self.rect.y += self.bullet_speed
                    self.last_y_greater = False
            else:
                if self.last_y_greater:
                    self.rect.y -= self.bullet_speed
                else:
                    self.rect.y += self.bullet_speed
            if self.rect.x == self.enemy_follow_x and self.rect.y == self.enemy_follow_y:
                self.hit_position = True
        else:
            if self.last_x_greater:
                self.rect.x -= self.bullet_speed
            else:
                self.rect.x += self.bullet_speed
            if self.last_y_greater:
                self.rect.y -= self.bullet_speed
            else:
                self.rect.y += self.bullet_speed

    def find_center(self):
        return (self.rect.x + (self.width / 2)), (self.rect.y + (self.height / 2))


def overlapping(x1, y1, width1, height1, x2, y2, width2, height2):
    if ((x1 == x2 and y1 == y2) or (x1 + width1 == x2 + width2 and y1 + height1 == y2 + height2)
            or (x1 < x2 and x1 + width1 > x2 and y1 < y2 and y1 + height1 > y2)
            or (x2 < x1 and x2 + width2 > x1 and y2 < y1 and y2 + height2 > y1)):
        return True
    return False


def make_round(enemy_amount_type, amount_each_times_through, start_enemy):
    # enemy amount is subtracted by whatever the start_enemy is to get how many each
    round_quantity = 0
    while round_quantity < amount_each_times_through:
        # subtract here to keep the while loop working
        times_through = start_enemy - 1
        while times_through < enemy_amount_type:
            enemy = Enemy(times_through + 1, 0 - (5 * round_quantity))
            list_all_enemies.add(enemy)
            times_through += 1
        round_quantity += 1
    total_amount_bullets = 0
    total_amount_towers = 0
    # make sure the bullets are destroyed
    while len(list_all_bullets) > 0:
        list_all_bullets.sprites()[0].kill()
    # reset the shots at the start of the round
    going_through = 0
    while going_through < len(list_all_towers):
        list_all_towers.sprites()[going_through].can_shoot = True
        going_through += 1


def restart_game():
    while len(list_all_bullets) > 0:
        list_all_bullets.sprites()[0].kill()
    while len(list_all_towers) > 0:
        list_all_towers.sprites()[0].kill()
    while len(list_all_enemies) > 0:
        list_all_enemies.sprites()[0].kill()
    while len(list_all_show_ranges) > 0:
        list_all_show_ranges.sprites()[0].kill()
    cash_amount = 500
    health_amount = 10
    pause_state = False
    set_round = 0
    return cash_amount, health_amount, pause_state, set_round


def on_path(x, y):
    variable_amount = 20
    min_variable_amount = 0
    if ((course_size_x_min - variable_amount < x < course_size_x + variable_amount) and (course_size_y_min - variable_amount < y < course_size_y_min + variable_amount)) or\
            ((course_size_x - variable_amount < x < course_size_x + variable_amount) and (course_size_y_min - variable_amount < y < course_size_y + variable_amount)) or\
            ((course_size_x_min - variable_amount < x < course_size_x + variable_amount) and (course_size_y - variable_amount < y < course_size_y + variable_amount)) or \
            ((min_variable_amount < x < variable_amount) and (min_variable_amount < y < variable_amount)):
        return True
    else:
        return False


if __name__ == "__main__":

    # map positioning
    global course_size_x
    global course_size_y
    global course_size_x_min
    global course_size_y_min
    global off_map
    course_size_x = 1450
    course_size_y = 750
    course_size_x_min = 10
    course_size_y_min = 10
    off_map = -10

    screen_size_x = 1500
    screen_size_y = 800

    # Form the screen with 1500x800 size
    # and with resizable format
    screen = pygame.display.set_mode((screen_size_x, screen_size_y),
                                     pygame.RESIZABLE)

    # set title
    pygame.display.set_caption('Tower Defense')

    # set window image
    Icon = pygame.image.load("duckpic.gif")
    pygame.display.set_icon(Icon)

    pygame.init()

    # set up the group lists using the Pygame function for later updating and tracking
    list_all_towers = pygame.sprite.Group()
    list_all_enemies = pygame.sprite.Group()
    list_all_show_ranges = pygame.sprite.Group()
    list_all_bullets = pygame.sprite.Group()

    # set the round to 0
    rounds = 0

    global cash
    cash = 500
    global player_health_points
    player_health_points = 10

    # run window
    running = True
    pause = False
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            # check if a key has been pressed
            elif event.type == pygame.KEYDOWN:
                # if the a key was pressed, check if it is one of these keys
                # make sure that someone can not unpause after a game over (even temporarily)
                if player_health_points > 0:
                    if event.key == pygame.K_RETURN:
                        # if pause is true, make it false
                        # otherwise, make it true
                        if pause:
                            pause = False
                        else:
                            pause = True
                else:
                    if event.key == pygame.K_c:
                        cash, player_health_points, pause, rounds = restart_game()
                    if event.key == pygame.K_e:
                        running = False
                if event.key == pygame.K_1:
                    mouse_position = pygame.mouse.get_pos()
                    check_on_path = on_path(mouse_position[0], mouse_position[1])
                    if not check_on_path:
                        if cash >= 100:
                            tower = Tower(20, 20)
                            list_all_towers.add(tower)
                            tower.placement(mouse_position)
                            cash -= 100
                if event.key == pygame.K_2:
                    mouse_position = pygame.mouse.get_pos()
                    check_on_path = on_path(mouse_position[0], mouse_position[1])
                    if not check_on_path:
                        if cash >= 150:
                            tower = Tower2(20, 20)
                            list_all_towers.add(tower)
                            tower.placement(mouse_position)
                            cash -= 150
                if event.key == pygame.K_3:
                    mouse_position = pygame.mouse.get_pos()
                    check_on_path = on_path(mouse_position[0], mouse_position[1])
                    if not check_on_path:
                        if cash >= 200:
                            tower = Tower3(20, 20)
                            list_all_towers.add(tower)
                            tower.placement(mouse_position)
                            cash -= 200
                # start rounds
                if event.key == pygame.K_b:
                    if len(list_all_enemies) == 0:
                        rounds += 1
                        if rounds == 1:
                            make_round(1, 1, 1)
                        elif rounds == 2:
                            make_round(2, 1, 2)
                        elif rounds == 3:
                            make_round(2, 1, 1)
                        elif rounds == 4:
                            make_round(1, 1, 3)
                        elif rounds == 5:
                            # two of the same enemy class are in here
                            make_round(3, 2, 1)
                        else:
                            make_round(4, 10, 4)
                # upgrade
                if event.key == pygame.K_u:
                    for towers in range(len(list_all_towers)):
                        # click box of tower / boundaries
                        if cash >= 50:
                            if ((list_all_towers.sprites()[towers].rect.x < pygame.mouse.get_pos()[0] and (
                                    list_all_towers.sprites()[towers].rect.x + 20) > pygame.mouse.get_pos()[0]) or
                                list_all_towers.sprites()[towers].rect.x == pygame.mouse.get_pos()[0] or (
                                        list_all_towers.sprites()[towers].rect.x + 20) == pygame.mouse.get_pos()[0]) \
                                    and ((list_all_towers.sprites()[towers].rect.y < pygame.mouse.get_pos()[1] and (
                                    list_all_towers.sprites()[towers].rect.y + 20) > pygame.mouse.get_pos()[1]) or
                                         list_all_towers.sprites()[towers].rect.y == pygame.mouse.get_pos()[1] or (
                                         list_all_towers.sprites()[towers].rect.y + 20) == pygame.mouse.get_pos()[1]):
                                list_all_towers.sprites()[towers].upgrade()
                                cash -= 50
                if event.key == pygame.K_y:
                    for towers in range(len(list_all_towers)):
                        if cash >= 75:
                            # click box of tower / boundaries
                            if ((list_all_towers.sprites()[towers].rect.x < pygame.mouse.get_pos()[0] and (
                                    list_all_towers.sprites()[towers].rect.x + 20) > pygame.mouse.get_pos()[0]) or
                                list_all_towers.sprites()[towers].rect.x == pygame.mouse.get_pos()[0] or (
                                        list_all_towers.sprites()[towers].rect.x + 20) == pygame.mouse.get_pos()[0]) \
                                    and ((list_all_towers.sprites()[towers].rect.y < pygame.mouse.get_pos()[1] and (
                                    list_all_towers.sprites()[towers].rect.y + 20) > pygame.mouse.get_pos()[1]) or
                                         list_all_towers.sprites()[towers].rect.y == pygame.mouse.get_pos()[1] or (
                                         list_all_towers.sprites()[towers].rect.y + 20) == pygame.mouse.get_pos()[1]):
                                list_all_towers.sprites()[towers].upgrade2()
                                cash -= 75
            elif event.type == pygame.MOUSEBUTTONDOWN:
                for towers in range(len(list_all_towers)):
                    # click box of tower / boundaries
                    if ((list_all_towers.sprites()[towers].rect.x < pygame.mouse.get_pos()[0] and (
                            list_all_towers.sprites()[towers].rect.x + 20) > pygame.mouse.get_pos()[0]) or
                        list_all_towers.sprites()[towers].rect.x == pygame.mouse.get_pos()[0] or (
                                list_all_towers.sprites()[towers].rect.x + 20) == pygame.mouse.get_pos()[0]) \
                            and ((list_all_towers.sprites()[towers].rect.y < pygame.mouse.get_pos()[1] and (
                            list_all_towers.sprites()[towers].rect.y + 20) > pygame.mouse.get_pos()[1]) or
                                 list_all_towers.sprites()[towers].rect.y == pygame.mouse.get_pos()[1] or (
                                         list_all_towers.sprites()[towers].rect.y + 20) == pygame.mouse.get_pos()[1]):
                        # run the clicked command for the specific tower object
                        x, y, width, height, tower_color, tower_range = list_all_towers.sprites()[towers].clicked()
                        x = int(x)
                        y = int(y)
                        width = int(width)
                        height = int(height)
                        circle = Range(x, y, width, height, tower_color, tower_range)
                        # make sure there are not two circles at once
                        try:
                            list_all_show_ranges.sprites()[0].kill()
                        except IndexError:
                            pass
                        list_all_show_ranges.add(circle)
                        # make sure that it can check one then move on
                        # - will allow for it to not get stuck on a singular tower (only create a ring around one)
                        break
                    else:
                        try:
                            list_all_show_ranges.sprites()[0].kill()
                        except IndexError:
                            pass

        if not pause:
            for amount_towers in range(len(list_all_towers)):
                for amount_enemies in range(len(list_all_enemies)):
                    tower_x, tower_y, tower_range_radius = list_all_towers.sprites()[amount_towers].give_center()
                    enemy_x, enemy_y = list_all_enemies.sprites()[amount_enemies].provide_center()
                    # pythagorean theorem for distance
                    # / 1.4 to make it closer to the accuracy of the range bubble
                    if math.sqrt(((enemy_x - tower_x) ** 2) + ((enemy_y - tower_y) ** 2)) <= (tower_range_radius/1.4):
                        if list_all_towers.sprites()[amount_towers].can_shoot == True:
                            bullet_amount = 0
                            while bullet_amount < (list_all_towers.sprites()[amount_towers].amount_bullets):
                                bullet = Bullet(list_all_enemies.sprites()[amount_enemies], list_all_towers.sprites()[amount_towers].bullet_speed, list_all_towers.sprites()[amount_towers].bullet_damage)
                                list_all_bullets.add(bullet)
                                bullet.spawn(tower_x, tower_y)
                                bullet_amount += 1

                            list_all_towers.sprites()[amount_towers].can_shoot = False
                            list_all_towers.sprites()[amount_towers].set_shot_time()
                        else:
                            list_all_towers.sprites()[amount_towers].count_since_shot()
                            list_all_towers.sprites()[amount_towers].timer_shot()
                        # attribute time to tower that counts until 2 seconds - boolean
                        break
            for bullets in range(len(list_all_bullets)):
                try:
                    list_all_bullets.sprites()[bullets].move()
                    # if a bullet hits any enemy, destroy bullet
                    amount_of_enemies = 0
                    for amount_of_enemies in range(len(list_all_enemies)):
                        collision = overlapping(list_all_bullets.sprites()[bullets].rect.x,
                                                list_all_bullets.sprites()[bullets].rect.y,
                                                list_all_bullets.sprites()[bullets].width,
                                                list_all_bullets.sprites()[bullets].height,
                                                list_all_enemies.sprites()[amount_of_enemies].rect.x,
                                                list_all_enemies.sprites()[amount_of_enemies].rect.y,
                                                list_all_enemies.sprites()[amount_of_enemies].width,
                                                list_all_enemies.sprites()[amount_of_enemies].height)
                        if collision:
                            list_all_enemies.sprites()[amount_of_enemies].hp -= list_all_bullets.sprites()[bullets].bullet_damage
                            cash += (list_all_bullets.sprites()[bullets].bullet_damage * 25)
                            # Delete the bullet last so the calculations can be done
                            list_all_bullets.sprites()[bullets].kill()
                    # times two to let the second half of the screen to work
                    if list_all_bullets.sprites()[bullets].rect.x < 0 or \
                            list_all_bullets.sprites()[bullets].rect.x > screen_size_x * 2 or \
                            list_all_bullets.sprites()[bullets].rect.y < 0 or \
                            list_all_bullets.sprites()[bullets].rect.x > screen_size_y * 2:
                        list_all_bullets.sprites()[bullets].kill()
                except IndexError:
                    pass

            for enemies in range(len(list_all_enemies)):
                # so if the list length changes when two or more objects exit at the same time
                # and the list changes and becomes out of range, skip
                try:
                    # evaluate the hp and speed levels of the enemies
                    list_all_enemies.sprites()[enemies].type()
                    # move the enemies
                    list_all_enemies.sprites()[enemies].moving()
                    # since each remove enemies, if the list decreased in moving, it means an enemy passed through
                    if list_all_enemies.sprites()[enemies].escaped:
                        player_health_points -= list_all_enemies.sprites()[enemies].hp
                        list_all_enemies.sprites()[enemies].kill()
                except IndexError:
                    pass
            list_all_bullets.update()
            list_all_towers.update()
            list_all_enemies.update()
            list_all_show_ranges.update()
        screen.fill((0, 0, 0))
        # "map"
        pygame.draw.lines(screen, (0, 124, 90), False, [[0, 0], [course_size_x_min, course_size_y_min],
                                                             [course_size_x, course_size_y_min],
                                                             [course_size_x, course_size_y],
                                                             [0, course_size_y]], 2)
        list_all_towers.draw(screen)
        list_all_enemies.draw(screen)
        list_all_show_ranges.draw(screen)
        list_all_bullets.draw(screen)

        writing_lives = "Lives Left: " + str(player_health_points)
        font = pygame.font.SysFont("didot.ttc", 36)
        writing = font.render(writing_lives, True, "PURPLE")

        writing_cash = "Cash Left: " + str(cash)
        font2 = pygame.font.SysFont("didot.ttc", 36)
        writing2 = font.render(writing_cash, True, "PURPLE")

        screen.blit(writing, (100, 100))
        screen.blit(writing2, (100, 150))

        if player_health_points <= 0:
            pause = True
            font3 = pygame.font.SysFont("chalkduster.ttf", 72)
            writing3 = font.render("Game Over", True, "RED")
            screen.blit(writing3, ((screen_size_x / 2), (screen_size_y / 2)))

        """Update the full display Surface to the screen"""
        pygame.display.flip()

    # quit pygame after closing window
    pygame.quit()
