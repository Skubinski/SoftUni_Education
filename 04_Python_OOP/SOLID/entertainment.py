class HDMICable:
    def connect_via_hdmi_cable(self, device): pass

class RCACable:
    def connect_via_rca_cable(self, device): pass

class ETHCable:
    def connect_via_eth_cable(self, device): pass

class PowerOutlet:
    def connect_to_power_outlet(self, device): pass

class Television(RCACable, HDMICable, PowerOutlet):
    def connect_to_dvd(self, dvd_player):
        self.connect_via_rca_cable(dvd_player)

    def connect_to_game_console(self, console):
        self.connect_via_rca_cable(console)

    def connect_power(self, power):
        self.connect_via_rca_cable(power)