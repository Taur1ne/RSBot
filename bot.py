import pyautogui
import random

pyautogui.PAUSE = 0.5
pyautogui.FAILSAFE = True


def main():
	pics = 'screenshots/'
	iron_ore_bank = 'iron_ore_bank.png'
	coal_ore_bank = 'coal_ore_bank.png'
	coal_ore_inv = 'coal_ore_inv.png'
	steel_bar_smelt = None
	
	open_bank()
	
	bank_setup(pics+'grey_x.png')
	empty_inventory(pics + 'empty_inventory.png')
	#print(pyautogui.center(pyautogui.locateOnScreen(pics+coal_ore_inv)))
	get_ore_from_bank(pics + coal_ore_bank)
	get_ore_from_bank(pics + iron_ore_bank)
	
	close_bank()
	find_furnance()
	move_to_furnance()
	smelt(steel_bar_smelt)
	move_to_bank()

def prep_for_steel_smelt(coal, iron):
	get_ore_from_bank(coal)
	get_ore_from_bank(iron)
	
def open_bank():
	print()
	
	
def close_bank():
	print()
	
	
def find_furnance():
	print()
	

def move_to_furnance():
	print()
	
	
def smelt(bar):
	print()
	
	
def move_to_bank():
	print()
	
	
def empty_inventory(empty, first_inv_empty):
# first inv pic
	if get_center(first_inv_empty) is None:
		first_inv_spot = (2351 + get_offset(), 1041 + get_offset())
		pyautogui.click(first_inv_spot)
	
def open_inventory_tab(unopened):
	try:
		x,y = get_center(unopened)
		pyautogui.click(x,y)
	except TypeError:
		print('Inventory is already opened')

	
def bank_setup(grey_x):
	try:
		coords = get_center(grey_x)
		if coords is not None:
			pyautogui.click(coords)
	except TypeError:
		print('Quantity must have been set already')

		
def get_center(pic):
	return pyautogui.center(pyautogui.locateOnScreen(pic))
		
		
def get_offset():
	return random.randint(-3,3)
		
		
def get_ore_from_bank(ore):
	try :
		x, y = get_center(ore)
		pyautogui.click(x+random.randint(-3,3), y+random.randint(-3,3))
		#print(list(pyautogui.locateAllOnScreen('coal.png')))
	except TypeError:
		print(ore + ' was not found in the bank')
		exit(1)
	
	
if __name__ == '__main__':
	main()
	



