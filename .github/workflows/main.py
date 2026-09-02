from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button

class TestApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')
        label = Label(text='Hello from Python!', font_size='24sp')
        btn = Button(text='Click Me', size_hint=(1, 0.2))
        btn.bind(on_press=lambda x: print("Clicked!"))
        layout.add_widget(label)
        layout.add_widget(btn)
        return layout

if __name__ == '__main__':
    TestApp().run()
