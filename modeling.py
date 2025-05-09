#!/usr/bin/env python3
#
# Copyright 2025 7 Elementts LLC, Troy Benjegerdes, and the q3ube project
#
# SPDX-License-Identifier: AGPL-3.0-or-later
#
# https://www.gnu.org/licenses/agpl-3.0.txt
# http://7el.us/q3/patent/agpl-3.0.tex
 
LICENSE = '''
    This design specification (the program) and it's derivative work output are
    free software: you can redistribute it and/or modify the program or design
    under the terms of the GNU Affero General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU Affero General Public License for more details.

    You should have received a copy of the GNU Affero General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.

    Commercial GPL exception licenses are available for use of this program
    and it's derivative work designs from 7 Elements LLC and authorized 
    resellers. We encourage and support use of this design in commercial
    and proprietary projects that give back to the communities they have in
    turn benefitted from. Contact a member of the Q3ube collective for more
    details and commercial licensing terms.
'''

import math


# Measurements of shipping container (in meters)
# Shipping container size (external)
EXT_LENGTH = 6.06       # Standard lengths: 6.06 for 20', 12.19 for 40'
EXT_WIDTH  = 2.44       # Standard width:   2.44
EXT_HEIGHT = 2.59       # Standard heights: 2.59 or 2.90 for High Cube

#EXT_SPACING = 0.028     # Conex stack pin height
EXT_SPACING = 0.110     # slide in/out rail spacing height


SIDES = 12
#HEIGHT = 11
HEIGHT = 7
CLUSTERS = 6
BH_W = 300 
BATT_V = 12.8 # battery volts
C_BATT_COUNT = 30
RACK_U = 42
RACK_V = BATT_V * C_BATT_COUNT # 380  # VDC for rack power bus
BOARD_X = 9
BOARD_Y = 9
BOARD_CHIPS = BOARD_X * BOARD_Y
BOARD_MEM_W = BOARD_CHIPS * 8 * 2.5
BOARD_W = BOARD_CHIPS * BH_W
RACK_A = RACK_U * BOARD_W / RACK_V
RACK_MW = RACK_A * RACK_V / 1e6
RACK_MEM_A = RACK_U * BOARD_MEM_W / RACK_V
RACK_MEM_MW = RACK_MEM_A * RACK_V / 1e6
TALL = HEIGHT * (EXT_HEIGHT + EXT_SPACING)
TALL_FT = TALL * 3.28084
C = 299792458 # speed of light
FIBERC = C * 2/3    # propaga

print(LICENSE)

print(f"per container: total full load {2*RACK_MW:.2f}MW ({2*RACK_A:.0f}A)")
print(f"  -> dram idle %.2fMW (%.1fA @ %dV)" % ( RACK_MEM_MW * 2, RACK_MEM_A * 2, RACK_V))

BATT_AH = 300
FL_DERATE = 0.5   # derating factor for full load ride-through
C_RUNTIME_S = 3600 * FL_DERATE * BATT_AH / (RACK_A * 2)
C_MEM_RUNTIME = BATT_AH / (RACK_MEM_A * 2)
BATT_COST = 500 # dollars
BATT_KG = 25
C_BATT_COST = C_BATT_COUNT * BATT_COST
C_BATT_KG = C_BATT_COUNT * BATT_KG

BOARD_COST = BOARD_CHIPS * 1000 # fudge factor from P150 $1399
C_BOARD_COST_M = 2 * RACK_U * BOARD_COST / 1e6

C_BATT_COUNT = RACK_V / BATT_V
C_BATT_KWH = RACK_V * BATT_AH / 1000

print(f"Board cost with {BOARD_CHIPS} chips ${BOARD_COST}")
print(f"Container with {C_BATT_COUNT:.0f}x{BATT_AH}AH battery ({C_BATT_KWH:.0f}KWH)")
print(f"  -> DRAM idle runtime: {C_MEM_RUNTIME:.2f} hours")
print(f"  -> Full load ride-through: {C_RUNTIME_S:.0f} seconds with derating factor of {FL_DERATE:.2f}")
print(f"  -> Battery cost: ${C_BATT_COST} weight: {C_BATT_KG}kg")
print(f"  -> Compute cost: ${C_BOARD_COST_M}M")

print("")

for SIDES in [6,12,24]:

    containers = SIDES * CLUSTERS * HEIGHT
    mw = containers * 2 * RACK_MW
    dram = containers * 2 * RACK_MEM_MW
    compute_cost = containers * C_BOARD_COST_M
    print(f"{containers} containers, ${compute_cost:.0f}M")
    print(f"  -- {TALL:.1f}m tall, ({TALL_FT:.0f}ft) total {mw:.0f}MW dram idle {dram:.2f}MW")

    inr = EXT_WIDTH / ( 2 * math.tan (math.pi / SIDES)) # inradius

    cir = EXT_WIDTH / ( 2 * math.sin (math.pi / SIDES)) # circumradius


    print(f"  -- Polygon with {SIDES} has Inradius {inr:.2f}m and "
      f"circumradious {cir:.2f}m")

    # Big hex of 6 of the above, spaced to open both doors
    bighex_s = inr + EXT_LENGTH + EXT_WIDTH + EXT_LENGTH + inr

    bighex_inr = bighex_s / ( 2 * math.tan (math.pi / CLUSTERS))
    bighex_cir = bighex_s / ( 2 * math.sin (math.pi / CLUSTERS))

    #print(bighex_inr, bighex_cir)

    maxcable = (
        HEIGHT * (EXT_HEIGHT + EXT_SPACING) + 2 * (inr + bighex_inr) )

    ns = 1e9 * maxcable/FIBERC
    print(f"  -- max cable length {maxcable:.1f}m, with {ns:.0f}ns fiber latency")
