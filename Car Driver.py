import pygame,os,random,sys
pygame.init()
os.environ['SDL_VIDEO_WINDOW_POS'] = f'{420},{30}'

screen = pygame.display.set_mode((700,900))
pygame.display.set_caption("Car Driver")

icon_surface = pygame.image.load("assets/icon.png").convert_alpha()
pygame.display.set_icon(icon_surface)



game_over_surface = pygame.image.load("assets/game_over.png")

#road
road_surface = pygame.image.load("assets/road.png").convert_alpha()

road_pos_y = 0

#car

blackviper_surface = pygame.image.load("assets/Black_viper.png").convert_alpha()
blackviper_rect = blackviper_surface.get_rect(midtop=(500,546))


audi_surface =pygame.image.load("assets/Audi.png")
taxi_surface = pygame.image.load("assets/taxi.png")
minivan_surface = pygame.image.load("assets/Mini_Van.png")
minitruck_surface = pygame.image.load("assets/Mini_truck.png")
truck_surface = pygame.image.load("assets/truck.png")

#police
police_surface = [pygame.image.load("assets/Police_animation/1.png"),pygame.image.load("assets/Police_animation/2.png"),pygame.image.load("assets/Police_animation/3.png")]
police = pygame.image.load("assets/Police_animation/2.png")
police_count = 0
POLICE =pygame.USEREVENT+1
pygame.time.set_timer(POLICE,200)


turn_velocity = 5

way = [500,100,420,135,275,600,243]




car_list = [police,audi_surface,taxi_surface,minivan_surface,minitruck_surface,truck_surface]
cars = []

#level up
car_rect_y_velocity = 4
car_spawn_time = 1400
road_pos_y_velocity = 6
level = 1








SPAWNCAR = pygame.USEREVENT
pygame.time.set_timer(SPAWNCAR,car_spawn_time)

game_active = True
game_status  = "continue"

clock = pygame.time.Clock()







#Functions
def draw_road():
    global road_pos_y
    if(road_pos_y >= 900):
        road_pos_y = 0
    
    screen.blit(road_surface,(0,road_pos_y))
    screen.blit(road_surface,(0,road_pos_y-900))
    

def create_car():
    way_choice = random.choice(way)
    car_surface_choice = random.choice(car_list)
    
    car_rectangle = car_surface_choice.get_rect(midtop=(way_choice,-300))
    
    return (car_surface_choice,car_rectangle)#(surface,rect)

def create_car_win():
    
    car_surface_choice = random.choice(car_list)
    
    car_rectangle = car_surface_choice.get_rect(midtop=(150,-300))
    
    return (car_surface_choice,car_rectangle)#(surface,rect)

def move_car(cars):

    for car_surface,car_rect in cars:
        car_rect.y += car_rect_y_velocity ##########
    return cars

def draw_cars(cars):
    global police_count
    for car_surface,car_rect in cars:
        if(car_surface == police):
            if(police_count>=3):
                police_count = 0

            elif(police_count == 2):
                screen.blit(police_surface[2],car_rect)
            elif(police_count == 1):
                screen.blit(police_surface[1],car_rect)
            elif(police_count == 0):
                screen.blit(police_surface[0],car_rect)
            
                                    
            
                
                
                

                
        else:
            screen.blit(car_surface,car_rect)
        
    
    
    
def level_up():
    global level
    global turn_velocity #sağ sol hızımız
    global car_spawn_time #araba spawn hızı
    global road_pos_y_velocity #yol akış hızı (a)[bizim hızımız]
    global car_rect_y_velocity #arabaların akış hızı (a)
    
    

    if(level == 1):

        pygame.time.set_timer(SPAWNCAR,1400)
        road_pos_y_velocity =7
        car_rect_y_velocity = 5
        turn_velocity = 6
        level += 1
    elif(level == 2):

        pygame.time.set_timer(SPAWNCAR,1000)
        road_pos_y_velocity =8
        car_rect_y_velocity = 6
        turn_velocity =7
        level += 1
    elif(level == 3):

        pygame.time.set_timer(SPAWNCAR,800)
        road_pos_y_velocity =10
        car_rect_y_velocity = 7
        turn_velocity = 7
        level +=1
    elif(level == 4):

        pygame.time.set_timer(SPAWNCAR,700)
        road_pos_y_velocity =11
        car_rect_y_velocity = 8
        turn_velocity = 7
        level += 1


   
    
    

def check_collision(cars):
    for car in cars:
        if(blackviper_rect.colliderect(car[1])):
            #print("collision")
            return True

    return False



def draw_text(text,font_type,color,surface,x,y,size):
    font = pygame.font.SysFont(font_type,size)
    text_surface = font.render(text,1,color)
    text_rect = text_surface.get_rect(center=(x,y))
    surface.blit(text_surface,text_rect)
    




#menus



def main_menu():
    global level
    global turn_velocity  # sağ sol hızımız
    global car_spawn_time  # araba spawn hızı
    global road_pos_y_velocity  # yol akış hızı (a)[bizim hızımız]
    global car_rect_y_velocity  # arabaların akış hızı (a)




    click = False

    while True:
        clock.tick(120)
        

        screen.fill((255, 186, 73))
        mx, my = pygame.mouse.get_pos()

        button_1 = pygame.Rect(250,300,200,50)
        button_2 = pygame.Rect(250,380,200,50)
        button_3 = pygame.Rect(250,460,200,50)
        

        if(button_1.collidepoint((mx,my))):
            if click:
                level = 1
                pygame.time.set_timer(SPAWNCAR, 1400)
                road_pos_y_velocity = 6
                car_rect_y_velocity = 4
                turn_velocity = 6

                main_game()

        if(button_2.collidepoint((mx,my))):
            if click:
                about_screen()
        if(button_3.collidepoint((mx,my))):
            if click:
                pygame.quit()
                sys.exit()

        pygame.draw.rect(screen,(255,80,91),button_1)
        pygame.draw.rect(screen,(255,80,91),button_2)
        pygame.draw.rect(screen,(255,80,91),button_3)
        
    
        draw_text("Başlat","Arial",(255,255,255),screen,button_1.centerx,button_1.centery-2,40)
        draw_text("Hakkında","Arial",(255,255,255),screen,button_2.centerx,button_2.centery-2,40)
        draw_text("Çıkış","Arial",(255,255,255),screen,button_3.centerx,button_3.centery-2,40)
        
        draw_text("Car Driver","Arial",(164, 169, 173),screen,350,170,130)
        draw_text("Author: DFErkim","Arial",(0,0,0),screen,350,880,10)

        
        click = False

        for event in pygame.event.get():
            if(event.type == pygame.QUIT):
                pygame.quit()
                sys.exit()
                
            if(event.type == pygame.MOUSEBUTTONDOWN):
                if (event.button == 1):
                    click = True
        

        pygame.display.update()






            

def about_screen():
    running = True
    click = False
    while running:
        

        clock.tick(120)

        mx, my = pygame.mouse.get_pos()

        button_1 = pygame.Rect(285,400,120,50)
        pygame.draw.rect(screen,(255,80,91),button_1)
        draw_text("Geri","Arial",(255,255,255),screen,button_1.centerx,button_1.centery-2,40)
            

        draw_text("Bu oyun DFErkim tarafından 7.08.2020 tarihinde yazılmaya başlanmış,","Arial",(255,255,255),screen,350,200,20)
        draw_text("8.08.2020 tarihinde tamamlanmıştır. ","Arial",(255,255,255),screen,350,220,20)
        draw_text("Oyundaki amaç arabalara çarpmadan 5.level'e ulaşmaktır.","Arial",(255,255,255),screen,350,300,20)
        draw_text(" Her levelde arabanın hızı artmakta ve trafik artmaktadır.","Arial",(255,255,255),screen,350,360,20)
        
        



        if(button_1.collidepoint((mx,my))):
            if click:
                running = False

        


        
        click = False
        for event in pygame.event.get():
            if(event.type == pygame.QUIT):
                pygame.quit()
                sys.exit()


            #if(event.type == pygame.KEYDOWN):
                #if(event.key == pygame.K_ESCAPE):
                    #running = False

            if(event.type == pygame.MOUSEBUTTONDOWN):
                if (event.button == 1):
                    click = True

        
        pygame.display.update()
            






def lose_screen():
    global police_count
    global cars
    global road_pos_y
    global road_pos_y_velocity
    global game_status
    global level

    running = True
    click = False
    while running:


    
        clock.tick(120)
        screen.blit(game_over_surface,(0,0))

        
        


        
        

        mx, my = pygame.mouse.get_pos()

        button_1 = pygame.Rect(95,800,200,50)
        button_2 = pygame.Rect(370,800,200,50)


        if(button_1.collidepoint((mx,my))):
            if click:
                game_status = "continue"
                cars.clear()

                main_menu()

        if(button_2.collidepoint((mx,my))):
            if click:
                pygame.quit()
                sys.exit()

        pygame.draw.rect(screen,(255,80,91),button_1)
        pygame.draw.rect(screen,(255,80,91),button_2)
        draw_text("Ana Menü","Arial",(255,255,255),screen,button_1.centerx,button_1.centery,40)
        draw_text("Çıkış","Arial",(255,255,255),screen,button_2.centerx,button_2.centery-4,40)


        
        click = False
        for event in pygame.event.get():
            if(event.type == pygame.QUIT):
                pygame.quit()
                sys.exit()
            

            
            if(event.type == pygame.MOUSEBUTTONDOWN):
                if (event.button == 1):
                    click = True
        

        
        

        pygame.display.update()



         
def win_screen():
    global police_count
    global cars
    global road_pos_y
    global road_pos_y_velocity
    global game_status
    global level
    cars.clear()
    level =  1
    running = True
    click = False
    while running:


    
        clock.tick(120)

        




        draw_road()
        road_pos_y += road_pos_y_velocity 


            
        cars = move_car(cars)
        draw_cars(cars)

        blackviper_rect.x = 500
        screen.blit(blackviper_surface,blackviper_rect)
        draw_text("Kazandınız","Arial",(255,255,255),screen,350,80,60)

        mx, my = pygame.mouse.get_pos()

        button_1 = pygame.Rect(95,800,200,50)
        button_2 = pygame.Rect(370,800,200,50)


        if(button_1.collidepoint((mx,my))):
            if click:
                game_status = "continue"
                main_menu()

        if(button_2.collidepoint((mx,my))):
            if click:
                pygame.quit()
                sys.exit()

        pygame.draw.rect(screen,(255,80,91),button_1)
        pygame.draw.rect(screen,(255,80,91),button_2)
        draw_text("Ana Menü","Arial",(255,255,255),screen,button_1.centerx,button_1.centery,40)
        draw_text("Çıkış","Arial",(255,255,255),screen,button_2.centerx,button_2.centery-4,40)


        
        click = False
        for event in pygame.event.get():
            if(event.type == pygame.QUIT):
                pygame.quit()
                sys.exit()
            if(event.type == SPAWNCAR):
                cars.append(create_car_win())
                
            if(event.type == POLICE):
                police_count +=1

            #if(event.type == pygame.KEYDOWN):
                #if(event.key ==pygame.K_ESCAPE):
                    #running = False
            if(event.type == pygame.MOUSEBUTTONDOWN):
                if (event.button == 1):
                    click = True
        

        
        

        pygame.display.update()

            

        
    

def main_game():
    global blackviper_rect
    global game_active
    global game_status
    global turn_velocity
    global road_surface
    global road_pos_y
    global blackviper_surface
    global blackviper_rect
    global audi_surface
    global taxi_surface
    global minivan_surface
    global minitruck_surface
    global truck_surface
    global police_surface
    global police
    global police_count
    global turn_velocity
    global way
    global car_list
    global cars
    global car_rect_y_velocity
    global car_spawn_time
    global road_pos_y_velocity
    global level
    global game_active
    global game_status


    running = True
    time = 0
    while running:
        time += 0.01

        


        clock.tick(120)


        for event in pygame.event.get():
            if(event.type == pygame.QUIT):
                pygame.quit()
                sys.exit()
            if(event.type == SPAWNCAR):
                cars.append(create_car())
                
            if(event.type == POLICE):
                police_count +=1

            if(event.type == pygame.KEYDOWN):
                if(event.key ==pygame.K_ESCAPE):
                    running = False



        keys = pygame.key.get_pressed()

        if(keys[pygame.K_LEFT] and blackviper_rect.left >=0  and game_active and game_status == "continue"):
            blackviper_rect.x -= turn_velocity
            
        if(keys[pygame.K_RIGHT] and blackviper_rect.right <=700 and game_active and game_status == "continue"):
            blackviper_rect.x += turn_velocity

        
            
            

        
        
        if(game_status == "continue"):
            
            #road
            draw_road()
            road_pos_y += road_pos_y_velocity ####################

            #player car
            screen.blit(blackviper_surface,blackviper_rect)

            #random car
            cars = move_car(cars)
            draw_cars(cars)
            #level
            level_rect = pygame.Rect(250,825,150,50)
            pygame.draw.rect(screen,(255,80,91),level_rect)
            draw_text(f"Level: {level}","Arial",(255,255,255),screen,level_rect.centerx,level_rect.centery,40)
            #level up
            if (15.02 > time > 15.01):
                level_up()

            elif (30.02 > time > 30.01):
                level_up()

            elif (45.02 > time > 45.01):
                level_up()

            elif (60.02 > time > 60.01):
                level_up()

            elif (75.02 > time > 75.01):
                game_status = "win"


            #collision check
            if (check_collision(cars)):
                lose_screen()
            

            

        elif(game_status == "win"):
            win_screen()
            

            
        
            

        

        
        pygame.display.update()
        



main_menu()
