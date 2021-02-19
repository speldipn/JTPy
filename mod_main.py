#import mod
#print(mod.add(10, 20))
#print(mod.sub(30,5))

# equal
#from mod import *
# <or>
#from mod import add
#from mod import sub 
from mod import add,sub

print(add(10, 20))
print(sub(30,5))

print(__name__)

from mod2 import Math

math = Math()
print(math.solv(10))

#import game.sound.echo
#game.sound.echo.echo_test()

#from game.sound.echo import echo_test
#echo_test()

from game.sound import *
echo.echo_test()

from game.graphic import *
render.render_test()
