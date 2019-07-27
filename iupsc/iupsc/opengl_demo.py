import  sys
from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
from math import sin,cos
window=0
ESC = 27
x, y,z = 0.0, -15.0,1.5
deltaMove,rotatel,rotater= 0.0,0.0,0.0
lx,ly = 0.0,  1.0
angle = 0.0
deltaAngle = 0.0
isDragging = 0
xDragStart = 0
dic=0
cl = []
br = []
mith =[]
D_bond =[]
T_bond=[]
color={'cloro':[0,255,0],'bromo':[165,42,42],'carbon':[41,53,66]}

def changeSize(w, h=1):
	 if h == 0:
		 h=1
	 ratio = (float(w) / float(h)) 
	 glMatrixMode(GL_PROJECTION); 
	 glLoadIdentity()
	 gluPerspective(45.0, ratio, 0.1, 100.0); 
	 glMatrixMode(GL_MODELVIEW)
	 glViewport(0, 0, w, h)

def update():
    global deltaMove,x,y,ly,lx,rotatel,rotater,deltaAngle,angle
    if(rotatel):
        deltaAngle = (10) * 0.005
        lx = -sin(angle + deltaAngle)
        ly = cos(angle + deltaAngle)
        angle += deltaAngle

    if(rotater):
        deltaAngle = (-10) * 0.005
        lx = -sin(angle + deltaAngle)
        ly = cos(angle + deltaAngle)
        angle += deltaAngle

    if (deltaMove or rotatel or rotater):
        x+=deltaMove*lx*(0.1)
        y+=deltaMove*ly*(0.1)
    glutPostRedisplay()

def xyz( x1,  y1, font, string):
	glRasterPos2f(x1, y1)
	for x in string:
		glutBitmapCharacter(font, ord(x))

def renderScene():
	global cl ,br ,mith ,D_bond ,T_bond,x,y,z,ly,lx,color,dic

	glClearColor(0.0, 0.7, 1.0, 1.0); 
	glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

	glLoadIdentity()


	gluLookAt(
		x, y, z,
		x + lx, y + ly, 1.5,
		0.0, 0.0, 1.0)



	glColor3f(0.0, 0.7, 0.0)
	glBegin(GL_QUADS)
	glVertex3f(-100.0, -100.0, -10.0)
	glVertex3f(-100.0, 100.0, -10.0)
	glVertex3f(100.0, 100.0, -10.0)
	glVertex3f(100.0, -100.0, -10.0)
	glEnd()

	
	glColor3f(0, 0, 0)
	glPushMatrix()
	glRotatef(90, 0, 1, 0)
	glTranslatef(-2, -12, -15)
	glRotatef(30, 1, 0, 0)
	xyz(0, 0, GLUT_BITMAP_TIMES_ROMAN_24, dic['Name'])
	glPopMatrix()

	glColor3f(1, 1, 1)
	glPushMatrix()
	glTranslatef(0, 0, 5.5)
	xyz(0, 0, GLUT_BITMAP_TIMES_ROMAN_24, "IUPSC NAMING")
	glPopMatrix()

	c_li = ((-10, 0), ( -7.5, 0 ), ( -5,0 ), (-2.5, 0 ), (0, 0 ), (2.5,0), (5, 0 ), (7.5, 0 ), ( 10, 0 ), )
	bond = ( -8.5,-6.5,-3.5,-1.25,1,3.5,6.5,8.5,8.5 )
	#{ {-10, 0}, { -7.5, 0 }, { -5,0 }, { -2.5, 0 }, { 0, 0 }, { 2.5,0 }, { 5, 0 }, { 7.5, 0 }, { 10, 0 }, };;;; { {0, 0}, {-2.5, 0}, {2.5,0} ,{-5,0}, {5, 0}, {-7.5, 0}, {7.5, 0}, {-10, 0}, {10, 0}, {-12.5, 0} }
	#{ -8.5,-6.5,-3.33,-1.25,1,3.33,6.5,8.5,8.5 } {0,-1.25,1.25,-3.33,3.33,-6.5,6.5,-8.5,8.5,-12.5}
	
	i = 1
	cl_i,br_i,d_b,t_b,mith_i=0,0,0,0,0
	

	while (i <= int(dic['C_N'][0][1])):
		glColor3ubv(color['carbon'])
		glPushMatrix()
		glTranslatef(c_li[i - 1][0], 0, 1.5)
		glScalef(0.40, 0.4, .4)
		glutSolidSphere(1, 500, 500)
		glPopMatrix()
		
		if (i > 1):
			if (i-1 not in D_bond and i-1 not in T_bond):
				glColor3ub(206, 205, 203)
				glPushMatrix()
				glTranslatef((bond[i-2]), 0, 1.5)
				glScalef(2.5, .1, .1)
				glutSolidCube(1)
				glPopMatrix()
			
			if (i == D_bond[d_b]+1):
				d_b+=1
				if d_b ==len(D_bond):
					d_b=0
				glColor3ub(206, 205, 203)
				glPushMatrix()
				glTranslatef((bond[i-2]), 0, 1.6)
				glScalef(2.5, .1, .1)
				glutSolidCube(1)
				glPopMatrix()
				glPushMatrix()
				glTranslatef((bond[i-2]), 0, 1.4)
				glScalef(2.5, .1, .1)
				glutSolidCube(1)
				glPopMatrix()
			
			if ( i == T_bond[t_b]+1):
				t_b+=1
				if t_b ==len(T_bond):
					t_b=0
				glColor3ub(206, 205, 203)
				glPushMatrix()
				glTranslatef((bond[i - 2]), 0, 1.7)
				glScalef(2.5, .1, .1)
				glutSolidCube(1)
				glPopMatrix()
				glPushMatrix()
				glTranslatef((bond[i - 2]), 0, 1.5)
				glScalef(2.5, .1, .1)
				glutSolidCube(1)
				glPopMatrix()
				glPushMatrix()
				glTranslatef((bond[i - 2]), 0, 1.3)
				glScalef(2.5, .1, .1)
				glutSolidCube(1)
				glPopMatrix()
			
				
		
		
		if (cl[cl_i] == i):
			glColor3ubv(color['cloro'])
			glPushMatrix()
			glTranslatef(c_li[i - 1][0], 0, 3.0)
			glScalef(0.40, 0.4, .4)
			glutSolidSphere(1, 500, 500)
			glPopMatrix()

			glColor3ubv(color['cloro'])
			glPushMatrix()
			glTranslatef(c_li[i - 1][0], 0, 2.5)
			glRotatef(90,0,1,0)
			glScalef(1.5, .1, .1)
			glutSolidCube(1)
			glPopMatrix()

			cl_i+=1
			if cl_i == len(cl):
				cl_i=0
		if (br[br_i] == i):
			glColor3ubv(color['bromo'])
			glPushMatrix()
			glTranslatef(c_li[i - 1][0], 0, 3.0)
			glScalef(0.40, 0.4, .4)
			glutSolidSphere(1, 500, 500)
			glPopMatrix()
			
			glColor3ubv(color['bromo'])
			glPushMatrix()
			glTranslatef(c_li[i - 1][0], 0, 2.5)
			glRotatef(90,0,1,0)
			glScalef(1.5, .1, .1)
			glutSolidCube(1)
			glPopMatrix()

			br_i+=1
			if br_i == len(br):
				br_i=0
		if (mith[mith_i] == i):
			glColor3ubv(color['carbon'])
			glPushMatrix()
			glTranslatef(c_li[i - 1][0], 0, 3.0)
			glScalef(0.40, 0.4, .4)
			glutSolidSphere(1, 500, 500)
			glPopMatrix()

			glColor3ub(206, 205, 203)
			glPushMatrix()
			glTranslatef(c_li[i - 1][0], 0, 2.5)
			glRotatef(90,0,1,0)
			glScalef(1.5, .1, .1)
			glutSolidCube(1)
			glPopMatrix()

			mith_i+=1
			if mith_i == len(mith):
				mith_i=0
		
		i += 1
	
	

	glutSwapBuffers(); 

def processNormalKeys(k, xx,yy):
	global window
	print("In keyboard function ")
	key = k.decode("utf-8")
	if (key == chr(27) or key == 'q' or key == 'Q'):
		print("In return statment")
		glutDestroyWindow(window)
		
	


def pressSpecialKey(key, xx, yy):
    global x,y,deltaMove,rotatel,rotater
    if key == GLUT_KEY_UP:
        deltaMove=4.0
    if key == GLUT_KEY_DOWN:
        deltaMove=-4
    if key==GLUT_KEY_LEFT:
        rotatel=1
        #x-=2
        #y+=1
        #deltamove-=1;
    if key==GLUT_KEY_RIGHT:
        rotater=1
        #x+=2
        #y-=1
        #deltamove+=1;

def releaseSpecialKey(key, x, y):
    global deltaMove,rotatel,rotater
    if key == GLUT_KEY_UP:
       deltaMove,rotatel,rotater= 0.0,0.0,0.0
    if key == GLUT_KEY_DOWN:
        deltaMove,rotatel,rotater= 0.0,0.0,0.0
    if key==GLUT_KEY_LEFT:
        deltaMove,rotatel,rotater= 0.0,0.0,0.0
    if key==GLUT_KEY_RIGHT:
        deltaMove,rotatel,rotater= 0.0,0.0,0.0

def initialize():
	global cl,br,mith,D_bond,T_bond
	for val in range(len(dic['substute'])):
		if dic['substute'][val][0] == 'cloro' :
			cl.append(int(dic['substute'][val][1]))
		if dic['substute'][val][0] == 'bromo' :
			br.append(int(dic['substute'][val][1]))
		if dic['substute'][val][0] == 'methyl' :
			mith.append(int(dic['substute'][val][1]))
	if len(cl)==0:
		cl.append(0)
	if len(br)==0:
		br.append(0)
	if len(mith)==0:
		mith.append(0)
	for val in range(len(dic['bond'])):
		if dic['bond'][val][0] == 'ene' :
			D_bond.append(int(dic['bond'][val][1]))
		if dic['bond'][val][0] == 'yne' :
			T_bond.append(int(dic['bond'][val][1]))
	if len(D_bond)==0:
		D_bond.append(0)
	if len(T_bond)==0:
		T_bond.append(0)
           
def main(s):
	global dic,cl,br,mith,D_bond,T_bond,window
	dic=s
	initialize()
	print("chlorine-Location: ",cl,"\nBromin-Location: ",br,"\nMithyle-Location: ",mith,"\nDouble Bond-Location: ",D_bond,"\nTriple Bond-Location: ",T_bond)
	glutInit(sys.argv)
	glutInitDisplayMode(GLUT_DEPTH | GLUT_DOUBLE | GLUT_RGBA)
	glutInitWindowPosition(1, 1)
	glutInitWindowSize(1366, 768)
	window = glutCreateWindow(b"OpenGL/GLUT Sampe Program")
	glutSetWindow(window)
	glutFullScreen()
	glutReshapeFunc(changeSize)
	glutDisplayFunc(renderScene) 
	glutIdleFunc(update)
	glutIgnoreKeyRepeat(1)
	glutKeyboardFunc(processNormalKeys)
	glutSpecialFunc(pressSpecialKey) 
	glutSpecialUpFunc(releaseSpecialKey)
	glEnable(GL_DEPTH_TEST)	
	glutMainLoop()
	return         

if __name__ =="__main__": main(" ")

