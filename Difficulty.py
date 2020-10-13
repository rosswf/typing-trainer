import  pygame


Width = 500
Height = 500
Window = pygame.display.set_mode((Width, Height))
pygame.display.set_caption("Typing Trainer")    

pygame.font.init()
font = pygame.font.SysFont("Consolas", 42) 

#Just some colors

BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
BLUE =  (  0,   0, 255)
GREEN = (  0, 255,   0)
RED =   (255,   0,   0)
BUTTONS = (139,  69,  19)
BEIGE = (88, 75, 86)


#definitions/settings of the game difficulty in this format:
#Name. words per second, Velocity, min word_length
DiffSettings = [
    ["Easy", 0.5, 180, 3],
    ["Medium", 0.8, 300, 4],
    ["Hard", 1.2, 420, 5]
    ]
 

def make_display():
    Window.fill(BEIGE)
    Increase = pygame.draw.polygon(Window, BUTTONS, [[400, Height-120], [400, Height-20], [500, Height-70]], 5)
    Decrease = pygame.draw.polygon(Window, BUTTONS, [[10, Height-70], [110, Height-120], [110, Height-20]], 5)


def write(text):
    make_display()
    textsurface = font.render(text, True, (WHITE))
    Window.blit(textsurface, (Width/2 - textsurface.get_rect().width/2, Height / 2 - 100))


def GameDifficulty():
    make_display()

    Index = 0    

    done = False
    clock = pygame.time.Clock()
    
    while not done:
        CurrentDiff = DiffSettings[Index]
        clock.tick(10)


        for event in pygame.event.get(): 
            if event.type == pygame.QUIT: 
                done=True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    return CurrentDiff

                if event.key == pygame.K_LEFT:
                    if Index <= 0:
                        pass
                    else:
                        Index -= 1
                if event.key == pygame.K_RIGHT:
                    if Index != len(DiffSettings) - 1:
                        Index += 1
                    else:
                        Index = 0

        write(CurrentDiff[0])
        pygame.display.update()

