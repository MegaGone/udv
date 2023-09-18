def user_interaction(device):
    device.power_on()
    device.make_call("+502 11223344")
    device.send_message("UDV", "Aprendiendo POO")
    device.power_off()
    print()