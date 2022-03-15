# Route State

## Route Set State

ルートに関する状態遷移。目的地へのルートが設定されているかを管理する。

![route-set-state](./route-set-state.drawio.svg)

| State    | Description                                        |
| -------- | -------------------------------------------------- |
| Unset    | ルートが設定されていない状態。                     |
| Set      | ルートを設定されている状態。                       |
| Changing | ルートを走りながら別のルートを切り替えている状態。 |

## Route Goal State

目的地に関する状態遷移。ルートが設定されている場合に有効になる。<br>
※Route State (Set, Changing) のサブ状態にすることも検討する。

![route-goal-state](./route-goal-state.drawio.svg)

| State        | Description                    |
| ------------ | ------------------------------ |
| On The Way   | ルートを走行している状態。     |
| Arrive Soon  | ルートの終点に近づいた状態。   |
| Arrived Goal | ルートの終点まで到着した状態。 |
