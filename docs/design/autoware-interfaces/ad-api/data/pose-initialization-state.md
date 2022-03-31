# Pose Initialization State

自己位置の初期化に関する状態遷移。

![pose-initialization-state](./pose-initialization-state.drawio.svg)

| State        | Description                      |
| ------------ | -------------------------------- |
| WAITING      | 自己位置の初期化が可能な状態。   |
| INITIALIZING | 自己位置を初期化している状態。   |
| REJECTING    | 自己位置が初期化ができない状態。 |
