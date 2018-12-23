#!/usr/bin/env python
# -*- coding: utf-8 -*-

print "Dnevni meni gostišča 'Pri debelem zajcu'"

meni_seznam = {}

while True:
    jed = raw_input("Vnesi jed: ")
    cena = raw_input("Vnesi ceno v €: ")
    print "Vpisal si jed " + jed + " ki stane " + cena + "€."

    meni_seznam[jed] = cena

    new = raw_input("Ali zelis nadaljevati (da/ne)? ")
    if new == "ne":
        break


for jed, cena in meni_seznam.iteritems():
   print "jed " + cena + "€"


meni_file = open("meni.txt", "w+")
meni_file.write("Jedilni list")

for jed, cena in meni_seznam.iteritems():
    meni_file.write("\n" + "- " + jed + " " + cena + "€")
meni_file.close