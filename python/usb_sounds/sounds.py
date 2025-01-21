from pynput import keyboard
import pygame

pygame.init()
pygame.joystick.init()
pygame.mixer.init()

sound_map = {
    0: 'sound_1.mp3',
    1: 'sound_2.mp3'
}


def play_sound(button):
    """Reproduce el sonido correspondiente al botón pulsado."""
    if button in sound_map:
        sound_file = sound_map[button]
        pygame.mixer.music.load(sound_file)
        pygame.mixer.music.play()


if pygame.joystick.get_count() == 0:
    print("No se detectó ningún mando conectado.")
    pygame.quit()
    exit()

joystick = pygame.joystick.Joystick(0)
joystick.init()
print(f"Mando detectado: {joystick.get_name()}")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.JOYBUTTONDOWN:
            button = event.button
            print(f"Botón {button} presionado")
            play_sound(button)

pygame.quit()
