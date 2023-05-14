
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label

COLOUR = (1, 0, 0, 1)
names = ["Nick", "Riston", "Mike", "John"]


class DynamicLabelApp(App):

    def build(self):
        self.title = "Dynamic Labels"
        self.root = Builder.load_file('dynamic_labels.kv')
        self.create_labels()
        return self.root

    def create_labels(self):
        for name in names:
            temp_label = Label(text=name)
            self.root.ids.main.add_widget(temp_label)


DynamicLabelApp().run()