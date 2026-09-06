from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class AdaApp(BoxLayout):
    def __init__(self, **kwargs):
        super(AdaApp, self).__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = 40
        self.spacing = 20

        # Title Label
        self.add_widget(Label(text='Welcome to Ada App', font_size=24))

        # Text Input
        self.user_input = TextInput(text='', hint_text='Enter your name here', multiline=False, font_size=18)
        self.add_widget(self.user_input)

        # Submit Button
        self.btn = Button(text='Submit', font_size=18, background_color=(0.1, 0.6, 0.3, 1))
        self.btn.bind(on_press=self.on_button_click)
        self.add_widget(self.btn)

        # Result Label
        self.result_label = Label(text='', font_size=18)
        self.add_widget(self.result_label)

    def on_button_click(self, instance):
        name = self.user_input.text
        if name:
            self.result_label.text = f'Hello, {name}! Ada is working.'
        else:
            self.result_label.text = 'Please enter a valid name.'

class MainApp(App):
    def build(self):
        return AdaApp()

if __name__ == '__main__':
    MainApp().run()
      
