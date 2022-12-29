t = ()
print(type(t)) # tuple

coordsGps = (45.9632, 21.7891)
print(coordsGps)
print("Latitude", coordsGps[0])
print("Longitude", coordsGps[1])

# Interdit sur Tuple (lecture seule)
#coordsGps[0] = 46.3322

# l = [12,13]
# print(l)
# l.append(14)
# print(l)

# pas possible, "AttributError", append n'existe pas pour les tuples
#coordsGps.append(89.2658)

lat, lng = coordsGps # tuple unpacked
print(lat, lng)