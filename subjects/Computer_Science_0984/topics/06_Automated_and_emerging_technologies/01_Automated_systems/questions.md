# 6.1 Automated systems — practice

Cambridge IGCSE (9–1) Computer Science 0984 · points 6.1.1–6.1.2 · Paper 1

No past papers are stored in `me/papers/Computer_Science_0984/` yet. The marking guidance below
is written for this repository and is **not an official Cambridge mark scheme**.

## Questions

1. State what is meant by an automated system. **[2]**
2. State the role of each of these in an automated system: (a) sensor (b) microprocessor
   (c) actuator. **[3]**
3. A greenhouse keeps the soil moist automatically. Describe how sensors, a microprocessor and
   actuators are used to do this. **[6]**
4. A car has adaptive cruise control that keeps a safe distance from the vehicle in front.
   Describe how the system works. **[5]**
5. An office switches its lights on only when it is dark and someone is in the room. Identify
   **two** sensors the system uses and give **one** advantage and **one** disadvantage of the
   system. **[4]**
6. A chemical factory uses an automated system to control a reaction vessel. Describe **two**
   advantages and **two** disadvantages of using the automated system instead of human
   operators. **[4]**
7. Automated weather stations are placed on remote mountains. Explain **two** reasons for using an
   automated system here. **[4]**
8. A laboratory runs an experiment automatically. Explain why the results are more reliable than
   when a technician runs it. **[2]**
9. A game console controller contains an accelerometer and a vibration motor. Describe how these
   are used, with the console's microprocessor, when the player tilts the controller. **[3]**

## Marking guidance

1. Hardware and software working together (1) to carry out a task without human intervention (1).
2. (a) measures a physical property / takes readings and sends them to the microprocessor (1)
   (b) compares readings with stored values and decides what action to take / sends signals (1)
   (c) receives a signal and produces physical movement, e.g. switches a pump / opens a valve (1).
3. One mark per point, max 6: moisture sensor measures soil moisture; data converted by ADC
   (if analogue); microprocessor compares reading with stored / preset value; if below value,
   microprocessor sends signal to actuator; actuator switches on water pump / opens valve (sprinkler);
   if at or above value, pump switched off / no action; process repeats continuously.
4. One mark per point, max 5: proximity (distance) sensors in the bumper send signals; readings sent
   to microprocessor; microprocessor calculates the distance to the vehicle in front; compares with
   stored safe distance; if too close, signal sent to actuators to apply brakes / reduce throttle;
   if distance safe and speed below set speed, actuators increase throttle; repeats continuously.
5. Light sensor (1); infra-red / motion sensor (1). Advantage, e.g. lights only on when needed so
   less energy used / longer bulb life (1). Disadvantage, e.g. a person sitting still may not be
   detected and the lights go off / expensive to install (1).
6. Advantages (1 each, max 2): reacts faster to dangerous changes; workers kept away from the
   hazardous process; runs 24/7; keeps optimum conditions / consistent product; lower staff costs.
   Disadvantages (1 each, max 2): expensive to set up / maintain; cannot cope with unforeseen
   conditions (safety risk); faulty sensor gives wrong data; can be hacked; job losses.
7. Two reasons, 2 marks each (reason + expansion): no staff need to travel to / stay in a dangerous,
   remote location (1) so no risk to people / lower costs (1); readings are taken 24/7 at fixed
   intervals (1) so there is a continuous, complete record (1).
8. Every run is carried out in exactly the same way / at the same time intervals (1), so results
   are consistent and repeatable; no human reading or timing errors (1).
9. Accelerometer measures the tilt / movement of the controller (1); microprocessor processes the
   reading and updates the game (1); microprocessor sends a signal to the vibration motor
   (actuator) to give feedback to the player (1).
