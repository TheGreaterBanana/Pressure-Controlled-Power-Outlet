# Pressure-Controlled-Power-Outlet
This is my (for sure) late Birthday present for my mom:

The idea for this project is that she have a water bin that holds water off of the roof of her house. Which my mother uses to water her gardens. The problem is that the pump she uses does not stop when the pressure starts to build!

So this is ment to fix this by using a water pressure sensor to see when the hose nozzel is closed by detecting a large jump in pressure then disablling the outlet that is powering the pump. Then when the nozzel is opened again this will detect the drop in pressure and re-enable the outlet.

This respository will have the code for the pico (RP2040) microcontroller, the schematics for the PCB and the case that will be used. 

The design philosophy for this project is to have everything as simple and cheap as possible, for this as many components as possible will be through hole as I dont want to pay to have parts placed on the pcb. If a part has to be surface mount it will have a extra large footprint to make it as easy as possible to assemble.

The specs:
    - 125V
    - 20A
    - GFCI protected outlets
    - Useable outdoors



