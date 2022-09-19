from cmath import tau
from secrets import token_bytes


tau = 0
wisky = 0

medisin = 0

gullklokke = 0

navn = input ("hva heter du ?")


print("Du heter " + navn)


print("år 1789")



print("du vokner i stua og det gjør ont i hode ditt. jeg husker ikke noe fra i går. tenkte " + navn)

print("plutselig banka det på døra. du hører at de sier noe men det er bare momling. kansjde jeg burde reise meg og se hvem det er. tenkte " + navn)

valg = input("skal du reise deg opp og se hvem det er eller go fortsete og lige på gulvet A: eller B: ->")

if valg =="B":
    print("du valkte og ligge der. og der lå du i hele dagen THE END ")

if valg =="A":
    print("du reiser deg opp og opna døra og det er en selger som selger mye rart. snaker om rart mannen var snodig han hadde en rar rød hatt og blå jakke med mørke røde bokser. hello! sier han. (kan jeg intresere deg i noen produkter?)")

valg = input("nei: eller ja: ->")

if valg =="nei":
    print("han så litt skufa ut men så litt iritasion og han stampa bort in i skogen.")


if valg =="ja":
    print("han opna jaken sin og viste mase forselge opjekter 1 tau 4 flasker med medisin 1 flaske wisky og en gullklokke. de alle så bra ut men jeg har bare rå til en av dem")
     
    valg = input("tau: medisin: wisky: gullklokke:")
    if valg =="tau":
        print("du hvelgte tauet")   
        tau += 1
        print("tau: ", tau)




if valg =="wisky":
    print("du hvelgte flaske med wisky")   
    wisky += 1
    print("wisky: ", wisky)



if valg =="medisin":
    print("du hvelgte medisinen")   
    medisin += 4
    print("medisin: ", medisin)




if valg =="gullklokke":
    print("du hvelgte gullklokka")   
    gullklokke += 1
    print("gullklokke: ", gullklokke)



print("han takker deg for handelen og går sin vei. mens du ser han gå ned over stien ser en mann løpe i full fart mot deg han roper etter deg.")


print("han roper navne ditt (HEI HELLO VENT " + navn)

valg = input("skal jeg lokke døra eller slipe han in->")



if valg =="lokke døra":
    print("du lokker døra men han stopper døra med foten sin i siste liten. du iriterte han litt.")   
    


if valg =="slip han in":
    print("du sliper han in")



print("han var anpusten og sliten fra all den løpingen (jeg har et helt super ting og vise deg min gode venn!) sa han")

print("han tokk opp et styke papir. dette er et skate kart og skaten er ikke så langt her fra!")

valg = input("A: hvem er du?: B: navnet ditt?:")

if valg =="A":
    print("han så forviret ut husker du meg ikke jeg hvar her i forie uke.")

if valg =="B":
    print("han så på meg rart husker du ikke navnet mitt?")

print("ikke nå vi har dårlig tid noen andre kan også lette etter skaten.")


valg = input("hvordan kan andre lette etter skaten hvis du har skartekarte? B: ok la oss dra! A:->")


if valg =="B":
    print("de kan kome hit og ta karte!") 
    
    print("jeg har ikke tid og forklare kom jeg hventer uten får du gjør deg klar.")

if valg =="A":
    print("ok jeg hventer uten for kom når du er klar.")


print("han går ut av huset og står uten får.")

print("jeg burde se i skape i såve romet.")


valg = input("free roming. sove rom.A: stua.B: sjøken.C: ut:")

if valg =="B":
    print("jeg går in i stua det er et rot der og det lokter som død hun jeg vil ikke hvere her ine jeg forter meg fort ut. og ente opp i skjøenet.")
    print("skjøkene er som alle andre skjøken")
    valg = input("lurerpå om det er noe i skofa A:.")
    
    if valg =="A":
        print("det er litt medisin")
        valg = input("ta den.t")
        if valg =="t":
            print("du tar medisinen.")
            valg = input("dra eller fortsete og se runt. sove rom.B:")
            if valg =="B":
                print("jeg går in i soveromet. det er ikke stort eller for lite det er akurat passe. og et lite vindu til høyere med senga. til venstere i gjørne i romet liger det et skap.")
                valg = input("åpne?.R")

            if valg == "R":
                 print("det er masse ting å ta med 1 tau: jeg er ikke den rikeste så det er alt.")
            valg = input("et tau?.U")

            if valg == "U":
               print("du tar tauet") 
            tau += 1
            print("tau: ", tau)
            print("tror det er på tide og gå ut")
            valg = input("ut.P")
            if valg =="P":
              print("du går ut der han venter på deg")
              
if valg =="A":
    print("jeg går in i soveromet. det er ikke stort eller for lite det er akurat passe. og et lite vindu til høyere med senga. til venstere i gjørne i romet liger det et skap.")
    valg = input("åpne?.Å->")

    if valg == "Å":
     print("det er masse ting å ta med 1 tau: jeg er ikke den rikeste så det er alt.")

    valg = input("et tau?.F")

    if valg == "F":
        print("du tar tauet") 
        tau += 1
        print("tau: ", tau)
        print("hvil du til stua.B: eller skjøkenet.C:")
        valg = input("velg")
        if valg =="C":
            print("skjøkene er som alle andre skjøken")
    valg = input("lurerpå om det er noe i skofa S:.")
    
    if valg =="S":
        print("det er litt medisin")
        valg = input("ta den.N")
        if valg =="N":
            print("du tar medisinen.")
            print("tror det er på tide og gå ut")
            valg = input("ut.M")
            if valg =="M":
              print("du går ut der han venter på deg")

if valg =="B":
    print("jeg går in i stua det er et rot der og det lokter som død hun jeg vil ikke hvere her ine jeg forter meg fort ut. og ente opp i skjøenet.")
    print("skjøkene er som alle andre skjøken")
    valg = input("lurerpå om det er noe i skofa H:.")
    
    if valg =="H":
        print("det er litt medisin")
        valg = input("ta den.Q")
        if valg =="Q":
            print("du tar medisinen.")
            print("tror det er på tide og gå ut")
            valg = input("ut.W")
            if valg =="W":
              print("du går ut der han venter på deg")


print("hei hvorfor tokk det så lang tid?")



print("hvem bryr seg kom")





