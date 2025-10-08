class BAC:
    def __init__(self, weight, gender):
        self._weight = weight
        self._gender = gender.lower()
    
    def calculate_bac(self, alc_percent, volume, quantity, hours):
        self._alc_percent = alc_percent
        self._volume = volume
        self._quantity = quantity
        self._hours = hours

        if self._weight <=0 or volume <=0 or quantity <=0 or hours <0 or alc_percent <=0:
            raise ValueError("All inputs must be positive numbers, and hours cannot be negative.")

        if self._gender == "male":
            body_water_constant = 0.68
        elif self._gender == "female":
            body_water_constant = 0.55
        else:
            raise ValueError("Please enter male or female")
        
        total_volume = self._volume * self._quantity
        alcohol_grams = total_volume * (self._alc_percent / 100) * 0.789 * 1000
        
        bac = (alcohol_grams / (self._weight * 1000 * body_water_constant)) * 100 - (0.015 * self._hours)
        return max(bac, 0)  # BAC cannot be negative
    


            