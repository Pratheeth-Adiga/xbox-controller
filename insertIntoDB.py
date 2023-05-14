import sqlite3

con = sqlite3.connect("control.db")
cur = con.cursor()

# cur.execute("CREATE TABLE profiles (id PRIMARY KEY, PROFILE_NAME, A, B, X, Y, START, BACK, LJ, RJ, LB, RB, LJ_XN, LJ_XP, LJ_YN, LJ_YP, RJ_XN, RJ_XP, RJ_YN, RJ_YP, LT, RT, TOP, BOTTOM, LEFT, RIGHT, TOP_LEFT, TOP_RIGHT, BOTTOM_LEFT, BOTTOM_RIGHT)")

id = 0
PROFILE_NAME = "General"
A = "enter"
B = "keyboardInterrupt_macro"
X = "click_macro"
Y = "screenshot_macro"
START = "win"
BACK = "esc"
LJ = "volumemute"
RJ = "doubleClick_macro"
LB = "profileSwitch_macro"
RB = "tab"
LJ_XN = "left"
LJ_XP = "right"
LJ_YN = "up"
LJ_YP = "down"
RJ_XN = "mouseMove_macro"
RJ_XP = "mouseMove_macro"
RJ_YN = "mouseMove_macro"
RJ_YP = "mouseMove_macro"
LT = "alt"
RT = "shift"
TOP = "brightnessIncrease_macro"
BOTTOM = "brightnessDecrease_macro"
LEFT = "volumedown"
RIGHT = "volumeup"
TOP_LEFT = "["
TOP_RIGHT = "]"
BOTTOM_LEFT = "b"
BOTTOM_RIGHT = "f"
data = (id,PROFILE_NAME,A,B,X,Y,START,BACK,LJ,RJ,LB,RB,LJ_XN,LJ_XP,LJ_YN,LJ_YP,RJ_XN,RJ_XP,RJ_YN,RJ_YP,LT,RT,TOP,BOTTOM,LEFT,RIGHT,TOP_LEFT,TOP_RIGHT,BOTTOM_LEFT,BOTTOM_RIGHT)
cur.execute("INSERT INTO profiles VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)", data)
con.commit()
# cur.execute(f"INSERT INTO PROFILE(id, PROFILE_NAME, A, B, X, Y, START, BACK, LJ, RJ, LB, RB, LJ_XN, LJ_XP, LJ_YN, LJ_YP, RJ_XN, RJ_XP, RJ_YN, RJ_YP, LT, RT, TOP, BOTTOM, LEFT, RIGHT, TOP_LEFT, TOP_RIGHT, BOTTOM_LEFT, BOTTOM_RIGHT) VALUES ('{id}','{PROFILE_NAME}','{A}','{B}','{X}','{Y}','{START}','{BACK}','{LJ}','{RJ}','{LB}','{RB}','{LJ_XN}','{LJ_XP}','{LJ_YN}','{LJ_YP}','{RJ_XN}','{RJ_XP}','{RJ_YN}','{RJ_YP}','{LT}','{RT}','{TOP}','{BOTTOM}','{LEFT}','{RIGHT}','{TOP_LEFT}','{TOP_RIGHT}','{BOTTOM_LEFT}','{BOTTOM_RIGHT}')")
# cur.execute("INSERT INTO PROFILE(id, PROFILE_NAME, A, B, X, Y, START, BACK, LJ, RJ, LB, RB, LJ_XN, LJ_XP, LJ_YN, LJ_YP, RJ_XN, RJ_XP, RJ_YN, RJ_YP, LT, RT, TOP, BOTTOM, LEFT, RIGHT, TOP_LEFT, TOP_RIGHT, BOTTOM_LEFT, BOTTOM_RIGHT) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)", data)
# cur.execute("INSERT INTO PROFILE VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)", data)
# cur.execute(f"INSERT INTO PROFILE({id},{PROFILE_NAME},{A},{B},{X},{Y},{START},{BACK},{LJ},{RJ},{LB},{RB},{LJ_XN},{LJ_XP},{LJ_YN},{LJ_YP},{RJ_XN},{RJ_XP},{RJ_YN},{RJ_YP},{LT},{RT},{TOP},{BOTTOM},{LEFT},{RIGHT},{TOP_LEFT},{TOP_RIGHT},{BOTTOM_LEFT},{BOTTOM_RIGHT})")
