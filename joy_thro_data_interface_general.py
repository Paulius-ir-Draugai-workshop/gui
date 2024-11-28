import pygame
import pygame_gui
from time import sleep

# Initialize pygame
pygame.init()

# Set up the main application window
window_size = (1050, 700)
window = pygame.display.set_mode(window_size)
pygame.display.set_caption("Joystick and Throttle Interface")

# Set up the GUI manager
manager = pygame_gui.UIManager(window_size)

# Create sliders for throttle (UIHorizontalSlider) widgets
slider5_rect = pygame.Rect((50, 50), (500, 40))
slider5 = pygame_gui.elements.UIHorizontalSlider(relative_rect=slider5_rect, start_value=0, value_range=(-1.0, 1.0), manager=manager)

slider6_rect = pygame.Rect((50, 120), (500, 40))
slider6 = pygame_gui.elements.UIHorizontalSlider(relative_rect=slider6_rect, start_value=0, value_range=(-1.0, 1.0), manager=manager)

slider7_rect = pygame.Rect((50, 190), (500, 40))
slider7 = pygame_gui.elements.UIHorizontalSlider(relative_rect=slider7_rect, start_value=0, value_range=(-1.0, 1.0), manager=manager)

slider10_rect = pygame.Rect((50, 260), (500, 40))
slider10 = pygame_gui.elements.UIHorizontalSlider(relative_rect=slider10_rect, start_value=0, value_range=(-1.0, 1.0), manager=manager)

slider11_rect = pygame.Rect((50, 330), (500, 40))
slider11 = pygame_gui.elements.UIHorizontalSlider(relative_rect=slider11_rect, start_value=0, value_range=(-1.0, 1.0), manager=manager)

# Create sliders for joystick (UIHorizontalSlider) widgets
slider1_rect = pygame.Rect((50, 410), (500, 40))
slider1 = pygame_gui.elements.UIHorizontalSlider(relative_rect=slider1_rect, start_value=0, value_range=(-1.0, 1.0), manager=manager)

slider2_rect = pygame.Rect((50, 480), (500, 40))
slider2 = pygame_gui.elements.UIHorizontalSlider(relative_rect=slider2_rect, start_value=0, value_range=(-1.0, 1.0), manager=manager)

slider3_rect = pygame.Rect((50, 550), (500, 40))
slider3 = pygame_gui.elements.UIHorizontalSlider(relative_rect=slider3_rect, start_value=0, value_range=(-1.0, 1.0), manager=manager)

slider4_rect = pygame.Rect((50, 620), (500, 40))
slider4 = pygame_gui.elements.UIHorizontalSlider(relative_rect=slider4_rect, start_value=0, value_range=(-1.0, 1.0), manager=manager)

# Main loop
clock = pygame.time.Clock()
running = True

# Initialize throttle and joystick
throttle = None
joystick = None

THROTTLE_NAME = "TWCS Throttle"
JOYSTICK_NAME = "T.16000M"

if pygame.joystick.get_count() >= 2:
    if pygame.joystick.Joystick(0).get_name() == THROTTLE_NAME and pygame.joystick.Joystick(1).get_name() == JOYSTICK_NAME:
        throttle = pygame.joystick.Joystick(0)
        joystick = pygame.joystick.Joystick(1)
    elif pygame.joystick.Joystick(1).get_name() == THROTTLE_NAME and pygame.joystick.Joystick(0).get_name() == JOYSTICK_NAME:
        throttle = pygame.joystick.Joystick(1)
        joystick = pygame.joystick.Joystick(0)
    else:
        print("Joysticks not supported.")
        exit(1)
else:
    print("Joysticks not detected.")
    exit(1)

# Main event loop
while running:
    time_delta = clock.tick(60) / 1000.0
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        # Handle events from the manager
        manager.process_events(event)
    
    # Update throttle values and sliders
    if throttle is not None:
        if throttle.get_numaxes() >= 8:
            slider5.set_current_value(throttle.get_axis(0))
            slider6.set_current_value(throttle.get_axis(1))
            slider7.set_current_value(throttle.get_axis(2))
            slider10.set_current_value(throttle.get_axis(5))
            slider11.set_current_value(throttle.get_axis(6))
    
    # Update joystick values and sliders
    if joystick is not None:
        if joystick.get_numaxes() >= 4:
            slider1.set_current_value(joystick.get_axis(0))
            slider2.set_current_value(joystick.get_axis(1))
            slider3.set_current_value(joystick.get_axis(2))
            slider4.set_current_value(joystick.get_axis(3))
    
    # Update the manager
    manager.update(time_delta)
    
    # Fill the window with a background color
    window.fill((200, 200, 200))
    
    # Draw the sliders' values as text
    font = pygame.font.Font(None, 36)
    text_surface5 = font.render( f"Throttle axis 1 (Mini Joystick X):         {slider5.get_current_value():.2f}", True, (0, 0, 0))
    window.blit(text_surface5, (50, 20))
    
    text_surface6 = font.render( f"Throttle axis 2 (Mini Joystick Y):         {slider6.get_current_value():.2f}", True, (0, 0, 0))
    window.blit(text_surface6, (50, 90))
    
    text_surface7 = font.render( f"Throttle axis 3 (Power):                        {slider7.get_current_value():.2f}", True, (0, 0, 0))
    window.blit(text_surface7, (50, 160))
    
    text_surface10 = font.render(f"Throttle axis 6 (Rudder):                     {slider10.get_current_value():.2f}", True, (0, 0, 0))
    window.blit(text_surface10, (50, 230))
    
    text_surface11 = font.render(f"Throttle axis 7 (Wheel):                        {slider11.get_current_value():.2f}", True, (0, 0, 0))
    window.blit(text_surface11, (50, 300))
    
    text_surface1 = font.render( f"Joystick axis 1 (Roll):                            {slider1.get_current_value():.2f}", True, (0, 0, 0))
    window.blit(text_surface1, (50, 380))
    
    text_surface2 = font.render( f"Joystick axis 2 (Pitch):                         {slider2.get_current_value():.2f}", True, (0, 0, 0))
    window.blit(text_surface2, (50, 450))
    
    text_surface3 = font.render( f"Joystick axis 3 (Rudder):                     {slider3.get_current_value():.2f}", True, (0, 0, 0))
    window.blit(text_surface3, (50, 520))
    
    text_surface4 = font.render( f"Joystick axis 4 (Power):                       {slider4.get_current_value():.2f}", True, (0, 0, 0))
    window.blit(text_surface4, (50, 590))
    
    # Draw joystick buttons in a matrix
    if joystick is not None:
        num_buttons = joystick.get_numbuttons()
        cols = 4  # Number of columns for the matrix
        for i in range(num_buttons):
            button_state = joystick.get_button(i)
            button_text = f"J B{i + 1}: {'1' if button_state else '0'}"
            row = i // cols
            col = i % cols
            text_surface = font.render(button_text, True, (0, 0, 0))
            window.blit(text_surface, (600 + col * 100, 50 + row * 40))
    
    # Draw throttle buttons in a matrix
    if throttle is not None:
        num_buttons = throttle.get_numbuttons()
        cols = 4  # Number of columns for the matrix
        for i in range(num_buttons):
            button_state = throttle.get_button(i)
            button_text = f"T B{i + 1}: {'1' if button_state else '0'}"
            row = i // cols
            col = i % cols
            text_surface = font.render(button_text, True, (0, 0, 0))
            window.blit(text_surface, (600 + col * 100, 300 + row * 40))
    
    # Draw joystick and throttle hats
    if joystick is not None:
        num_hats = joystick.get_numhats()
        for i in range(num_hats):
            hat_value = joystick.get_hat(i)
            hat_text = f"J Hat {i + 1}: {hat_value}"
            text_surface = font.render(hat_text, True, (0, 0, 0))
            window.blit(text_surface, (600, 500))
    
    if throttle is not None:
        num_hats = throttle.get_numhats()
        for i in range(num_hats):
            hat_value = throttle.get_hat(i)
            hat_text = f"T Hat {i + 1}: {hat_value}"
            text_surface = font.render(hat_text, True, (0, 0, 0))
            window.blit(text_surface, (600, 530))
    
    # Draw the UI
    manager.draw_ui(window)
    
    # Update the display
    pygame.display.flip()

# Quit pygame
pygame.quit()
