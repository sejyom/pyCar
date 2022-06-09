#수정00
import random
from time import *
import pygame
from tkinter import *

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 480
heart_count = 5

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GRAY = (150, 150, 150)
CYAN = (0, 242, 242)
ORANGE = (250, 112, 70)
PURPLE = (136, 93, 201)
PINK = (201, 93, 198)
MINT = (0, 255, 183)
MELON = (182, 255, 148)
SKYBLUE = (148, 219, 255)
APRICOT = ( 255, 180, 148)
INDIGO = (14, 37, 92)

score = 0
level = 1
color = '1.png' # 이미지 셀렉 안하면 1.png로!!
car_count = 4
x = 600
y = random.randrange(0, WINDOW_HEIGHT - 55)
# ******Car객체 생성
class Car:
    global image_car
    image_car = ['1.png', '2.png', '3.png', '4.png',
                 '5.png', '6.png', '7.png', '8.png',
                 '9.png', '10.png', '11.png', '12.png',
                 '13.png', '14.png', '15.png', '16.png',
                 '17.png', '18.png', '19.png', '20.png']

    def __init__(self, x=0, y=0, dx=0, dy=0):
        self.image = ""
        self.x = x
        self.y = y
        self.dx = dx  # direction
        self.dy = dy

    def player_image(self, color):
        self.image = pygame.image.load(color)
        self.width = self.image.get_rect().size[0]
        self.height = self.image.get_rect().size[1]
        
    def load_image(self):  # 가져온 이미지 로드
        self.image = pygame.image.load(random.choice(image_car))
        self.width = self.image.get_rect().size[0]
        self.height = self.image.get_rect().size[1]

    def draw_image(self):
        screen.blit(self.image, [self.x, self.y])  # draw

    def move_x(self):  # 실제 좌표 x에 direction 하는 만큼 더해쥼
        self.x += self.dx

    def move_y(self):
        self.y += self.dy

    def check_out_of_screen(self):  # 화면을 넘어가는지 체크
        if self.y + self.height > WINDOW_HEIGHT or self.y < 0:
            self.y -= self.dy
        if self.x < 0 or self.x > WINDOW_WIDTH - 133:
            self.x -= self.dx
        # 실제 자기 위치의 x좌표와 자기의 너비를 더해주면 실제 자동차의 크기가 나오는데 이게 윈도우 창 크기를 넘어가면 안 됨
        # ㄴ 은 창에서 오른쪽으로 넘어갔을 때를 체크
        # 왼쪽 끝은 좌표가 0이니까 그걸 넘어가면 그만큼 빼줘야 됨

    def check_crash(self, car):  # 플레이어의 자동차와 다른 자동차의 충돌 여부를 가려주는 함수
        if (self.y < car.y + car.height) and (car.y < self.y + self.height) and (self.x < car.x + car.width) and (car.x < self.x + self.width):
            return True
        else:
            return False

# ******heart객체 생성
class Teddybear:
    def __init__(self, x, y, dx, dy):
        self.image = ""
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy

    # ******하트곰돌 드랍
    def teddybear_load(self):
        self.image = pygame.image.load('teddybear.png')
        self.width = self.image.get_rect().size[0]
        self.height = self.image.get_rect().size[1]

    def draw_teddybear(self):
        screen.blit(self.image, [self.x, self.y])

    def move_x(self):
        self.x += self.dx

    def move_y(self):
        self.y += self.dy

    def teddybear_crash(self, player):  # 플레이어의 자동차와 곰돌이의 충돌 여부를 가려주는 함수
        if (self.y < player.y + player.height) and (player.y < self.y + self.height) and (self.x < player.x + player.width) and (player.x < self.x + self.width):
            return True
        else:
            return False

# ******장애물 객체 생성
class Obtacle:

    def __init__(self, x, y, dx, dy):
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy

    def obtacle_load(self):
        self.image = pygame.image.load('obtacle.png')
        self.width = self.image.get_rect().size[0]
        self.height = self.image.get_rect().size[1]

    def draw_obtacle(self):
        screen.blit(self.image, [self.x, self.y])

    def move_x(self):
        self.x += self.dx

    def move_y(self):
        self.y = self.dy

    def obtacle_crash(self, player):  # 플레이어의 자동차와 표지판의 충돌 여부를 가려주는 함수
        if (self.y < player.y + player.height) and (player.y < self.y + self.height) and (self.x < player.x + player.width) and (player.x < self.x + self.width):
            return True
        else:
            return False

# ******메인메뉴 그리기
def draw_main_menu():
    draw_x = WINDOW_WIDTH / 2  # 400
    draw_y = (WINDOW_HEIGHT / 2)  # 40

    image_intro = pygame.image.load('PyCar.png')
    screen.blit(image_intro, [draw_x - 350, draw_y - 150])  # PyCar.png (50, 90)
    font_35 = pygame.font.SysFont("arial", 35, True, False)
    font_32 = pygame.font.SysFont("arial", 32, True, True)
    font_25 = pygame.font.SysFont("arial", 25, True, False)

    text_title = font_35.render("PyCar: Racing Car Game", True, BLACK)
    screen.blit(text_title, [draw_x - 50, draw_y - 80])  # 타이틀 출력 (360, 140)
    draw_score()
    draw_level()
    text_start = font_32.render("Press Space Key to Start!", True, RED)  # 스페이스바 누르면 게임 스타트를 알려줌
    screen.blit(text_start, [draw_x - 40, draw_y - 30])
    j=0
    for i in range(len(image_car)): # 1.png ~ 20.png
        img = pygame.image.load(str(i+1)+'.png')
        img = pygame.transform.scale(img, (50, 30))
        if i < 10: #1.png ~ 10.png
            screen.blit(img, [WINDOW_WIDTH / 10 + (i*66), WINDOW_HEIGHT - 120])
        else: # 11.png ~ 20.png
            screen.blit(img, [WINDOW_WIDTH / 10 + (j*66), WINDOW_HEIGHT - 80])
            j+=1
            
    
    pygame.display.flip()  # 실제로 드로잉해주기


# ******게임 중 스코어 출력
def draw_score():
    font_25 = pygame.font.SysFont("arial", 25, True, False)  # 폰트 원하면 다른걸루
    text_score = font_25.render("Score: " + str(score), True, WHITE)  # 플레이어의 득점을 출력
    screen.blit(text_score, [10, 10])  # 좌측 상단에 점수 출력

# ******게임 중 레벨 출력
def draw_level():
    font_25 = pygame.font.SysFont("arial", 25, True, False)
    text_level = font_25.render("Level: " + str(level), True, WHITE)
    screen.blit(text_level, [10, 35])

# ******게임 중 생명 출력
def draw_heart(heart_count):
    for i in range(heart_count):
        if i<5:
            heart_image = pygame.image.load('heart.png')
            heart_image = pygame.transform.scale(heart_image, (30, 30))
            px = WINDOW_WIDTH - 40 - (i*30)
            screen.blit(heart_image, [px, 15])
        else: # 하트 개수가 5개를 넘으면
            font_25 = pygame.font.SysFont("arial", 25, True, False)
            text_heart = font_25.render("+" + str(heart_count - 5), True, WHITE)
            text_heart_x = WINDOW_WIDTH - 70 - (5*30)
            screen.blit(text_heart, [text_heart_x, 25])

# ******레벨에 따른 도로 색 지정
def change_screenColor(level):
    if level == 1:
        screen.fill(GRAY)
    elif level == 2:
        screen.fill(CYAN)
    elif level == 3:
        screen.fill(ORANGE)
    elif level == 4:
        screen.fill(PURPLE)
    elif level == 5:
        screen.fill(PINK)
    elif level == 6:
        screen.fill(MINT)
    elif level == 7:
        screen.fill(MELON)
    elif level == 8:
        screen.fill(SKYBLUE)
    elif level == 9:
        screen.fill(APRICOT)
    elif level == 10:
        screen.fill(INDIGO)

def select_color():
    global color_entry
    global win
    win = Tk()
    win.title("Select Color")
    notice=Label(win, text='Input Color Number', width = 20)
    notice.grid(row = 0, column = 0)
    color_entry = Entry(win)
    color_entry.grid(row = 1, column = 0)
    inbutton = Button(win, text = "Select", width = 20, command = clicked)
    inbutton.grid(row = 2, column = 0, columnspan = 2)
    win.mainloop()

def clicked():
    global color
    for i in image_car:
        if i == color_entry.get()+'.png':
            color = i
    win.destroy()

if __name__ == '__main__':
        pygame.init()

        screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT)) # 스크린 크기 잡아줌
        pygame.display.set_caption("PyCar: Racing Car Game")
        clock = pygame.time.Clock()
        screen.fill((150, 150, 150)) # 화면 회색(도로색)으로

        pygame.mixer.music.load('race.wav')  # 게임 시작되는 음향 삽입
        sound_crash = pygame.mixer.Sound('crash.wav')  # 충돌 사운드
        sound_engine = pygame.mixer.Sound('engine.wav')  # 게임 시작 시 나는 엔진 소리

        player = Car(30, WINDOW_HEIGHT / 2, 0, 0)  # Player 객체 생성

        player.player_image(color)
        heart_count = 5
        # 상대 자동차 드롭
        cars = []
        for i in range(car_count):
            car = Car(x, y, random.randint(5, 7), 0)
            car.load_image()
            cars.append(car)

        # 하트곰 드롭
        heart_bears = []
        for i in range(2):
            heart_bear = Teddybear(x, y, random.randint(5, 8), 0)
            heart_bear.teddybear_load()
            heart_bears.append(heart_bear)

        # 장애물 표지판 드롭
        stops = []
        for i in range(3):
            stop = Obtacle(x, y, random.randint(5, 8), 0)
            stop.obtacle_load()
            stops.append(stop)
            
        # 중앙선 그리기
        lanes = []
        lane_width = 180
        lane_height = 10
        lane_margin = 20
        lane_count = 20  # 화면 내에 20개의 사각형 모양 차선이 계속 돌게끔
        lane_x = 800
        lane_y = (WINDOW_HEIGHT - lane_height) / 2
        for i in range(lane_count):  # 20개의 사각형 모양 차선 만듦
            lanes.append([lane_x, lane_y])
            lane_x += lane_width + lane_margin

        crash = True  # 충돌 여부 불리언 타입 변수
        game_on = True  # 게임이 실행중인지를 확인

        # ******게임 중
        while game_on:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:  # event.type이 QUIT면 False로 바꿔서 게임 나가게끔
                    game_on = False
                
                if crash:  # 충돌 났으면
                    if event.type == pygame.KEYDOWN and event.key == pygame.K_0:
                        select_color()
                    if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:  # 스페이스 버튼이 눌렸으면 게임 시작
                    
                        crash = False  # 충돌 여부를 False로 바꿔 다시 시작되게
                        score = 0  # 점수 초기화
                        level = 1
                        heart_count = 5

                        # 장애물 자동차의 위치를 다시 잡음
                        for i in range(car_count):
                            cars[i].x = random.randrange(770, 800)
                            cars[i].y = random.randrange(0, WINDOW_HEIGHT - cars[i].y)
                            cars[i].load_image()

                        player.player_image(color)  # 플레이어 이미지도 바꿔줌
                        player.x = 10
                        player.dx = 0
                        player.y = WINDOW_HEIGHT / 2
                        player.dy = 0
                        pygame.mouse.set_visible(False)  # 화면에 마우스 안 보이게
                        sound_engine.play()  # 스페이스 누르면 엔진소리 들리게
                        sleep(0.5)
                        pygame.mixer.music.play(-1)  # -1을 주면 소리파일 무한루프

                # ******충돌 안 났으면
                if not crash:
                    if event.type == pygame.KEYDOWN:  # 키 눌렀을 때
                        if event.key == pygame.K_RIGHT:
                            player.dx = 6
                        elif event.key == pygame.K_LEFT:
                            player.dx = -6  # 좌우

                        elif event.key == pygame.K_UP:
                            player.dy = -6
                        elif event.key == pygame.K_DOWN:
                            player.dy = 6  # 상하 추가

                    if event.type == pygame.KEYUP:  # 키 뗐을 때
                        if event.key == pygame.K_RIGHT:
                            player.dx = 0  # 움직이면 안 되니까 0으로 잡아줌
                        elif event.key == pygame.K_LEFT:
                            player.dx = 0  # 좌우

                        elif event.key == pygame.K_UP:
                            player.dy = 0
                        elif event.key == pygame.K_DOWN:
                            player.dy = 0  # 상하

            change_screenColor(level)

            if level == 3:
                car_count = 5
                car = Car(x, y, random.randint(4, 8), 0)
                car.load_image()
                cars.append(car)
            if level == 5:
                car_count = 6
                car = Car(x, y, random.randint(4, 8), 0)
                car.load_image()
                cars.append(car)
            if level == 7:
                car_count = 7
                car = Car(x, y, random.randint(4, 8), 0)
                car.load_image()
                cars.append(car)
            if level == 9:
                car_count = 8
                car = Car(x, y, random.randint(5, 10), 0)
                car.load_image()
                cars.append(car)

            if not crash:  # 충돌 안 났으니까 차선 계속 움직여줌
                for i in range(lane_count):
                    pygame.draw.rect(screen, WHITE, [lanes[i][0], lanes[i][1], lane_width, lane_height])
                    lanes[i][0] += 10  # 차선 내려오는 속도 알아서 조정
                    if lanes[i][0] > WINDOW_WIDTH:  # 전체 게임 크기를 차선이 넘어갔을 때
                        lanes[i][0] = -40 - lane_width

                player.draw_image()  # 플레이어 자동차 그림
                player.move_x()  # 키 조작에 따라 좌우로 움직임 x축만 건드림
                player.move_y()  # y축 추가 (상하)
                player.check_out_of_screen()  # 플레이어의 차가 스크린을 벗어나는지 체크
                if level >= 2:
                    for i in range(2):
                        stops[i].draw_obtacle()
                        stops[i].x -= stops[i].dx

                        if stops[i].obtacle_crash(player):
                            score -= 10
                            heart_count -= 2
                            draw_heart(heart_count)
                            if heart_count <= 0:
                                crash = True
                                pygame.mixer.music.stop()  # 레이싱 음악 종료
                                sound_crash.play()  # 추돌소리 삽입
                                pygame.mouse.set_visible(True)  # 겜 끝났으니까 마우스 보이게 설정
                                draw_main_menu()

                            stops[i].x = random.randrange(770, 800)
                            stops[i].y = random.randrange(0, WINDOW_HEIGHT - stops[i].height)
                            stops[i].obtacle_load()
                        if stops[i].x < 0:
                            stops[i].x = random.randrange(770, 800)
                            stops[i].y = random.randrange(0, WINDOW_HEIGHT - stops[i].height)
                            stops[i].dx = random.randint(4, 7)
                            stops[i].obtacle_load()
                if level >= 3:
                    for i in range(2):  # 하트 곰돌이 내려오게
                        heart_bears[i].draw_teddybear()
                        heart_bears[i].x -= heart_bears[i].dx  # 내려오는 곰들은 x축만 건드림

                        if heart_bears[i].teddybear_crash(player):
                            # 하트 곰돌이와 플레이어가 충돌하고 있는지 아닌지
                            heart_count += 1
                            draw_heart(heart_count)

                            heart_bears[i].x = random.randrange(770, 800)
                            heart_bears[i].y = random.randrange(0, WINDOW_HEIGHT - heart_bears[i].height)
                            heart_bears[i].teddybear_load()
                        if heart_bears[i].x < 0:
                            heart_bears[i].x = random.randrange(770, 800)
                            heart_bears[i].y = random.randrange(0, WINDOW_HEIGHT - heart_bears[i].height)
                            heart_bears[i].dx = random.randint(5, 8)  # 내려오는 곰돌이들 속도 정해줌
                            heart_bears[i].teddybear_load()  # 곰돌이 다시 그려주기

                for i in range(car_count):  # 장애물 자동차 내려오게
                    cars[i].draw_image()
                    cars[i].x -= cars[i].dx  # 내려오는 차들은 x축만 건드림
                    if cars[i].x < 0:
                        # 내려오는 자동차들이 화면을 벗어났을 경우
                        score += 10  # 피했으니까 점수 주기
                        if score % 200 == 0:  # 200점씩 딸 때마다 레벨 업
                            level += 1
                        cars[i].x = random.randrange(770, 800)
                        cars[i].y = random.randrange(0, WINDOW_HEIGHT - cars[i].height)
                        cars[i].dx = random.randint(4, 8)  # 내려오는 차들 속도 정해줌
                        cars[i].load_image()  # 자동차 그려주기


                for i in range(car_count):
                    if player.check_crash(cars[i]):
                        # 플레이어의 차가 내려오는 차들과 충돌 하고 있는지 아닌지
                        heart_count -= 1
                        if heart_count == 0:
                            crash = True
                            pygame.mixer.music.stop()  # 레이싱 음악 종료
                            sound_crash.play()  # 추돌소리 삽입
                            pygame.mouse.set_visible(True)  # 겜 끝났으니까 마우스 보이게 설정
                            break
                        if player.x+player.width > cars[i].x:
                            # 장애물 자동차의 위치를 다시 잡아줌
                            cars[i].x = random.randrange(770, 800)
                            cars[i].y = random.randrange(0, WINDOW_HEIGHT - cars[i].height)
                            cars[i].load_image()
                        if heart_count <= 0:
                            crash = True
                            pygame.mixer.music.stop()  # 레이싱 음악 종료
                            sound_crash.play()  # 추돌소리 삽입
                            pygame.mouse.set_visible(True)  # 겜 끝났으니까 마우스 보이게 설정
                            break

                draw_score()  # 점수 보여주는 함수
                draw_level()
                draw_heart(heart_count)
                pygame.display.flip()

            else:  # 충돌 났으면 게임 다시 해야함
                draw_main_menu()  # 메인메뉴 보여줌

            clock.tick(60)

        pygame.quit()  # 종료
