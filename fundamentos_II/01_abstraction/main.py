from smart_fridge import SmartFridge

udv_fridge = SmartFridge("Samsung", "Cooling plus", 10)

udv_fridge.connect_to_network("udv_wifi", "Password!234")
udv_fridge.dispense_water(8)
udv_fridge.disconnect_from_network()

## Jimmy Martínez - Carné No. 202302745
## Repo - https://github.com/MegaGone/udv/blob/develop/fundamentos_II/01_abstraction/