blob= Actor('character1')
blob.position = 200, 200

BACKGROUND_COLOR = (0,0,255)
WIDTH = 500
HEIGHT = 300

def draw():
    screen.fill((0,0,255))
    blob.draw()
def update():
    blob.left = blob.left + 2
    if blob.left > WIDTH:
        blob.right = 0
def on_mouse_down(pos):
    if blob.collidepoint(pos):
        print("Eek!")
    else:
        print("You missed me!")
