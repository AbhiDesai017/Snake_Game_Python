from turtle import Turtle
starting_position = [(0, 0), (-20, 0), (-40, 0)]
move_distance = 20
Up = 90
Down = 270
Right = 0
Left = 180
class Snake:

     def __init__(self):
         self.segment = []
         self.create_snake()
         self.head = self.segment[0]

     def create_snake(self):
         for position in starting_position:
             self.add_segment(position)


     def add_segment(self,position):
         new_segment = Turtle("square")
         new_segment.color("white")
         new_segment.penup()
         new_segment.goto(position)
         self.segment.append(new_segment)

     def extend(self):
         self.add_segment(self.segment[-1].position())

     def move(self):
         for seg_num in range(len(self.segment) - 1, 0, -1):
             x_num = self.segment[seg_num - 1].xcor()
             y_num = self.segment[seg_num - 1].ycor()
             self.segment[seg_num].goto(x_num, y_num)
         self.head.forward(move_distance)

     def up(self):
         if self.head.heading() != Down:
            self.head.setheading(Up)

     def down(self):
         if self.head.heading() != Up:
            self.head.setheading(Down)

     def left(self):
         if self.head.heading() != Right:
            self.head.setheading(Left)

     def right(self):
         if self.head.heading() != Left:
            self.head.setheading(Right)


















