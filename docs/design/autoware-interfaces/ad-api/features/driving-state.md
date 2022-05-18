# Driving State

## Description

The driving state shows whether the vehicle is driving or can start driving. The vehicle holds a stop when the state is not DRIVING.
This state is mainly used to implement a departure button.

The state changes depending on each state of the vehicle and becomes READY when it is ready to start driving.
Then, when the service to engage is called, the state becomes DRIVING and the vehicle starts driving.
Finally, when the vehicle arrives at the destination, the state returns to NOT_READY and it is checked for READY.
The state can be manually returned to NOT_READY by calling service to disengage.

![driving-state](./driving-state.drawio.svg)

| State     | Description                                       |
| --------- | ------------------------------------------------- |
| NOT_READY | The vehicle cannot start driving for some reason. |
| READY     | The vehicle is ready to start driving             |
| DRIVING   | The vehicle is driving toward the destination.    |

## Related API

- /api/driving/state
- /api/driving/engage
