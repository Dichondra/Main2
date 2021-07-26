# Nowe okno graficzne
# Demonstruje tworzenie okna graficznego

from livewires import games

games.init(screen_width = 640, screen_height = 480, fps = 50)

try:
    games.screen.mainloop()
except:
    quit()