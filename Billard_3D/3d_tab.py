
import pygame
import numpy as np
from math import *

WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
vert=(100,128,0)
gray = (123, 125, 125)
grisfoncé= (20, 20, 20)
grisfoncé_1=(40, 40, 40)
WIDTH, HEIGHT = 1380, 700
pygame.display.set_caption("3D projection ")

screen = pygame.display.set_mode((WIDTH, HEIGHT))

position_cube = [WIDTH//2, HEIGHT//2]
angle_x=0
angle_y=0
angle_z = 0
speed_rotation=0.01
points = []
#----------------------------cube principale -------------------
points.append(np.matrix([10,5,3]))#0
points.append(np.matrix([10,-5,3]))#1
points.append(np.matrix([-10,-5,3]))#2
points.append(np.matrix([-10,5,3]))#3
points.append(np.matrix([10,5,-3]))#4
points.append(np.matrix([10,-5,-3]))#5
points.append(np.matrix([-10,-5,-3]))#6
points.append(np.matrix([-10,5,-3]))#7
#---------------bordure bas-----------------------------
points.append(np.matrix([7.5,3.5,3]))#8
points.append(np.matrix([1,3.5,3]))#9

points.append(np.matrix([-1,3.5,3]))#10
points.append(np.matrix([-7.5,3.5,3]))#11
#-----------------bordure droite-------------------------
points.append(np.matrix([8.5,2.5,3]))#12
points.append(np.matrix([8.5,-2.5,3]))#13

#---------------bordure haut----------------------------
points.append(np.matrix([7.5,-3.5,3]))#14
points.append(np.matrix([1,-3.5,3]))#15

points.append(np.matrix([-1,-3.5,3]))#16
points.append(np.matrix([-7.5,-3.5,3]))#17

#----------bordure gauche----------------------------
points.append(np.matrix([-8.5,2.5,3]))#18
points.append(np.matrix([-8.5,-2.5,3]))#19

#-----------pocket1-droite coin-bas----------------------
points.append(np.matrix([9.5,5,3]))#20
points.append(np.matrix([8.5,5,3]))#21
points.append(np.matrix([7.5,4.5,3]))#22

points.append(np.matrix([10,4.5,3]))#23
points.append(np.matrix([10,3.5,3]))#24
points.append(np.matrix([9.5,2.5,3]))#25
#----------pocket2-droite coin-haut-----------------
points.append(np.matrix([9.5,-5,3]))#26
points.append(np.matrix([8.5,-5,3]))#27
points.append(np.matrix([7.5,-4.5,3]))#28

points.append(np.matrix([10,-4.5,3]))#29
points.append(np.matrix([10,-3.5,3]))#30
points.append(np.matrix([9.5,-2.5,3]))#31
#--------------pocket3 gauche coin haut--------------
points.append(np.matrix([-9.5,-5,3]))#32
points.append(np.matrix([-8.5,-5,3]))#33
points.append(np.matrix([-7.5,-4.5,3]))#34

points.append(np.matrix([-10,-4.5,3]))#35
points.append(np.matrix([-10,-3.5,3]))#36
points.append(np.matrix([-9.5,-2.5,3]))#37
#--------------pocket4 gauche coin bas--------------
points.append(np.matrix([-8.5,5,3]))#38
points.append(np.matrix([-9.5,5,3]))#39
points.append(np.matrix([-7.5,4.5,3]))#40


points.append(np.matrix([-10,4.5,3]))#41
points.append(np.matrix([-10,3.5,3]))#42
points.append(np.matrix([-9.5,2.5,3]))#43
#-------------pocket5 bas milieu-------------

points.append(np.matrix([0,5,3]))#44
points.append(np.matrix([-.8,4.5,3]))#45
points.append(np.matrix([.8,4.5,3]))#46
#--------------pocket haut milieu----------------
points.append(np.matrix([0,-5,3]))#47
points.append(np.matrix([-.8,-4.5,3]))#48
points.append(np.matrix([.8,-4.5,3]))#49

#--------------------------arriere---------

points.append(np.matrix([10,5,2]))#50
points.append(np.matrix([10,-5,2]))#51
points.append(np.matrix([-10,-5,2]))#52
points.append(np.matrix([-10,5,2]))#53

#------------------------------------------------------------------------------------------------------
#---------------bordure bas-----------------------------
points.append(np.matrix([7.5,3.5,2]))#54
points.append(np.matrix([1,3.5,2]))#55

points.append(np.matrix([-1,3.5,2]))#56
points.append(np.matrix([-7.5,3.5,2]))#57
#-----------------bordure droite-------------------------
points.append(np.matrix([8.5,2.5,2]))#58
points.append(np.matrix([8.5,-2.5,2]))#59

#---------------bordure haut----------------------------
points.append(np.matrix([7.5,-3.5,2]))#60
points.append(np.matrix([1,-3.5,2]))#61

points.append(np.matrix([-1,-3.5,2]))#62
points.append(np.matrix([-7.5,-3.5,2]))#63

#----------bordure gauche----------------------------
points.append(np.matrix([-8.5,2.5,2]))#64
points.append(np.matrix([-8.5,-2.5,2]))#65
#-------------------------------------------------------------------------------------------------
#-----------pocket1-droite coin-bas----------------------
points.append(np.matrix([9.5,5,2]))#66
points.append(np.matrix([8.5,5,2]))#67
points.append(np.matrix([7.5,4.5,2]))#68

points.append(np.matrix([10,4.5,2]))#69
points.append(np.matrix([10,3.5,2]))#70
points.append(np.matrix([9.5,2.5,2]))#71
#----------pocket2-droite coin-haut-----------------
points.append(np.matrix([9.5,-5,2]))#72
points.append(np.matrix([8.5,-5,2]))#73
points.append(np.matrix([7.5,-4.5,2]))#74

points.append(np.matrix([10,-4.5,2]))#75
points.append(np.matrix([10,-3.5,2]))#76
points.append(np.matrix([9.5,-2.5,2]))#77
#--------------pocket3 gauche coin haut--------------
points.append(np.matrix([-9.5,-5,2]))#78
points.append(np.matrix([-8.5,-5,2]))#79
points.append(np.matrix([-7.5,-4.5,2]))#80

points.append(np.matrix([-10,-4.5,2]))#81
points.append(np.matrix([-10,-3.5,2]))#82
points.append(np.matrix([-9.5,-2.5,2]))#83
#--------------pocket4 gauche coin bas--------------

points.append(np.matrix([-8.5,5,2]))#84
points.append(np.matrix([-9.5,5,2]))#85
points.append(np.matrix([-7.5,4.5,2]))#86


points.append(np.matrix([-10,4.5,2]))#87
points.append(np.matrix([-10,3.5,2]))#88
points.append(np.matrix([-9.5,2.5,2]))#89
#-------------pocket5 bas milieu-------------

points.append(np.matrix([0,5,2]))#90
points.append(np.matrix([-.8,4.5,2]))#91
points.append(np.matrix([.8,4.5,2]))#92
#--------------pocket6 haut milieu----------------
points.append(np.matrix([0,-5,2]))#93
points.append(np.matrix([-.8,-4.5,2]))#94
points.append(np.matrix([.8,-4.5,2]))#95

#-----------------pied---------------------------
      #--------pied gauche haut--------
points.append(np.matrix([-8.5,-5,-3]))#96-79
points.append(np.matrix([-10,-3.5,-3]))#97-82

    #---------------droite haut--------------
points.append(np.matrix([8.5,-5,-3]))#98-73
points.append(np.matrix([10,-3.5,-3]))#99-76
    #--------------droite bas-------
points.append(np.matrix([10,3.5,-3]))#100-70
points.append(np.matrix([8.5,5,-3]))#101-67
    #----------------gauche bas----------
points.append(np.matrix([-8.5,5,-3]))#102-84
points.append(np.matrix([-10,3.5,-3]))#103-88
#----------------------------------------------------------------------------------------
size=400
alpha=1
beta=1

points_projecter = [
    [n, n] for n in range(len(points))
]
print("points_projecter",points_projecter)
print("point0",points_projecter[0])
def Lien_points(i, j, points,color):
    pygame.draw.line(screen,color, (points[i][0], points[i][1]), (points[j][0], points[j][1]),0)

#-------------------------------------------------------les Matrices de rotation (x,y,z)--------------
def rot_x(angle_x):
    rotation_x = np.matrix([
        [1, 0, 0],
        [0, cos(angle_x), -sin(angle_x)],
        [0, sin(angle_x), cos(angle_x)],
    ])
    return rotation_x
def rot_y(angle_y):
    rotation_y = np.matrix([
        [cos(angle_y), 0, sin(angle_y)],
        [0, 1, 0],
        [-sin(angle_y), 0, cos(angle_y)],
    ])
    return rotation_y
def rot_z(angle_z):
    rotation_z = np.matrix([
        [cos(angle_z), -sin(angle_z), 0],
        [sin(angle_z), cos(angle_z), 0],
        [0, 0, 1],
    ])
    return rotation_z



screen.fill((0, 0, 0), rect=((0,0),(1,1)))
clock = pygame.time.Clock()
#----------------------------------------------------------------------------------------
while True:
    clock.tick(30)

    screen.fill(WHITE)
    i = 0
    for point in points:
        rotation_2d = np.dot(rot_y(angle_y), point.reshape(3,1))
        rotation_2d = np.dot(rot_x(angle_x), rotation_2d)
        rotation_2d = np.dot(rot_z(angle_z), rotation_2d)
        f=25
        z=rotation_2d[2][0]
        m=1/(f-z)
        if m==0:
            m=1
        matrice_projection = np.matrix([
            [m, 0, 0],
            [0, m, 0],
            [0, 0, 1]
        ])
        projection_2d = np.dot(matrice_projection, rotation_2d)
        x=projection_2d[0][0]
        y=projection_2d[1][0]
        #z = int(rotation_2d[2][0])

        u = int(x*size) + position_cube[0]
        v = int(y*size) + position_cube[1]

        points_projecter[i] = [u, v]
        pygame.draw.circle(screen, BLACK, (u, v), 0)
        i += 1
#----------------------------cube------------------------
    Lien_points(0,1,points_projecter,grisfoncé)
    Lien_points(1,2,points_projecter,grisfoncé)
    Lien_points(2,3,points_projecter,grisfoncé)
    Lien_points(0,3,points_projecter,grisfoncé)
    Lien_points(4,5,points_projecter,grisfoncé)
    Lien_points(5,6,points_projecter,grisfoncé)
    Lien_points(6,7,points_projecter,grisfoncé)
    Lien_points(3,7,points_projecter,grisfoncé)
    Lien_points(0,4,points_projecter,grisfoncé)
    Lien_points(1,5,points_projecter,grisfoncé)
    Lien_points(2,6,points_projecter,grisfoncé)
    Lien_points(4,7,points_projecter,grisfoncé)
#------------------bordure---------------------------------
    Lien_points(8,9,points_projecter,grisfoncé)
    Lien_points(10,11,points_projecter,grisfoncé)
    Lien_points(12,13,points_projecter,grisfoncé)
    Lien_points(14, 15, points_projecter, grisfoncé)
    Lien_points(16, 17, points_projecter, grisfoncé)
    Lien_points(18, 19, points_projecter, grisfoncé)
    pygame.draw.polygon(screen,gray,(points_projecter[8],points_projecter[9],points_projecter[46],points_projecter[44],points_projecter[21],points_projecter[22],points_projecter[8]),width =0)
#------------------pocket1 coin bas droite-------------------------------
    Lien_points(20, 23, points_projecter, grisfoncé)
    Lien_points(20, 21, points_projecter, grisfoncé)
    Lien_points(21, 22, points_projecter, grisfoncé)
    Lien_points(22, 8, points_projecter, grisfoncé)
    Lien_points(23, 24, points_projecter, grisfoncé)
    Lien_points(24, 25, points_projecter, grisfoncé)
    Lien_points(25, 12, points_projecter, grisfoncé)

#-----------------------pocket 2- coin haut droite------------
    Lien_points(29, 26, points_projecter, grisfoncé)
    Lien_points(26, 27, points_projecter, grisfoncé)
    Lien_points(27, 28, points_projecter, grisfoncé)
    Lien_points(28, 14, points_projecter, grisfoncé)
    Lien_points(29, 30, points_projecter, grisfoncé)
    Lien_points(30, 31, points_projecter, grisfoncé)
    Lien_points(31, 13, points_projecter, grisfoncé)
#--------------------------------------pocket 3- coin haut gauche----------

    Lien_points(32, 35, points_projecter, grisfoncé)
    Lien_points(35, 36, points_projecter, grisfoncé)
    Lien_points(36, 37, points_projecter, grisfoncé)
    Lien_points(32, 33, points_projecter, grisfoncé)
    Lien_points(33, 34, points_projecter, grisfoncé)
    Lien_points(34, 17, points_projecter, grisfoncé)
    Lien_points(37, 19, points_projecter, grisfoncé)
    # --------------------------------------pocket 4- coin bas gauche----------

    Lien_points(38, 39, points_projecter, grisfoncé)
    Lien_points(39, 41, points_projecter, grisfoncé)

    Lien_points(41,42 , points_projecter, grisfoncé)
    Lien_points(42, 43, points_projecter, grisfoncé)
    Lien_points(43, 18, points_projecter, grisfoncé)
    Lien_points(38, 40, points_projecter, grisfoncé)
    Lien_points(40, 11, points_projecter, grisfoncé)
#------------------pocket5 milieu bas--------------------
    Lien_points(44, 45, points_projecter, grisfoncé)
    Lien_points(44, 46, points_projecter, grisfoncé)
    Lien_points(45, 10, points_projecter, grisfoncé)
    Lien_points(46, 9, points_projecter, grisfoncé)
    # ------------------pocket5 milieu haut--------------------
    Lien_points(47, 48, points_projecter, grisfoncé)
    Lien_points(47, 49, points_projecter, grisfoncé)
    Lien_points(48, 16, points_projecter, grisfoncé)
    Lien_points(49, 15, points_projecter, grisfoncé)
    #--------arrier bordure-----------------
    Lien_points(50, 51, points_projecter, grisfoncé)
    Lien_points(51, 52, points_projecter, grisfoncé)
    Lien_points(52, 53, points_projecter, grisfoncé)
    Lien_points(53, 50, points_projecter, grisfoncé)
#------------------------------------------------------arriere,plan ----------------------------
    Lien_points(54, 55, points_projecter, grisfoncé)
    Lien_points(56, 57, points_projecter, grisfoncé)

    Lien_points(64, 65, points_projecter, grisfoncé)

    Lien_points(60, 61, points_projecter, grisfoncé)
    Lien_points(62, 63, points_projecter, grisfoncé)

    Lien_points(58, 59, points_projecter, grisfoncé)
#---------------------pocket1 arrier coin bas ------------
    Lien_points(66, 67, points_projecter, grisfoncé)
    Lien_points(67, 68, points_projecter, grisfoncé)
    Lien_points(68, 54, points_projecter, grisfoncé)
    Lien_points(54, 8, points_projecter, grisfoncé)
    Lien_points(68,22 , points_projecter, grisfoncé)
    Lien_points(69, 70, points_projecter, grisfoncé)
    Lien_points(70, 71, points_projecter, grisfoncé)
    Lien_points(58, 71, points_projecter, grisfoncé)
    Lien_points(69, 66, points_projecter, grisfoncé)
    Lien_points(58, 12, points_projecter, grisfoncé)
    #Lien_points(69, 22, points_projecter, WHITE)

#---------------pockt 2 arriere coin _haut-----------------------------------
    pygame.draw.polygon(screen,gray,(points_projecter[54],points_projecter[55],points_projecter[92],points_projecter[90],points_projecter[67],points_projecter[68],points_projecter[54]),width =0)
    pygame.draw.polygon(screen,gray,(points_projecter[90],points_projecter[91],points_projecter[56],points_projecter[57],points_projecter[86],points_projecter[84],points_projecter[85]),width=0)

    pygame.draw.polygon(screen,gray,(points_projecter[10],points_projecter[11],points_projecter[40],points_projecter[38],points_projecter[39],points_projecter[44],points_projecter[45]),width=0)

    pygame.draw.polygon(screen,gray,(points_projecter[82],points_projecter[83],points_projecter[65],points_projecter[64],points_projecter[89],points_projecter[88]),width=0)
    pygame.draw.polygon(screen,gray,(points_projecter[18],points_projecter[43],points_projecter[42],points_projecter[36],points_projecter[37],points_projecter[19]),width=0)

    pygame.draw.polygon(screen,gray,(points_projecter[33],points_projecter[34],points_projecter[17],points_projecter[16],points_projecter[48],points_projecter[47]),width=0)
    pygame.draw.polygon(screen,gray,(points_projecter[79],points_projecter[80],points_projecter[63],points_projecter[62],points_projecter[94],points_projecter[93]),width=0)

    pygame.draw.polygon(screen,gray,(points_projecter[47],points_projecter[49],points_projecter[15],points_projecter[14],points_projecter[28],points_projecter[27]),width=0)
    pygame.draw.polygon(screen,gray,(points_projecter[93],points_projecter[95],points_projecter[61],points_projecter[60],points_projecter[74],points_projecter[73]),width=0)

    pygame.draw.polygon(screen,grisfoncé,(points_projecter[30],points_projecter[31],points_projecter[13],points_projecter[12],points_projecter[25],points_projecter[24]),width=0)
    pygame.draw.polygon(screen,gray,(points_projecter[76],points_projecter[77],points_projecter[59],points_projecter[58],points_projecter[71],points_projecter[70]),width=0)
#-------------------------------------------------------------bordure table-----------
    pygame.draw.polygon(screen,grisfoncé,(points_projecter[0],points_projecter[50],points_projecter[51],points_projecter[1]),width=0)
    pygame.draw.polygon(screen, grisfoncé,
                        (points_projecter[1], points_projecter[51], points_projecter[52], points_projecter[2]), width=0)
    pygame.draw.polygon(screen, grisfoncé,
                        (points_projecter[2], points_projecter[52], points_projecter[53], points_projecter[3]), width=0)
    pygame.draw.polygon(screen,grisfoncé,(points_projecter[3],points_projecter[53],points_projecter[50],points_projecter[0]),width=0)
#-------------------------------------pocket gauche haut---------------
    pygame.draw.polygon(screen,BLACK,(points_projecter[17],points_projecter[63],points_projecter[80],points_projecter[34]),width=0)
    pygame.draw.polygon(screen,BLACK,(points_projecter[34],points_projecter[33],points_projecter[79],points_projecter[80]),width=0)
    pygame.draw.polygon(screen,BLACK,(points_projecter[33],points_projecter[32],points_projecter[78],points_projecter[79]),width=0)
    pygame.draw.polygon(screen,BLACK,(points_projecter[32],points_projecter[35],points_projecter[81],points_projecter[78]),width=0)
    pygame.draw.polygon(screen,BLACK,(points_projecter[35],points_projecter[36],points_projecter[82],points_projecter[81]),width=0)
    pygame.draw.polygon(screen,BLACK,(points_projecter[36],points_projecter[37],points_projecter[83],points_projecter[82]),width=0)
    pygame.draw.polygon(screen,BLACK,(points_projecter[37],points_projecter[19],points_projecter[65],points_projecter[83]),width=0)
    pygame.draw.polygon(screen, grisfoncé_1,(points_projecter[65], points_projecter[83], points_projecter[82], points_projecter[81],points_projecter[78],points_projecter[79],points_projecter[80],points_projecter[63]), width=0)

#------------------------------------pocket gauche bas-----------------------------------
    pygame.draw.polygon(screen, BLACK,(points_projecter[18], points_projecter[64], points_projecter[89], points_projecter[43]), width=0)
    pygame.draw.polygon(screen, BLACK,(points_projecter[43], points_projecter[89], points_projecter[88], points_projecter[42]),width=0)
    pygame.draw.polygon(screen, BLACK,(points_projecter[42], points_projecter[41], points_projecter[87], points_projecter[88]),width=0)
    pygame.draw.polygon(screen, BLACK,(points_projecter[41], points_projecter[87], points_projecter[85], points_projecter[39]),width=0)
    pygame.draw.polygon(screen, BLACK,(points_projecter[39], points_projecter[38], points_projecter[84], points_projecter[85]),width=0)
    pygame.draw.polygon(screen, BLACK,(points_projecter[38], points_projecter[40], points_projecter[86], points_projecter[84]), width=0)
    pygame.draw.polygon(screen, grisfoncé_1,(points_projecter[57], points_projecter[86], points_projecter[84], points_projecter[85],points_projecter[87],points_projecter[88],points_projecter[89],points_projecter[64]), width=0)

   #-------------------pocket milieu bas---------------------
    pygame.draw.polygon(screen, BLACK,(points_projecter[10], points_projecter[56], points_projecter[91], points_projecter[45]), width=0)
    pygame.draw.polygon(screen, BLACK,(points_projecter[45], points_projecter[91], points_projecter[90], points_projecter[44]), width=0)
    pygame.draw.polygon(screen, BLACK,(points_projecter[44], points_projecter[46], points_projecter[92], points_projecter[90]), width=0)
    pygame.draw.polygon(screen, BLACK,(points_projecter[92], points_projecter[55], points_projecter[9], points_projecter[46]), width=0)
    pygame.draw.polygon(screen, grisfoncé_1,(points_projecter[56], points_projecter[91], points_projecter[90], points_projecter[92],points_projecter[55]), width=0)

#-----------------pocket milieu haut-----------------------------
    pygame.draw.polygon(screen, BLACK,(points_projecter[16], points_projecter[62], points_projecter[94], points_projecter[48]), width=0)
    pygame.draw.polygon(screen, BLACK,(points_projecter[48], points_projecter[94], points_projecter[93], points_projecter[47]), width=0)
    pygame.draw.polygon(screen, BLACK,(points_projecter[47], points_projecter[49], points_projecter[95], points_projecter[93]), width=0)
    pygame.draw.polygon(screen, BLACK,(points_projecter[49], points_projecter[15], points_projecter[61], points_projecter[95]), width=0)
    pygame.draw.polygon(screen, grisfoncé_1,(points_projecter[62], points_projecter[94], points_projecter[93], points_projecter[95],points_projecter[61]), width=0)

#-------------------------------pocket droite haut -----------------
    pygame.draw.polygon(screen, BLACK,(points_projecter[14], points_projecter[60], points_projecter[74], points_projecter[28]), width=0)
    pygame.draw.polygon(screen, BLACK,(points_projecter[74], points_projecter[73], points_projecter[27], points_projecter[28]), width=0)
    pygame.draw.polygon(screen, BLACK,(points_projecter[27], points_projecter[26], points_projecter[72], points_projecter[73]), width=0)
    pygame.draw.polygon(screen, BLACK,(points_projecter[72], points_projecter[75], points_projecter[29], points_projecter[26]), width=0)
    pygame.draw.polygon(screen, BLACK,(points_projecter[29], points_projecter[75], points_projecter[76], points_projecter[30]), width=0)
    pygame.draw.polygon(screen, BLACK,(points_projecter[30], points_projecter[76], points_projecter[77], points_projecter[31]), width=0)
    pygame.draw.polygon(screen, BLACK,(points_projecter[31], points_projecter[77], points_projecter[59], points_projecter[13]), width=0)
    pygame.draw.polygon(screen, grisfoncé_1,(points_projecter[59], points_projecter[77], points_projecter[76], points_projecter[75],points_projecter[72],points_projecter[73],points_projecter[74],points_projecter[60]), width=0)

#--------------------------pocket droite bas ----------------
    pygame.draw.polygon(screen, BLACK,(points_projecter[12], points_projecter[58], points_projecter[71], points_projecter[25]), width=0)
    pygame.draw.polygon(screen, BLACK,(points_projecter[25], points_projecter[71], points_projecter[70], points_projecter[24]), width=0)
    pygame.draw.polygon(screen, BLACK,(points_projecter[24], points_projecter[70], points_projecter[69], points_projecter[23]), width=0)
    pygame.draw.polygon(screen, BLACK,(points_projecter[23], points_projecter[69], points_projecter[66], points_projecter[20]), width=0)
    pygame.draw.polygon(screen, BLACK,(points_projecter[20], points_projecter[66], points_projecter[67], points_projecter[21]), width=0)
    pygame.draw.polygon(screen, BLACK,(points_projecter[21], points_projecter[67], points_projecter[68], points_projecter[22]), width=0)
    pygame.draw.polygon(screen, BLACK,(points_projecter[22], points_projecter[68], points_projecter[54], points_projecter[8]), width=0)
    pygame.draw.polygon(screen, grisfoncé_1,(points_projecter[54], points_projecter[68], points_projecter[67], points_projecter[66],points_projecter[69],points_projecter[70],points_projecter[71],points_projecter[58]), width=0)

#-------------------surface de la table ---------------------------

    pygame.draw.polygon(screen, BLACK,(points_projecter[54], points_projecter[57], points_projecter[64], points_projecter[65],points_projecter[63],points_projecter[60],points_projecter[59],points_projecter[58]), width=0)

    pygame.draw.polygon(screen, grisfoncé_1,(points_projecter[54], points_projecter[8], points_projecter[9], points_projecter[55]), width=0)
    pygame.draw.polygon(screen, grisfoncé_1,(points_projecter[56], points_projecter[10], points_projecter[11], points_projecter[57]), width=0)
    pygame.draw.polygon(screen, grisfoncé_1,(points_projecter[18], points_projecter[64], points_projecter[65], points_projecter[19]), width=0)
    pygame.draw.polygon(screen, grisfoncé_1,(points_projecter[17], points_projecter[63], points_projecter[62], points_projecter[16]), width=0)
    pygame.draw.polygon(screen, grisfoncé_1,(points_projecter[15], points_projecter[61], points_projecter[60], points_projecter[14]), width=0)
    pygame.draw.polygon(screen, grisfoncé_1,(points_projecter[13], points_projecter[59], points_projecter[58], points_projecter[12]), width=0)

#-----------------------pied--------------------------------------------
         #--------pied gauche haut-------------------------
    #pygame.draw.polygon(screen, BLACK,(points_projecter[79], points_projecter[96], points_projecter[97], points_projecter[82]), width=0)
    pygame.draw.polygon(screen, BLACK,(points_projecter[79], points_projecter[2], points_projecter[6], points_projecter[96]), width=0)
    pygame.draw.polygon(screen, BLACK,(points_projecter[82], points_projecter[2], points_projecter[6], points_projecter[97]), width=0)
        #-----------pied droite haut------------------------
    pygame.draw.polygon(screen, BLACK,(points_projecter[73], points_projecter[1], points_projecter[5], points_projecter[98]), width=0)
    pygame.draw.polygon(screen, BLACK,(points_projecter[76], points_projecter[1], points_projecter[5], points_projecter[99]), width=0)
        #-------------pied droite bas------------------------
    pygame.draw.polygon(screen, BLACK,(points_projecter[70], points_projecter[0], points_projecter[4], points_projecter[100]), width=0)
    pygame.draw.polygon(screen, BLACK,(points_projecter[67], points_projecter[0], points_projecter[4], points_projecter[101]), width=0)
        #---------pied gauche bas---------------------
    pygame.draw.polygon(screen, BLACK,(points_projecter[84], points_projecter[3], points_projecter[7], points_projecter[102]), width=0)
    pygame.draw.polygon(screen, BLACK,(points_projecter[88], points_projecter[3], points_projecter[7], points_projecter[103]), width=0)

#----------------------------------------------------------------------------------------------------------------------------------------------------
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                exit()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_r]:
            angle_y = angle_x = angle_z = 0
        if keys[pygame.K_q]:
            angle_z -= speed_rotation
        if keys[pygame.K_e]:
            angle_z+= speed_rotation
        if keys[pygame.K_KP_PLUS] or (keys[pygame.K_LSHIFT] or keys[pygame.K_RSHIFT]) and keys[pygame.K_EQUALS]:
            size+=.5
        if keys[pygame.K_KP_MINUS] or (keys[pygame.K_LSHIFT] or keys[pygame.K_RSHIFT]) and keys[pygame.K_6] and size> 0.2:
            size-= .5
    if keys[pygame.K_UP]:
        angle_x-=speed_rotation
    if keys[pygame.K_DOWN]:
        angle_x+= speed_rotation
    if keys[pygame.K_LEFT]:
        angle_y +=speed_rotation
    if keys[pygame.K_RIGHT]:
        angle_y-=speed_rotation

    pygame.display.update()


