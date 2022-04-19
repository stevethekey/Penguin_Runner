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
    def __init__(self, x, y, height, width, sprite, level):
        self.x = x
        self.y = y
        self.sprite = sprite
        self.rect = pygame.Rect(x, y, width, height)
        self.level = level

        if level == 1:
            death_list1.append(self)


deathSpike_1 = Death(250, 568, 16, 32, pygame.image.load(os.path.join('Images', 'spikes_up.png')), 1)
deathSpike_2 = Death(282, 568, 16, 32, pygame.image.load(os.path.join('Images', 'spikes_up.png')), 1)
deathSpike_3 = Death(314, 568, 16, 32, pygame.image.load(os.path.join('Images', 'spikes_up.png')), 1)


deathSpike2_1 = Death(550, 568, 16, 32, pygame.image.load(os.path.join('Images', 'spikes_up.png')), 1)
deathSpike2_2 = Death(582, 568, 16, 32, pygame.image.load(os.path.join('Images', 'spikes_up.png')), 1)
deathSpike2_3 = Death(614, 568, 16, 32, pygame.image.load(os.path.join('Images', 'spikes_up.png')), 1)
deathSpike2_4 = Death(646, 568, 16, 32, pygame.image.load(os.path.join('Images', 'spikes_up.png')), 1)



death_down = Death(512, 330, 16, 32, pygame.image.load(os.path.join('Images', 'spikes.png')), 1)



class PolarBear:
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

class Instruction:
    def __init__(self, name, x, y, sprite, height, width):
        self.name = name
        self.x = x
        self.y = y
        self.sprite = pygame.image.load(os.path.join('Images', 'instruction.jpg'))
        self.rect = pygame.Rect(x, y, width, height)


goal_1 = Igloo(825, -50, 64, 64)

goal_2 = Igloo(512, 512, 64, 64)

goal_3 = Igloo(512, 512, 64, 64)


box_list1 = []
box_list2 = []
box_list3 = []


class Box:

    def __init__(self, name, x, y, height, width, level):
        self.name = name
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
box_FLOOR = Box("box1", 0, 600, 64, 1024, 1)


igloo_FLOOR = Box("box5", 725, 108, 10, 500, 1)

# level 2 boxes
box1 = Box("box1", 0, 600, 64, 1024, 2)

# level 3 boxes

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
def keep_drawing(player, death_list, Instruction, Igloo, box_list):
    WIN.fill(COLOR_BACKGROUND)

    WIN.blit(player.sprite, (player.x, player.y))

    for d in death_list:
        WIN.blit(d.sprite, (d.x, d.y))

    for box in box_list:
        pygame.draw.rect(WIN, (50, 50, 50), box.rect)

    WIN.blit(Instruction.sprite, (Instruction.x, Instruction.y))
    WIN.blit(Igloo.sprite, (Igloo.x, Igloo.y))

    pygame.draw.rect(WIN, (255, 0, 0), player.rect, 2)
    for a in death_list:
        pygame.draw.rect(WIN, (50, 50, 50), a.rect , 2)

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

        keys = pygame.key.get_pressed()

        # moving left to right logic
        if (player.x - 6 >= 0):
            if keys[pygame.K_a]:
                player.move(-6, 0)

        if (player.x + 6 >= 0):
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
                player.y += 8
                player.rect.move_ip(0, 8)

        WIN.fill(COLOR_BACKGROUND)
        keep_drawing(player, current_level.death_list, instruction, current_level.goal, current_level.box_list)

    pygame.quit()  # pygame will only quit if run is false


if __name__ == "__main__":  # if mario.py is the executable, then execute main
    main()
