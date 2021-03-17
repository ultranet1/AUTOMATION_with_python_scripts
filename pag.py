import pyautogui as pag


pag.FAILSAFE = True

#To check PC screen size open CMD in windows & type python then import pyautogui then pag.size()

pag.size()

# Size is (width=1366, height=768)
pag.moveTo(90, 754)




pag.click(90, 754)
pag.PAUSE = 2
pag.typewrite('Excel')
pag.press('enter')
pag.PAUSE = 3
#pag.click(1147, 750)
pag.PAUSE = 9
#pag.click(884, 566)
pag.press('enter')
pag.PAUSE = 9
pag.press('enter')
#pag.click(641, 414)


pag.PAUSE= 5

def type (state, capital):
	pag.typewrite(state)
	pag.press('tab')
	pag.typewrite(capital)
	pag.press('enter')
	pag.press('back')

pag.PAUSE= 7
pag.press('caps lock')
type('STATE', 'CAPITAL')
type('ABIA', 'UMUAHIA')
type('ADAMAWA', 'YOLA')
type ('AKWA IBOM', 'UYO')
type('BAUCHI', 'BAUCHI')
type('BENUE', 'MAKURDI')
type('BORNO', 'MADUGURI')
type('CROSS RIVER', 'CALABAR')
type('DELTA', 'ASABA')
type('EDO', 'BENIN')
type('ENUGU', 'ENUGU')
type('GOMBE', 'GOMBE')

pag.hotkey('ctrl', 's')
pag.press('enter')
pag.PAUSE = 2
pag.press('enter')
pag.PAUSE = 2
pag.press('enter')
pag.typewrite('STATE_BOT')
pag.press('enter')
pag.PAUSE = 2
pag.press('tab')
pag.PAUSE = 2
pag.press('enter')

