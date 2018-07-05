showroom = {'Tesla', 'Ford', 'Hyundai', 'Bus'}
print(showroom)
showroom.add("Tesla")
print(showroom)
showroom.update({"Toyota", "VW"})
showroom.discard("Toyota")
print(showroom)

junkyard = {'Tesla', 'Chevy', 'VW', 'Buick'}

print(showroom.intersection(junkyard))
showroom = showroom.union(junkyard)
print(showroom)
showroom.discard('Chevy')
showroom.discard('VW')
print(showroom)