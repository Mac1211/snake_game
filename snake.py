from turtle import Turtle,Screen
STARTING_POSITION = [(0,0), (-20,0), (-40,0)]
Move_Distance = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
class Snake():
    def __init__(self):
        self.new_segment = []
        self.snake_creation() 

    def snake_creation(self):
        for i in STARTING_POSITION:
            self.add_segment(i)

    def add_segment(self,i):
        segment = Turtle("square")
        segment.color('white')
        segment.penup()
        segment.goto(i)
        self.new_segment.append(segment)

    def extend(self):
        self.add_segment(self.new_segment[-1].position())
    
    def up(self):
        if self.new_segment[0].heading() != DOWN:
            self.new_segment[0].setheading(UP)
    def down(self):
        if self.new_segment[0].heading() != UP:
            self.new_segment[0].setheading(DOWN)
    def left(self):
        if self.new_segment[0].heading() != RIGHT:
            self.new_segment[0].setheading(LEFT)
    def right(self):
        if self.new_segment[0].heading() != LEFT:
            self.new_segment[0].setheading(RIGHT)

    def reset(self):
        for seg in self.new_segment:
            seg.goto(1000,1000)
        self.new_segment.clear()
        self.snake_creation()


    def move(self):
        
        for seg in range(len(self.new_segment)-1, 0, -1):
            new_x = self.new_segment[seg - 1].xcor()
            new_y = self.new_segment[seg - 1].ycor()
            self.new_segment[seg].goto(new_x,new_y)
        self.new_segment[0].forward(Move_Distance) 