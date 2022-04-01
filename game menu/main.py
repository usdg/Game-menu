import pygame , os , sys, time
from pygame import mixer

pygame.init()
#basic variables
Width = 1000
Height = 800
black = (0,0,0)
click = False

#button width and height
sz = 190
wys = 90

sz_s = 100
wys_s = 150
#buttons placement
x = 400
y = 370
#window icon
icon = pygame.image.load(os.path.join('data','Assets', 'game-controller.png'))
#uploading pngs
background_menu_img = pygame.image.load(os.path.join('data','Assets', 'background.png'))
background_menu = pygame.transform.scale(background_menu_img,(1000,800))
play_img = pygame.image.load(os.path.join('data','Assets', 'play.png'))
play = pygame.transform.scale(play_img,(sz,wys))
options_img = pygame.image.load(os.path.join('data','Assets','options.png'))
opcje = pygame.transform.scale(options_img,(sz,wys))
suwak_img = pygame.image.load(os.path.join('data','Assets','suwak.png'))
suwak = pygame.transform.scale(suwak_img,(sz_s,wys_s))
back_img = pygame.image.load(os.path.join('data','Assets',"back.png"))
back = pygame.transform.scale(back_img,(sz,wys))
levels_img = pygame.image.load(os.path.join('data','Assets','levels.png'))
levels = pygame.transform.scale(levels_img,(sz,wys))
online_img = pygame.image.load(os.path.join('data','Assets','online.png'))
online = pygame.transform.scale(online_img,(sz,wys))
#fps 
clock = pygame.time.Clock()
FPS = 60

#basic window settings
WIN = pygame.display.set_mode((Width,Height))
pygame.display.set_caption('King Game')
pygame.display.set_icon(icon)
#sounds
pygame.mixer.music.load(os.path.join('data','sounds', 'music_for_game.wav'))
click_sound = mixer.Sound(os.path.join('data','sounds', 'click.wav'))

def draw_main_menu():
    WIN.blit(background_menu,(0,0))
    WIN.blit(play,(x,y))
    WIN.blit(opcje,(x,y+110))

def music_bg():
    pygame.mixer.music.play(-1)
    f = open(os.path.join('data','ustawienia', 'muzyka.txt'),("r"))
    content = f.read()
    f.close()
    f = open(os.path.join('data','ustawienia', 'efekty.txt'),("r"))
    content_2 = f.read()
    f.close()
    pygame.mixer.music.set_volume(float(content))
    click_sound.set_volume(float(content_2))

def main_menu(click):
    music_bg()
    while True:
        clock.tick(FPS)
        draw_main_menu()
        #buttons
        mx,my = pygame.mouse.get_pos()
        play_button = pygame.Rect(x,y,sz,wys)
        options_button = pygame.Rect(x,y+110,sz,wys)
        if play_button.collidepoint((mx,my)):
            clicked_play_img = pygame.image.load(os.path.join('data','Assets', 'play_clicked.png'))
            clicked_play = pygame.transform.scale(clicked_play_img,(sz,wys))
            WIN.blit(clicked_play,(x,y))
            if click:
                click_sound.play()
                game()
        if options_button.collidepoint((mx,my)):
            clicked_options_img = pygame.image.load(os.path.join('data','Assets', 'options_clicked.png'))
            clicked_options = pygame.transform.scale(clicked_options_img,(sz,wys))
            WIN.blit(clicked_options,(x,y+110))
            if click:
                click_sound.play()
                options()
        #events
        click = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
        pygame.display.update()
def game():
    while True:
        #basic settings
        mx,my = pygame.mouse.get_pos()
        clock.tick(FPS)
        #variables
        levels_hit = pygame.Rect(405,355,sz,wys)
        hit_back = pygame.Rect(25,680,sz,wys)
        online_hit = pygame.Rect(405,450,sz,wys)
        #drawing
        WIN.blit(background_menu,(0,0))
        WIN.blit(levels,(405,355))
        WIN.blit(back,(25,680))
        WIN.blit(online,(405,450))
        #events
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                            click = True
                if event.type == pygame.MOUSEBUTTONUP:
                    if event.button == 1:
                            click = False  
        #level button backend
        if levels_hit.collidepoint((mx,my)):
            clicked_levels_img = pygame.image.load(os.path.join('data','Assets', 'levels_clicked.png'))
            clicked_levels = pygame.transform.scale(clicked_levels_img,(sz,wys))
            WIN.blit(clicked_levels,(405,355))
        #back button backend
        if hit_back.collidepoint((mx,my)):            
            clicked_back_img = pygame.image.load(os.path.join('data','Assets', 'back_clicked.png'))
            clicked_back = pygame.transform.scale(clicked_back_img,(sz,wys))
            WIN.blit(clicked_back,(25,680))
            if click:
                click_sound.play()
                return 
        #online button backend
        if online_hit.collidepoint((mx,my)):
            clicked_online_img = pygame.image.load(os.path.join('data','Assets','online_clicked.png')) 
            clicked_online = pygame.transform.scale(clicked_online_img,(sz,wys))
            WIN.blit(clicked_online,(405,450))  
        pygame.display.update()   
def options():
    f = open(os.path.join('data','ustawienia', 'muzyka.txt'),("r"))
    content = f.read()
    f.close()
    f = open(os.path.join('data','ustawienia', 'efekty.txt'),("r"))
    content_2 = f.read()
    f.close()
    sz_p = float(content) *400
    sz_p_2 = float(content_2) *400
    suwak_x = sz_p + 257
    suwak_x_2 = sz_p_2 + 257
    click = False
    while True:
        clock.tick(FPS)
        mx,my = pygame.mouse.get_pos()
        x_p = 300
        x_p_2 = 300
        y_p = 300
        y_p_2 = 450
        wys_p = 30
        suwak_y = 257
        suwak_y_2 = 407
        font = pygame.font.Font('freesansbold.ttf',35)
        textX = 350
        textY = 250
        textY2 = 400
        text1 = font.render("Głośność muzyki",True,(230,10,20))
        text2 = font.render("Głośność efektów",True,(230,10,20))
        #hit-box
        back_button = pygame.Rect(25,680,sz,wys)
        hit_suwak = pygame.Rect(suwak_x,suwak_y,100,150)
        p_kreska = pygame.Rect(x_p,y_p,sz_p,wys_p)
        p_kreska_bck = pygame.Rect(x_p,y_p,400,wys_p)
        hit_suwak_2 = pygame.Rect(suwak_x_2,suwak_y_2,100,150)
        p_kreska_2 = pygame.Rect(x_p_2,y_p_2,sz_p_2,wys_p)
        p_kreska_bck_2 = pygame.Rect(x_p_2,y_p_2,400,wys_p)
        #drawing
        WIN.blit(background_menu,(0,0))
        pygame.draw.rect(WIN,(37, 37, 50),p_kreska_bck)
        pygame.draw.rect(WIN,(0,255,0),p_kreska)
        pygame.draw.rect(WIN,(37, 37, 50),p_kreska_bck_2)
        pygame.draw.rect(WIN,(0,255,0),p_kreska_2)
        WIN.blit(suwak,(suwak_x,suwak_y))
        WIN.blit(suwak,(suwak_x_2,suwak_y_2))
        WIN.blit(back,(25,680))
        WIN.blit(text1,(textX,textY))
        WIN.blit(text2,(textX,textY2))
        #first slider
        if hit_suwak.collidepoint((mx,my)):
            if click:
                if mx > x_p and mx < 675:
                    glosnosc_muzyki = float(sz_p/400)
                    f = open(os.path.join('data','ustawienia', 'muzyka.txt'),("w+"))
                    f.write(str(glosnosc_muzyki))
                    f.close()
                    f = open(os.path.join('data','ustawienia', 'muzyka.txt'),("r"))
                    content = f.read()
                    f.close()
                    pygame.mixer.music.set_volume(float(content))
                    suwak_x = mx - 45
                    if sz_p > mx - x_p or sz_p < mx - x_p:
                        sz_p = mx - x_p
        #second slider
        if hit_suwak_2.collidepoint((mx,my)):
            if click:
                if mx > x_p_2 and mx < 675:
                    glosnosc_efektow = float(sz_p_2/400)
                    f2 = open(os.path.join('data','ustawienia', 'efekty.txt'),("w+"))
                    f2.write(str(glosnosc_efektow))
                    f2.close()
                    f2 = open(os.path.join('data','ustawienia', 'efekty.txt'),("r"))
                    content2 = f2.read()
                    f2.close()
                    click_sound.set_volume(float(content2))
                    suwak_x_2 = mx - 45
                    if sz_p_2 > mx - x_p_2 or sz_p_2 < mx - x_p_2:
                        sz_p_2 = mx - x_p_2
        #back button
        if back_button.collidepoint((mx,my)):            
            clicked_back_img = pygame.image.load(os.path.join('data','Assets', 'back_clicked.png'))
            clicked_back = pygame.transform.scale(clicked_back_img,(sz,wys))
            WIN.blit(clicked_back,(25,680))
            if click:
                click_sound.play()
                return
        pygame.display.update()
        #events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                        click = True
            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                        click = False                      
#start
if __name__ == "__main__":
    main_menu(click)