from data import globz, hasznos, objektumok, resource


def szintlepes(kar, volt, lett):
    # Fejlesztés alatt...
    print("Szint változás! Volt:", volt, "Lett:", lett)


def kornyezet_inicializalasa(kar):
    for tipus in hasznos.get_sorted_list(resource.fegyverek):
        for fegyver in resource.fegyverek[tipus]:
            globz.fegyverek[fegyver] = objektumok.Fegyver(kar, tipus, fegyver)


def full(kar):
    kap(kar)
    foTul(kar)
    kar.magia.update()
    fpep(kar)
    kp(kar)
    hm(kar)
    pszi(kar)
    magia(kar)


def szemelyes_forrasok(kar):
    for dep, adat_nev, res in \
            zip(("Iskola", "Kaszt altípus", "Isten", "Ország"),
                ("Kaszt", "Kaszt", "Vallás", "Szülőföld"),
                (resource.iskolak, resource.kaszt_altipusok, resource.istenek, resource.orszagok)):
        resource.szemelyes_adat_sz[dep] = res[kar.szemelyes_adatok[adat_nev].get()]


def kp(kar):
    if kar.szint.get == 1:
        kar.kp_alap.set(kar.fo_tulajdonsagok["INT"].get())  # Ez nem jár szintenként

    kar.kp.set((kar.kp_alap.get() + kar.kp_KAP.get()) - kar.kp_elkoltott.get())
    kap(kar)


def kap(kar):
    kar.szint.set(hasznos.calc_szint(kar.TP.get()))
    x = 0
    for c in kar.hatterek.values():
        if c.get() in ('', ' '): continue
        x += int(c.get())
    kar.KAP_szintenkent = 50 - x
    # Minden háttér értéke levonódik a szintenként elosztható KAP-ok számából

    # Ez a blokk konzisztens abból a szempontból, hogy mindig az vásárolt pontok
    # mennyiségével számol, nem pedig a rá költött KAP-ok számával.
    kap = kar.KAP_szintenkent * kar.szint.get()
    kap -= (kar.foTul_KAP.get() * 20)
    kap -= kar.kp_KAP.get()  # Itt egy az egyhez a váltószám
    kap -= (kar.fp_KAP.get() * 2)
    for c in kar.harcertekek_KAP.values():
        kap -= (c.get() * 2)
    kap -= (kar.pszi_KAP.get() * 2)
    kap -= (kar.mana_KAP.get() * 3)
    # KEGYPONTOK???

    kar.KAP.set(int(kap))


def KAP(kar):
    kap(kar)


def foTul(kar, melyik=None):
    # EZ A FÜGGVÉNY NEM SZÁMOL A KÉPZETTSÉGEK 4. FOKÁNAK ELÉRÉSE UTÁNI BÓNUSZOKKAL
    # A frame osztályának spinbox_update metódusa számol a faji bónuszokkal.
    # beépítendő: 20 KAP-ért lehet vásárolni +1 fő tulajdonságot!

    # Faji bónuszok update-je
    if kar.szemelyes_adatok["Faj"].get() not in [" ", ""]:
        kar.faji_bonuszok = resource.faji_bonuszok[kar.szemelyes_adatok['Faj'].get()]

        for kulcs, bonusz in kar.faji_bonuszok.items():
            kar.fo_tulajdonsagok_faji[kulcs].set(bonusz)

    maradt = 135 + int(kar.hatterek['Adottság'].get()) + kar.foTul_KAP.get()
    for c in kar.fo_tulajdonsagok.values():
        maradt -= c.get()
    kar.foTul_eloszthato.set(maradt)  # frissítjük az elosztható pontok változóját


def fpep(kar):
    fp(kar)
    ep(kar)


def fp(kar):
    # kepz_bonusz = kar.bonuszok["fp"].get()
    fp = kar.fo_tulajdonsagok['ÁLL'].get() + \
         kar.fo_tulajdonsagok['AKE'].get() + \
         kar.fp_KAP.get() / 2

    kar.fp_max.set(int(fp))

    kar.fp_akt.set(kar.fp_max.get())


def ep(kar):  # ezt talán lehetne merge-elni az fp-vel
    kar.ep_max.set(kar.fo_tulajdonsagok['EGÉ'].get())
    kar.ep_akt.set(kar.ep_max.get())


def hm(kar):
    # kar.bonuszok.update()
    sz = kar.fo_tulajdonsagok

    # kepzettsegbol = kar.bonuszok["hm"].get()

    # A harcértékek_alap-ot külön kéne kezelni, egyfajta állandóként és kéne
    # még egy szótár kar.harcertekek néven, ami az aktuális értékeket
    # tartalmazza. Ehhez jön majd a fegyver is!
    kar.harcertekek_alap['KÉ'].set(int(sz['GYO'].get() + sz['ÉRZ'].get()
                                       + kar.harcertekek_KAP['KÉ'].get() / 2))
    kar.harcertekek_alap['TÉ'].set(int(sz['ÜGY'].get() + sz['GYO'].get() + sz['ERŐ'].get()
                                       + kar.harcertekek_KAP['TÉ'].get() / 2))
    kar.harcertekek_alap['VÉ'].set(int(sz['ÜGY'].get() + sz['GYO'].get() + 50
                                       + kar.harcertekek_KAP['VÉ'].get() / 2))
    kar.harcertekek_alap['CÉ'].set(int(sz['ÜGY'].get() + sz['ÉRZ'].get()
                                       + kar.harcertekek_KAP['CÉ'].get() / 2))

    faj = kar.szemelyes_adatok["Faj"].get()
    if faj in ("Elf", "Félelf"):
        hasznos.mod_IntVar(kar.harcertekek_alap['CÉ'],
                           {"Elf": 10, "Félelf": 5}[faj])

    for d in resource.harcertekek_resource:
        for c in kar.fegyverek:
            if not c: continue
            c.ossz[d].set(kar.harcertekek_alap[d].get() + c.mods[d].get())


def pszi(kar):
    """Ez a metódus újraszámolja,\
és update-eli a pszivel kapcsolatos pontokat és widgeteket."""

    # 1. a képzettségből származó bónuszok kiszámítása

    # kar.bonuszok.update()
    # kepz = kar.bonuszok["pszi"].get()

    # 2. A maximális mana pont meghatározása: majdnem jó ->
    # nem számol az egyéb bónuszokkal (pl. varázstárgyak)
    # Képlet: INT + képzettségből + KAPból vásárolt
    kar.pszi_max.set(kar.fo_tulajdonsagok['INT'].get() +
                     int(kar.pszi_KAP.get() / 2))
    if kar.pszi_fok.get == 0:  # Ha nincs felvéve a pszi képzettség,
        kar.pszi_max.set(0)  # akkor nullázunk.

    # Nem számol a hátterekkel (Szellemek jóindulata, mágiatagadás, etc)
    # sem pedig egyéb módosítókkal (pl. varázstárgyak, idegen pszihasználó által
    # épített dinamikus pajzs, stb.
    kar.AME.set(kar.fo_tulajdonsagok['AST'].get())
    kar.MME.set(kar.fo_tulajdonsagok['AKE'].get())

    if kar.pszi_fok.get() >= 2:
        # Statikus pajzsok -> feltételezzük, hogy
        # maximumon tartja a statikus pajzsokat a karakter
        hasznos.mod_IntVar(kar.AME, kar.pszi_max.get())
        hasznos.mod_IntVar(kar.MME, kar.pszi_max.get())

    ###############################################
    # Dinamikus pajzsokat is meg lehetne csinálni!#
    ###############################################

    if kar.pszi_akt.get() > kar.pszi_max.get():
        # Ha kevesebb a maximum, mint az aktuális, akkor visszavesszük.
        # logikusabb lenne egyenlőre tenni minden esetben, de fuck it!
        kar.pszi_akt.set(kar.pszi_max.get())


def magia(kar):
    mana(kar)


def mana(kar):
    # kommenteket lásd a pszi metódusnál (kb ugyanez :D)
    kar.magia.update()
    # kepz_bonusz = kar.bonuszok["mana"].get()
    kar.mana_max.set(int(kar.mana_KAP.get() / 3))
    kar.mana_akt.set(kar.mana_max.get())
