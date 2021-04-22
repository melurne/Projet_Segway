v 20200319 2
C 40000 40000 0 0 0 title-B.sym
C 45500 41600 1 0 0 connector20-2.sym
{
T 47200 50200 5 10 1 1 0 6 1
refdes=raspberry
T 45900 50150 5 10 0 0 0 0 1
device=CONNECTOR_20
T 45900 50350 5 10 0 0 0 0 1
footprint=SIP20N
}
C 47100 41600 1 0 1 connector20-2.sym
{
T 46300 50200 5 10 0 1 0 0 1
refdes=CONN?
T 46700 50150 5 10 0 0 0 6 1
device=CONNECTOR_20
T 46700 50350 5 10 0 0 0 6 1
footprint=SIP20N
}
G 36300 40456 3186 10244 270 0 0
/home/maxence/Desktop/Projet_Segway/Datasheets/raspberry-pi-pinout.png
C 51500 50800 1 180 0 ground.sym
C 50200 46400 1 0 0 connector8-2.sym
{
T 50900 50000 5 10 1 1 0 6 1
refdes=Motor driver
T 50500 50050 5 10 0 0 0 0 1
device=CONNECTOR_8
T 50500 50250 5 10 0 0 0 0 1
footprint=SIP8N
}
C 50900 50300 1 270 0 connector2-2.sym
{
T 52200 49600 5 10 0 1 270 6 1
refdes=CONN?
T 52150 50000 5 10 0 0 270 0 1
device=CONNECTOR_2
T 52350 50000 5 10 0 0 270 0 1
footprint=SIP2N
}
C 52400 46800 1 0 1 connector6-2.sym
{
T 51700 49700 5 10 0 1 0 0 1
refdes=CONN?
T 52100 49650 5 10 0 0 0 6 1
device=CONNECTOR_6
T 52100 49850 5 10 0 0 0 6 1
footprint=SIP6N
}
B 50500 46400 1600 3600 3 10 1 0 -1 -1 0 -1 -1 -1 -1 -1
C 50200 41700 1 0 0 connector8-2.sym
{
T 50500 45350 5 10 0 0 0 0 1
device=CONNECTOR_8
T 50500 45550 5 10 0 0 0 0 1
footprint=SIP8N
T 50900 45400 5 10 1 1 0 6 1
refdes=Motor driver
}
C 50900 45600 1 270 0 connector2-2.sym
{
T 52200 44900 5 10 0 1 270 6 1
refdes=CONN?
T 52150 45300 5 10 0 0 270 0 1
device=CONNECTOR_2
T 52350 45300 5 10 0 0 270 0 1
footprint=SIP2N
}
C 52400 42100 1 0 1 connector6-2.sym
{
T 51700 45000 5 10 0 1 0 0 1
refdes=CONN?
T 52100 44950 5 10 0 0 0 6 1
device=CONNECTOR_6
T 52100 45150 5 10 0 0 0 6 1
footprint=SIP6N
}
B 50500 41700 1600 3600 3 10 1 0 -1 -1 0 -1 -1 -1 -1 -1
N 48900 44900 50200 44900 4
N 48900 41200 48900 49700 4
N 40700 41000 48600 41000 4
N 48600 41000 48600 49200 4
N 48600 44500 50200 44500 4
C 51500 50500 1 0 0 vcc-1.sym
N 51300 50500 51300 50300 4
N 51700 50500 51700 50300 4
C 51500 46100 1 180 0 ground.sym
C 51500 45800 1 0 0 vcc-1.sym
N 51300 45800 51300 45600 4
N 51700 45800 51700 45600 4
N 48600 49200 50200 49200 4
N 48900 49600 50200 49600 4
C 42100 44300 1 0 0 connector6-2.sym
{
T 42400 47150 5 10 0 0 0 0 1
device=CONNECTOR_6
T 42400 47350 5 10 0 0 0 0 1
footprint=SIP6N
}
C 43500 44300 1 0 1 connector6-2.sym
{
T 43200 47150 5 10 0 0 0 6 1
device=CONNECTOR_6
T 43200 47350 5 10 0 0 0 6 1
footprint=SIP6N
}
C 42400 47800 1 270 0 connector1-2.sym
{
T 43250 47500 5 10 0 0 270 0 1
device=CONNECTOR_1
T 43450 47500 5 10 0 0 270 0 1
footprint=SIP1N
}
C 43200 43600 1 90 0 connector1-2.sym
{
T 42350 43900 5 10 0 0 90 0 1
device=CONNECTOR_1
T 42150 43900 5 10 0 0 90 0 1
footprint=SIP1N
}
N 42800 47800 42800 48900 4
N 42800 48900 45600 48900 4
N 43500 46700 43500 49300 4
N 43500 49300 45600 49300 4
C 45400 50500 1 0 0 resistor-2.sym
{
T 45800 50850 5 10 0 0 0 0 1
device=RESISTOR
T 45600 50800 5 10 1 1 0 0 1
refdes=R
}
C 45400 49700 1 90 0 resistor-2.sym
{
T 45050 50100 5 10 0 0 90 0 1
device=RESISTOR
T 45100 49900 5 10 1 1 90 0 1
refdes=R
}
N 45300 49700 45600 49700 4
N 40700 41000 40700 50900 4
N 40700 50900 46300 50900 4
C 44800 49500 1 90 0 resistor-2.sym
{
T 44450 49900 5 10 0 0 90 0 1
device=RESISTOR
T 44500 49700 5 10 1 1 90 0 1
refdes=Rp
}
C 44300 49500 1 90 0 resistor-2.sym
{
T 43950 49900 5 10 0 0 90 0 1
device=RESISTOR
T 44000 49700 5 10 1 1 90 0 1
refdes=Rp
}
N 44700 49500 44700 49300 4
N 44200 49500 44200 48900 4
N 46300 50900 46300 50600 4
N 42100 50600 45400 50600 4
N 44700 50600 44700 50400 4
N 44200 50400 44200 50600 4
N 42100 46300 40700 46300 4
N 42100 45500 40700 45500 4
N 42100 45100 40700 45100 4
N 43500 46300 43900 46300 4
N 43900 46300 43900 41000 4
C 43700 40700 1 0 0 ground.sym
N 42100 46700 42100 50600 4
N 42100 47000 41800 47000 4
N 41800 47000 41800 43600 4
N 41800 43600 42800 43600 4
C 43300 42600 1 180 0 resistor-2.sym
{
T 42900 42250 5 10 0 0 180 0 1
device=RESISTOR
T 43100 42300 5 10 1 1 180 0 1
refdes=R
}
N 42400 42200 42400 42500 4
N 42400 42500 42100 42500 4
N 42100 42500 42100 44700 4
C 42500 41300 1 90 0 resistor-2.sym
{
T 42150 41700 5 10 0 0 90 0 1
device=RESISTOR
T 42200 41500 5 10 1 1 90 0 1
refdes=R
}
N 42400 41300 42400 41000 4
N 47000 49700 48900 49700 4
N 48900 41200 43300 41200 4
N 43300 41200 43300 42500 4
N 45600 42100 45400 42100 4
N 45400 42100 45400 41000 4
C 53400 48500 1 270 0 2phase-stepper-1.sym
{
T 55200 48300 5 10 0 0 270 0 1
device=2PHASE-STEPPER-4LEADS
T 55000 48500 5 10 1 1 270 0 1
refdes=stepper gauche
}
C 53400 43800 1 270 0 2phase-stepper-1.sym
{
T 55200 43600 5 10 0 0 270 0 1
device=2PHASE-STEPPER-4LEADS
T 55000 43800 5 10 1 1 270 0 1
refdes=stepper droit
}
N 52400 42500 53400 42500 4
N 53400 42700 52400 42700 4
N 52400 42700 52400 42900 4
N 53400 43300 52400 43300 4
N 53400 43500 52400 43500 4
N 52400 43500 52400 43700 4
N 53400 47200 52400 47200 4
N 53400 47400 52400 47400 4
N 52400 47400 52400 47600 4
N 53400 48000 52400 48000 4
N 53400 48200 52400 48200 4
N 52400 48200 52400 48400 4
N 47000 47700 48300 47700 4
N 48300 44100 48300 48800 4
N 48300 48800 50200 48800 4
N 50200 44100 48300 44100 4
N 45600 48500 45400 48500 4
N 45400 48500 45400 48700 4
N 45400 48700 49700 48700 4
N 49700 48700 49700 48400 4
N 49700 48400 50200 48400 4
N 45600 47700 45400 47700 4
N 45400 47700 45400 47900 4
N 45400 47900 49700 47900 4
N 49700 47900 49700 48000 4
N 49700 48000 50200 48000 4
N 45600 47300 45400 47300 4
N 45400 47300 45400 47500 4
N 45400 47500 49700 47500 4
N 49700 47500 49700 47200 4
N 49700 47200 50200 47200 4
N 45600 46900 45400 46900 4
N 45400 46900 45400 47100 4
N 45400 47100 49700 47100 4
N 49700 47100 49700 46800 4
N 49700 46800 50200 46800 4
N 45600 42500 45400 42500 4
N 45400 42500 45400 42700 4
N 45400 42700 49700 42700 4
N 49700 42700 49700 42100 4
N 49700 42100 50200 42100 4
N 45600 43300 45400 43300 4
N 45400 43300 45400 43100 4
N 45400 43100 49800 43100 4
N 49800 42500 49800 43100 4
N 49800 42500 50200 42500 4
N 45600 43700 45400 43700 4
N 45400 43700 45400 43900 4
N 45400 43900 47700 43900 4
N 47700 43900 47700 43300 4
N 47700 43300 50200 43300 4
N 45600 44100 45400 44100 4
N 45400 44100 45400 44300 4
N 45400 44300 47900 44300 4
N 47900 44300 47900 43700 4
N 47900 43700 50200 43700 4
T 43000 47600 5 10 1 0 0 0 1
Inclinometre
