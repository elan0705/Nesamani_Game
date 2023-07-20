#!/usr/bin/env python
# coding: utf-8

# In[1]:


import arcade
import random
import arcade.gui as ag
import pyglet
import pyglet.media as media
import time
#from goto import goto, label

SCREEN_WIDTH = 1300
SCREEN_HEIGHT = 1300
SCREEN_TITLE = "Contractor NESAMANI"
SCALING = 0.25 

class Contractor_Nesamani(arcade.Window):
    
    def __init__(self,width,height,title,level): 
        super().__init__(width,height,title)
        arcade.set_background_color(arcade.color.SKY_BLUE)
        self.audio = arcade.load_sound(r"C:\Users\DELL\OneDrive\Details\Kaipulla Comedy Bgm.mp3",True)
        self.audio1 = arcade.load_sound(r"C:\Users\DELL\OneDrive\Details\Ada Nasama Pora Dialogue.mp3",False)
        self.audio2 = arcade.load_sound(r"C:\Users\DELL\OneDrive\Details\be happy.mp3",False)
        self.enemies_list = arcade.SpriteList()
        self.clouds_list = arcade.SpriteList()
        self.thunder_list = arcade.SpriteList()
        self.coins_list = arcade.SpriteList()
        self.all_sprites = arcade.SpriteList()
        self.pause = 0
        self.resume = 0
        self.score = 0
        self.level = level
        self.o = None
        self.R = 0
    def setup(self):
        self.player = arcade.Sprite(r"C:\Users\DELL\OneDrive\Pictures\Camera Roll\vadivelu.png",0.5)
        self.player.center_y = self.height/2
        self.player.left = 10
        
        self.o=arcade.play_sound(self.audio,1.0,0.0,True)
        
        self.all_sprites.append(self.player)
        arcade.schedule(self.add_enemy,1.5)
        arcade.schedule(self.add_coin,1.5)
        if self.level==2:
            arcade.schedule(self.add_clouds,1.5)
        if self.level==3:
            arcade.schedule(self.add_thunder,1.5)
        return self.R
            
    def add_enemy(self, delta_time: float):
        enemy = arcade.Sprite(r"C:\Users\DELL\OneDrive\Pictures\Camera Roll\hammer1.png",SCALING )
        enemy.left = random.randint(200,self.width-50)
        enemy.top = random.randint(10,self.height-10)
        
        enemy.velocity = (random.randint(-20, -5), 0)

        if self.pause==0:
            self.enemies_list.append(enemy)
            self.all_sprites.append(enemy)
            
    def add_coin(self, delta_time: float):
        coin = arcade.Sprite(r"C:\Users\DELL\OneDrive\Pictures\Camera Roll\coin1.png",SCALING )
        coin.left = random.randint(200,self.width-50)
        coin.top = random.randint(10,self.height-10)
        
        coin.velocity = (random.randint(-20, -5), 0)

        if self.pause==0:
            self.coins_list.append(coin)
            self.all_sprites.append(coin)
    
    def add_clouds(self, delta_time: float):
        cloud = arcade.Sprite(r"C:\Users\DELL\OneDrive\Pictures\Camera Roll\cloud1.png",SCALING )
        cloud.left = random.randint(200,self.width-50)
        cloud.top = random.randint(10,self.height-10)
        
        cloud.velocity = (random.randint(-20, -5), 0)

        if self.pause==0:
            self.clouds_list.append(cloud)
            self.all_sprites.append(cloud)
            
    def add_thunder(self, delta_time: float):
        thunder = arcade.Sprite(r"C:\Users\DELL\OneDrive\Pictures\Camera Roll\thunder1.png",SCALING )
        thunder.left = random.randint(200,self.width-50)
        thunder.top = random.randint(10,self.height-10)
        
        thunder.velocity = (random.randint(-20, -5), 0)

        if self.pause==0:
            self.thunder_list.append(thunder)
            self.all_sprites.append(thunder)
            
    def Dead_display(self,x1,y1):
        arcade.open_window(x1, y1, 'DEAD')            #Setting window size
        arcade.set_background_color(arcade.color.SKY_BLUE)      #setting backGround
        background = arcade.load_texture(r"C:\Users\DELL\OneDrive\Pictures\Camera Roll\pray_for_nesamani.png") #welcome_image         
        arcade.start_render()
        self.o=arcade.play_sound(self.audio1,1.0,0.0,False)
        arcade.draw_texture_rectangle(500.0, 700.0, 320, 320, background) #end Image positioning
        arcade.draw_text(self.score,700.0,400.0,arcade.color.DARK_GREEN,30,80,'left',font_name='GARA') #Welcome text
        arcade.draw_text("YOUR SCORE:",300.0,400.0,arcade.color.DARK_GREEN,30,80,'left',font_name='GARA') #Welcome text
        arcade.finish_render() 
        arcade.run()
        
    def level_display(self,x2,y2):
        arcade.open_window(x2, y2, 'LEVEL_COMPLETE')            #Setting window size
        arcade.set_background_color(arcade.color.SKY_BLUE)      #setting backGround
        background1 = arcade.load_texture(r"C:\Users\DELL\OneDrive\Pictures\Camera Roll\congrats.png") #welcome_image         
        arcade.start_render()
        self.o=arcade.play_sound(self.audio2,1.0,0.0,False)
        arcade.draw_text("CONGRATULATIONS!!",250.0,800.0,arcade.color.DARK_GREEN,30,80,'left',font_name='GARA') #Welcome text
        arcade.draw_texture_rectangle(450.0, 600.0, 320, 320, background1) #end Image positioning
        arcade.draw_text(self.score,600.0,400.0,arcade.color.DARK_GREEN,30,80,'left',font_name='GARA') #Welcome text
        arcade.draw_text("YOUR SCORE:",250.0,400.0,arcade.color.DARK_GREEN,30,80,'left',font_name='GARA') #Welcome text
        arcade.finish_render() 
        arcade.run()
        self.R = 1
        return self.R
        
    def update(self, deltatime: float):
        if self.pause==1:
            return
        if self.pause==0:
            self.all_sprites.update()
            if self.player.right<0:
                self.remove_from_sprite_lists()
        
            if self.player.top > self.height:
                self.player.top = self.height
            elif self.player.right > self.width:
                self.player.right = self.width
            elif self.player.bottom < 0:
                self.player.bottom = 0
            elif self.player.left < 0:
                self.player.left = 0
            #else:
            #    print("No Updates")
            if self.level==1:
                self.L=15
            elif self.level==2:
                self.L=25
            elif self.level==3:
                self.L=45
            
            if self.player.collides_with_list(self.coins_list):
                for coin in self.player.collides_with_list(self.coins_list):  
                    self.score= self.score+1
                    coin.kill()
                    #print(self.score)
                    
            if self.score==self.L:
                arcade.stop_sound(self.o)
                arcade.close_window()
                print(self.score)
                self.level_display(900,900)
                    
            if self.player.collides_with_list(self.enemies_list):
                arcade.stop_sound(self.o)
                
                arcade.close_window()
                print(self.score)
                self.Dead_display(900,900)
                
                
            
            if self.player.collides_with_list(self.thunder_list):
                arcade.stop_sound(self.o)
                arcade.close_window()
                print(self.score)
                self.Dead_display(900,900)
            
    
    
    def on_draw(self):
        arcade.start_render()
        self.all_sprites.draw()
        self.enemies_list.draw()
        self.coins_list.draw()
        self.clouds_list.draw()
        self.thunder_list.draw()
        arcade.draw_text("CONTROLS [↑,↓], Q = Quit, P = Pause, R = Resume",10.0,1280.0,arcade.color.DARK_GREEN,10,20,'left',font_name='BLACK')
        arcade.draw_text(self.score,1100.0,1250.0,arcade.color.DARK_GREEN,30,80,'right',font_name='BLACK')
        arcade.finish_render() 
    def on_key_press(self, symbol,modifiers):
        if symbol == arcade.key.Q:
            arcade.stop_sound(self.o)
            arcade.close_window()    
        if symbol == arcade.key.P:
            self.pause = 1
            arcade.stop_sound(self.o)
        if symbol == arcade.key.R:
            self.pause = 0
        elif symbol == arcade.key.I or symbol == arcade.key.UP:
            self.player.change_y = 5
        elif symbol == arcade.key.K or symbol == arcade.key.DOWN:
            self.player.change_y = -5
       # elif symbol == arcade.key.J or symbol == arcade.key.LEFT:
       #     self.player.change_x = -5
       # elif symbol == arcade.key.L or symbol == arcade.key.RIGHT:
       #     self.player.change_x = 5
        #else:
        #    print(" invalid key")
            
    def on_key_release(self, symbol:int,modifiers:int):
        if (symbol == arcade.key.I or symbol == arcade.key.K or symbol == arcade.key.UP or symbol == arcade.key.DOWN):
            self.player.change_y = 0
        #elif (symbol == arcade.key.J or symbol == arcade.key.L or symbol == arcade.key.LEFT or symbol == arcade.key.RIGHT):
        #    self.player.change_x = 0
        #else:
        #    print("Good")
                    
        
    
class Welcome(arcade.Window):
    
    def __init__(self,width,height,title):
        super().__init__(width,height,title)
        arcade.set_background_color(arcade.color.SKY_BLUE)
        self.uimanager = ag.UIManager()                        #initaializing user input
        self.uimanager.enable()
        self.aud = arcade.load_sound(r"C:\Users\DELL\OneDrive\Details\Ne Pudungurathu Puram (mp3cut.net).mp3",False)
        self.entr=0
        self.o=None
    def entered(self):
        bg = arcade.load_texture(r"C:\Users\DELL\OneDrive\Pictures\Camera Roll\welcome_image.png") #welcome_image
        enter_button = ag.UIFlatButton(width=300,text="ENTER")
        quit_button = ag.UIFlatButton(width=100,text="QUIT")
        
        self.uimanager.add(ag.UIAnchorWidget(anchor_x="center", anchor_y="center", child=enter_button))  #start button_anchor
        self.uimanager.add(ag.UIAnchorWidget(anchor_x="right", anchor_y="top", child=quit_button))
        
        enter_button.on_click = self.clicked_enter
        quit_button.on_click = self.clicked_quit
        
        arcade.start_render()
        self.uimanager.draw() 
        self.o = arcade.play_sound(self.aud,1.0,0.0, False)
        arcade.draw_texture_rectangle(650.0, 1000.0, 320, 320, bg) #welcome Image positioning
        arcade.draw_text("WELCOME",550.0,1200.0,arcade.color.DARK_GREEN,30,80,'left',font_name='GARA') #Welcome text
        arcade.finish_render()                            #end creating welcome window
        arcade.run()
        return self.entr
      
        
    def clicked_enter(self,event):
        print("ENTERED")
        self.entr = 1
        arcade.stop_sound(self.o)
        arcade.close_window()
        return self.entr    
        
    def clicked_quit(self,event):
        print("LEVEL 2")
        self.entr = 0
        arcade.stop_sound(self.o)
        arcade.close_window()
        return self.entr 
        
        
class Level(arcade.Window):
    def __init__(self,width,height,title):
        super().__init__(width,height,title)
        arcade.set_background_color(arcade.color.SKY_BLUE)
        self.uipmanager = ag.UIManager()                        #initaializing user input
        self.uipmanager.enable()
        self.audi = arcade.load_sound(r"C:\Users\DELL\OneDrive\Details\Amaithiya Vella Parunga Dialogue.mp3",False)
        self.lvl= 0
        self.o = None
    
    def levels(self):
        background = arcade.load_texture(r"C:\Users\DELL\OneDrive\Pictures\Camera Roll\vadivelan1.png") #welcome_image
        
        level1_button = ag.UIFlatButton(width=300,text="LEVEL 1")
        level2_button = ag.UIFlatButton(width=300,text="LEVEL 2") #start button initialization
        level3_button = ag.UIFlatButton(width=300,text="LEVEL 3")
        quit_button = ag.UIFlatButton(width=100,text="QUIT")
        
        self.uipmanager.add(ag.UIAnchorWidget(anchor_x="center", anchor_y="center", child=level2_button))  #start button_anchor
        self.uipmanager.add(ag.UIAnchorWidget(anchor_x="right", anchor_y="center", child=level3_button))  #start button_anchor
        self.uipmanager.add(ag.UIAnchorWidget(anchor_x="left", anchor_y="center", child=level1_button))
        self.uipmanager.add(ag.UIAnchorWidget(anchor_x="right", anchor_y="top", child=quit_button))
        
        level1_button.on_click = self.clicked_level1
        level2_button.on_click = self.clicked_level2
        level3_button.on_click = self.clicked_level3
        quit_button.on_click = self.click_quit
        
        arcade.start_render()
        self.uipmanager.draw()
        self.o = arcade.play_sound(self.audi,1.0,0.0, False)
        arcade.draw_texture_rectangle(650.0, 1000.0, 320, 320, background) #welcome Image positioning
        arcade.draw_text("SELECT LEVEL",500.0,1200.0,arcade.color.DARK_GREEN,30,80,'left',font_name='GARA') #Welcome text
        arcade.finish_render()                            #end creating welcome window
        arcade.run()
        return self.lvl 
        
    def clicked_level1(self,event):
        print("LEVEL 1")
        self.lvl = 1
        arcade.stop_sound(self.o)
        arcade.close_window()
        return self.lvl
        
    def clicked_level2(self,event):
        print("LEVEL 2")
        self.lvl = 2
        arcade.stop_sound(self.o)
        arcade.close_window()
        return self.lvl
        
    def clicked_level3(self,event):
        print("LEVEL 3")
        self.lvl = 3
        arcade.stop_sound(self.o)
        arcade.close_window()
        return self.lvl
        
    def click_quit(self,event):
        print("LEVEL 2")
        arcade.stop_sound(self.o)
        arcade.close_window()
    
        


        
if __name__ == "__main__":
    k =  Welcome(SCREEN_WIDTH,SCREEN_HEIGHT,SCREEN_TITLE)
    e = k.entered()
    print(e)
    b= print("level display")
    #label.levels
    if e == 1:
        L =  Level(SCREEN_WIDTH,SCREEN_HEIGHT,SCREEN_TITLE)
        d = L.levels()
        print(d)
        LEVEL = d
        obj = Contractor_Nesamani(SCREEN_WIDTH,SCREEN_HEIGHT,SCREEN_TITLE,LEVEL) #,K
        n = obj.setup()
        arcade.run()
        if n == 1:
            Goto *b
        


# In[ ]:





# In[ ]:




