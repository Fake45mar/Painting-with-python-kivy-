from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.config import Config
from kivy.graphics import (Color, Ellipse, Rectangle, Line)
from kivy.core.window import Window
from random import random
Window.clearcolor = (0.5,0.5,0.5,1)
width_paint = 10
random_color = False
loop = 0
class PaintApp(Widget):
	global random_color
	global loop
	def on_touch_down(self, touch):
		global width_paint
		with self.canvas:
			if not random_color:
				Color(1, 0, 1, 1)
			elif random_color:
				Color(random(), random(), random(), 1)
			self.touch = Ellipse(pos = (touch.x - width_paint/2, touch.y - width_paint/2), size = (width_paint, width_paint))
			touch.ud['line'] = Line(points = (touch.x, touch.y), width = width_paint, on_touch_move=self.on_touch_move)
	def on_touch_move(self, touch):
		touch.ud['line'].points += (touch.x, touch.y)
class buildApp(App):
	def clear_canvas(self, instance):
		self.painter.canvas.clear()
	def save_canvas(self, instance):
		file_name = input("Enter file name ") + '.png'
		self.painter.size = (Window.size[0], Window.size[1])
		self.painter.export_to_png(file_name)
	def screenshot_canvas(self, instance):
		file_name = input("Enter file name ") + '.png'
		Window.screenshot(file_name)
	def random_colors(self, instance):
		global loop, random_color
		loop += 1
		if loop % 2 != 0:
			random_color = True
		else:
			random_color = False
	def set_size_width(self, instance):
		print(self.textinput.text)
		global width_paint
		width_paint = int(self.textinput.text)
	def build(self):
		self.icon = 'icon.png'
		self.title = 'Painting'
		self.parent = Widget()
		self.painter = PaintApp()
		self.textinput = TextInput(pos = (400, 0), size = (100, 50))
		self.parent.add_widget(self.painter)
		self.parent.add_widget(Button(text = "Clear", on_press = self.clear_canvas, pos = (0, 0),size = (100, 50)))
		self.parent.add_widget(Button(text = "Save", on_press = self.save_canvas, pos = (100, 0),size = (100, 50)))
		self.parent.add_widget(Button(text = "Screenshot", on_press = self.screenshot_canvas, pos = (200, 0),size = (100, 50)))
		self.parent.add_widget(Button(text = "Random color", on_press = self.random_colors, pos = (300, 0),size = (100, 50)))
		self.parent.add_widget(self.textinput)
		self.parent.add_widget(Button(text = "Set size", on_press = self.set_size_width, pos = (500, 0),size = (100, 50)))
		print(self.get_application_icon)
		return self.parent
if __name__ == '__main__':
	buildApp().run()