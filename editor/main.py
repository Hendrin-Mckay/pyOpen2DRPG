import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW

class GameEditor(toga.App):
    def startup(self):
        self.main_window = toga.MainWindow(title=self.name)

        main_box = toga.Box()
        main_box.style.update(direction=COLUMN, padding=10)

        label = toga.Label("Hello, Toga!")
        label.style.update(padding_bottom=10)
        main_box.add(label)

        self.main_window.content = main_box
        self.main_window.show()

def main():
    return GameEditor('Game Editor', 'org.example.gameeditor')

if __name__ == '__main__':
    main().main_loop()
