# Research

I am interested in how systems composed of non-equilibrium elements exhibit collective phenomena. Examples include granular systems, where particle sizes are large and thermal relaxation is negligible, and active matter systems, where particles consume energy and self-propel.

Currently, I conduct experiments with bacteria and colloidal systems to measure the response of orientational order under applied magnetic fields in active matter.

## Skills I Believe I Have

I designed and built experimental setups to apply magnetic fields to active systems and observe their behavior. Through this work, I developed skills in the following areas.

### Camera Systems

- I wrote code to control USB cameras (GenICam) and high-speed imaging cameras (FASTCAM). These are operated in synchronization with the coil-related devices described below.
- The former was implemented in Python, and the latter in C++.

### Coil Design and Fabrication

- I designed and built coils to apply magnetic fields to samples for microscopic observation.
- In practice, this requires balancing trade-offs: air-core coils are used to produce a uniform field, while strong fields are also needed. Simply increasing coil turns or current can exceed power-supply limits or overheat and damage the coil.
- To address this, I modeled coil heating and cooling (thermal diffusion) and designed coils that can generate sufficiently strong fields within power-supply specifications without burning out.

### Coil Control

- This research requires applying magnetic fields to samples while simultaneously observing samples and monitoring magnetic-field output. I developed control code to perform these operations.
- Devices (coil power supplies and data loggers that monitor coil output) are controlled via SCPI and VISA communication.
- I also implemented parallel control with the cameras so each device can run concurrently. (This is actually quite tricky due to VISA-related constraints.) This enabled the measurement experiments described above.