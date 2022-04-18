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


death_list = []


class Death:
    def __init__(self, name, x, y, sprite, height, width):
        self.name = name
        self.x = x
        self.y = y
        self.sprite = sprite
        self.rect = pygame.Rect(x, y, width, height)

        death_list.append(self)

    def reveal_all(self):
        print("Your name is ", self.name, " and your score is ", self.score)


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
    def __init__(self, name, x, y, sprite, height, width):
        self.name = name
        self.x = x
        self.y = y
        self.sprite = sprite
        self.rect = pygame.Rect(x, y, width, height)


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
box1 = Box("box1", 0, 600, 64, 1024, 1)
box2 = Box("box2", 64, 580, 64, 64, 1)
box3 = Box("box3", 64, 520, 10, 64, 1)
box4 = Box("box4", 64, 430, 10, 64, 1)
box5 = Box("box5", 725, 108, 10, 500, 1)

# level 2 boxes

# level 3 boxes


def keep_drawing(player, death_list, PolarBear, Instruction, Igloo, box_list):
    WIN.fill(COLOR_BACKGROUND)

    WIN.blit(player.sprite, (player.x, player.y))

    for d in death_list:
        WIN.blit(d.sprite, (d.x, d.y))

    for box in box_list:
        pygame.draw.rect(WIN, (50, 50, 50), box.rect)

    WIN.blit(PolarBear.sprite, (PolarBear.x, PolarBear.y))
    WIN.blit(Instruction.sprite, (Instruction.x, Instruction.y))
    WIN.blit(Igloo.sprite, (Igloo.x, Igloo.y))

    pygame.draw.rect(WIN, (255, 0, 0), player.rect, 2)
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
death_box1 = Death("death_box1", 512, 512, pygame.image.load("death.png"), 64, 64)
death_box2 = Death("death_box2", 512, 330, pygame.image.load("death.png"), 64, 64)

player = Player("Penguin", 0, 512, runner_model_1, player_width, player_height)
instruction = Instruction("instruction_contents", 25, 15, pygame.image.load(
    os.path.join('Images', 'instruction.jpg')), 64, 64)

penguin_home = Igloo("end_goal", 825, -50,
                     pygame.image.load(os.path.join('Images', 'igloo.png')), 64, 64)


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
    current_level = 0
    current_box_list = box_list2

    jump_up_counter = 0
    jump_down_counter = 0
    jumped = False

    # playerName = input("Hey player! Please enter your name: ")
    # user1 = Player(playerName)
    # user1.reveal_all()

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
        if keys[pygame.K_a]:
            player.move(-6, 0)

        elif keys[pygame.K_d]:

            player.move(6, 0)

        WIN.fill(COLOR_BACKGROUND)
        keep_drawing(player, death_list, polarBear, instruction, penguin_home, current_box_list)

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

        if player.rect.colliderect(death_box1.rect) and jumped is False:
            reset(player)

        for d in death_list:
            if player.rect.colliderect(d.rect):
                reset(player)

        if collide_top(player, current_box_list):
            player.falling = False
        else:
            player.falling = True

        if player.falling is True:
            if jumped is False:
                player.y += 8
                player.rect.move_ip(0, 8)

    pygame.quit()  # pygame will only quit if run is false


if __name__ == "__main__":  # if mario.py is the executable, then execute main
    main()
