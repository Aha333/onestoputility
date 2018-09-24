# what I didnt know before is that you can actually inherit anything!
# this also means the internal object like list, dict
# source http://oez.es/Expert%20Python%20Programming.pdf
# page 65
import pandas as pd
class NewDF (pd.DataFrame):
    pass

newdf=NewDF()
newdf['a'] = 1

#print dir(newdf)

class newlist(list):

    pass

# todo : I want to lookat another video about this

