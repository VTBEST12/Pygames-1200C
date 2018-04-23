from gamelib import *
game = Game(800, 800, "1200°C")
#Graphics variables
bk = Image("BK.png",game)
bk.resizeTo(800,800)
game.setBackground(bk)

lav = Sound("lava.wav",1)
wing = Sound("wing.ogg",2)

die = Sound("die.ogg",3)
lnd = Sound("lnd.wav",4)
music = Sound("Mystical.wav",5) 

f = Font(red,20,white,"Times")

jumping = False
landed = False
factor = 1

title = Image("Title.png",game)
title.y -= 200
title.resizeTo(250,200)

hero = Animation("Molten.png",3,game,380,370,frate=6)
hero.resizeTo(125,115)


human = Animation("Human.png",3,game,1600/4,400,frate=12)
human.resizeTo(125,115)

lava = Animation("Lava.png",4,game,1600/4,300,frate=6)
lava.moveTo(400,555)
lava.resizeBy(165)

end = Image("End.jpg",game)
end.resizeTo(800,800)

platform = Image("Platform.png",game)

platform2 = Image("Platform2.png",game)
platform2.resizeBy(-55)
platform3 = Image("Platform3.png",game)
platform3.resizeBy(-55)
platform4 = Image("Platform4.png",game)
platform4.resizeBy(-55)
platform5 = Image("Platform4.png",game)
platform5.resizeBy(-55)
lose = Animation("YouLose.png",1,game,32,32,frate=9)
lose.resizeTo(600,600)

win = Animation("YouWin.png",2,game,64/2,64,frate=9)
win.resizeTo(600,600)
game.over = False
while not game.over:
    game.processInput()
    game.scrollBackground("down",2)
    music.play()
    'game.setMusic("Mystical.wav")'
    'game.playMusic()'
    title.draw()
    hero.draw()
    game.drawText("Instructions: Jump to each platform and get to the top. Don't let the Human touch you!",75,600,f)
    game.drawText("CONTROLS:",300,650,f)
    game.drawText("JUMP: ↑",300,675,f)
    game.drawText("LEFT: ←",300,725,f)
    game.drawText("Right:  →",300,775,f)
    game.drawText("PRESS ↑ TO START",300,500,f)
    if keys.Pressed[K_UP]:
        game.over = True

    game.update(30)

game.over = False
while not game.over:
    game.processInput()
    music.play()
    'game.setMusic("Mystical.wav")'
    'game.playMusic()'
    'lav.play(10)'
    game.scrollBackground("down",2)
    hero.draw()
    lava.draw()
    human.draw()
    human.moveTo(600,300)
    human.move(True)
    platform.draw()
    platform2.draw()
    platform3.draw()
    platform4.draw()
    platform5.draw()
    platform.moveTo(400,473)
    platform2.moveTo(575,380)
    platform3.moveTo(300,300)
    platform4.moveTo(190,180)
    platform5.moveTo(490,100)
    'human.moveTowards(hero,50)'
        
        
    #Control
    
    if keys.Pressed[K_LEFT]:
        hero.x -= 4
    if keys.Pressed[K_RIGHT]:
        hero.x += 4

    if keys.Pressed[K_UP] and landed and not jumping:
        jumping = True
        wing.play()
    if not hero.collidedWith(platform):
        landed = False
    else:
        landed = True
   
    if hero.collidedWith(platform) or hero.collidedWith(platform2) or hero.collidedWith(platform3) or hero.collidedWith(platform4) or hero.collidedWith(platform5):
        landed = True
        lnd.play()
    if jumping:
        hero.y -=15*factor
        #Make the character go up.  Factor creates a slowing effect to the jump
        factor*=.95#fall slowly
        landed = False
        #Since you are jumping you are no longer staying on land
    if factor < .18:
            jumping = False
            #Stop jumping once the slowing effect finishes
            factor = 1
            
    if not landed:
        hero.y += 4#adjust as needed

    if hero.y> 800 or hero.collidedWith(human):
        game.over = True
        die.play()
        game.stopMusic()

    if hero.y< 0:
        game.over = True
        game.stopMusic()

    game.update(30)
#Ending Screen
game.over = False
while not game.over:
    game.processInput()
    if hero.y> 800 or hero.collidedWith(human):
        end.draw()
        lose.draw()
        

    if hero.y< 0:
        end.draw()
        win.draw()
    if keys.Pressed[K_UP]:
        game.over = True
    game.update(30)
game.quit()
