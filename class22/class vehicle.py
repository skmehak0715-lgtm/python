class vehicle:

    def __init__(self, max_speed, mileage):

        self.max_speed = max_speed
        self.mileage = mileage

mode1x = vehicle(240, 18)

print("model max speed:",mode1x.max_speed)
print("model mileage:", mode1x.mileage)