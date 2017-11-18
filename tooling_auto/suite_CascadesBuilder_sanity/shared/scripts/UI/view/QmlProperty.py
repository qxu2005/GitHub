import squish


def getText():
    ''' get Text info '''
    
    squish.snooze(2)
    obj = squish.waitForObject(':QML Properties_Text')
    return obj.getText()
    

def setText(txtinfo):
    ''' set Text info '''
    
    obj = squish.waitForObject(':QML Properties_Text')
    obj.setText(txtinfo)
    squish.snooze(2)
    

def getId():
    ''' get ID info '''
    
    squish.snooze(2)
    obj = squish.waitForObject(':QML Properties.ID_Text')
    return obj.getText()
    
    

def setId(idinfo):
    ''' set ID info '''
    
    obj = squish.waitForObject(':QML Properties.ID_Text')
    obj.setText(idinfo)
    squish.snooze(2)
       