from pygame import Rect
from config import FONTS, COLORS

class TextBox:
	def __init__(self, text, color, x, y, w, h):
		self.color = color
		self.text = text
		self.rendered_text = FONTS["DEFAULT"].render(text, True, color)
		self.rect = Rect(x,y,w,h)

	def display(self, screen):
		screen.blit(self.rendered_text, self.rect)

class InputTextBox:
	def __init__(self, text, color, x, y, w, h):
		self.color = color
		self.text = text
		self.rendered_text = FONTS["DEFAULT"].render(text, True, color)
		self.rect = Rect(x,y,w,h)

	# Need to render new text graphic from font when the text changes
	def render(self):
		self.rendered_text = FONTS["DEFAULT"].render(self.text, True, self.color)

	def display(self, screen):
		screen.blit(self.rendered_text, self.rect)

	def set_text(self, text):
		self.text = text
		self.render()

	def append(self, char):
		self.text += char
		self.render()

	def backspace(self):
		self.text = self.text[:-1]
		self.render()

# DEFAULT TEXT BOXES
TEXT_BOXES = {
	"NAME_PROMPT": TextBox(
		'What is your name, traveller?',
		COLORS["WHITE"],
		0, 0, 500, 50
	),
	"NAME_INPUT": InputTextBox(
		'',
		COLORS["WHITE"],
		0, 50, 500, 50
	)
}
