import pygame
import sys
import random
pygame.font.init()
from collections import Counter

class DICE:
    def __init__(self, x, y):
        self.active = True
        self.x = x
        self.y = y
        self.number = 0
        self.one = pygame.transform.scale(pygame.image.load("Desktop/GameCreations/one.png"), (dsize, dsize)).convert_alpha()
        self.two = pygame.transform.scale(pygame.image.load("Desktop/GameCreations/two.png"), (dsize, dsize)).convert_alpha()
        self.three = pygame.transform.scale(pygame.image.load("Desktop/GameCreations/three.png"), (dsize, dsize)).convert_alpha()
        self.four = pygame.transform.scale(pygame.image.load("Desktop/GameCreations/four.png"), (dsize, dsize)).convert_alpha()
        self.five = pygame.transform.scale(pygame.image.load("Desktop/GameCreations/five.png"), (dsize, dsize)).convert_alpha()
        self.six = pygame.transform.scale(pygame.image.load("Desktop/GameCreations/six.png"), (dsize, dsize)).convert_alpha()
        self.face = self.one
        self.dice_rect = pygame.Rect(int(self.x), int(self.y), dsize, dsize)

    def draw_dice(self):
        self.number = random.randint(1, 6)
        if self.number == 1: self.face = self.one
        elif self.number == 2: self.face = self.two
        elif self.number == 3: self.face = self.three
        elif self.number == 4: self.face = self.four
        elif self.number == 5: self.face = self.five
        elif self.number == 6: self.face = self.six
        dice_rect = pygame.Rect(int(self.x), int(self.y), dsize, dsize)
        screen.blit(self.face, dice_rect)
    def rest_dice(self):
        dice_rect = pygame.Rect(int(self.x), int(self.y), dsize, dsize)
        screen.blit(self.face, dice_rect)

class BOX:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.rect = pygame.Rect(x, y, width, height)
        self.value = 0
        self.active = True
        self.text = font.render("", 1, "black")

class MAIN:
    def __init__(self):
        self.extra_35 = True
        self.bottom_total = 0 #Bottom sum
        self.bottom_count = 0 #Boxes filled of bottom
        self.round = 0
        self.round_text = font.render(f"rolls left: 3", 1, "black")
        self.summation = 0 # sum of top
        self.top = 0 #Boxes filled of top
        self.dice_list = []
        self.box_totals = []
        for i in range(5):
            die = DICE(5, (i * (dsize + 8) + 5))
            self.dice_list.append(die)
        self.boxes = []
        self.ones = BOX(438, 150, 50, 30)
        self.boxes.append([self.ones.rect, self.ones.text])
        self.twos = BOX(438, 185, 50, 30)
        self.boxes.append([self.twos.rect, self.twos.text])
        self.threes = BOX(438, 220, 50, 30)
        self.boxes.append([self.threes.rect, self.threes.text])
        self.fours = BOX(438, 255, 50, 30)
        self.boxes.append([self.fours.rect, self.fours.text])
        self.fives = BOX(438, 292, 50, 30)
        self.boxes.append([self.fives.rect, self.fives.text])
        self.sixes = BOX(438, 328, 50, 30)
        self.boxes.append([self.sixes.rect, self.sixes.text])
        self.boxes_objects = [self.ones, self.twos, self.threes, self.fours, self.fives, self.sixes]

        self.extra = []
        self.total_score = BOX(438, 358, 50, 20)
        self.extra.append([self.total_score.rect, self.total_score.text])
        self.bonus_score = BOX(438, 385, 50, 25)
        self.extra.append([self.bonus_score.rect, self.bonus_score.text])
        self.total = BOX(438, 416, 50, 20)
        self.extra.append([self.total.rect, self.total.text])
        self.total_lower = BOX(438, 696, 50, 30)
        self.extra.append([self.total_lower.rect, self.total_lower.text])
        self.total_upper = BOX(438, 732, 50, 30)
        self.extra.append([self.total_upper.rect, self.total_upper.text])
        self.grand_total = BOX(438, 767, 50, 20)
        self.extra.append([self.grand_total.rect, self.grand_total.text])

        self.exact_score = []
        self.full_house = BOX(438, 534, 50, 15)
        self.exact_score.append([self.full_house.rect, self.full_house.text])
        self.small_straight = BOX(438, 556, 50, 15)
        self.exact_score.append([self.small_straight.rect, self.small_straight.text])
        self.large_straight = BOX(438, 580, 50, 15)
        self.exact_score.append([self.large_straight.rect, self.large_straight.text])
        self.yahtzee = BOX(438, 601, 50, 15)
        self.exact_score.append([self.yahtzee.rect, self.yahtzee.text])
        self.exact_score_objects = [self.full_house, self.small_straight, self.large_straight, self.yahtzee]

        self.three_kind = BOX(438, 460, 50, 30)
        self.box_totals.append([self.three_kind.rect, self.three_kind.text])
        self.four_kind = BOX(438, 497, 50, 30)
        self.box_totals.append([self.four_kind.rect, self.four_kind.text])
        self.chance = BOX(438, 625, 50, 30)
        self.box_totals.append([self.chance.rect, self.chance.text])
        self.box_totals_objects = [self.three_kind, self.four_kind, self.chance]

    def find_box_num(self, index):
        if index == 0:
            return 1
        elif index == 1:
            return 2
        elif index == 2:
            return 3
        elif index == 3:
            return 4
        elif index == 4:
            return 5
        elif index == 5:
            return 6

    def drawer(self):
        screen.blit(score_sheet, (200, 0))
        for die in self.dice_list:
            die.rest_dice()
        pygame.draw.line(screen, "black", ((200, 0)), ((200, 800)), width=5)
        for i in range(len(self.boxes)):
            pygame.draw.rect(screen, (255, 255, 255), self.boxes[i][0])
            screen.blit(self.boxes[i][1], self.boxes[i][0])
        for i in range(len(self.extra)):
            pygame.draw.rect(screen, (255, 255, 255), self.extra[i][0])
            screen.blit(self.extra[i][1], self.extra[i][0])
        for i in range(len(self.exact_score)):
            pygame.draw.rect(screen, (255, 255, 255), self.exact_score[i][0])
            screen.blit(self.exact_score[i][1], self.exact_score[i][0])
        for i in range(len(self.box_totals)):
            pygame.draw.rect(screen, (255, 255, 255), self.box_totals[i][0])
            screen.blit(self.box_totals[i][1], self.box_totals[i][0])
    
    def round_drawer(self):
        self.round_text = font.render(f"rolls left: {3 - self.round}", 1, "black")
        screen.blit(self.round_text, (5, 300))
        pygame.display.update()

    def dice_roller(self):
        for i in range(20):
            if self.dice_list[0].active: self.dice_list[0].draw_dice()
            if self.dice_list[1].active: self.dice_list[1].draw_dice()
            if self.dice_list[2].active: self.dice_list[2].draw_dice()
            if self.dice_list[3].active: self.dice_list[3].draw_dice()
            if self.dice_list[4].active: self.dice_list[4].draw_dice()
            pygame.display.update()
            pygame.time.delay(100)
        self.round += 1

    def check(self, mouse):
        mouse_square = pygame.Rect(mouse[0], mouse[1], 1, 1)
        die_faces = []
        for die in self.dice_list:
            die_faces.append(die.number)
        counts = Counter(die_faces)
        most_frequent, the_count = counts.most_common(1)[0]
        items = Counter(die_faces).keys()
        for die in self.dice_list:
            if die.dice_rect.colliderect(mouse_square):
                if die.active: 
                    die.active = False
                    die.x += 30
                    die.dice_rect.x += 30
                elif not die.active: 
                    die.active = True
                    die.x -= 30
                    die.dice_rect.x -= 30
        for i in range(len(self.boxes)):
            if self.round == 0 and self.boxes[i][0].colliderect(mouse_square):
                need_num = font.render("You Must Roll!", 1, "black")
                screen.blit(need_num, (5, 600))
                pygame.display.update()
                pygame.time.delay(500)
            elif self.boxes[i][0].colliderect(mouse_square) and self.boxes_objects[i].active:
                self.top += 1
                self.round = 0
                num = self.dice_count(self.find_box_num(i))
                if i == 0:
                    self.ones.value = num
                    self.boxes[i][1] = font.render(f"{num}", 1, "black")
                    self.ones.active = False
                if i == 1:
                    self.twos.value = num
                    self.boxes[i][1] = font.render(f"{num}", 1, "black")
                    self.twos.active = False
                if i == 2:
                    self.threes.value = num
                    self.boxes[i][1] = font.render(f"{num}", 1, "black")
                    self.threes.active = False
                if i == 3:
                    self.fours.value = num
                    self.boxes[i][1] = font.render(f"{num}", 1, "black")
                    self.fours.active = False
                if i == 4:
                    self.fives.value = num
                    self.boxes[i][1] = font.render(f"{num}", 1, "black")
                    self.fives.active = False
                if i == 5:
                    self.sixes.value = num
                    self.boxes[i][1] = font.render(f"{num}", 1, "black")
                    self.sixes.active = False
                self.summation += num
                self.boxes[i][1] = font.render(f"{num}", 1, "black")
                self.reset_dice()
        for i in range(len(self.box_totals)):
            if self.round == 0 and self.box_totals[i][0].colliderect(mouse_square):
                need_num = font.render("You Must Roll!", 1, "black")
                screen.blit(need_num, (5, 600))
                pygame.display.update()
                pygame.time.delay(500)
            elif self.box_totals[i][0].colliderect(mouse_square) and self.box_totals_objects[i].active:
                self.bottom_count += 1
                self.round = 0
                all_die = 0
                for die in self.dice_list:
                    all_die += die.number
                if i == 0 or i == 1:
                    if (the_count < 3 and i == 0) or (the_count < 4 and i == 1):
                        all_die = 0
                if (i == 0 and self.three_kind.active):
                    self.three_kind.value = all_die
                    self.box_totals[i][1] = font.render(f"{all_die}", 1, "black")
                    self.three_kind.active = False
                if i == 1 and self.four_kind.active:
                    self.four_kind.value = all_die
                    self.box_totals[i][1] = font.render(f"{all_die}", 1, "black")
                    self.four_kind.active = False
                if i == 2 and self.chance.active:
                    self.chance.value = all_die
                    self.box_totals[i][1] = font.render(f"{all_die}", 1, "black")
                    self.chance.active = False
                self.reset_dice()
        for i in range(len(self.exact_score)):
            if self.round == 0 and self.exact_score[i][0].colliderect(mouse_square):
                need_num = font.render("You Must Roll!", 1, "black")
                screen.blit(need_num, (5, 600))
                pygame.display.update()
                pygame.time.delay(500)
            elif self.exact_score[i][0].colliderect(mouse_square) and self.exact_score_objects[i].active:
                self.bottom_count += 1
                self.round = 0
                if self.full_house.active and i == 0:
                    if the_count == 3 and len(items) == 2:
                        self.exact_score[i][1] = font.render(f"25", 1, "black")
                        self.full_house.value = 25
                    else:
                        self.exact_score[i][1] = font.render(f"0", 1, "black")
                    self.full_house.active = False
                if self.small_straight.active and i == 1:
                    if (6 in die_faces and 5 in die_faces and 4 in die_faces and 3 in die_faces) or (5 in die_faces and 4 in die_faces and 3 in die_faces and 2 in die_faces) or (4 in die_faces and 3 in die_faces and 2 in die_faces and 1 in die_faces):
                        self.exact_score[i][1] = font.render(f"30", 1, "black")
                        self.small_straight.value = 30
                    else:
                        self.exact_score[i][1] = font.render(f"0", 1, "black")
                    self.small_straight.active = False
                if self.large_straight.active and i == 2:
                    if the_count == 1 and (6 not in die_faces or 1 not in die_faces):
                        self.exact_score[i][1] = font.render(f"40", 1, "black")
                        self.large_straight.value = 40
                    else:
                        self.exact_score[i][1] = font.render(f"0", 1, "black")
                    self.large_straight.active = False
                if self.yahtzee.active and i == 3:
                    if the_count == 5:
                        self.exact_score[i][1] = font.render(f"50", 1, "black")
                        self.yahtzee.value = 50
                    else:
                        self.exact_score[i][1] = font.render(f"0", 1, "black")
                    self.yahtzee.active = False
                self.reset_dice()
        if self.top >= 6:
            self.extra[0][1] = font.render(f"{self.summation}", 1, "black")
            if self.summation >= 63 and self.extra_35:
                self.summation += 35
                self.extra[1][1] = font.render(f"35", 1, "black")
                self.extra_35 = False
            elif self.extra_35:
                self.extra[1][1] = font.render(f"0", 1, "black")
                self.extra_35 = False
            self.extra[2][1] = font.render(f"{self.summation}", 1, "black")
            self.extra[4][1] = font.render(f"{self.summation}", 1, "black")
        if self.bottom_count >= 7:
            counting = 0
            counting += self.three_kind.value
            counting += self.four_kind.value
            counting += self.full_house.value
            counting += self.small_straight.value
            counting += self.large_straight.value
            counting += self.yahtzee.value
            counting += self.chance.value
            self.extra[3][1] = font.render(f"{counting}", 1, "black")
        if self.bottom_count >= 7 and self.top >= 6:
            self.extra[5][1] = font.render(f"{self.summation + counting}", 1, "black")

    def dice_count(self, number):
        count = 0
        for die in self.dice_list:
            if die.number == number:
                count += number
        return count
    
    def reset_dice(self):
        for die in self.dice_list:
            if not die.active:
                die.x -= 30
                die.dice_rect.x -= 30
                die.active = True

height = 800
width = 800
dsize = 50
screen = pygame.display.set_mode((width, height))
score_sheet = pygame.transform.scale(pygame.image.load("Desktop/GameCreations/sheet.webp"), (600, 800)).convert_alpha()
clock = pygame.time.Clock()
font = pygame.font.SysFont("timesnewroman", 20)

pygame.init()
main_game = MAIN()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                main_game.dice_roller()
        if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                main_game.check(pos)
        while main_game.round >= 3:
            need_num = font.render("Choose a box!", 1, "black")
            screen.blit(need_num, (5, 600))
            main_game.round_drawer()
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONUP:
                    pos = pygame.mouse.get_pos()
                    main_game.check(pos)
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
    screen.fill((216, 235, 221))
    main_game.drawer()
    main_game.round_drawer()
    pygame.display.update()
    clock.tick(60)
 