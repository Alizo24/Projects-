import flet as ft

def main(page: ft.Page):
    songs = [
        {
            "title": "Camila - Todo Cambio",
            "url": "https://github.com/Alizo24/songs/raw/main/Camila-Todo-Cambio-_Official-Video_.mp3",
        },
        {
            "title": "Ed Maverick - Fuentes De Ortiz",
            "url": "https://github.com/Alizo24/songs/raw/main/Ed-Maverick-Fuentes-De-Ortiz.mp3",
        },
        {
            "title": "Juan Luis Guerra 4.40 - Mambo 23",
            "url": "https://github.com/Alizo24/songs/raw/main/Juan-Luis-Guerra-4.40-Mambo-23-_Video-Oficial_.mp3",
        },
        {
            "title": "Lo Grande Que Es Perdonar",
            "url": "https://github.com/Alizo24/songs/raw/main/Lo-Grande-Que-Es-Perdonar.mp3",
        },
        {
            "title": "Tony Dize - El Doctorado",
            "url": "https://github.com/Alizo24/songs/raw/main/Tony-Dize-El-Doctorado-_Official-Video_.mp3",
        }
    ]
    
    current_song_index = [0]
    is_playing = [False]  # Usamos una lista para manejar el estado de reproducción
    audio_control = ft.Audio(src=songs[current_song_index[0]]["url"], autoplay=False)
    page.overlay.append(audio_control)
    
    current_song_title = ft.Text(value=songs[current_song_index[0]]["title"], size=20)
    page.add(current_song_title)
    
    def change_song(song_index):
        current_song_index[0] = song_index
        audio_control.src = songs[song_index]["url"]
        current_song_title.value = songs[song_index]["title"]
        audio_control.play()
        is_playing[0] = True  # Actualizar el estado de reproducción
        update_play_pause_icon()
        page.update()
    
    def next_song(_):
        next_index = (current_song_index[0] + 1) % len(songs)
        change_song(next_index)
    
    def prev_song(_):
        prev_index = (current_song_index[0] - 1) % len(songs)
        change_song(prev_index)
    
    def toggle_play_pause(_):
        if is_playing[0]:
            audio_control.pause()
            is_playing[0] = False
        else:
            audio_control.play()
            is_playing[0] = True
        update_play_pause_icon()
        page.update()
    
    def update_play_pause_icon():
        if is_playing[0]:
            play_pause_button.icon = ft.icons.PAUSE
        else:
            play_pause_button.icon = ft.icons.PLAY_ARROW
    
    play_pause_button = ft.IconButton(icon=ft.icons.PLAY_ARROW, on_click=toggle_play_pause)
    prev_button = ft.IconButton(icon=ft.icons.SKIP_PREVIOUS, on_click=prev_song)
    next_button = ft.IconButton(icon=ft.icons.SKIP_NEXT, on_click=next_song)
    
    page.add(prev_button, play_pause_button, next_button)

ft.app(target=main)
