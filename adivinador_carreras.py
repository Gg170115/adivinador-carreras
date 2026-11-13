tickets=[
    ("1", {"Interes_Negocios", "Gusto_Numeros"}),
    ("2", {"Interes_Negocios", "Gusto_Organizacion"}),
    ("3", {"Interes_Tecnologia", "Gusto_Proyectos_Software"}),
    ("4", {"Interes_Tecnologia", "Gusto_Sistemas"}),
    ("5", {"Interes_Mecanica", "Gusto_Robots"}),
    ("6", {"Interes_Mecanica", "Gusto_Electricidad"}),
    ("7", {"Interes_Mecanica", "Gusto_Maquinas"}),
    ("8", {"Interes_Quimica", "Gusto_Alimentos"}),
    ("9", {"Interes_Quimica", "Gusto_Laboratorio"}),
]
reglas = [
    {
        "id": "R1",
        "prioridad": 70,
        "necesita": {"Interes_Negocios"},
        "prohibe" : set(),
        "agrega": {"Area_Negocios"},
        "quita": set(),
    },
    {
        "id": "R2",
        "prioridad": 70,
        "necesita": {"Interes_Tecnologia"},
        "prohibe" : set(),
        "agrega": {"Area_Ingenieria"},
        "quita": set(),
    },
    {
        "id": "R3",
        "prioridad": 70,
        "necesita": {"Interes_Mecanica"},
        "prohibe": set(),
        "agrega": {"Area_Mecanica"},
        "quita": set(),
    },
    {
        "id": "R4",
        "prioridad": 70,
        "necesita": {"Interes_Quimica"},
        "prohibe": set(),
        "agrega": {"Area_Quimica"},
        "quita": set(),
    },
    {
        "id": "R5",
        "prioridad": 60,
        "necesita": {"Area_Negocios", "Gusto_Numeros"},
        "prohibe": set(),
        "agrega": {"Carrera: Contador Publico"},
        "quita": set(),
    },
    {
        "id": "R6",
        "prioridad": 60,
        "necesita": {"Area_Negocios", "Gusto_Organizacion"},
        "prohibe": set(),
        "agrega": {"Carrera: Administracion de empresas"},
        "quita": set(),
    },
    {
        "id": "R7",
        "prioridad": 60,
        "necesita": {"Area_Ingenieria", "Gusto_Proyectos_Software"},
        "prohibe": set(),
        "agrega": {"Carrera: Ingenieria Informatica"},
        "quita": set(),
    },
    {
        "id": "R8",
        "prioridad": 60,
        "necesita": {"Area_Ingenieria", "Gusto_Sistemas"},
        "prohibe": set(),
        "agrega": {"Carrera: Ingenieria Sistemas Computacionales"},
        "quita": set(),
    },
    {
        "id": "R9",
        "prioridad": 60,
        "necesita": {"Area_Mecanica", "Gusto_Robots"},
        "prohibe": set(),
        "agrega": {"Carrera: Ingenieria Mecatronica"},
        "quita": set(),
    },
    {
        "id": "R10",
        "prioridad": 60,
        "necesita": {"Area_Mecanica", "Gusto_Electricidad"},
        "prohibe": set(),
        "agrega": {"Carrera: Ingenieria Electrica"},
        "quita": set(),
    },
    {
        "id": "R11",
        "prioridad": 60,
        "necesita": {"Area_Mecanica", "Gusto_Maquinas"},
        "prohibe": set(),
        "agrega": {"Carrera: Ingenieria Mecanica"},
        "quita": set(),
    },
    {
        "id": "R12",
        "prioridad": 60,
        "necesita": {"Area_Quimica", "Gusto_Alimentos"},
        "prohibe": set(),
        "agrega": {"Carrera: Ingenieria en industrias alimentarias"},
        "quita": set(),
    },
    {
        "id": "R13",
        "prioridad": 60,
        "necesita": {"Area_Quimica", "Gusto_Laboratorio"},
        "prohibe": set(),
        "agrega": {"Carrera: Ingenieria Quimica"},
        "quita": set(),
    },
]

for nombreticket, hechosiniciales in tickets:
    hechos = hechosiniciales.copy()
    usadas = set()
    traza = []

    while True:
        disponibles = []
        for regla in reglas:
            if (regla["id"] not in usadas
                    and regla["necesita"].issubset(hechos)
                    and not (regla["prohibe"] & hechos)):
                disponibles.append(regla)

        if not disponibles:
            break

        regla = disponibles[0]
        for otra in disponibles:
            if otra["prioridad"] > regla["prioridad"]:
                regla = otra

        hechos.update(regla["agrega"])
        hechos.difference_update(regla["quita"])
        usadas.add(regla["id"])
        traza.append(regla["id"] + " -> " + str(regla["agrega"]))

    carrera = "No se encontro una carrera"
    for hecho in hechos:
        if hecho.startswith("Carrera:"):
            carrera = hecho[9:]

    print("CARRERA RECOMENDADA:", carrera)
    print("REGLAS DISPARADAS:", " -> ".join(traza))


