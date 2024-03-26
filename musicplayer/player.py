import pygame

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((800, 600))
done = False

songs = ["musicplayer/somebodyelse.mp3", "musicplayer/help.mp3", "musicplayer/love.mp3"]
current_song_index = 0

def play_song():
    pygame.mixer.music.load(songs[current_song_index])
    pygame.mixer.music.play()

playing = False
play_first_time = True
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if play_first_time:
                    play_song()
                    play_first_time = False
                    playing = True
                elif playing:
                    pygame.mixer.music.pause()
                    playing = False
                else:
                    pygame.mixer.music.unpause()
                    playing = True
            elif event.key == pygame.K_RIGHT:
                current_song_index = (current_song_index + 1) % len(songs)
                play_song()
            elif event.key == pygame.K_LEFT:
                current_song_index = (current_song_index - 1) % len(songs)
                play_song()


    screen.fill((255, 255, 255))

    pygame.display.flip()
        
        

    




