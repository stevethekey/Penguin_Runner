import pygame
import os  # used to define or obtain paths to modles/images

# Going off YouTuber Tech with Tim, https://www.youtube.com/watch?v=jO6qQDNa2UY
WIN_WIDTH, WIN_HEIGHT = 1024, 680
WIN = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
pygame.display.set_caption("Penguin Runner")

COLOR_BACKGROUND = (255, 255, 255)  # Light blue pop up window

# After reviewing some character ideas, I thought a penguin model would be a good starting point.
runner_model_1 = pygame.image.load(os.path.join('Images', 'penguin.png'))
runner_model_1 = pygame.transform.scale(runner_model_1, (64, 64))


class Player:
    def __init__(self, name, x, y, sprite, height, width):
        self.name = name
        self.x = x
        self.y = y
        self.sprite = sprite
        self.rect = pygame.Rect(x, y, width, height)

        self.falling = False

        self.score = 0

    def reveal_all(self):
        print("Your name is ", self.name, " and your score is ", self.score)

    def move(self, horizontal, vertical):
        self.x += horizontal
        self.y += vertical
        self.rect.move_ip(horizontal, vertical)


death_list1 = []
death_list2 = []
death_list3 = []


class Death:
    def __init__(self, x, y, height, width, level):
        self.x = x
        self.y = y
        self.sprite = pygame.image.load("spikes.png")
        self.rect = pygame.Rect(x, y, width, height)
        self.level = level

        if level == 1:
            death_list1.append(self)

        if level == 2:
            death_list2.append(self)


class PolarBear:
    def __init__(self, name, x, y, sprite, height, width):
        self.name = name
        self.x = x
        self.y = y
        self.sprite = sprite
        self.rect = pygame.Rect(x, y, width, height)


class Instruction:
    def __init__(self, name, x, y, sprite, height, width):
        self.name = name
        self.x = x
        self.y = y
        self.sprite = sprite
        self.rect = pygame.Rect(x, y, width, height)


class Igloo:
    def __init__(self, x, y, height, width):
        self.x = x
        self.y = y
        self.sprite = pygame.image.load(os.path.join('Images', 'igloo.png'))
        self.rect = pygame.Rect(x, y, width, height)

        self.sprite = pygame.transform.scale(self.sprite, (height, width))


goal_1 = Igloo(800, 512, 64, 64)

goal_2 = Igloo(0, 0, 96, 96)

goal_3 = Igloo(1024, 1024, 64, 64)


box_list1 = []
box_list2 = []
box_list3 = []


class Box:

    def __init__(self, x, y, height, width, level):
        self.x = x
        self.y = y
        self.rect = pygame.Rect(x, y, width, height)
        self.level = level

        if level == 1:
            box_list1.append(self)

        if level == 2:
            box_list2.append(self)

        if level == 3:
            box_list3.append(self)


# level 1 boxes
box1 = Box(0, 600, 64, 1024, 1)
box2 = Box(64, 580, 64, 64, 1)
box3 = Box(64, 520, 10, 64, 1)
box4 = Box(64, 430, 10, 64, 1)
box5 = Box(725, 108, 10, 500, 1)

box6 = Box(256, 512, 64, 64, 1)

death_box1 = Death(512, 512, 10, 40, 1)
death_box2 = Death(512, 330, 10, 40, 1)

# level 2 boxes
box21 = Box(0, 600, 64, 1024, 2)
box22 = Box(67, 550, 64, 64, 2)
box23 = Box(90, 425, 8, 64, 2)

box24 = Box(553, 340, 8, 64, 2)
box25 = Box(553, 475, 8, 64, 2)

box26 = Box(951, 340, 8, 64, 2)
box27 = Box(951, 475, 8, 64, 2)

box28 = Box(951, 205, 8, 64, 2)

box29 = Box(640, 182, 8, 64, 2)

box210 = Box(509, 45, 8, 64, 2)

box211 = Box(130, 113, 8, 64, 2)


death_box21 = Death(90, 470, 10, 40, 2)
death_box22 = Death(130, 550, 10, 40, 2)

death_box23 = Death(200, 290, 10, 40, 2)
death_box24 = Death(155, 440, 10, 40, 2)

death_box25 = Death(364, 562, 10, 40, 2)
death_box26 = Death(480, 562, 10, 40, 2)

death_box27 = Death(733, 300, 10, 40, 2)

death_box28 = Death(703, 369, 10, 40, 2)

death_box29 = Death(685, 432, 10, 40, 2)

death_box29 = Death(663, 491, 10, 40, 2)

death_box210 = Death(639, 548, 10, 40, 2)

death_box210 = Death(906, 297, 10, 40, 2)
death_box211 = Death(872, 365, 10, 40, 2)

death_box212 = Death(830, 439, 10, 40, 2)
death_box213 = Death(140, 72, 10, 40, 2)

box214 = Box(130, 113, 8, 64, 2)

# level 3 boxes
box31 = Box(0, 600, 64, 1024, 3)


level_list = []


class level:

    def __init__(self, box_list, death_list, goal):
        self.box_list = box_list
        self.death_list = death_list
        self.goal = goal
        self.level = level

        level_list.append(self)


level1 = level(box_list1, death_list1, goal_1)
level2 = level(box_list2, death_list2, goal_2)
level3 = level(box_list3, death_list3, goal_3)


# main graphical
def keep_drawing(player, death_list, PolarBear, Instruction, Igloo, box_list):
    WIN.blit(Instruction.sprite, (Instruction.x, Instruction.y))
    WIN.blit(player.sprite, (player.x, player.y))

    for d in death_list:
        WIN.blit(d.sprite, (d.x, d.y))

    for box in box_list:
        pygame.draw.rect(WIN, (50, 50, 50), box.rect)

    # WIN.blit(PolarBear.sprite, (PolarBear.x, PolarBear.y))

    WIN.blit(Igloo.sprite, (Igloo.x, Igloo.y))

    # pygame.draw.rect(WIN, (255, 0, 0), player.rect, 2)
    # pygame.draw.rect(WIN, (255, 0, 0), Igloo.rect, 2)
    # pygame.draw.rect(WIN, (50, 50, 50), death.rect, 2)

    pygame.display.update()


start_x = 0
start_y = 512


def reset(player):
    player.x = start_x
    player.y = start_y
    player.rect = pygame.Rect(start_x, start_y, player_width, player_height)


player_width = 64
player_height = 64

polarBear = PolarBear("Polar_Bear", 512, 400, pygame.image.load(
    os.path.join('Images', 'PolarBear.png')), 64, 64)


player = Player("Penguin", 0, 512, runner_model_1, player_width, player_height)
instruction = Instruction("instruction_contents", 25, 15, pygame.image.load(
    os.path.join('Images', 'instruction.jpg')), 64, 64)


def collide_top(player, box_list):
    # check is player is colliding with the top of any box
    for box in box_list:
        # if player.rect.colliderect(box.rect):
        #     return True
        if player.rect.bottom >= box.rect.top and player.rect.bottom <= box.rect.bottom:
            if (player.x >= box.rect.left and player.x <= box.rect.left + box.rect.width) or (player.x + player.rect.width >= box.rect.left and player.x + player.rect.width <= box.rect.left + box.rect.width):
                return True

    return False


def main():
    level_num = 1
    current_level = level1

    jump_up_counter = 0
    jump_down_counter = 0
    jumped = False

    clock = pygame.time.Clock()
    run = True

    while run:

        # starting the game loop
        # Control speed of the while loop. It will run 60 times per second (60 frames per second)
        clock.tick(60)
        for event in pygame.event.get():  # checks event done by user
            if event.type == pygame.QUIT:  # if event is quit
                run = False  # exits game loop
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if jumped is False and player.falling is False:

                        jump_up_counter = 0
                        jump_down_counter = 0
                        jumped = True

        pos = pygame.mouse.get_pos()

        pressed1, pressed2, pressed3 = pygame.mouse.get_pressed()

        if pressed1:
            player.x, player.y = pos
            player.rect = pygame.Rect(pos[0], pos[1], player_width, player_height)
            print(pos)

        keys = pygame.key.get_pressed()

        # moving left to right logic
        if (player.x - 6 >= 0):
            if keys[pygame.K_a]:
                player.move(-6, 0)

        if (player.x + 6 < WIN_WIDTH):
            if keys[pygame.K_d]:
                player.move(6, 0)

        # jumping logic
        if jumped is True:
            if jump_up_counter <= 16:
                player.move(0, -8)
                jump_up_counter += 1
            else:
                if jump_down_counter <= 16:
                    jump_down_counter += 4
                else:
                    jumped = False

        if player.rect.colliderect(current_level.goal.rect):
            level_num += 1
            current_level = level_list[level_num - 1]
            reset(player)

        for d in current_level.death_list:
            if player.rect.colliderect(d.rect):
                reset(player)

        if collide_top(player, current_level.box_list):
            player.falling = False
        else:
            player.falling = True

        if player.falling is True:
            if jumped is False:
                player.move(0, 8)

        WIN.fill(COLOR_BACKGROUND)

        if level_num == 3:
            WIN.blit(pygame.image.load("win screen.png"), (170, 170))

        keep_drawing(player, current_level.death_list, polarBear,
                     instruction, current_level.goal, current_level.box_list)

    pygame.quit()  # pygame will only quit if run is false


if __name__ == "__main__":  # if mario.py is the executable, then execute main
    main()
