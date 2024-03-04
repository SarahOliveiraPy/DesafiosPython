import pygame

# Inicializa o pygame
pygame.init()

# Carrega e reproduz o arquivo de áudio MP3
pygame.mixer.music.load('Desafio021.mp3')
pygame.mixer.music.play()

# Aguarda um tempo fixo antes de encerrar o pygame
pygame.time.delay(10000000) #tempo que vai rodar a música

# Encerra o pygame
pygame.quit()
