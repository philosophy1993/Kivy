from kivy.app import App
from kivy.uix.widget import Widget
 
class KurikkuInput(Widget):
    def on_touch_down(self, touch):
        print(touch)
 
class IntroKivy(App):
    def build(self):
        return KurikkuInput()
 
if __name__ == "__main__":
    IntroKivy().run()
