import squish
from  Wrapper.Tree import Tree


def select(path):
    ''' select path from Exporte Tree '''
    Tree.click(path,squish.waitForObject(":Export_Tree"))
    squish.clickButton(squish.waitForObject(":Export.Next >_Button"))
   