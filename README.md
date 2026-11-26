## Štruktúra projektu

~/robot/<br>
├── main.py                  # spúšťač: vyberie režim (sim / real)<br>
├── config.py                # rozmery bunky, rýchlosti, porty, prahy<br>
├── interfaces/<br>
│   ├── base.py  # abstraktné rozhranie robota<br>
│   ├── webots_robot.py      # implementácia pre simuláciu<br>
│   └── teensy_robot.py      # implementácia cez serial (neskôr)<br>
├── core/                    # čistý Python, bez hardvéru<br>
│   ├── maze_map.py          # mriežka, steny, navštívené bunky<br>
│   ├── localization.py      # pozícia (x, y) a smer N/E/S/W<br>
│   ├── explorer.py          # DFS + backtracking<br>
│   └── pathfinder.py        # BFS / A*<br>
├── vision/<br>
│   └── smiley.py            # rozpoznanie smajlíkov<br>
├── comms/<br>
│   └── protocol.py          # formát správ Pi ↔ Teensy<br>
├── telemetry/<br>
│   └── logger.py            # logy, export mapy<br>
├── tests/                   # testy core/ bez simulátora<br>
└── firmware/                # kód pre Teensy (PlatformIO)<br>