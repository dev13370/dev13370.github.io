import ISS_Info



logo = f"""
<>---<>---<>---<>---<>---<>---<>---<>---<>
           [+]Space tool[+]  
<>---<>---<>---<>---<>---<>---<>---<>---<>   
     Developer >> Naplon ◕_◕ 
	 _   _             _             
| \ | |           | |            
|  \| | __ _ _ __ | | ___  _ __  
| . ` |/ _` | '_ \| |/ _ \| '_ \ 
| |\  | (_| | |_) | | (_) | | | |
|_| \_|\__,_| .__/|_|\___/|_| |_|
            | | instagram: 3h6h                 
            |_| Telegram: naplon0       
            
Performance characteristics - It tells you how many astronauts are currently🧑‍🚀, the name of each person - the current location of the International Space Station📍- and the transit times of the space station🕔
----------------------------------
"""
print(logo)

user = input("1)Enter 1 to run\n")
print('[*]🛰🪐🛸🧑‍🚀📍[*]')
print('__________________________________')

if user == '1':
	nap = ISS_Info.iss_people_in_space()
	print("Currently there {} astronauts in space:"
	.format(nap['number']))
for n in nap['people']:
	print("Name: {} ('Craft: {}'))"
	.format(n['name'],n['craft']))
	
loc = ISS_Info.iss_current_loc()
print("📍The current location of the International Space Station: ",loc)
  
time = ISS_Info.iss_passes(43.5,-74,200,3)
print("🕔Space station passage time: ", time)
	

	