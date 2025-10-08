class BAC:
    def __init__(self, weight, gender):
        self._weight = weight
        self._gender = gender.lower()
    
    def calculate_bac(self, alc_percent, volume, quantity, hours):
        self._alc_percent = alc_percent
        self._volume = volume
        self._quantity = quantity
        self._hours = hours

        total_volume = self._volume * self._quantity
        alcohol_grams = total_volume * (self._alc_percent / 100) * 0.789 * 1000

        if self._gender == "male":
            body_water_constant = 0.68

            