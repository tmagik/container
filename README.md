# MIND::Container

(Machine Intelligence Next Derivative)
This is an SCAD file to model and develop a containerized building block
for a supercomputer system capable of scaling to at least 1GW of renewable
energy input power.

See the file Container.md for the original source and documentation.

##
One of the working concept designs for the MIND::container consists of 
504 containers with free-air cooling via the fan/radiator cutouts on the 
left and right sides.

Based on the radiator dimensions of 1MW diesel gensets, which are 
likely to require well over 2MW of heat rejection at full load, it
is believed a 1.5M square radiator opening on both sides will be sufficient
for cooling. Internally there may be heat pumps to get sufficient delta-T
vs traditional data center 'dry coolers' which are generally larger.

Compute is mounted to the rear of the container, in two nominally standard
42U racks. Primary network access ports for fiber or other network interconnect
will be ported to access panels on the rear of the container, with power and
cooling routed toward the openable doors on the end. Design goals are for a
maintenance access path to the rear.

Gen1 containers will use 12KV to 35KV nominal 3-phase AC power, for a nominal
container fuse rating of 100 amps at 7200 phase-to-neutral voltage. 

Dual-feed (left and right side) container options will use 50amps at 7200 P-N,
with a left and right transformer feeding into a common DC bus, which may
optionally include energy storage components.

Transformers may optional be mounted externally to containers, with left and
right side power feeds of one of the following intermediate voltage categories:
 * Low-voltage interemediate
     * 380/416VDC (loaded/idle)
     * 208/120VAC (Delta)
     * 240VAC (Delta)
 * Medium voltage intermediate
     * 768/832VDC (loaded/idle)
     * 600/346VAC (Delta)

With external transformers, power feed cables (multiple conductors per phase)
will support a maximum of 1500 amps with appropriate transformer or inline fusing
to limit current. At the 208/120VAC power option, this derates the container to
540 KW per container with a single feed, and 1MW with dual left/right feeds.

Container doors SHALL be interlocked with a minimum of 2 redundant magnetic locks
to prevent opening the doors when power is supplied to either transformer on any
combination of phases. Maglocks may be supplied by multiple isolated 12 or 24VDC
power supplies with a passive diode-OR bridge.

Transformers and/or DC power systems shall be floating-ground isolated systems.
Each container will have a DC-side isolation monitoring and ground-fault detection
system similiar to those used on EV charging systems.





## IP Patent disclosure
This work is a derivative of the [Q3ube](http://7el.us/q3),
[7 Elements LED weeder](https://github.com/tmagik/DEW/blob/master/patent/US11690369.pdf)
and [DEW](https://github.com/tmagik/DEW) IP patent portfolio. Please be
aware that there may be unpublished or pending patents. You are free to join
the Q3ube collective to use, share, and remix this work provided you continue
to follow the collective author's intent to share alike.

Commerical licensing exceptions may also be available for a fee, as this
helps us continue to develop and release new content for the betterment of
all thinking entities.

* Additional Features:
    * system-wide water cooling and heat reacovery
    * renewable energy integration
    * ethanol distillation
    * greenhouse heating
    * residential combined heat and power
    * Butterfly/Dragonfly/etc cluster interconnect
    * 48V power distribution to compute boards

## Prerequisites

This should work with any recent version of
[OpenSCAD](https://www.openscad.org).

# Author and license

(C) 2025 by 7 Elements LLC and Troy Benjegerdes (tmagik)

(C) 2019 by Philipp Reichmuth (phrxmd)

This work is licensed under the [AGPLv3.0 license](https://www.gnu.org/licenses/agpl-3.0.en.html).

# Acknowledgement

The parametric\_container.scad file was derived from
[phrxmd](https://github.com/phrxmd/container), which was in turn derived from
[gundyboyz](https://www.thingiverse.com/gundyboyz/about)' Parametric
Shipping Container model published on
[Thingiverse](https://www.thingiverse.com/thing:1392128) under a
Creative Commons Attribution 3.0 Unported license.
