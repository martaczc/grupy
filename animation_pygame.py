import sys, pygame
import math, random

pygame.init()

yellow = 255, 255, 153
blue = 0, 0, 255
black = 0,0,0
num_pathes = 9
screen = pygame.display.set_mode()
w,h = screen.get_width(),screen.get_height()
print w,h

def minimum(x,y):
    if x<y:
        return x
    else:
        return y

m = minimum(w,h) 
external_margin = m/10 
interwal = 0.2

#center = w/2,h/2
#radius = minimum(w,h)/6

'''class path:
    def __init__(self, radius, center)'''

def path_parameters(num_pathes, interwal, w, m, external_margin):
    root = math.sqrt(num_pathes)
    rows = math.ceil(root)
    m2 = m - 2*external_margin
    radius = m2/(2*rows + interwal*(rows + 1)) #m2 = 2*row*radius + (row+1)*radius*interwal
    diffrence = math.fabs(w-h)
    margin = diffrence/2
    shorter = []
    longer = []
    s = (1 + interwal)*radius + external_margin 
    l = margin + external_margin 
    i = 0
    while i<num_pathes:
        i += 1
        if l + (2 + interwal)*radius < m + margin - external_margin:
            l += (1 + interwal)*radius
        else:
            l = margin + (1 + interwal)*radius + external_margin 
            s += (2 + interwal)*radius
        shorter.append(int(s))
        longer.append(int(l))
        l += radius
    if w == m:
        x = shorter
        y = longer
    else:
        y = shorter
        x = longer
    centers = [(x[j],y[j]) for j in xrange(num_pathes)]  
    return {'radius':int(radius), 'centers':centers}  

def random_from_circle(center,radius):
    t = 2*math.pi*random.random()
    u = random.random() + random.random()
    if u>1:
        r = 2-u
    else: 
        r = u
    return [r*math.cos(t)*radius + center[0], r*math.sin(t)*radius + center[1]]  

class Ind:
    def __init__(self, position, size, color): 
        self.position = [int(p) for p in position]
        self.size = int(size)
        self.color = color 
    def draw(self, screen):
        pygame.draw.circle(screen, self.color, self.position, self.size)


class Path:

    def __init__(self, center, radius, back_color, ind_colors):
        self.center = center
        self.radius = radius
        self.size = radius/20
        self.color = back_color
        self.individuals = [Ind(random_from_circle(center, radius*9/10), self.size, color) for color in ind_colors]
     
    def draw(self, screen):
        pygame.draw.circle(screen, self.color, self.center, self.radius)
        for ind in self.individuals:
            ind.draw(screen)
        


parameters = path_parameters(num_pathes, interwal, w, m, external_margin)
ind_colors = [blue for n in xrange(30)]
#for center in parameters['centers']:
#    print center, parameters['radius'], yellow, ind_colors
radius = parameters['radius']
centers = parameters['centers']
pathes = [Path(center, radius, yellow, ind_colors) for center in centers]
screen.fill(black)
for path in pathes:
    path.draw(screen)
pygame.display.flip()

'''radius = parameters['radius']
print radius
centers = parameters['centers']
screen.fill(black)
for center in centers:
    print center
    pygame.draw.circle(screen, yellow, center, radius)
pygame.display.flip()'''




