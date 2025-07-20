from kivy.app import App
from kivy.lang import Builder


class BoxLayoutDemo(App):
    """BoxLayoutDemo is a demo for boxlayout"""
    def build(self):
        """build a kivy app from the kivy file"""
        self.title = "Box Layout Demo"
        self.root = Builder.load_file('box_layout.kv')
        return self.root

    def output_label(self):
        """create greeting string to label"""
        self.root.ids.output_label.text = f"Hello {self.root.ids.input_name.text}"
