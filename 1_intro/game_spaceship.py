# program template for Spaceship
import simplegui
import math
import random

# globals for user interface
WIDTH = 800
HEIGHT = 600
score = 0
lives = 3
time = 0
friction_rate = 0.005
started = False


# Game state class
# game = Game(xxxxxx)

class ImageInfo:
    def __init__(self, center, size, radius=0, lifespan=None, animated=False):
        self.center = center
        self.size = size
        self.radius = radius
        if lifespan:
            self.lifespan = lifespan
        else:
            self.lifespan = float('inf')
        self.animated = animated

    def get_center(self):
        return self.center

    def get_size(self):
        return self.size

    def get_radius(self):
        return self.radius

    def get_lifespan(self):
        return self.lifespan

    def get_animated(self):
        return self.animated


# art assets created by Kim Lathrop, may be freely re-used in non-commercial projects, please credit Kim

# debris images - debris1_brown.png, debris2_brown.png, debris3_brown.png, debris4_brown.png
#                 debris1_blue.png, debris2_blue.png, debris3_blue.png, debris4_blue.png, debris_blend.png
debris_info = ImageInfo([320, 240], [640, 480])
debris_image = simplegui.load_image(
    "http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/debris2_blue.png")

# nebula images - nebula_brown.png, nebula_blue.png
nebula_info = ImageInfo([400, 300], [800, 600])
nebula_image = simplegui.load_image(
    "http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/nebula_blue.f2014.png")

# splash image
splash_info = ImageInfo([200, 150], [400, 300])
splash_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/splash.png")

# ship image
ship_info = ImageInfo([45, 45], [90, 90], 35)
ship_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/double_ship.png")

# missile image - shot1.png, shot2.png, shot3.png
missile_info = ImageInfo([5, 5], [10, 10], 3, 150)
missile_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/shot2.png")

# asteroid images - asteroid_blue.png, asteroid_brown.png, asteroid_blend.png
asteroid_info = ImageInfo([45, 45], [90, 90], 40)
asteroid_image = simplegui.load_image(
    "http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/asteroid_blue.png")

# animated explosion - explosion_orange.png, explosion_blue.png, explosion_blue2.png, explosion_alpha.png
explosion_info = ImageInfo([64, 64], [128, 128], 17, 24, True)
explosion_image = simplegui.load_image(
    "http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/explosion_alpha.png")

# sound assets purchased from sounddogs.com, please do not redistribute
soundtrack = simplegui.load_sound(
    "http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/soundtrack.mp3")
soundtrack2 = simplegui.load_sound(
    "https://storage.googleapis.com/codeskulptor-assets/ricerocks_theme.mp3")
missile_sound = simplegui.load_sound(
    "http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/missile.mp3")
missile_sound.set_volume(.4)
ship_thrust_sound = simplegui.load_sound(
    "http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/thrust.mp3")
explosion_sound = simplegui.load_sound(
    "http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/explosion.mp3")


# alternative upbeat soundtrack by composer and former IIPP student Emiel Stopler
# please do not redistribute without permission from Emiel at http://www.filmcomposer.nl


# helper functions to handle transformations
def angle_to_vector(ang):
    return [math.cos(ang), math.sin(ang)]


def dist(p, q):
    """
    helper function to calculate distance between two points in 2D
    """
    return math.sqrt((p[0] - q[0]) ** 2 + (p[1] - q[1]) ** 2)


def process_sprite_group(sprite_set, canvas):
    """
    helper function takes a set and a canvas and call the update and draw methods
    for each sprite in the group
    """
    shadow_set = set(sprite_set)
    for sprite in shadow_set:
        sprite.draw(canvas)
        if sprite.update():
            sprite_set.remove(sprite)


# take a set group and a sprite other_object and check for collisions between other_object and elements of the group
def group_collide(group, other_object):
    shadow_group = set(group)
    for elem in shadow_group:
        if elem.collide(other_object):
            new_explosion = Sprite(elem.get_position(), [0, 0], 0, 0,
                                   explosion_image, explosion_info, explosion_sound)
            explosion_group.add(new_explosion)
            group.remove(elem)
            return True
    return False


def group_group_collide(group_one, group_two):
    shadow_group = set(group_one)
    elements_collide = 0
    for elem in shadow_group:
        if group_collide(group_two, elem):
            elements_collide += 1
            group_one.discard(elem)
    return elements_collide


# Ship class
class Ship:
    def __init__(self, pos, vel, angle, image, info):
        self.pos = [pos[0], pos[1]]
        self.vel = [vel[0], vel[1]]
        self.thrust = False
        self.angle = angle
        self.angle_vel = 0
        self.forward_vector = []
        self.image = image
        self.image_center = info.get_center()
        self.image_size = info.get_size()
        self.radius = info.get_radius()

    def get_position(self):
        return self.pos

    def get_radius(self):
        return self.radius

    def draw(self, canvas):
        if self.thrust:
            canvas.draw_image(self.image, (self.image_center[0] * 3, self.image_center[1]), self.image_size,
                              self.pos, self.image_size, math.radians(self.angle))
        else:
            canvas.draw_image(self.image, self.image_center, self.image_size,
                              self.pos, self.image_size, math.radians(self.angle))

    def update(self):
        # update position
        self.pos[0] = (self.pos[0] + self.vel[0]) % WIDTH
        self.pos[1] = (self.pos[1] + self.vel[1]) % HEIGHT

        # update angle
        self.angle += self.angle_vel

        # define acceleration vector and use it during thrust on
        self.forward_vector = angle_to_vector(math.radians(self.angle))
        if self.thrust:
            self.vel[0] = self.vel[0] + 0.03 * self.forward_vector[0]
            self.vel[1] = self.vel[1] + 0.03 * self.forward_vector[1]

        # add friction
        self.vel[0] *= (1 - friction_rate)
        self.vel[1] *= (1 - friction_rate)

    def turn_right(self):
        self.angle_vel += 2

    def turn_left(self):
        self.angle_vel -= 2

    def thrusters_burst(self, status):
        self.thrust = status
        if self.thrust:
            ship_thrust_sound.play()
        else:
            ship_thrust_sound.rewind()
        print(str(status))

    def shoot(self):
        global missile_group
        missile = Sprite(
            [self.pos[0] + self.radius * self.forward_vector[0], self.pos[1] + self.radius * self.forward_vector[1]],
            [self.vel[0] + self.forward_vector[0] * 2, self.vel[1] + self.forward_vector[1] * 2],
            0, 0, missile_image, missile_info, missile_sound)
        missile_group.add(missile)


# Sprite class
class Sprite:
    def __init__(self, pos, vel, ang, ang_vel, image, info, sound=None):
        self.pos = [pos[0], pos[1]]
        self.vel = [vel[0], vel[1]]
        self.angle = ang
        self.angle_vel = ang_vel
        self.image = image
        self.image_center = info.get_center()
        self.image_size = info.get_size()
        self.radius = info.get_radius()
        self.lifespan = info.get_lifespan()
        self.animated = info.get_animated()
        self.age = 0
        if sound:
            sound.rewind()
            sound.play()

    def get_position(self):
        return self.pos

    def get_radius(self):
        return self.radius

    def draw(self, canvas):
        if self.animated:
            image_tile = (self.age % 20) // 1
            self.image_center = [self.image_center[0] + image_tile * self.image_size[0],
                                 self.image_center[1]]
        canvas.draw_image(self.image, self.image_center, self.image_size,
                              self.pos, self.image_size, math.radians(self.angle))

    def update(self):
        self.pos[0] = (self.pos[0] + self.vel[0]) % WIDTH
        self.pos[1] = (self.pos[1] + self.vel[1]) % HEIGHT
        self.angle += self.angle_vel
        self.age += 1
        if self.age >= self.lifespan:
            return True
        else:
            return False

    def collide(self, other_object):
        distance_is = dist(self.pos, other_object.get_position())
        distance_no = self.radius + other_object.get_radius()
        if distance_is < distance_no:
            return True
        else:
            return False


def draw(canvas):
    global time, lives, score, started, rock_group, missile_group, explosion_group

    # animiate background
    time += 1
    wtime = (time / 4) % WIDTH
    center = debris_info.get_center()
    size = debris_info.get_size()
    canvas.draw_image(nebula_image, nebula_info.get_center(), nebula_info.get_size(), [WIDTH / 2, HEIGHT / 2],
                      [WIDTH, HEIGHT])
    canvas.draw_image(debris_image, center, size, (wtime - WIDTH / 2, HEIGHT / 2), (WIDTH, HEIGHT))
    canvas.draw_image(debris_image, center, size, (wtime + WIDTH / 2, HEIGHT / 2), (WIDTH, HEIGHT))

    # draw ship and sprites
    my_ship.draw(canvas)

    # update ship and sprites
    my_ship.update()

    # update and draw sprites (rocks, missles and explosions)
    process_sprite_group(rock_group, canvas)
    process_sprite_group(missile_group, canvas)
    process_sprite_group(explosion_group, canvas)

    # to determine if the ship hit any of the rocks
    if group_collide(rock_group, my_ship):
        lives -= 1

    # to determine if the missile hits any of the rocks and score it if so
    score += group_group_collide(missile_group, rock_group)

    # if the number of lives becomes 0, the game is reset
    if lives <= 0:
        started = False
        lives = 3
        score = 0
        rock_group = set()
        missile_group = set()
        explosion_group = set()

    # draw UI
    canvas.draw_text("Lives: " + str(lives), (60, 30), 30, 'White')
    canvas.draw_text("Score: " + str(score), (WIDTH - 140, 30), 30, 'White')

    # draw splash screen if not started
    if not started:
        canvas.draw_image(splash_image, splash_info.get_center(),
                          splash_info.get_size(), [WIDTH / 2, HEIGHT / 2],
                          splash_info.get_size())
        timer.stop()
        soundtrack2.play()


# dismiss the splash screen image (in the start of the game) with a mouse click
def click(pos):
    global started
    center = [WIDTH / 2, HEIGHT / 2]
    size = splash_info.get_size()
    inwidth = (center[0] - size[0] / 2) < pos[0] < (center[0] + size[0] / 2)
    inheight = (center[1] - size[1] / 2) < pos[1] < (center[1] + size[1] / 2)
    if (not started) and inwidth and inheight:
        started = True
        timer.start()
        soundtrack2.rewind()
        soundtrack.rewind()
        soundtrack.play()


def key_down(key):
    # ship's rotation keys handlers
    if key == simplegui.KEY_MAP["right"]:
        my_ship.turn_right()
    elif key == simplegui.KEY_MAP["left"]:
        my_ship.turn_left()

    # ship's truster handler
    if key == simplegui.KEY_MAP["up"]:
        my_ship.thrusters_burst(True)

    # missle launch handler
    if key == simplegui.KEY_MAP["space"]:
        my_ship.shoot()


def key_up(key):
    # ship's rotation keys handlers
    if key == simplegui.KEY_MAP["right"]:
        my_ship.turn_left()
    elif key == simplegui.KEY_MAP["left"]:
        my_ship.turn_right()

    # ship's truster handler
    if key == simplegui.KEY_MAP["up"]:
        my_ship.thrusters_burst(False)


# timer handler that adds a rock into a set "rock_group" (limit = 12 rocks)
def rock_spawner():
    global rock_group
    if len(rock_group) < 12:
        rock = Sprite([random.random() * WIDTH, random.random() * HEIGHT],
                      [random.randrange(-7, 7) / 5, random.randrange(-7, 7) / 5],
                      random.randrange(0, 360), random.random() / random.choice([-2, 2]),
                      asteroid_image, asteroid_info)
        rock_position = rock.get_position()
        my_ship_position = my_ship.get_position()
        if (my_ship_position[0] - 250) < rock_position[0] < (my_ship_position[0] + 250) or \
                (my_ship_position[1] + 250) < rock_position[0] < (my_ship_position[1] + 250):
            pass
        else:
            rock_group.add(rock)


# initialize frame
frame = simplegui.create_frame("Asteroids", WIDTH, HEIGHT)

# register handlers
frame.set_draw_handler(draw)
frame.set_mouseclick_handler(click)
frame.set_keydown_handler(key_down)
frame.set_keyup_handler(key_up)
timer = simplegui.create_timer(1000.0, rock_spawner)

# initialize ship and two sprites
my_ship = Ship([WIDTH / 2, HEIGHT / 2], [0, 0], 0, ship_image, ship_info)
rock_group = set()
missile_group = set()
explosion_group = set()

# get things rolling
frame.start()
soundtrack2.play()
