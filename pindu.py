import pygame as pp
import gif_pygame as gf
import os

pp.init()
pp.mixer.init()
clock = pp.time.Clock()

cake = gf.load("static/cake.GIF")
pp.mixer.music.load("static/pindu.mp3")
font = pp.font.Font(None, 30)

screen = pp.display.set_mode((300, 300))

def main():
    pp.display.set_caption(" To Pindu ")
    running = True
    in_party = False
    
    while running:
        for event in pp.event.get():
            if event.type == pp.QUIT:
                running = False
        screen.fill('pink')
        if in_party: party() 
        else: 
            if button(): 
                in_party = True
        pp.display.flip()
    pp.quit()

def party():
    # music
    if not pp.mixer.music.get_busy():
        pp.mixer.music.play(-1)
        
    # cake
    cake_rect = cake.get_rect()
    cake_rect.center = (screen.get_width() // 2, screen.get_height() // 2)
    cake.render(screen, cake_rect.topleft)
    clock.tick(30)

def button():
    mouse = pp.mouse.get_pos()

    button_x, button_y = 70, 110
    # Center the button
    button_x = (screen.get_width() - 200) // 2
    button_y = (screen.get_height() - 50) // 2
    button_width, button_height = 200, 50

    # Always draw the button (default color)
    pp.draw.rect(screen, (255, 105, 210), (button_x, button_y, button_width, button_height), border_radius=10)

    # Draw button label
    label = font.render("Click me!", True, "white")
    label_rect = label.get_rect(center=(button_x + button_width // 2, button_y + button_height // 2))
    screen.blit(label, label_rect)

    # Check for click
    if button_x <= mouse[0] <= button_x + button_width and button_y <= mouse[1] <= button_y + button_height:
        if pp.mouse.get_pressed()[0]:  # Left mouse click
            msg = "Happy birthday Pinduu! you are finally turning 20 bwahah feel old yet? i hope this year brings you loads and loads of happiness and joy, cuz u deserve it ^^ thank you for randomly coming into my life when i was down in the dumps :') u are one of the things that made 2025 bareable and i love ya for it. i hope wherever ya go our friendship stays solid ^^ couldnt have asked for a better softie than ya <3. anywhoo i actually hope u see this cuz u can be a blind fuck sometimes XD. Here's to many more of ur mischief! huggg ...happy 20th!"
            print(msg)
            return True
    
if __name__ == "__main__":
    main()