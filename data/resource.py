##### SZEMÉLYES ADATOK #####

szemelyes_adat_nevek = ('Faj', 'Kaszt', 'Iskola', 'Jellem', 'Vallás', 'Isten',
                        'Szülőföld', 'Ország', 'Kaszt altípus')

fajok = ('Ember', 'Elf', 'Félelf', 'Udvari ork', 'Törpe', 'Kyr származék')

kasztok = ('Harcos', 'Lovag', 'Fejvadász',
           'Tolvaj', 'Bárd',
           'Harcművész',
           'Pap', 'Paplovag',
           'Boszorkány',
           'Boszorkánymester',
           'Tűzvarázsló',
           'Varázsló')

fokasztok = (
    'Harcos iskolák', 'Lovagrendek', 'Fejvadászklánok',
    'Tolvaj klánok', 'Bárdszervezetek',
    'Harcművész iskolák',
    'Papi rendek', 'Paplovag rendek',
    'Boszorkányszekták',
    'Boszorkánymesteri céhek',
    'Tűzvarázslói rendek',
    'Varázslórendek')

kasztok_fokasztok = dict(zip(kasztok, fokasztok))

iskolak = \
    {
        'Harcos': ('Amazon', 'Barbár', 'Erigowi számszeríjász',
                   'Siedon', 'Predoci vértes', "Egyéb harcos"),
        'Lovag': ('Feketerend', 'Marico con Rabora lovagrend',
                  'Isten kardja lovagrend', 'Erigowi Krad lovagrend',
                  "Egyéb lovag"),
        'Fejvadász': ('Vértestvérek', 'Anat-Akhan', 'Ikrek', 'Embervadászok',
                      "Egyéb fejvadász"),
        'Tolvaj': ('Kobrák', 'Talavra csodaművesei', 'Szürkecsuklyások',
                   "Egyéb tolvaj"),
        'Bárd': ('Aszisz énekmondó', 'Lombhullás árvái',
                 'Vándorló dalnok', 'Sötét bárd', "Egyéb bárd"),
        'Harcművész': ('Shien-ka-to (tűz)', 'Dart-nid-kinito (víz)',
                       'Avad-ka-kinito (föld)', 'Nisen-nid-to (levegő)',
                       'Udvari irányzat (kardművész)', 'A harc útja (kardművész)',
                       "Egyéb harcművész", "Egyéb kardművész"),
        'Pap': ('Domvik-pap', 'Ranagol-pap', 'Arel-pap',
                'Kyel-pap', 'Sogron-pap', 'Tharr-pap',
                "Egyéb pap"),
        'Paplovag': ('Darton-paplovag', 'Domvik-paplovag', 'Dreina-paplovag',
                     'Aranykör lovag', 'Ranagol-paplovag', 'Főnix',
                     'Bosszúangyal', "Egyéb paplovag"),
        'Boszorkány': ('Liviniai Gyülekezet', 'Maida Saluquas', 'Stella Prosylens',
                       'Alidaxi boszorkányrend', 'Ezer fátyol nővérei',
                       "Egyéb boszorkány"),
        'Boszorkánymester': ('Aszisz vérkelyhesek', 'Ascens Morga',
                             'Hergoli villámmesterek', "Egyéb boszorkánymester"),
        'Tűzvarázsló': ('Tűz Táplálói', 'Tűz Hordozói', 'Tűz Harcosai',
                        'Aschaon Tűzmesterei', "Egyéb tűzvarázsló"),
        'Varázsló': ('Lar-Dori Varázslórend', 'Pyarroni Varázslórend', 'Dorani Varázslórend',
                     "Egyéb varázsló"),
        ' ': None
    }

kaszt_altipusok = \
    {'Harcos': None,
     'Lovag': None,
     'Fejvadász': ('harcos', 'orgyilkos', 'felderítő', 'testőr'),
     'Tolvaj': ('zsebes', 'hamisító', 'besurranó', 'egyéb'),
     'Bárd': None,
     'Harcművész': None,
     'Kardművész': None,
     'Pap': None,
     'Paplovag': None,
     'Boszorkány': None,
     'Boszorkánymester': None,
     'Tűzvarázsló': None,
     'Varázsló': None,
     ' ': None}

jellemek = ('Élet', 'Élet, Rend', 'Élet, Káosz',
            'Halál', 'Halál, Rend', 'Halál, Káosz',
            'Rend', 'Rend, Élet', 'Rend, Halál',
            'Káosz', 'Káosz, Élet', 'Káosz, Halál',)

vallasok = ("Egyistenhit", "Pyarroni panteon", "Kyr panteon", "Dzsad panteon",
            "Amund panteon", "Törpe panteon", "Ork héroszok", "Elf Kalahorák",
            "Káosz-angyalok", "Egyéb")

istenek = \
    {
        "Egyistenhit": (
            "Domvik", "Ranagol",
            "Ranil", "Kaoraku", "Orwella"),

        "Pyarroni panteon": (
            "Adron", "Alborne", "Antoh", "Arel", "Darton",
            "Della", "Dreina", "Ellana", "Gilron", "Krad",
            "Kyel", "Noir", "Uwel", "Teljes panteon"),

        "Kyr panteon": (
            "Igere", "Weila", "Morgena",
            "Sogron", "Tharr", "Teljes panteon"),

        "Dzsad panteon": (
            "Galradzsa", "Doldzsah",
            "Dzsah", "Teljes panteon"),

        "Amund panteon": (
            "Amhe-Ramun", "Nesire",
            "Refis", "Themes", "Teljes panteon"),

        "Törpe panteon": (
            "Bul Ruurig,\na Kőatya",
            "Kadal,\na Tárnákat Zengető",
            "Tooma,\na Fejszés",
            "Zimah,\na Szökevény", "Teljes panteon"),

        "Ork héroszok": (
            "Hram,\na mélységben lakozó",
            "Tha'ushur,\na Szunnyadó",
            "Nagy Vordak", "Bhaer-Shadagg",
            "Ghazga", "Hurag Dhaur,\na Szürke Öreg",
            "Ughjorbagan,\na Falánk",
            "Oothr,\na Titokzatos", "Gar Bokkar",
            "Minden hérosz"),

        "Elf Kalahorák": (
            "Narmiraen,\na Ködökön Járó",
            "Tyssa L'imenel,\na Vér Nélkül Való",
            "Veela Luminatar,\naz Egykor Volt Fényesség",
            "Finna Lies,\na Korokon Tanító",
            "Siena Boralisse,\naz Érintéssel Enyhítő",
            "Magon L'levar,\na Szavakat Ismerő",
            "Eidhil K'Meakhan,\na Dalokban Élő",
            "Nemathiel Airaven,\na Tűzhelyre Vigyázó",
            "Rhienna Malvaureen,\na Tűz Csiholója",
            "Flidalis D'amatel,\na Lombok Őre",
            "Moranna Naranol,\na Homály Lakója",
            "Hantien Harran,\naz Árnyékban Neszező",
            "Gor Hannain,\na Tűzben Élő",
            "Mallior,\naz Éjben Kacagó",
            "Északi kalahorák",
            "Déli kalahorák"),

        "Káosz-angyalok": (
            "Káosz-Abbog", "Káosz-Buulzaab", "Káosz-Huvargh",
            "Káosz-Khakht", "Káosz-Metha", "Káosz-Oudakka",
            "Káosz-Raddaq", "Káosz-Samambrag", "Káosz-Sraddhu",
            "Káosz-Thuragh", "Káosz-Uqmat", "Káosz-Vulak",
            "Káosz-Yukk'rt", "Minden Káoszangyal"),

        "Egyéb": (
            "Egyéb isten", "Vallástalan"),

        " ": None
    }

szulofoldek = ("Északi-szövetség", "Toron és fegyvertársai", "Quiron-pentád",
               "Egyéb északi államok",
               "Pyarroni Államközösség", "Egyéb déli államok")

orszagok = \
    {
        "Északi-szövetség": (
            "Doran", "Dwyll Unió", "Gianag", "Eren",
            "Haonwell", "Erigow", "Ilanor", "Tarin",
            "Tiadlan"),

        "Toron és fegyvertársai": (
            "Abaszisz", "Gro-Ugon", "Toron"),

        "Egyéb északi államok": (
            "Alidax", "Alidar", "Arguren", "Kahre", "Rowon", "Más"),

        "Quiron-pentád": (
            "Yankar", "Daerim", "Keanor", "Dsidon", "Alcara"),

        "Pyarroni Államközösség": (
            "Pyarron", "Ó-Pyarron", "Hat Város", "Predoc", "Edorl",
            "Sempyer", "Syburr", "Ensymon", "Viadomo", "Lar-Dor",
        ),

        "Egyéb déli államok": (
            "Yllinor", "Kereskedőhercegségek", "Déli városállamok",
            "Erion", "Ordan", "Dzsad államalakulatok", "Shadon", "Krán",
            "Gorvik", "Más"),
        " ": None
    }

szemelyes_adat_sz = \
    {
        'Faj': fajok,
        'Kaszt': kasztok,
        'Kaszt altípus': None,
        'Iskola': None,
        'Jellem': jellemek,
        'Vallás': vallasok,
        'Isten': None,
        'Szülőföld': szulofoldek,
        'Ország': None
    }

szemelyes_adat_dependencia = \
    {
        'Kaszt altípus': kaszt_altipusok,
        'Iskola': iskolak,
        'Isten': istenek,
        'Ország': orszagok
    }

# Kasztok KAP költségei
kasztok_KAP = dict(zip(kasztok, (5, 6, 7, 6, 6, 10, 7, 6, 5, 6, 6, 10)))

##### HÁTTEREK #####

# Név                     KAP
hatterek_resource = {'Adottság': 20,
                     'Faj': 1,
                     'Holtak szeme': 1,
                     'Kegyelt': 1,
                     'Klán, rend, iskola': 0,
                     'Léleknyomat': 1,
                     'Mágiatagadás': 5,
                     'Mágikus fogékonyság': 1,
                     'Manalátó': 3,
                     'Művésztehetség': 1,
                     'Nemesi vér': 1,
                     'Pszi érzékenység': 1,
                     'Rang': 3,
                     'Sugallat': 1,
                     'Szellemek jóindulata': 3,
                     'Vagyon': 3
                     }

##### FŐ TULAJDONSÁGOK #####

fo_tulajdonsag_nevek = ('ERŐ', 'GYO', 'ÜGY', 'ÁLL', 'EGÉ',
                        'KAR', 'INT', 'AKE', 'AST', 'ÉRZ')
tulajdonsagok = {"Fizikai": ('ERŐ', 'GYO', 'ÜGY', 'ÁLL', 'EGÉ'),
                 "Szellemi": ('KAR', 'INT', 'AKE', 'AST', 'ÉRZ')}

faji_bonuszok = {

    'Ember': {'ERŐ': 0},

    'Elf': {'ERŐ': -2, 'ÁLL': -2,
            'GYO': 2, 'ÉRZ': 2},
    'Félelf': {'ERŐ': -1, 'ÁLL': -1,
               'GYO': 1, 'ÉRZ': 1},
    'Udvari ork': {'ERŐ': 2, 'ÁLL': 2,
                   'GYO': -2, 'ÉRZ': -2},
    'Törpe': {'ERŐ': 1, 'ÁLL': 1,
              'GYO': -1, 'ÉRZ': -1},
    'Kyr származék': {'ERŐ': -1, 'ÁLL': -1, 'EGÉ': -1,
                      'KAR': 1, 'INT': 1, 'AST': 1}
}

##### KÉPZETTSÉGEKBŐL FAKADÓ BÓNUSZOK #####

bonusz_mitmihez = \
    {
        "fp": ("Fájdalomtűrés", None),
        "hm": ("Harctéri gyakorlat", None),
        "pszi": ("Pszi", "Pszi fogékonyság"),
        "mana": (None, "Mágia érzékenység"),
        "kegy": ("Vallásismeret", "Kegyelt")
    }

pontok = ("fp", "hm", "pszi", "mana", "kegy")

##### KAP KÖLTSÉGEK, VÁSÁROLHATÓ PONTOK #####
pont_KAP_szorzok = {zip(pontok, (1, 2, 2, 3, 3))}

##### HARC ÉS HARCÉRTÉKEK #####

harcertekek_resource = ('KÉ', 'TÉ', 'VÉ', 'CÉ')

vertpajzs = ("Vértezet Típusa", "Vértezet MGT", "Vértezet Max.SFÉ",
             "Vértezet Akt.SFÉ", "Vértezet Vértviselet foka", "Pajzs Típusa",
             "Pajzs MGT", "Pajzs VÉ", "Pajzs Sebzés",
             "Pajzs Pajzshasználat foka")

vedett_testtajak = ('Fej', 'Mellkas/Hát', 'Karok', 'Has/Derék', 'Lábak')

fegyverek = {
    # Név:  méretkategória időigény  Sp   KÉ TÉ/CÉ VÉ  súly     ár  Lefegyverzés, Fegyvertörés, Átütés)
    "Puszta kéz jellegű fegyverek": {
        'Puszta kéz': (1, 3, '1k3', 0, 0, 0, 0.0, '0r', False, False, False),
        'Vasököl': (1, 3, '1k10', 0, 0, 0, 0.4, '1e', False, False, False),
    },

    "Tőrök": {
        'Béltépő': (2, 3, '1k10', 4, 9, 2, 0.5, '5e', False, False, False),
        'Dzsambia': (2, 3, '1k10', 6, 12, 2, 0.3, '1a 5e', False, False, False),
        'Kés': (2, 3, '1k6', 5, 8, 2, 0.3, '50r', False, False, False),
        'Levéltőr': (2, 3, '1k6+1', 6, 10, 5, 0.3, '5a', False, False, False),
        'Méregfog': (2, 3, '1k6', 5, 8, 2, 0.2, '2a', False, False, False),
        'Pugoss': (2, 3, '1k10', 6, 10, 3, 0.5, '1a', False, False, False),
        'Ramiera': (2, 3, '1k6+2', 6, 10, 5, 0.4, '2a', False, False, False),
        'Tőr': (2, 3, '1k10', 6, 10, 4, 0.5, '1e', False, False, False),
    },

    "Egykezes kardok": {
        'Dzsenn szablya': (3, 5, '1k10+1', 6, 14, 14, 1.0, '120a', True, False, False),
        'Emrelin kard': (3, 5, '1k10+1', 5, 12, 12, 1.3, '2a', True, False, False),
        'Fejvadászkard': (3, 5, '1k10', 6, 14, 10, 0.8, '2a', False, False, False),
        'Hárítótőr': (3, 3, '1k6+1', 5, 8, 20, 1.0, '2a', True, True, False),
        'Hiequar': (3, 5, '1k10+1', 6, 14, 8, 1.0, '50a', False, False, False),
        'Hosszú kard': (3, 5, '2k6', 5, 10, 10, 1.5, '1a 5e', True, True, False),
        'Jatagán': (3, 5, '1k6+2', 9, 14, 8, 0.9, '3a', True, True, False),
        'Khossas': (3, 5, '1k10+1', 6, 14, 8, 0.7, '15a', False, False, False),
        'Kígyókard': (3, 5, '1k10+1', 6, 13, 10, 1.6, '2a', True, True, False),
        'Lagoss': (3, 5, '1k10+1', 8, 15, 5, 1.0, '5a', False, False, False),
        'Meneth': (3, 5, '2k6+1', 1, 10, 8, 2.2, '15a', True, True, False),
        'Mesterkard': (3, 5, '2k6', 5, 13, 7, 1.2, '8a', False, False, False),
        'Predoci egyeneskard': (3, 5, '1k10+2', 5, 11, 10, 1.2, '1a 5e', True, True, False),
        'Rapír': (3, 3, '1k10', 7, 10, 13, 1.8, '5a', True, False, False),
        'Rövid kard': (3, 5, '1k10+1', 5, 10, 8, 1.0, '1a', False, True, True),
        'Sequor': (3, 5, '1k6+2', 5, 13, 13, 0.8, '1a 3e', False, False, False),
        'Slan kard': (3, 5, '1k10+2', 6, 18, 12, 1.6, '100a', True, True, True),
        'Slan tőr': (3, 3, '1k10', 8, 14, 8, 0.9, '30a', True, True, True),
        'Szablya': (3, 5, '1k10+1', 6, 10, 12, 1.2, '3a', True, False, False),
    },

    "Egykezes csatabárdok": {
        'Egykezes csatabárd': (3, 5, '2k6+1', 3, 10, 5, 1.0, '6e', True, True, True),
        # 'Csatacsillag': (3, 5, '2k6+2', 4, 13, 4, 2.2, '2a', True, False, True),
        'Csatacsákány': (3, 5, '2k6+3', 3, 11, 5, 2.0, '8e', True, False, True),
    },

    "Egykezes buzogányok": {
        'Egykezes buzogány': (3, 5, '2k6', 5, 10, 5, 1.3, '5e', True, True, True),
        'Harci kalapács': (3, 5, '2k6+1', 2, 11, 5, 1.5, '1a', True, True, True),
        'Shadleki buzogány': (3, 5, '2k6', 5, 13, 7, 2.0, '1a', True, True, True),
        'Csatacsillag': (3, 5, '2k6', 6, 13, 6, 1.5, '1a 2e', True, True, True),
    },

    "Egykezes botok": {
        'Furkósbot': (3, 5, '1k10', 5, 10, 10, 1.0, '0r', False, False, False),
        'Rövid bot': (3, 5, '1k6+2', 8, 12, 12, 1.1, '30r', True, True, True),
    },

    "Nehézkardok": {
        'Lovagkard': (4, 5, '3k6', 3, 12, 15, 2.0, '3a', True, True, True),
        'Másfélkezes kard': (4, 5, '3k6', 4, 15, 11, 2.5, '2a 5e', True, True, True),
        'Kétkezes kard': (4, 10, '4k6+2', 2, 16, 8, 4.0, '5a', False, True, True),
        'Mara-sequor': (4, 5, '3k6', 7, 16, 12, 2.2, '2a', True, True, True),
        'Slan csatakard': (4, 5, '3k6', 7, 15, 8, 2.0, '20a', True, True, True),
    },

    "Kétkezes csatabárdok": {
        'Kétkezes csatabárd': (4, 10, '5k6', 0, 15, 5, 5.0, '2a', False, True, True),
    },

    "Kétkezes buzogányok": {
        'Kétkezes buzogány': (4, 10, '3k6+2', 0, 16, 5, 5.0, '1a 2e', False, False, True),
        'Láncos buzogány': (4, 5, '2k6+1', 5, 18, 10, 2.0, '6e', True, False, False),
    },

    "Kétkezes botok": {
        'Hosszú bot': (4, 5, '2k6', 9, 10, 16, 2.0, '50r', True, True, False),
    },

    "Szálfegyverek": {
        'Alabárd': (5, 10, '5k6', 10, 15, 15, 4.0, '5a', True, True, True),
        'Lándzsa': (5, 5, '2k6+2', 13, 15, 13, 2.3, '8e', True, False, True),
        'Lovaskopja': (5, 0, '4k6', 15, 20, 1, 3.0, '1a', False, False, True),
        'Nehézlovas kopja': (5, 0, '5k6', 15, 19, 1, 5.0, '1a 5e', False, False, True),
        'Pika': (5, 5, '3k6+2', 10, 14, 12, 2.0, '4e', False, False, True),
        'Szigony': (5, 5, '3k6+1', 8, 14, 16, 2.2, '5e', True, True, True),
    },

    "Hajítófegyverek": {
        'Bola': ('táv', 5, '1k6', 2, 5, 0, 1.0, '40r', False, False, False),
        'Dobóháló': ('táv', 10, '0k6', 0, 1, 8, 4.0, '3e', False, False, False),
        'Dobótőr': ('táv', 3, '1k6', 10, 5, 2, 0.5, '1e 50r', False, False, False),
        'Hajítóbárd': ('táv', 3, '1k6+2', 9, 6, 4, 1.2, '1e', False, False, False),
        'Hajítódárda': ('táv', 5, '2k6+1', 8, 13, 5, 1.0, '5e', False, False, True),
        'Slan csillag': ('táv', 3, '1k3', 10, 4, 0, 0.1, '40r', False, False, False),
    },

    "Íjak": {
        'Rövid íj': ('táv', 3, '1k6', 5, 5, 0, 0.5, '2a', False, False, False),
        'Hosszú íj': ('táv', 3, '2k6+1', 4, 4, 0, 1.0, '3a 5e', False, False, False),
        'Visszacsapó íj': ('táv', 3, '2k6+2', 3, 8, 0, 1.0, '25a', False, False, False),
        'Elf íj': ('táv', 3, '2k6+2', 6, 15, 0, 0.7, '120a', False, False, True),
    },

    "Nyílpuskák/számszeríjak": {
        'Könnyű nyílpuska': ('táv', 3, '1k6', 5, 5, 0, 1.3, '20a', False, False, False),
        'Kahrei nyílpuska': ('táv', 5, '2k6', 6, 14, 0, 4.0, '120a', False, False, True),
        'Vadász számszeríj': ('táv', 10, '3k6', 5, 15, 0, 4.0, '8a', False, False, True),
        'Nehéz nyílpuska': ('táv', 20, '6k6', 0, 15, 0, 7.0, '12a', False, False, True),
        'Shadoni páncéltörő': ('táv', 40, '8k6', 0, 20, 0, 20.0, '40a', False, False, True),
    },

    "Egyéb távolsági fegyverek": {
        'Fúvócső': ('táv', 3, '1k3', 8, 7, 0, 0.4, '6e', False, False, False),
        'Tűvető': ('táv', 3, '1k2', 10, 2, 0, 0.2, '6e', False, False, False),
        'Parittya': ('táv', 5, '2k6', 4, 6, 0, 0.1, '30r', False, False, False)
    }
}

# KÉPZETTSÉGEK

kepzettsegek = {
    # Képzettség neve, nehézsége, képzettségkövetelményei(erős, gyenge), tulajdonságkövetelményei
    'Harci': {
        'Fájdalomtűrés': (2, (), ('ÁLL', 'AKE')),
        '!Fegyverhasználat': (3, (), ('ERŐ', 'GYO', 'ÜGY', 'ÉRZ')),
        '!Fegyver specializáció': (3, (), ('ERŐ', 'GYO', 'ÜGY', 'ÉRZ')),
        'Fegyverismeret': (2, (), ('INT', 'ÉRZ')),
        'Hadvezetés': (3, ('Lélektan', 'Térképészet'), ('INT', 'KAR')),
        'Harci láz': (2, (), ('ÁLL', 'EGÉ')),
        '!Harcművészet': (4, (), ('ERŐ', 'GYO', 'ÜGY', 'AST')),
        'Harctéri gyakorlat': (2, (), ('GYO', 'ÜGY', 'ÉRZ')),
        'Kétkezes harc': (3, ('Fegyverhasználat', None), ('GYO', 'ÜGY')),
        '!Pajzshasználat': (2, (), ('ERŐ', 'ÜGY')),
        'Pusztakezes harc': (2, (), ('ERŐ', 'GYO', 'ÁLL')),
        '!Pusztakezes harc specializáció': (2, (), ('ERŐ', 'GYO', 'ÁLL')),
        'Pusztítás': (3, ('Fegyverhasználat', 'Élettan'), ('ERŐ',)),
        'Taktika': (2, (), ('ÉRZ',)),
        'Vakharc': (3, (), ('ÉRZ',)),
        '!Vértviselet': (2, (), ('ERŐ',))
    },

    'Alvilági': {
        'Álcázás/álruha': (2, ('Kultúra', None), ('ÜGY', 'ÉRZ')),
        'Hamisítás': (3, (), ('GYO', 'ÜGY')),
        'Jelbeszéd': (2, (), ('ÉRZ', 'INT')),
        'Kocsmai verekedés': (1, (), ('ERŐ', 'GYO', 'ÜGY')),
        'Méregkeverés/semlegesítés': (2, ('Herbalizmus', 'Alkímia'), ('INT',)),
        'Orvtámadás': (2, ('Fegyverhasználat', 'Élettan'), ('ÜGY',)),
        'Kínzás': (2, (), ('ÜGY', 'INT')),
        'Szabadulóművészet': (3, ('Csomózás', 'Zárnyitás'), ('ÜGY',)),
        'Szerencsejáték': (2, (), ('ÜGY', 'INT')),
        'Csapdakeresés': (0, (), ('ÉRZ',)),
        'Lopódzás': (0, (), ('ÜGY', 'ÉRZ')),
        'Rejtőzködés': (0, (), ('ÜGY', 'ÉRZ')),
        'Rejtekhely kutatás': (0, (), ('ÉRZ',)),
        'Zárnyitás': (0, (), ('ÜGY', 'ÉRZ')),
        'Zsebmetszés': (0, (), ('ÜGY', 'ÉRZ')),
        'Veszélyérzék': (0, (), ('ÉRZ',))
    },

    'Világi': {
        '!Állatismeret': (1, (), ()),
        'Csapdaállítás': (2, ('Csomózás', 'Mechanika'), ('ÜGY',)),
        'Csomózás': (2, (), ('ÜGY',)),
        'Értékbecslés': (1, (), ('INT', 'ÉRZ')),
        'Futás': (1, (), ('ÁLL', 'EGÉ')),
        'Hajózás': (2, (), ()),
        'Hangutánzás': (2, (), ('ÉRZ',)),
        '!Helyismeret': (1, (), ()),
        '!Idomítás': (2, ('Állatismeret', None), ('AST',)),
        'Időjóslás': (2, (), ('ÉRZ', 'INT')),
        'Kocsihajtás': (1, (None, 'Állatismeret'), ('ÜGY',)),
        'Lovaglás': (1, (None, 'Állatismeret'), ('ÜGY',)),
        'Nyomolvasás': (2, (), ('ÉRZ',)),
        '!Szakma': (2, (), ()),
        'Úszás': (1, (), ('ERŐ', 'ÁLL', 'EGÉ')),
        '!Vadonjárás': (2, ('Herbalizmus', 'Állatismeret'), ('ÉRZ',)),
        'Akrobatika': (0, (), ('ÜGY',)),
        'Esés': (0, (), ('ÜGY',)),
        'Mászás': (0, (), ('ERŐ', 'ÜGY'))
    },

    'Tudományos': {
        'Alkímia': (3, ('Számtan/mértan', None), ('INT',)),
        '!Élettan': (3, (None, 'Írás/olvasás'), ('INT',)),
        'Építészet': (3, ('Számtan/mértan', 'Írás/olvasás'), ('INT',)),
        'Herbalizmus': (2, (), ('INT',)),
        'Írás/olvasás': (3, ('Nyelvtudás', None), ('INT',)),
        'Jog/törvénykezés': (3, ('Kultúra', 'Írás/olvasás'), ('INT', 'AST')),
        'Legendaismeret': (2, ('Kultúra', None), ('INT',)),
        'Mechanika': (3, ('Számtan/mértan', None), ('ÜGY', 'INT')),
        'Oktatás': (3, (None, 'Lélektan'), ('INT', 'AST')),
        'Orvoslás': (3, ('Élettan', 'Herbalizmus'), ('INT',)),
        '!Ősi nyelv': (4, (None, 'Írás/olvasás'), ('INT',)),
        'Számtan/mértan': (3, (None, 'Írás/olvasás'), ('INT',)),
        'Térképészet': (3, ('Számtan/mértan', 'Művészet'), ('INT',)),
        'Történelem': (2, (None, 'Írás/olvasás'), ('INT',)),
        '!Vallásismeret': (2, ('Kultúra', None), ('INT', 'AST')),
        '!Vallásismeret specializáció': (2, ('Kultúra', None), ('INT', 'AST'))
    },

    'Szociális': {
        'Ékesszólás': (2, ('Kultúra', 'Lélektan'), ('INT', 'AST', 'KAR')),
        'Heraldika': (2, ('Kultúra', None), ('INT',)),
        '!Kultúra': (1, ('Nyelvtudás', None), ()),
        'Lélektan': (3, (), ('INT', 'AST', 'ÉRZ')),
        '!Művészet': (2, (), ()),
        '!Nyelvtudás': (1, (), ()),
        'Párbaj': (2, ('Udvari etikett', None), ('INT', 'AST', 'KAR')),
        'Politika/diplomácia': (3, ('Udvari etikett', 'Történelem'), ('INT', 'AST', 'KAR',)),
        'Szexuális kultúra': (1, (), ('AST', 'KAR')),
        'Színészet': (3, ('Lélektan', None), ('INT', 'AST', 'KAR')),
        'Udvari etikett': (2, ('Kultúra', None), ('INT', 'AST', 'KAR'))
    },

    'Misztikus': {
        'Démonológia': (4, ('Ősi nyelv', None), ('INT', 'AKE')),
        'Drágakőmágia': (4, ('Szakma', None), ('INT', 'AKE', 'AST')),
        'Magas mágia': (4, ('Ősi nyelv', None), ('INT', 'AKE', 'AST')),
        'Nekromancia': (4, ('Élettan', None), ('INT', 'AKE', 'AST')),
        'Őselemi mágia': (4, ('Ősi nyelv', None), ('INT', 'AKE', 'AST')),
        '!Pszi': (4, (), ('INT', 'AKE', 'AST')),
        '!Pszi specializáció': (4, (), ('INT', 'AKE', 'AST')),
        'Rúnamágia': (4, ('Ősi nyelv', None), ('INT', 'AKE', 'AST')),
        '!Tapasztalati mágia': (4, (), ('INT', 'AKE', 'AST'))
    }
}

specializalhato_kepzettsegek = \
    ("Fegyverhasználat", "Pszi", "Vallásismeret")

kepzettseg_alcsoportok = \
    {
        # Kivétel-azonosítók: key végén 2/3: 3. foktól specializáció
        #                    value üres tuple: nincsenek altípusok
        #                    value[0] = "USERDEF": user definiálja

        "Fegyverhasználat": tuple(sorted(fegyverek.keys())),
        "Fegyver specializáció": ("SPECIFY",),
        "Harcművészet": tuple(sorted([csop.keys() for csop in fegyverek.values()])),
        "Pajzshasználat": ("kis pajzsok", "közepes pajzsok", "nagy pajzsok"),
        "Pusztakezes harc specializáció": ("ökölharc", "bírkózás", "rúgások"),
        "Vértviselet": ("könnyű vértek", "rugalmas nehézvértek", "merev nehézvértek"),
        "Állatismeret": ("USERDEF", "Hátas állatok"),
        "Vadonjárás": ("USERDEF", "Keleti puszták"),
        "Helyismeret": ("USERDEF", "Keleti puszták"),
        "Idomítás": ("USERDEF", "Hátas állatok"),
        "Szakma": ("USEDEF", "Ács", "Kovács", "Vadász"),
        "Élettan": ("USERDEF", "Ember"),
        "Ősi nyelv": ("USERDEF", "aquir", "óelf", "dzsenn", "amund", "kyr", "crantai", "lupár",
                      "dolamin", "godoni", "híl (törpe)", "lingua domini"),
        "Vallásismeret": None,  # kívülről
        "Vallásismeret specializáció": ("USERDEF", "SPECIFY"),
        "Kultúra": ("USERDEF", "Toroni", "Crantai", "Kahrei", "Shadoni", "Pyarroni"),
        "Művészet": ("USERDEF", "rajz", "szobrászat", "festészet", "ének", "zene", "tánc"),
        "Nyelvtudás": ("USERDEF", "pyarroni", "shadoni", "kyr", "toroni"),
        "Pszi": ("Pyarroni módszer", "Kyr metódus", "Slan út", "Godoni ösvény"),
        "Pszi specializáció": ("Pyarroni módszer (test)", "Pyarroni módszer (tudat)",
                               "Kyr metódus (tudat)", "Slan út (test)", "Godoni ösvény (tudat)"),
        "Tapasztalati mágia": ("Bárdmágia", "Boszorkánymágia", "Boszorkánymesteri mágia",
                               "Tűzmágia"),
    }

for panteon in istenek.values():
    if not panteon: continue
    kepzettseg_alcsoportok["Vallásismeret"] = ["USERDEF"] + list(panteon)

kaszt_indulo_kepzettsegek = \
    {
        "Egyéb harcos": {
            "Fegyverhasználat": 3,
            "Fegyverhasználat": 2,
            "Fegyverhasználat": 2,
            "Fegyverhasználat": 2,
            "Fegyverismeret": 2,
            "Fájdalomtűrés": 2,
            "Harctéri gyakorlat": 2,
            "Pajzshasználat": 2,
            "Állatismeret": 1,
            "Lovaglás": 2,
            "Futás": 2,
            "Mászás": 15,
            "Esés": 15,
            "Akrobatika": 15
        },

        "Amazon": {
            "Fegyverhasználat": 3,
            "Fegyverhasználat": 2,
            "Fegyverhasználat": 2,
            "Fegyverismeret": 2,
            "Fájdalomtűrés": 2,
            "Harctéri gyakorlat": 2,
            "Állatismeret": 2,
            "Futás": 2,
            "Úszás": 2,
            "Vadonjárás": 2,
            "Időjóslás": 2,
            "Herbalizmus": 2,
            "Lélektan": 1,
            "Udvari etikett": 1,
            "Mászás": 10,
            "Esés": 10,
            "Akrobatika": 10
        },

        "Barbár": {
            "Fegyverhasználat": 3,
            "Fegyverhasználat": 2,
            "Fegyverhasználat": 2,
            "Fájdalomtűrés": 2,
            "Harctéri gyakorlat": 2,
            "Harci láz": 2,
            "Pusztakezes harc": 2,
            "Fegyverismeret": 2,
            "Futás": 2,
            "Úszás": 2,
            "Vadonjárás": 2,
            "Herbalizmus": 2,
            "Állatismeret": 2,
            "Szakma": 2,
        },

        "Erigowi számszeríjász": {
            "Fegyverhasználat": 3,
            "Fegyverhasználat": 2,
            "Csapdaállítás": 1,
            "Fegyverismeret": 2,
            "Futás": 2,
            "Úszás": 2,
            "Vadonjárás": 2,
            "Nyomolvasás": 2,
            "Kocsmai verekedés": 1,
            "Jelbeszéd": 1,
            "Lopódzás": 25,
            "Rejtőzködés": 25,
        },

        "Siedon": {
            "Fegyverhasználat": 3,
            "Fegyverhasználat": 2,
            "Fegyverhasználat": 2,
            "Orvtámadás": 2,
            "Fegyverismeret": 2,
            "Élettan": 1,
            "Udvari etikett": 2,
            "Úszás": 2,
            "Heraldika": 1,
            "Párbaj": 2,
            "Írás/olvasás": 2,
            "Fájdalomtűrés": 2,
            "Lopódzás": 15
        },

        "Predoci vértes": {
            "Fegyverhasználat": 3,
            "Fegyverhasználat": 2,
            "Fegyverhasználat": 2,
            "Fegyverismeret": 2,
            "Harctéri gyakorlat": 2,
            "Pajzshasználat": 2,
            "Vértviselet": 3,
            "Lovaglás": 3,
            "Heraldika": 2,
            "Udvari etikett": 2,
            "Állatismeret": 2
        },

        "Egyéb lovag": {
            "Fegyverhasználat": 3,
            "Fegyverhasználat": 2,
            "Fegyverhasználat": 2,
            "Harctéri gyakorlat": 2,
            "Fegyverismeret": 2,
            "Vértviselet": 3,
            "Hadvezetés": 1,
            "Lovaglás": 3,
            "Udvari etikett": 2,
            "Heraldika": 2,
            "Párbaj": 2,
            "Állatismeret": 2,
            "Történelem": 2,
            "Írás/olvasás": 2,
        },

        "Feketerend": {
            "Fegyverhasználat": 3,
            "Fegyverhasználat": 2,
            "Harctéri gyakorlat": 2,
            "Pajzshasználat": 2,
            "Fájdalomtűrés": 2,
            "Fegyverismeret": 2,
            "Vértviselet": 3,
            "Hadvezetés": 1,
            "Lovaglás": 3,
            "Udvari etikett": 2,
            "Heraldika": 2,
            "Párbaj": 1,
            "Állatismeret": 2,
            "Történelem": 2,
            "Írás/olvasás": 2,
            "Vallásismeret": 3,
            "Ősi nyelv": 1
        },

        "Marico con Rabora lovagrend": {
            "Fegyverhasználat": 3,
            "Fegyverhasználat": 2,
            "Harctéri gyakorlat": 2,
            "Pajzshasználat": 3,
            "Fegyverismeret": 2,
            "Vértviselet": 2,
            "Hadvezetés": 1,
            "Lovaglás": 3,
            "Udvari etikett": 2,
            "Heraldika": 2,
            "Párbaj": 1,
            "Állatismeret": 2,
            "Történelem": 2,
            "Írás/olvasás": 2,
            "Vallásismeret": 3
        },

        "Isten kardja lovagrend": {
            "Fegyverhasználat": 3,
            "Fegyverhasználat": 2,
            "Harctéri gyakorlat": 2,
            "Pajzshasználat": 2,
            "Fegyverismeret": 2,
            "Vértviselet": 3,
            "Hadvezetés": 1,
            "Lovaglás": 3,
            "Udvari etikett": 2,
            "Heraldika": 2,
            "Párbaj": 1,
            "Állatismeret": 2,
            "Történelem": 2,
            "Írás/olvasás": 2,
            "Vallásismeret": 3,
            "Ősi nyelv": 2
            #    "!!":                   None
        },

        "Erigowi Krad lovagrend": {
            "Fegyverhasználat": 3,
            "Fegyverhasználat": 2,
            "Harctéri gyakorlat": 2,
            "Fegyverismeret": 2,
            "Vértviselet": 3,
            "Hadvezetés": 3,
            "Lovaglás": 3,
            "Udvari etikett": 2,
            "Heraldika": 2,
            "Párbaj": 1,
            "Lélektan": 2,
            "Állatismeret": 2,
            "Történelem": 3,
            "Írás/olvasás": 2,
            "Számtan/mértan": 2,
            "Térképészet": 2
        },

        "Fejvadász (harcos)": {
            "Fegyverhasználat": 3,
            "Fegyverhasználat": 2,
            "Fegyverhasználat": 1,
            "Fegyverhasználat": 1,
            "Fegyverhasználat": 1,
            "Fegyverhasználat": 1,
            "Fegyverhasználat": 1,
            "Fegyverhasználat": 1,
            "Pusztakezes harc": 2,
            "Fájdalomtűrés": 2,
            "Fegyverismeret": 2,
            "Álcázás/álruha": 2,
            "Orvtámadás": 2,
            "Élettan": 2,
            "Futás": 2,
            "Úszás": 2,
            "Pszi": 2,
            "Írás/olvasás": 1,
            "Lopódzás": 20,
            "Rejtőzködés": 20,
            "Csapdakeresés": 10,
            "Mászás": 10,
            "Esés": 10,
            "Akrobatika": 10
        },

        "Fejvadász (orgyilkos)": {
            "Fegyverhasználat": 3,
            "Fegyverhasználat": 2,
            "Fegyverhasználat": 1,
            "Fegyverhasználat": 1,
            "Fegyverhasználat": 1,
            "Fegyverhasználat": 1,
            "Fegyverhasználat": 1,
            "Fegyverhasználat": 1,
            "Pusztakezes harc": 1,
            "Fájdalomtűrés": 1,
            "Fegyverismeret": 2,
            "Álcázás/álruha": 3,
            "Színészet": 2,
            "Lélektan": 2,
            "Orvtámadás": 3,
            "Élettan": 2,
            "Futás": 2,
            "Úszás": 2,
            "Pszi": 2,
            "Írás/olvasás": 2,
            "Lopódzás": 30,
            "Rejtőzködés": 30,
            "Csapdakeresés": 10,
            "Mászás": 30,
            "Esés": 10,
            "Akrobatika": 10
        },

        "Fejvadász (felderítő)": {
            "Fegyverhasználat": 2,
            "Fegyverhasználat": 2,
            "Fegyverhasználat": 1,
            "Fegyverhasználat": 1,
            "Fegyverhasználat": 1,
            "Fegyverhasználat": 1,
            "Fegyverhasználat": 1,
            "Fegyverhasználat": 1,
            "Fájdalomtűrés": 1,
            "Fegyverismeret": 2,
            "Álcázás/álruha": 3,
            "Színészet": 2,
            "Lélektan": 2,
            "Orvtámadás": 1,
            "Élettan": 1,
            "Futás": 2,
            "Úszás": 2,
            "Pszi": 2,
            "Térképészet": 2,
            "Nyomolvasás": 2,
            "Művészet": 2,
            "Számtan/mértan": 2,
            "Lopódzás": 25,
            "Rejtőzködés": 25,
            "Csapdakeresés": 10,
            "Mászás": 20,
            "Akrobatika": 10,
            "Veszélyérzék": 10,
            "Zárnyitás": 20,
            "Vadonjárás": 2,  # EZ VAGYLAGOS A SZAKMÁVAL!
            "Szakma": 2
        },

        "Fejvadász (testőr)": {
            "Fegyverhasználat": 3,
            "Fegyverhasználat": 2,
            "Fegyverhasználat": 1,
            "Fegyverhasználat": 1,
            "Fegyverhasználat": 1,
            "Fegyverhasználat": 1,
            "Fegyverhasználat": 1,
            "Fegyverhasználat": 1,
            "Fájdalomtűrés": 2,
            "Vértviselet": 2,
            "Fegyverismeret": 2,
            "Harctéri gyakorlat": 2,
            "Hadvezetés": 2,
            "Taktika": 1,
            "Lélektan": 2,
            "Térképészet": 1,
            "Orvtámadás": 2,
            "Élettan": 2,
            "Futás": 2,
            "Úszás": 2,
            "Pszi": 2,
            "Lopódzás": 10,
            "Rejtőzködés": 10,
            "Csapdakeresés": 20,
            "Esés": 10,
            "Akrobatika": 15,
            "Veszélyérzék": 20
        },

        "Tolvaj (egyéb)": {
            "Fegyverhasználat": 2,
            "Lélektan": 1,
            "Csomózás": 2,
            "Értékbecslés": 2,
            "Álcázás/álruha": 2,
            "Jelbeszéd": 1,
            "Orvtámadás": 1,
            "Szabadulóművészet": 1,
            "Szerencsejáték": 1,
            "Mechanika": 2,
            "Számtan/mértan": 2,
            "Rejtekhely kutatás": 15,
            "Zárnyitás": 15,
            "Zsebmetszés": 15,
            "Lopódzás": 15,
            "Rejtőzködés": 15,
            "Mászás": 15,
            "Esés": 15,
            "Akrobatika": 15,
            "Csapdakeresés": 15
        },

        "Tolvaj (zsebes)": {
            "Fegyverhasználat": 2,
            "Álcázás/álruha": 2,
            "Mechanika": 2,
            "Számtan/mértan": 2,
            "Értékbecslés": 2,
            "Orvtámadás": 1,
            "Jelbeszéd": 1,
            "Szabadulóművészet": 1,
            "Csomózás": 1,
            "Szerencsejáték": 1,
            "Rejtekhely kutatás": 15,
            "Zárnyitás": 15,
            "Zsebmetszés": 45,
            "Lopódzás": 30,
            "Rejtőzködés": 15,
            "Mászás": 15,
            "Esés": 15,
            "Akrobatika": 15
        },

        "Tolvaj (hamisító)": {
            "Fegyverhasználat": 2,
            "Hamisítás": 3,
            "Mechanika": 2,
            "Számtan/mértan": 2,
            "Értékbecslés": 3,
            "Ékesszólás": 2,
            "Szakma": 2,
            "Lélektan": 1,
            "Csomózás": 1,
            "Heraldika": 2,
            "Művészet": 2,
            "Írás/olvasás": 3,
            "Rejtekhely kutatás": 10,
            "Zárnyitás": 10,
            "Lopódzás": 10,
            "Rejtőzködés": 10,
            "Mászás": 10,
            "Esés": 10,
            "Akrobatika": 10
        },

        "Tolvaj (besurranó)": {
            "Fegyverhasználat": 2,
            "Álcázás/álruha": 2,
            "Mechanika": 2,
            "Számtan/mértan": 2,
            "Értékbecslés": 3,
            "Orvtámadás": 1,
            "Jelbeszéd": 1,
            "Szabadulóművészet": 1,
            "Csomózás": 1,
            "Lélektan": 1,
            "Rejtekhely kutatás": 30,
            "Zárnyitás": 30,
            "Zsebmetszés": 10,
            "Lopódzás": 30,
            "Rejtőzködés": 30,
            "Mászás": 30,
            "Esés": 15,
            "Akrobatika": 30,
            "Csapdakeresés": 20,
            "Veszélyérzék": 15
        },

        "Egyéb bárd": {
            "Fegyverhasználat": 2,
            "Szexuális kultúra": 2,
            "Művészet": 3,
            "Művészet": 3,
            "Nyelvtudás": 4,
            "Kultúra": 4,
            "Legendaismeret": 3,
            "Tapasztalati mágia": 3,
            "Lopódzás": 10,
            "Rejtőzködés": 10
        },

        "Aszisz énekmondó": {
            "Fegyverhasználat": 2,
            "Fegyverhasználat": 2,
            "Kocsmai verekedés": 2,
            "Értékbecslés": 1,
            "Szerencsejáték": 2,
            "Szexuális kultúra": 2,
            "Művészet": 1,
            "Művészet": 1,
            "Lélektan": 1,
            "Tapasztalati mágia": 3,
            "Akrobatika": 10,
            "Lopódzás": 10,
            "Rejtőzködés": 10,
            "Zsebmetszés": 10,
            "Csapdakeresés": 10,
            "Rejtekhely kutatás": 10
        },

        "Lombhullás árvái": {
            "Fegyverhasználat": 2,
            "Fegyverhasználat": 2,
            "Művészet": 3,
            "Művészet": 2,
            "Művészet": 2,
            "Művészet": 2,
            "Párbaj": 2,
            "Heraldika": 1,
            "Írás/olvasás": 2,
            "Legendaismeret": 2
        },

        "Vándorló dalnok": {
            "Fegyverhasználat": 2,
            "Fegyverhasználat": 2,
            "Lovaglás": 3,
            "Idomítás": 2,
            "Állatismeret": 2,
            "Vadonjárás": 2,
            "Nyomolvasás": 2,
            "Herbalizmus": 1,
            "Művészet": 2,
            "Művészet": 2,
            "Legendaismeret": 2,
            "Tapasztalati mágia": 3,
            "Mászás": 10,
            "Esés": 10,
            "Akrobatika": 10
        },

        "Sötét bárd": {
            "Fegyverhasználat": 2,
            "Fegyverhasználat": 2,
            "Kínzás": 2,
            "Orvtámadás": 2,
            "Élettan": 2,
            "Írás/olvasás": 2,
            "Udvari etikett": 2,
            "Lélektan": 1,
            "Vallásismeret": 1,
            "Álcázás/álruha": 2,
            "Művészet": 2,
            "Művészet": 2,
            "Művészet": 1,
            "Művészet": 1,
            "Tapasztalati mágia": 3,
            "Lopódzás": 10,
            "Rejtőzködés": 10
        },

        "Harcművész": {
            "Harcművészet": 3,
            "Harcművészet": 3,
            "Pszi": 3,
            "Írás/olvasás": 1,
            "Orvoslás": 2,
            "Élettan": 2,
            "Herbalizmus": 2,
            "Esés": 10,
            "Akrobatika": 10
        },

        "Kardművész": {
            "Harcművészet": 3,
            "Harcművészet": 3,
            "Pszi": 3,
            "Írás/olvasás": 1,
            "Orvoslás": 2,
            "Élettan": 2,
            "Herbalizmus": 2,
            "Esés": 10,
            "Akrobatika": 10
        },

        "Egyéb pap": {
            "Fegyverhasználat": 2,
            "Vallásismeret": 3,
            "Lélektan": 2,
            "Ékesszólás": 2,
            "Írás/olvasás": 3,
            "Nyelvtudás": 3,
            "Történelem": 2,
            "Legendaismeret": 1
        },

        "Domvik-pap": {
            "Fegyverhasználat": 2,
            "Vallásismeret": 3,
            "Lélektan": 2,
            "Ékesszólás": 2,
            "Írás/olvasás": 3,
            "Nyelvtudás": 3,
            "Történelem": 2,
            "Legendaismeret": 1,
            "Jog/törvénykezés": 2,
            "Ősi nyelv": 3,
            "Herbalizmus": 2,
            "Orvoslás": 2,
            "Élettan": 2
        },

        "Ranagol-pap": {
            "Fegyverhasználat": 2,
            "Vallásismeret": 3,
            "Lélektan": 2,
            "Ékesszólás": 2,
            "Írás/olvasás": 3,
            "Nyelvtudás": 3,
            "Történelem": 2,
            "Legendaismeret": 1,
            "Ősi nyelv": 2,
            "Pszi": 3,
            "Kínzás": 2,
            "Élettan": 2,
            "Méregkeverés/semlegesítés": 2,
            "Alkímia": 1,
            "Herbalizmus": 1
        },

        "Arel-pap": {
            "Fegyverhasználat": 2,
            "Vallásismeret": 3,
            "Lélektan": 2,
            "Ékesszólás": 2,
            "Írás/olvasás": 3,
            "Nyelvtudás": 3,
            "Történelem": 2,
            "Legendaismeret": 1,
            "Fegyverhasználat": 3,
            "Harctéri gyakorlat": 2,
            "Lovaglás": 3,
            "Vadonjárás": 2,
            "Állatismeret": 2,
            "Idomítás": 2,
            "Szakma": 3
        },

        "Kyel-pap": {
            "Fegyverhasználat": 2,
            "Vallásismeret": 3,
            "Lélektan": 2,
            "Ékesszólás": 2,
            "Írás/olvasás": 3,
            "Nyelvtudás": 3,
            "Történelem": 2,
            "Legendaismeret": 1,
            "Vértviselet": 2,
            "Hadvezetés": 1,
            "Harctéri gyakorlat": 1,
            "Pajzshasználat": 2,
            "Pusztítás": 2,
            "Élettan": 1,
            "Jog/törvénykezés": 3,
            "Pszi": 2
        },

        "Sogron-pap": {
            "Fegyverhasználat": 2,
            "Vallásismeret": 3,
            "Lélektan": 2,
            "Ékesszólás": 2,
            "Írás/olvasás": 3,
            "Nyelvtudás": 3,
            "Történelem": 2,
            "Legendaismeret": 1,
            "Hadvezetés": 2,
            "Vértviselet": 1,
            "Őselemi mágia": 2,
            "Ősi nyelv": 2  # Kyr!
        },

        "Tharr-pap": {
            "Fegyverhasználat": 2,
            "Vallásismeret": 3,
            "Lélektan": 2,
            "Ékesszólás": 2,
            "Írás/olvasás": 3,
            "Nyelvtudás": 3,
            "Történelem": 2,
            "Legendaismeret": 1,
            "Élettan": 2,
            "Kínzás": 2,
            "Politika/diplomácia": 2,
            "Orvtámadás": 2,
            "Méregkeverés/semlegesítés": 2,
            "Herbalizmus": 1,
            "Alkímia": 1,
            "Udvari etikett": 2
        },

        "Egyéb paplovag": {
            "Fegyverhasználat": 3,
            "Fegyverhasználat": 2,  # EZ VAGYLAGOS A PAJZSHASZNÁLATTAL!
            "Pajzshasználat": 2,
            "Fájdalomtűrés": 2,
            "Hadvezetés": 2,
            "Harctéri gyakorlat": 2,
            "Vértviselet": 3,
            "Állatismeret": 2,
            "Lovaglás": 3,
            "Heraldika": 2,
            "Lélektan": 2,
            "Udvari etikett": 2,
            "Írás/olvasás": 2,
            "Történelem": 2,
            "Vallásismeret": 3
        },

        "Darton-paplovag": {
            "Fegyverhasználat": 3,
            "Fegyverhasználat": 2,
            "Pajzshasználat": 2,
            "Fájdalomtűrés": 2,
            "Hadvezetés": 2,
            "Harctéri gyakorlat": 3,
            "Vértviselet": 3,
            "Állatismeret": 2,
            "Lovaglás": 3,
            "Heraldika": 2,
            "Lélektan": 2,
            "Udvari etikett": 2,
            "Írás/olvasás": 2,
            "Történelem": 2,
            "Vallásismeret": 3,
            "Élettan": 2,
            "Pusztítás": 2,
            "Pusztakezes harc": 2,
            "Kocsmai verekedés": 2,
            "Szerencsejáték": 2
        },

        "Domvik-paplovag": {
            "Fegyverhasználat": 3,
            "Fegyverhasználat": 2,
            "Pajzshasználat": 2,
            "Fájdalomtűrés": 2,
            "Hadvezetés": 2,
            "Harctéri gyakorlat": 2,
            "Vértviselet": 3,
            "Állatismeret": 2,
            "Lovaglás": 3,
            "Heraldika": 2,
            "Lélektan": 2,
            "Udvari etikett": 2,
            "Írás/olvasás": 2,
            "Történelem": 2,
            "Vallásismeret": 3,
            "Ékesszólás": 2,
            "Politika/diplomácia": 2,
            "Herbalizmus": 2,
            "Orvoslás": 2,
            "Élettan": 2,
            "Ősi nyelv": 2
        },

        "Dreina-paplovag": {
            "Fegyverhasználat": 3,
            "Fegyverhasználat": 2,
            "Pajzshasználat": 2,
            "Fájdalomtűrés": 2,
            "Hadvezetés": 2,
            "Harctéri gyakorlat": 2,
            "Vértviselet": 3,
            "Állatismeret": 2,
            "Lovaglás": 3,
            "Heraldika": 2,
            "Lélektan": 2,
            "Udvari etikett": 2,
            "Írás/olvasás": 2,
            "Történelem": 2,
            "Vallásismeret": 3,
            "Számtan/mértan": 2,
            "Szakma": 2,
            "Jog/törvénykezés": 2,
            "Politika/diplomácia": 2,
            "Kultúra": 2,
            "Nyelvtudás": 2
        },

        "Aranykör lovag": {
            "Fegyverhasználat": 3,
            "Fegyverhasználat": 2,
            "Pajzshasználat": 2,
            "Fájdalomtűrés": 2,
            "Hadvezetés": 2,
            "Harctéri gyakorlat": 2,
            "Vértviselet": 3,
            "Állatismeret": 2,
            "Lovaglás": 3,
            "Heraldika": 2,
            "Lélektan": 2,
            "Udvari etikett": 2,
            "Írás/olvasás": 3,
            "Történelem": 2,
            "Vallásismeret": 3,
            "Számtan/mértan": 2,
            "Történelem": 3,
            "Térképészet": 2,
            "Legendaismeret": 2,
            "Kultúra": 2,
            "Nyelvtudás": 2
        },

        "Ranagol-paplovag": {
            "Fegyverhasználat": 3,
            "Fegyverhasználat": 2,
            "Pajzshasználat": 2,
            "Fájdalomtűrés": 2,
            "Hadvezetés": 2,
            "Harctéri gyakorlat": 2,
            "Vértviselet": 3,
            "Állatismeret": 2,
            "Lovaglás": 3,
            "Heraldika": 2,
            "Lélektan": 2,
            "Udvari etikett": 2,
            "Írás/olvasás": 2,
            "Történelem": 2,
            "Vallásismeret": 3,
            "Fegyverhasználat": 2,
            "Élettan": 2,
            "Kínzás": 2,
            "Orvtámadás": 2,
            "Méregkeverés/semlegesítés": 2,
            "Herbalizmus": 1,
            "Alkímia": 1
        },

        "Főnix": {
            "Fegyverhasználat": 3,
            "Fegyverhasználat": 2,
            "Pajzshasználat": 2,
            "Fájdalomtűrés": 2,
            "Hadvezetés": 2,
            "Harctéri gyakorlat": 2,
            "Vértviselet": 3,
            "Állatismeret": 2,
            "Lovaglás": 3,
            "Heraldika": 2,
            "Lélektan": 2,
            "Udvari etikett": 2,
            "Írás/olvasás": 2,
            "Történelem": 2,
            "Vallásismeret": 3,
            "Tapasztalati mágia": 2,
            "Taktika": 2
        },

        "Bosszúangyal": {
            "Fegyverhasználat": 3,
            "Fegyverhasználat": 2,
            "Pajzshasználat": 2,
            "Fájdalomtűrés": 2,
            "Hadvezetés": 2,
            "Harctéri gyakorlat": 2,
            "Vértviselet": 3,
            "Állatismeret": 2,
            "Lovaglás": 3,
            "Heraldika": 2,
            "Lélektan": 2,
            "Udvari etikett": 2,
            "Írás/olvasás": 2,
            "Történelem": 2,
            "Vallásismeret": 3,
            "Térképészet": 2,
            "Jog/törvénykezés": 2,
            "Pusztítás": 2,
            "Számtan/mértan": 2,
            "Élettan": 2
        },

        "Boszorkány": {
            "Lélektan": 2,
            "Művészet": 2,
            "Nyelvtudás": 3,
            "Szexuális kultúra": 2,
            "Udvari etikett": 2,
            "Alkímia": 2,
            "Herbalizmus": 3,
            "Írás/olvasás": 2,
            "Legendaismeret": 2,
            "Pszi": 2,
            "Tapasztalati mágia": 3
        },

        "Egyéb boszorkánymester": {
            "Fegyverhasználat": 2,
            "Nyelvtudás": 2,
            "Alkímia": 2,
            "Élettan": 2,
            "Herbalizmus": 2,
            "Írás/olvasás": 2,
            "Méregkeverés/semlegesítés": 2,
            "Számtan/mértan": 2,
            "Nekromancia": 2,
            "Pszi": 2,
            "Tapasztalati mágia": 3
        },

        "Aszisz vérkelyhesek": {
            "Fegyverhasználat": 2,
            "Alkímia": 3,
            "Élettan": 2,
            "Herbalizmus": 3,
            "Írás/olvasás": 2,
            "Méregkeverés/semlegesítés": 3,
            "Számtan/mértan": 3,
            "Nekromancia": 2,
            "Pszi": 2,
            "Nyelvtudás": 2,
            "Politika/diplomácia": 3,
            "Udvari etikett": 3,
            "Történelem": 3,
            "Tapasztalati mágia": 3
        },

        "Ascens Morga": {
            "Fegyverhasználat": 2,
            "Fegyverhasználat": 2,
            "Nyelvtudás": 2,
            "Alkímia": 3,
            "Élettan": 2,
            "Orvtámadás": 2,
            "Herbalizmus": 3,
            "Írás/olvasás": 2,
            "Méregkeverés/semlegesítés": 3,
            "Számtan/mértan": 3,
            "Nekromancia": 1,
            "Pszi": 2,
            "Tapasztalati mágia": 3,
            "Politika/diplomácia": 1,
            "Udvari etikett": 2,
            "Történelem": 2
        },

        "Hergoli villámmesterek": {
            "Fegyverhasználat": 2,
            "Alkímia": 2,
            "Herbalizmus": 2,
            "Írás/olvasás": 2,
            "Méregkeverés/semlegesítés": 2,
            "Számtan/mértan": 2,
            "Pszi": 2,
            "Tapasztalati mágia": 3,
            "Politika/diplomácia": 2,
            "Csomózás": 2,
            "Értékbecslés": 2,
            "Hajózás": 2
        },

        "Tűzvarázsló": {
            "Fegyverhasználat": 2,
            "Fegyverhasználat": 2,
            "Nyelvtudás": 3,
            "Írás/olvasás": 3,
            "Ősi nyelv": 3,
            "Vallásismeret": 2,
            "Őselemi mágia": 2,
            "Pszi": 3,
            "Tapasztalati mágia": 3
        },

        "Varázsló": {
            "Nyelvtudás": 3,
            "Nyelvtudás": 2,
            "Politika/diplomácia": 2,
            "Udvari etikett": 2,
            "Írás/olvasás": 3,
            "Ősi nyelv": 3,
            "Számtan/mértan": 3,
            "Történelem": 2,
            "Magas mágia": 3,
            "Pszi": 4
        },
    }

##### MÁGIA ÉS PSZI #####

tapasztalati_magiaformak = ("Bárd", "Boszorkány", "Boszorkánymester", "Tűzvarázsló")
magiahasznalok = tuple(list(tapasztalati_magiaformak) + ["Varázsló"])
muveszet_formak = ("Rajz", "Ének", "Szobrászat", "Festészet", "Zene")
pszi_iskolak = ('Pyarroni módszer', 'Kyr metódus', 'Slan út', 'Godoni ösvény')

##### KÉPZETTSÉG BÓNUSZOK: OKTATÁS, FAJI ELŐNYÖK #####

oktatas_bonuszok = {
    "Egyéb harcos": \
        ("Akrobatika", "Állatismeret", "Esés", "Fájdalomtűrés",
         "Fegyverhasználat", "Futás", "Harctéri gyakorlat", "Hadvezetés",
         "Harci láz", "Lélektan", "Lovaglás", "Mászás", "Művészet",
         "Pajzshasználat", "Pusztakezes harc", "Számtan/mértan", "Taktika",
         "Térképészet", "Úszás", "Vértviselet"),

    "Amazon": "Egyéb harcos",

    "Barbár": \
        ("Minden Harci", "Minden Világi"),

    "Erigowi számszeríjász": \
        ("Akrobatika", "Esés", "Fájdalomtűrés",
         "Fegyverhasználat", "Futás", "Hadvezetés", "Harctéri gyakorlat",
         "Jelbeszéd", "Lélektan", "Mászás", "Mechanika", "Művészet",
         "Nyomolvasás", "Számtan/mértan", "Taktika", "Térképészet",
         "Úszás", "Vadonjárás"),

    "Siedon": \
        ("Akrobatika", "Álcázás/álruha", "Csapdakeresés", "Csomózás",
         "Fájdalomtűrés", "Fegyverhasználat", "Fegyverismeret", "Futás",
         "Harctéri gyakorlat", "Heraldika", "Írás/olvasás",
         "Kétkezes harc", "Kultúra", "Lopódzás", "Orvtámadás", "Párbaj",
         "Rejtekhely kutatás", "Rejtőzködés", "Szabadulóművészet",
         "Udvari etikett", "Vértviselet", "Zárnyitás"),

    "Predoci vértes": \
        ("Állatismeret", "Esés", "Fájdalomtűrés",
         "Fegyverhasználat", "Fegyverismeret", "Hadvezetés",
         "Harctéri gyakorlat", "Heraldika", "Idomítás",
         "Írás/olvasás", "Kultúra", "Lélektan", "Lovaglás",
         "Mászás", "Művészet", "Párbaj", "Számtan/mértan",
         "Taktika", "Térképészet", "Udvari etikett", "Úszás",
         "Vértviselet"),

    "Egyéb lovag": \
        ("Állatismeret", "Élettan", "Esés", "Fájdalomtűrés", "Fegyverhasználat",
         "Fegyverismeret", "Hadvezetés", "Harctéri gyakorlat", "Heraldika",
         "Írás/olvasás", "Kultúra", "Lélektan", "Lovaglás", "Művészet",
         "Nyelvtudás", "Pajzshasználat", "Párbaj", "Számtan/mértan", "Taktika",
         "Térképészet", "Történelem", "Udvari etikett", "Vértviselet"),

    "Feketerend": \
        ("Állatismeret", "Élettan", "Esés", "Fájdalomtűrés", "Fegyverhasználat",
         "Fegyverismeret", "Hadvezetés", "Harctéri gyakorlat", "Heraldika",
         "Írás/olvasás", "Kultúra", "Lélektan", "Lovaglás", "Művészet",
         "Nyelvtudás", "Ősi nyelv", "Pajzshasználat", "Párbaj", "Pszi", "Pusztítás",
         "Számtan/mértan", "Taktika", "Térképészet", "Történelem", "Udvari etikett",
         "Vértviselet"),

    "Marico con Rabora lovagrend": \
        ("Állatismeret", "Esés", "Fájdalomtűrés", "Fegyverhasználat",
         "Fegyverismeret", "Hadvezetés", "Harctéri gyakorlat", "Heraldika",
         "Írás/olvasás", "Kultúra", "Legendaismeret", "Lélektan", "Lovaglás",
         "Művészet", "Nyelvtudás", "Pajzshasználat", "Párbaj", "Pszi",
         "Számtan/mértan", "Taktika", "Térképészet",
         "Történelem", "Udvari etikett", "Vallásismeret", "Vértviselet"),

    "Isten kardja lovagrend": \
        ("Állatismeret", "Esés", "Fájdalomtűrés", "Fegyverhasználat",
         "Fegyverismeret", "Hadvezetés", "Harctéri gyakorlat", "Heraldika",
         "Írás/olvasás", "Kultúra", "Legendaismeret", "Lélektan", "Lovaglás",
         "Művészet", "Nyelvtudás", "Ősi nyelv", "Pajzshasználat", "Párbaj", "Pszi",
         "Számtan/mértan", "Taktika", "Térképészet", "Történelem", "Udvari etikett",
         "Vallásismeret", "Vértviselet"),

    "Erigowi Krad lovagrend": \
        ("Állatismeret", "Esés", "Fájdalomtűrés", "Fegyverhasználat",
         "Fegyverismeret", "Hadvezetés", "Harctéri gyakorlat", "Heraldika",
         "Írás/olvasás", "Kultúra", "Legendaismeret", "Lélektan", "Lovaglás",
         "Művészet", "Pajzshasználat", "Párbaj", "Pszi", "Számtan/mértan",
         "Taktika", "Térképészet", "Történelem", "Udvari etikett",
         "Vallásismeret", "Vértviselet"),

    "Fejvadász (harcos)": \
        ("Akrobatika", "Álcázás/álruha", "Csapdaállítás", "Csapdakeresés",
         "Csomózás", "Élettan", "Esés", "Fájdalomtűrés", "Fegyverhasználat",
         "Fegyverismeret", "Harcművészet", "Harctéri gyakorlat", "Írás/olvasás",
         "Jelbeszéd", "Kétkezes harc", "Kínzás", "Kultúra", "Lopódzás", "Mászás",
         "Mechanika", "Nyomolvasás", "Orvtámadás", "Pszi",
         "Pusztakezes harc", "Pusztítás", "Rejtekhely kutatás", "Rejtőzködés",
         "Szabadulóművészet", "Számtan/mértan", "Színészet", "Taktika", "Vakharc",
         "Vértviselet", "Zárnyitás"),

    "Fejvadász (orgyilkos)": \
        ("Akrobatika", "Álcázás/álruha", "Csapdaállítás", "Csapdakeresés",
         "Csomózás", "Élettan", "Esés", "Fájdalomtűrés", "Fegyverhasználat",
         "Fegyverismeret", "Harcművészet", "Harctéri gyakorlat", "Írás/olvasás",
         "Jelbeszéd", "Kétkezes harc", "Kínzás", "Kultúra", "Lopódzás", "Mászás",
         "Mechanika", "Nyomolvasás", "Orvtámadás", "Pszi",
         "Pusztakezes harc", "Pusztítás", "Rejtekhely kutatás", "Rejtőzködés",
         "Szabadulóművészet", "Számtan/mértan", "Színészet", "Taktika", "Vakharc",
         "Vértviselet", "Zárnyitás"),

    "Fejvadász (felderítő)": \
        ("Akrobatika", "Álcázás/álruha", "Csapdaállítás", "Csapdakeresés",
         "Csomózás", "Élettan", "Esés", "Fájdalomtűrés", "Fegyverhasználat",
         "Fegyverismeret", "Harcművészet", "Harctéri gyakorlat", "Írás/olvasás",
         "Jelbeszéd", "Kétkezes harc", "Kínzás", "Kultúra", "Lélektan", "Lopódzás",
         "Mászás", "Mechanika", "Művészet", "Nyomolvasás", "Orvtámadás", "Pszi",
         "Rejtekhely kutatás", "Rejtőzködés", "Szabadulóművészet", "Szakma",
         "Számtan/mértan", "Színészet", "Taktika", "Vakharc", "Zárnyitás"),

    "Fejvadász (testőr)": \
        ("Akrobatika", "Álcázás/álruha", "Csapdaállítás", "Csapdakeresés",
         "Csomózás", "Élettan", "Esés", "Fájdalomtűrés", "Fegyverhasználat",
         "Fegyverismeret", "Harcművészet", "Harctéri gyakorlat", "Írás/olvasás",
         "Jelbeszéd", "Kétkezes harc", "Kínzás", "Kultúra", "Lopódzás", "Mászás",
         "Mechanika", "Nyomolvasás", "Orvtámadás", "Pszi", "Pusztakezes harc",
         "Pusztítás", "Rejtekhely kutatás", "Rejtőzködés", "Szabadulóművészet",
         "Számtan/mértan", "Színészet", "Taktika", "Vakharc", "Vértviselet",
         "Zárnyitás"),

    "Tolvaj": \
        ("Akrobatika", "Álcázás/álruha", "Csapdakeresés", "Csomózás",
         "Ékesszólás", "Élettan", "Építészet", "Értékbecslés", "Esés",
         "Fegyverhasználat", "Hamisítás", "Helyismeret", "Heraldika", "Írás/olvasás",
         "Jelbeszéd", "Kétkezes harc", "Kocsmai verekedés", "Kultúra",
         "Legendaismeret", "Lélektan", "Lopódzás", "Mászás", "Mechanika",
         "Művészet", "Nyomolvasás", "Orvtámadás", "Rejtekhely kutatás",
         "Rejtőzködés", "Szabadulóművészet", "Számtan/mértan",
         "Szerencsejáték", "Színészet", "Udvari etikett", "Zárnyitás",
         "Zsebmetszés"),

    "Egyéb bárd": \
        ("Álcázás/álruha", "Ékesszólás", "Értékbecslés", "Fegyverhasználat",
         "Írás/olvasás", "Heraldika", "Kocsmai verekedés", "Kultúra",
         "Legendaismeret", "Lélektan", "Lopódzás", "Művészet", "Nyelvtudás",
         "Párbaj", "Rejtekhely kutatás", "Rejtőzködés", "Szerencsejáték",
         "Szexuális kultúra", "Színészet", "Tapasztalati mágia", "Történelem",
         "Udvari etikett", "Zárnyitás"),

    "Aszisz énekmondó": \
        ("Akrobatika", "Álcázás/álruha", "Csapdakeresés", "Csomózás",
         "Értékbecslés", "Fegyverhasználat", "Hamisítás", "Írás/olvasás",
         "Heraldika", "Kocsihajtás", "Kocsmai verekedés", "Kultúra",
         "Legendaismeret", "Lélektan", "Lopódzás", "Művészet", "Rejtekhely kutatás",
         "Rejtőzködés", "Szabadulóművészet", "Szerencsejáték", "Szexuális kultúra",
         "Színészet", "Tapasztalati mágia", "Történelem",
         "Zárnyitás", "Színészet"),

    "Lombhullás árvái": \
        ("Akrobatika", "Értékbecslés", "Fegyverhasználat", "Heraldika",
         "Legendaismeret", "Lélektan", "Lopódzás", "Művészet", "Nyelvtudás",
         "Rejtekhely kutatás", "Rejtőzködés", "Szerencsejáték", "Szexuális kultúra",
         "Színészet", "Tapasztalati mágia", "Történelem"),

    "Vándorló dalnok": \
        ("Akrobatika", "Állatismeret", "Csomózás", "Értékbecslés", "Esés",
         "Fegyverhasználat", "Hangutánzás", "Harctéri gyakorlat", "Herbalizmus",
         "Idomítás", "Kocsmai verekedés", "Kultúra", "Legendaismeret", "Lélektan",
         "Lopódzás", "Lovaglás", "Mászás", "Művészet", "Párbaj", "Rejtőzködés",
         "Szexuális kultúra", "Tapasztalati mágia", "Vadonjárás"),

    "Sötét bárd": \
        ("Fegyverhasználat", "Vallásismeret", "Kínzás", "Lélektan", "Művészet",
         "Színészet", "Álcázás/álruha", "Orvtámadás", "Lopódzás", "Rejtőzködés",
         "Kétkezes harc", "Kultúra", "Élettan", "Írás/olvasás", "Legendaismeret",
         "Történelem", "Udvari etikett", "Tapasztalati mágia"),

    "Harcművész": \
        ("Akrobatika", "Élettan", "Esés", "Fájdalomtűrés", "Fegyverismeret",
         "Futás", "Harcművészet", "Harctéri gyakorlat", "Herbalizmus", "Írás/olvasás",
         "Kétkezes harc", "Kultúra", "Művészet", "Nyelvtudás", "Orvoslás", "Párbaj",
         "Pszi", "Udvari etikett", "Vakharc", "Vértviselet"),

    "Kardművész": "Harcművész",

    "Egyéb pap": \
        ("Ékesszólás", "Élettan", "Fegyverhasználat", "Heraldika", "Herbalizmus",
         "Írás/olvasás", "Jog/törvénykezés", "Kultúra", "Legendaismeret", "Lélektan",
         "Művészet", "Nyelvtudás", "Orvoslás", "Ősi nyelv", "Politika/diplomácia",
         "Pszi", "Számtan/mértan", "Térképészet", "Történelem", "Udvari etikett",
         "Vallásismeret"),

    "Domvik-pap": \
        ("Ékesszólás", "Élettan", "Fegyverhasználat", "Heraldika", "Herbalizmus",
         "Írás/olvasás", "Jog/törvénykezés", "Kultúra", "Legendaismeret", "Lélektan",
         "Művészet", "Nyelvtudás", "Orvoslás", "Ősi nyelv", "Politika/diplomácia",
         "Pszi", "Számtan/mértan", "Térképészet", "Történelem", "Udvari etikett",
         "Vallásismeret", "Hadvezetés", "Oktatás", "Ősi nyelv"),

    "Ranagol-pap": \
        ("Ékesszólás", "Élettan", "Fegyverhasználat", "Heraldika", "Herbalizmus",
         "Írás/olvasás", "Jog/törvénykezés", "Kultúra", "Legendaismeret", "Lélektan",
         "Művészet", "Nyelvtudás", "Orvoslás", "Ősi nyelv", "Politika/diplomácia",
         "Pszi", "Számtan/mértan", "Térképészet", "Történelem", "Udvari etikett",
         "Vallásismeret", "Alkímia", "Kínzás", "Művészet", "Ősi nyelv"),

    "Arel-pap": \
        ("Ékesszólás", "Élettan", "Fegyverhasználat", "Heraldika", "Herbalizmus",
         "Írás/olvasás", "Jog/törvénykezés", "Kultúra", "Legendaismeret", "Lélektan",
         "Művészet", "Nyelvtudás", "Orvoslás", "Ősi nyelv", "Politika/diplomácia",
         "Pszi", "Számtan/mértan", "Térképészet", "Történelem", "Udvari etikett",
         "Vallásismeret", "Állatismeret", "Hadvezetés", "Harci láz",
         "Harctéri gyakorlat", "Fájdalomtűrés", "Fegyverismeret", "Idomítás",
         "Kocsmai verekedés", "Lovaglás", "Nyomolvasás", "Szakma", "Szerencsejáték",
         "Vadonjárás"),

    "Kyel-pap": \
        ("Ékesszólás", "Élettan", "Fegyverhasználat", "Heraldika", "Herbalizmus",
         "Írás/olvasás", "Jog/törvénykezés", "Kultúra", "Legendaismeret", "Lélektan",
         "Művészet", "Nyelvtudás", "Orvoslás", "Ősi nyelv", "Politika/diplomácia",
         "Pszi", "Számtan/mértan", "Térképészet", "Történelem", "Udvari etikett",
         "Vallásismeret", "Fegyverismeret", "Hadvezetés", "Harctéri gyakorlat",
         "Pajzshasználat", "Pusztítás", "Vértviselet"),

    "Sogron-pap": \
        ("Ékesszólás", "Élettan", "Fegyverhasználat", "Heraldika", "Herbalizmus",
         "Írás/olvasás", "Jog/törvénykezés", "Kultúra", "Legendaismeret", "Lélektan",
         "Művészet", "Nyelvtudás", "Orvoslás", "Ősi nyelv", "Politika/diplomácia",
         "Pszi", "Számtan/mértan", "Térképészet", "Történelem", "Udvari etikett",
         "Vallásismeret", "Hadvezetés", "Tapasztalati mágia", "Vértviselet"),

    "Tharr-pap": \
        ("Ékesszólás", "Élettan", "Fegyverhasználat", "Heraldika", "Herbalizmus",
         "Írás/olvasás", "Jog/törvénykezés", "Kultúra", "Legendaismeret", "Lélektan",
         "Művészet", "Nyelvtudás", "Orvoslás", "Ősi nyelv", "Politika/diplomácia",
         "Pszi", "Számtan/mértan", "Térképészet", "Történelem", "Udvari etikett",
         "Vallásismeret", "Alkímia", "Kínzás", "Méregkeverés/semlegesítés",
         "Orvtámadás"),

    "Egyéb paplovag": \
        ("Állatismeret", "Ékesszólás", "Fájdalomtűrés", "Fegyverhasználat",
         "Fegyverismeret", "Hadvezetés", "Harctéri gyakorlat", "Heraldika",
         "Herbalizmus", "Írás/olvasás", "Kultúra", "Legendaismeret", "Lélektan",
         "Lovaglás", "Művészet", "Nyelvtudás", "Orvoslás", "Pajzshasználat",
         "Pszi", "Számtan/mértan", "Térképészet", "Történelem", "Udvari etikett",
         "Vallásismeret", "Vértviselet"),

    "Darton-paplovag": \
        ("Állatismeret", "Ékesszólás", "Fájdalomtűrés", "Fegyverhasználat",
         "Fegyverismeret", "Hadvezetés", "Harctéri gyakorlat", "Heraldika",
         "Herbalizmus", "Írás/olvasás", "Kultúra", "Legendaismeret", "Lélektan",
         "Lovaglás", "Művészet", "Nyelvtudás", "Orvoslás", "Pajzshasználat",
         "Pszi", "Számtan/mértan", "Térképészet", "Történelem", "Udvari etikett",
         "Vallásismeret", "Vértviselet", "Kocsmai verekedés", "Élettan",
         "Pusztítás", "Pusztakezes harc", "Szerencsejáték"),

    "Domvik-paplovag": \
        ("Állatismeret", "Ékesszólás", "Fájdalomtűrés", "Fegyverhasználat",
         "Fegyverismeret", "Hadvezetés", "Harctéri gyakorlat", "Heraldika",
         "Herbalizmus", "Írás/olvasás", "Kultúra", "Legendaismeret", "Lélektan",
         "Lovaglás", "Művészet", "Nyelvtudás", "Orvoslás", "Pajzshasználat",
         "Pszi", "Számtan/mértan", "Térképészet", "Történelem", "Udvari etikett",
         "Vallásismeret", "Vértviselet", "Élettan", "Jog/törvénykezés",
         "Politika/diplomácia", "Ősi nyelv"),

    "Dreina-paplovag": \
        ("Állatismeret", "Ékesszólás", "Fájdalomtűrés", "Fegyverhasználat",
         "Fegyverismeret", "Hadvezetés", "Harctéri gyakorlat", "Heraldika",
         "Herbalizmus", "Írás/olvasás", "Kultúra", "Legendaismeret", "Lélektan",
         "Lovaglás", "Művészet", "Nyelvtudás", "Orvoslás", "Pajzshasználat",
         "Pszi", "Számtan/mértan", "Térképészet", "Történelem", "Udvari etikett",
         "Vallásismeret", "Vértviselet", "Értékbecslés", "Jog/törvénykezés",
         "Politika/diplomácia", "Szakma"),

    "Aranykör lovag": \
        ("Állatismeret", "Ékesszólás", "Fájdalomtűrés", "Fegyverhasználat",
         "Fegyverismeret", "Hadvezetés", "Harctéri gyakorlat", "Heraldika",
         "Herbalizmus", "Írás/olvasás", "Kultúra", "Legendaismeret", "Lélektan",
         "Lovaglás", "Művészet", "Nyelvtudás", "Orvoslás", "Pajzshasználat",
         "Pszi", "Számtan/mértan", "Térképészet", "Történelem", "Udvari etikett",
         "Vallásismeret", "Vértviselet", "Jog/törvénykezés", "Térképészet"),

    "Ranagol-paplovag": \
        ("Állatismeret", "Ékesszólás", "Fájdalomtűrés", "Fegyverhasználat",
         "Fegyverismeret", "Hadvezetés", "Harctéri gyakorlat", "Heraldika",
         "Herbalizmus", "Írás/olvasás", "Kultúra", "Legendaismeret", "Lélektan",
         "Lovaglás", "Művészet", "Nyelvtudás", "Orvoslás", "Pajzshasználat",
         "Pszi", "Számtan/mértan", "Térképészet", "Történelem", "Udvari etikett",
         "Vallásismeret", "Vértviselet", "Méregkeverés/semlegesítés",
         "Alkímia", "Orvtámadás", "Kínzás"),

    "Főnix": \
        ("Állatismeret", "Ékesszólás", "Fájdalomtűrés", "Fegyverhasználat",
         "Fegyverismeret", "Hadvezetés", "Harctéri gyakorlat", "Heraldika",
         "Herbalizmus", "Írás/olvasás", "Kultúra", "Legendaismeret", "Lélektan",
         "Lovaglás", "Művészet", "Nyelvtudás", "Orvoslás", "Pajzshasználat",
         "Pszi", "Számtan/mértan", "Térképészet", "Történelem", "Udvari etikett",
         "Vallásismeret", "Vértviselet", "Hajózás", "Térképészet",
         "Tapasztalati mágia", "Csomózás", "Ősi nyelv", "Taktika"),

    "Bosszúangyal": \
        ("Állatismeret", "Ékesszólás", "Fájdalomtűrés", "Fegyverhasználat",
         "Fegyverismeret", "Hadvezetés", "Harctéri gyakorlat", "Heraldika",
         "Herbalizmus", "Írás/olvasás", "Kultúra", "Legendaismeret", "Lélektan",
         "Lovaglás", "Művészet", "Nyelvtudás", "Orvoslás", "Pajzshasználat",
         "Pszi", "Számtan/mértan", "Térképészet", "Történelem", "Udvari etikett",
         "Vallásismeret", "Vértviselet", "Pusztítás", "Jog/törvénykezés"),

    "Boszorkány": \
        ("Alkímia", "Állatismeret", "Ékesszólás", "Élettan", "Értékbecslés",
         "Fegyverhasználat", "Lélektan", "Heraldika", "Herbalizmus",
         "Írás/olvasás", "Kultúra", "Legendaismeret", "Méregkeverés/semlegesítés",
         "Művészet", "Nyelvtudás", "Orvoslás", "Pszi", "Szakma",
         "Számtan/mértan", "Szexuális kultúra", "Tapasztalati mágia",
         "Történelem", "Udvari etikett", "Vallásismeret"),

    "Egyéb boszorkánymester": \
        ("Alkímia", "Élettan", "Fegyverhasználat", "Heraldika", "Herbalizmus",
         "Időjóslás", "Írás/olvasás", "Kultúra", "Legendaismeret",
         "Méregkeverés/semlegesítés", "Nekromancia", "Nyelvtudás", "Orvoslás",
         "Orvtámadás", "Pszi", "Szakma", "Számtan/mértan", "Tapasztalati mágia",
         "Történelem"),

    "Aszisz vérkelyhesek": \
        ("Alkímia", "Élettan", "Fegyverhasználat", "Heraldika", "Herbalizmus",
         "Időjóslás", "Írás/olvasás", "Kultúra", "Legendaismeret",
         "Méregkeverés/semlegesítés", "Nekromancia", "Nyelvtudás", "Orvoslás",
         "Orvtámadás", "Pszi", "Szakma", "Számtan/mértan", "Tapasztalati mágia",
         "Történelem", "Udvari etikett", "Politika/diplomácia"),

    "Ascens Morga": \
        ("Alkímia", "Élettan", "Fegyverhasználat", "Heraldika", "Herbalizmus",
         "Időjóslás", "Írás/olvasás", "Kultúra", "Legendaismeret",
         "Méregkeverés/semlegesítés", "Nekromancia", "Nyelvtudás", "Orvoslás",
         "Orvtámadás", "Pszi", "Szakma", "Számtan/mértan", "Tapasztalati mágia",
         "Történelem", "Udvari etikett", "Politika/diplomácia", "Térképészet",
         "Lélektan", "Hadvezetés", "Taktika", "Művészet", "Rúnamágia",
         "Színészet"),

    "Hergoli villámmesterek": \
        ("Alkímia", "Élettan", "Fegyverhasználat", "Heraldika", "Herbalizmus",
         "Időjóslás", "Írás/olvasás", "Kultúra", "Legendaismeret",
         "Méregkeverés/semlegesítés", "Nekromancia", "Nyelvtudás", "Orvoslás",
         "Orvtámadás", "Pszi", "Szakma", "Számtan/mértan", "Tapasztalati mágia",
         "Történelem", "Hadvezetés", "Lélektan", "Térképészet", "Művészet",
         "Hajózás", "Csomózás", "Értékbecslés", "Kultúra", "Szakma",
         "Politika/diplomácia", "Udvari etikett"),

    "Tűzvarázsló": \
        ("Csomózás", "Fegyverhasználat", "Hadvezetés", "Hajózás", "Heraldika",
         "Időjóslás", "Írás/olvasás", "Kultúra", "Lélektan", "Művészet",
         "Nyelvtudás", "Ősi nyelv", "Őselemi mágia", "Politika/diplomácia",
         "Pszi", "Rúnamágia", "Számtan/mértan", "Tapasztalati mágia", "Térképészet",
         "Történelem", "Udvari etikett", "Úszás", "Vallásismeret"),

    "Varázsló": \
        ("Alkímia", "Démonológia", "Drágakőmágia", "Élettan", "Építészet",
         "Heraldika", "Herbalizmus", "Írás/olvasás", "Kultúra", "Legendaismeret",
         "Lélektan", "Magas mágia", "Nekromancia", "Nyelvtudás", "Orvoslás",
         "Őselemi mágia", "Ősi nyelv", "Politika/diplomácia", "Pszi", "Rúnamágia",
         "Történelem", "Szakma", "Számtan/mértan", "Udvari etikett")
}

oktatas_bonuszok["Amazon"] = oktatas_bonuszok["Egyéb harcos"]

oktatas_bonuszok["Barbár"] = []
for kepz in list(kepzettsegek["Harci"].keys()) + \
        list(kepzettsegek["Világi"].keys()):
    if kepz[0] == "!":
        kepz = kepz[1:]
    oktatas_bonuszok["Barbár"].append(kepz)

oktatas_bonuszok["Kardművész"] = oktatas_bonuszok["Harcművész"]

faji_kepzettseg_elonyok = \
    {
        "Elf": ("Állatismeret", "Idomítás", "Vadonjárás", "Lovaglás", 4),
        "Félelf": ("Állatismeret", "Idomítás", "Vadonjárás", "Lovaglás", 3),
        "Udvari ork": ("Építészet", 0),
        "Törpe": ("Építészet", "Térképészet", "Mechanika", "Művészet", "Szakma", 4),
        "Kyr származék": [],
        "Ember": ("Építészet", 0)
    }

for kepz in kepzettsegek["Szociális"].keys():
    if kepz[0] == "!": kepz = kepz[1:]
    faji_kepzettseg_elonyok["Kyr származék"].append(kepz)
faji_kepzettseg_elonyok["Kyr származék"].append(4)
