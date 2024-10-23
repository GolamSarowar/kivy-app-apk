import json
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.spinner import Spinner
from kivy.uix.button import Button

class MyLayout(BoxLayout):
    def __init__(self, **kwargs):
        super(MyLayout, self).__init__(**kwargs)
        self.orientation = 'vertical'
        
        self.add_widget(Label(text='Select Information', font_size=24))
        
        self.spinner = Spinner(
            text='Select an option',
            values=['Symptoms', 'Medication', 'Consultation'],
            size_hint=(1, None),
            height=50
        )
        self.add_widget(self.spinner)

        self.button = Button(
            text='Show',
            size_hint=(1, None),
            height=50
        )
        self.add_widget(self.button)

        self.button.bind(on_press=self.show_info)

        self.display_label = Label(
            text='',
            font_size=18,
            size_hint=(1, None),
            height=50
        )
        self.add_widget(self.display_label)

        # Load the disease information from a JSON file
        try:
            with open('data/info.json', 'r') as f:
                self.disease_info = json.load(f)
        except Exception as e:
            print(f"Error loading JSON file: {e}")
            self.disease_info = {}

    def show_info(self, instance):
        selected_option = self.spinner.text
        info = self.disease_info.get(selected_option, "Information not available.")
        self.display_label.text = f'{selected_option}: {info}'

class MyApp(App):
    def build(self):
        return MyLayout()

if __name__ == '__main__':
    MyApp().run()
