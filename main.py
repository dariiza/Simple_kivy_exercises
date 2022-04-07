from kivy.app import App
from kivy.graphics import Line, Color, Rectangle, Ellipse
from kivy.properties import StringProperty, BooleanProperty, Clock
from kivy.metrics import dp


from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.stacklayout import StackLayout




class WidgetsExample(GridLayout):
    on = BooleanProperty(False)
    count = 1
    my_text = StringProperty("1")
    text_input_str = StringProperty("foo")
    #slider_txt = StringProperty("Value")
    def on_button_click(self):
        if self.on == True:
            self.count += 1
            print("button clicked")
            self.my_text = str(self.count)
        else:
            pass

    def on_toggle_button_state(self, toggle_button):
        print("toggle state: " + toggle_button.state)

        if toggle_button.state == "normal":
            toggle_button.text = "OFF"
            self.on = False
        else:
            toggle_button.text = "ON"
            self.on = True

    def on_switch_active(self, widget):
        print("switch: " + str(widget.active))

    def on_slider_value(self, widget):
        self.slider_txt = str(int(widget.value))
        print("Slider: " + str(int(widget.value)))

    def on_text_validate(self, widget):
        self.text_input_str = widget.text


class GridLayoutExample(GridLayout):
    pass


class StackLayoutExample(StackLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        #self.orientation = "rl-tb"
        for i in range(0,100):
            size = dp(100)
            b = Button(text = str(i+1), size_hint=(None, None), size = (size, size))
            self.add_widget(b)

class AnchorLayoutExample(AnchorLayout):
    pass

class BoxLayoutExample(BoxLayout):
    pass
"""     def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = "vertical"
        b1 = Button(text = "a")
        b2 = Button(text = "b")
        b3 = Button(text = "c")


        self.add_widget(b1)
        self.add_widget(b2)
        self.add_widget(b3)

"""
class MainWidget(Widget):
    pass

class TheLabApp(App):
    pass


class CanvasExample1(Widget):
    pass

class CanvasExample2(Widget):
    pass

class CanvasExample3(Widget):
    pass



class CanvasExample4(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        with self.canvas:
            Line(points=(100, 100, 400, 500), width = 2)
            Color(0,1,0)
            Line(circle=(400,200,100))
            Line(rectangle=(400, 200, 100, 300))
            self.rect = Rectangle(pos=(700, 200), size=(150, 100))

    def on_button_click(self):
        #print("foo")
        x, y = self.rect.pos
        w, h = self.rect.size
        inc = dp(100)

        diff = self.width -(x+w)

        if diff < inc:
            inc = diff

        x += inc

        self.rect.pos = (x,y)


class CanvasExample5(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.ball_size = dp(50)
        self.vx = dp(3)
        self.vy = dp(4)
        with self.canvas:
            self.ball = Ellipse(pos = self.center, size =(self.ball_size, self.ball_size) )
        Clock.schedule_interval(self.update, 1/60)

    def on_size(self, *args):
        self.ball.pos = (self.center_x - self.ball_size/2, self.center_y - self.ball_size/2)

    def update(self, dt):
        x,y = self.ball.pos

        x += self.vx
        y += self.vy


        if y + self.ball_size > self.height:
            y = self.height-self.ball_size
            self.vy = -self.vy
        if x + self.ball_size > self.width:
            self.vx = -self.vx
        if y < 0:
            y = 0
            self.vy = -self.vy
        if x < 0:
            x = 0
            self.vx = -self.vx




        self.ball.pos = (x, y)


class CanvasExample6(Widget):
    pass

class CanvasExample7(BoxLayout):
    pass


TheLabApp().run()