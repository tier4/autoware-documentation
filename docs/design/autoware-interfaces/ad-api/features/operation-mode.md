# Operation Mode

## Description

This feature manages the operator of the vehicle. The operation modes are roughly classified into manual, transition, and autonomous.
Since Autoware may not be able to guarantee safety, such as switching to autonomous mode during overspeed, it changes to transition mode before autonomous mode.
During the transition mode, the previous operator should ensure safety. If Autoware succeeds in taking over, the mode changes to autonomous.

The manual mode is direct, none, local or remote.
Autoware does not guarantee safety in these modes unless it is stopped by none mode.
Direct mode is supported on some vehicles that have an interface to operate directly, such as steering and pedals, etc.
None mode is used to stop the vehicle when the operator is temporarily absent due to a change of operator.
In local and remote modes, Autoware controls the vehicle based on commands from the operator.

![operation-mode](./operation-mode.drawio.svg)

| State      | Description                                                                                                        |
| ---------- | ------------------------------------------------------------------------------------------------------------------ |
| DIRECT     | The vehicle is operated directly without Autoware. This mode is only available on some vehicles.                   |
| NONE       | The vehicle is not operated by anyone. Autoware controls the vehicle to hold a stop.                               |
| LOCAL      | The vehicle is operated by the local operator. Autoware controls the vehicle based on commands from the operator.  |
| REMOTE     | The vehicle is operated by the remote operator. Autoware controls the vehicle based on commands from the operator. |
| AUTONOMOUS | The vehicle is operated autonomously. Autoware controls the vehicle.                                               |
| TRANSITION | The vehicle is operated autonomously. Autoware is trying to take over the operation of the vehicle.                |
