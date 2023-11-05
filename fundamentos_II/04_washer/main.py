from washer import WashingMachine

washing_machine = WashingMachine()
washing_machine.load_clothes(["Shirt", "Pants", "Socks"])
washing_machine.start_wash(3, 1)
unloaded_clothes = washing_machine.unload_clothes()
print("Unloaded clothes:", unloaded_clothes)
washing_machine.stop_wash()

## Jimmy Martínez - Carné No. 202302745
## Repo - https://github.com/MegaGone/udv/blob/develop/fundamentos_II/04_washer/