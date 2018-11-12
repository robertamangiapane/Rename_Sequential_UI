import maya.cmds as cmds

mainWindow = None

def CreateWindow(windowName):
    if cmds.window(windowName, exists=True):
        cmds.deleteUI(windowName)

    global mainWindow
    mainWindow = cmds.window(windowName, title=windowName)

    cmds.showWindow(mainWindow)
    return mainWindow


def RenameSequentialUI():
    selection = cmds.ls(selection=True, dag=False, long=False)
    if len(selection) == 0:
        raise Exception("You have to select an object!")

    editedWindow = CreateWindow("Rename")
    cmds.window(editedWindow, edit=True, title="Rename", widthHeight=(300, 100))
    cmds.rowColumnLayout(nc=2, cal=[(1, "center"), (2, "center")], columnWidth=[(1, 150), (2, 150)],
                         cat=[(1, "both", 10), (2, "both", 10)], rs=[(1, 10), (2, 10)],
                         rat=[(1, "both", 10), (2, "both", 5)])
    cmds.text(label="Write new name + #")
    cmds.textField('textField')
    cmds.button(label="Okay", width=270, c=RenameSelection)


def RenameSelection(*args):

    selection = cmds.ls(selection=True, dag=False)
    selection.sort(key=len, reverse=True)

    selectionLength = len(selection)
    i = 0
    newName = GetTextFieldValue()

    while i < selectionLength:
        print selection[i]
        jointName = cmds.joint(selection[i], query=True, name=True)
        cmds.rename(jointName, newName)

        i += 1

    global mainWindow
    cmds.deleteUI(mainWindow)


def GetTextFieldValue():
    newName = cmds.textField('textField', query=True, text=True)
    return newName


RenameSequentialUI()
