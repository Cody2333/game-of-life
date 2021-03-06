# button.py
from graphics import *
import time
class Button:
	"""A button is a labeled rectangle in a window.
	It is activated or deactivated with the activate()
	and deactivate() methods. The clicked(p) method
	returns true if the button is active and p is inside it."""
	
	def __init__(self, win, center, width, height, label,color = "grey"):
		""" Creates a rectangular button, eg:
		qb = Button(myWin, Point(30,25), 20, 10, 'Quit') """
		w,h = width/2.0, height/2.0
		x,y = center.getX(), center.getY()
		self.xmax, self.xmin = x+w, x-w
		self.ymax, self.ymin = y+h, y-h
		p1 = Point(self.xmin, self.ymin)
		p2 = Point(self.xmax, self.ymax)
		self.rect = Rectangle(p1,p2)
		self.rect.setOutline('#32cd32')
		self.rect.setFill('black')
		self.rect.draw(win)
		self.label = Text(center, label)
		self.label.draw(win)
		self.deactivate()
		
	def clicked(self, p):
		"RETURNS true if button active and p is inside"
		flag= self.active and \
		self.xmin <= p.getX() <= self.xmax and \
		self.ymin <= p.getY() <= self.ymax
		
		if flag:
			self.rect.setFill("#32cd32")
			self.deactivate()
			time.sleep(0.1)
			self.activate()
			self.rect.setFill('black')
		return flag
	def getLabel(self):
		"RETURNS the label string of this button."
		return self.label.getText()
		
	def activate(self):
		"Sets this button to 'active'."
		self.label.setFill('#32cd32')
		self.rect.setWidth(2)
		self.active = 1
		
	def deactivate(self):
		"Sets this button to 'inactive'."
		self.label.setFill('darkgrey')
		self.rect.setWidth(1)
		self.active = 0

