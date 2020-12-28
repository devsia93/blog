from turtle import *

ANGLE = 60
STEP_COUNT = 10
FORWARD_ALPHABET = ('F')
LENGTH = 5

penup()
hideturtle()
setposition(0, -300)
left(90)
screensize(3800, 2600)
tracer(0)
pendown()

axiom = list('F++F++F')
rule = {'F':'F-F++F-F'}
result = axiom.copy()
stack = []
iterations = []
rec_it = 0

def turtle_driver(symbol, i = -1):
    if symbol in FORWARD_ALPHABET:
        if i > -1:
            global iterations, rec_it
            if i > iterations[rec_it]:
                rec_it += 1
            forward(STEP_COUNT ** -rec_it)
        else:
            forward(STEP_COUNT)
    elif symbol in '+':
        right(ANGLE)
        forward(STEP_COUNT)
    elif symbol in '-':
        left(ANGLE)
        forward(STEP_COUNT)
    elif symbol in '[':
        d = {'pos': pos(), 'heading': heading()}
        stack.append(d)
    elif symbol in ']':
        d = stack.pop()
        penup()
        goto(d['pos'])
        setheading(d['heading'])
        pendown()


for i in range(LENGTH):
    current_position = 0
    for a in range(len(axiom)):
        current_drawer = axiom[a]
        if current_drawer in rule.keys():
            result.pop(current_position)
            result[current_position:current_position] = list(
                rule[current_drawer])
            current_position += len(rule[current_drawer])
        else:
            current_position += 1
    axiom = list(result)
    iterations.append(len(axiom))

fillcolor('blue')
begin_fill()
for i in range(len(result)):
    turtle_driver(result[i], i)
end_fill()

update()
done()
