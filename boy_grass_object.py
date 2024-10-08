from pico2d import *
import random

# Game object class here
class Grass:
    #생성자를 이용해서 객체의 초기 상태를 정의
    def __init__(self):
        self.image = load_image("grass.png")

    def update(self):
        pass

    def draw(self):
        self.image.draw(400,30)

    pass

class Boy:
    def __init__(self):
        self.x, self.y = random.randint(100, 300), 90
        self.frame = 0

        self.image = load_image("run_animation.png")

    def update(self):
        self.frame = random.randint(0 ,7)
        self.x += 8


    def draw(self):
        self.image.clip_draw(self.frame *100, 0, 100, 100, self.x , self.y)


class Ball2:
    def __init__(self):
        self.x, self.y = random.randint(100, 700), 599
        self.image = load_image("ball21x21.png")

    def update(self):
        self.frame = 0
        if self.y > 60:
            self.y -= random.randint(0,7)
        else:
            self.y -= 0


    def draw(self):
        self.image.draw(self.x , self.y)

class Ball1:
    def __init__(self):
        self.x, self.y = random.randint(100, 700), 599
        self.image = load_image("ball41x41.png")

    def update(self):
        self.frame = 0
        if self.y > 70:
            self.y -= random.randint(0,7)
        else:
            self.y -= 0


    def draw(self):
        self.image.draw(self.x , self.y)

def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

def update_world():
    for o in world:
        o.update()

def render_world():
    clear_canvas()
    for o in world:
        o.draw()
    update_canvas()

def reset_world():
    global count
    global running
    global grass
    global team
    global balls1
    global balls2
    global world
    running = True
    world = []
    count = random.randint(0,20)
    grass = Grass() #Grass 클래스 이용해서 grass 찍어내기
    world.append(grass)
    team = [Boy() for i in range(11)]
    balls2 = [Ball2() for i in range(count)]
    balls1 = [Ball1() for i in range(20 - count)]
    world += team
    world += balls2
    world += balls1
open_canvas()

# initialization code
reset_world()

# game main loop code
while running:
    handle_events()
    update_world()
    render_world()
    delay(0.05)
# finalization code

close_canvas()
