import kivy.uix.button as kb
from kivy.app import App
from kivy.uix.widget import Widget


class Button_Widget(Widget):

    def __init__(self, **kwargs):
        super(Button_Widget, self).__init__(**kwargs)
        btn1 = kb.Button(text='Hello World 1')
        btn1.bind(on_press=self.callback)
        self.add_widget(btn1)

    def callback(self, instance):
        print('The button %s state is <%s>' % (instance, instance.state))


class ButtonApp(App):

    def build(self):
        return Button_Widget()


if __name__ == "__main__":
    ButtonApp().run()