import pathlib

path = pathlib.Path('.') / "5.example.txt"
with open(path, "r") as f:
    input_list = f.read().strip().split("\n\n")

seeds = input_list[0].split("\n")
seeds_to_soil = input_list[1].split("\n")
soil_to_fertilizer = input_list[2].split("\n")
fertilizer_to_water = input_list[3].split("\n")
water_to_light = input_list[4].split("\n")
light_to_temperature = input_list[5].split("\n")
temperature_to_humidity = input_list[6].split("\n")
humidity_to_location = input_list[7].split("\n")


class Mapper:
    def __init__(self, s):
        self.ranges = []
        for line in s[1:]:
            dest, src, rangee = line.split()
            self.ranges.append((int(dest), int(src), int(rangee)))

    def return_match(self, number): 
        for dest, src, rangee in self.ranges:
            if src <= number <= src + rangee:
                to_return = (number - src)+dest
                return to_return
        return number

seeds_to_soil = Mapper(seeds_to_soil)
soil_to_fertilizer = Mapper(soil_to_fertilizer)
fertilizer_to_water = Mapper(fertilizer_to_water)
water_to_light = Mapper(water_to_light)
light_to_temperature = Mapper(light_to_temperature)
temperature_to_humidity = Mapper(temperature_to_humidity)
humidity_to_location = Mapper(humidity_to_location)

_, seeds = seeds[0].split(": ")
seeds = [int(x) for x in seeds.split()]

locations = []

for seed in seeds:
    soil = seeds_to_soil.return_match(seed)
    fertilizer = soil_to_fertilizer.return_match(soil)
    water = fertilizer_to_water.return_match(fertilizer)
    light = water_to_light.return_match(water)
    temperature = light_to_temperature.return_match(light)
    humidity = temperature_to_humidity.return_match(temperature)
    location = humidity_to_location.return_match(humidity)
    locations.append(location)
    


