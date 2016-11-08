class Bil:
    def __init__(self,registreringsnr,merke):
        self.registreringsnr = registreringsnr
        self.merke = merke
    def __call__(self):
        return "Registreringsnr: "+str(self.registreringsnr)+" Merke: "+str(self.merke)
