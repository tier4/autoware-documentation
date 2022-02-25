# Autoware States

## Power State

システムの起動と終了に関する状態を管理する。

![power-state](./power.drawio.svg)

| State     | Description  |
| --------- | ------------ |
| Start Up  | 起動処理中   |
| Power On  | 起動処理完了 |
| Shut Down | 終了処理中   |
| Power Off | 終了処理完了 |

## Driving State

車両の走行に関わる状態を管理する。他の状態遷移を参照している。

![driving-state](./driving.drawio.svg)

| State     | Description                                                                  |
| --------- | ---------------------------------------------------------------------------- |
| Preparing | ルートの待ち、ドアの開閉中、自己位置初期化中などの発車条件を満たさない状態。 |
| Ready     | 発車条件を満たしており、ユーザーからの承認操作を待っている状態。             |
| Driving   | 目的地に向かって走行している状態。                                           |

## Operation Mode

車両の制御モード。

![operation-mode](./operation-mode.drawio.svg)

| State      | Description |
| ---------- | ----------- |
| Direct     | 直接操作    |
| Stop       | 停止保持    |
| Autonomous | 自律制御    |
| Local      | 近接操作    |
| Remote     | 遠隔操作    |

## Route State

ルートに関する状態遷移。目的地へのルートが設定されているかを管理する。

![route-state](./route.drawio.svg)

| State    | Description                                        |
| -------- | -------------------------------------------------- |
| Unset    | ルートが設定されていない状態。                     |
| Set      | ルートを設定されている状態。                       |
| Arrived  | ルートの終点まで到着した状態。                     |
| Changing | ルートを走りながら別のルートを切り替えている状態。 |

## Localization State

位置推定に関する状態遷移。車両の位置を推定されているかを管理する。

![localization-state](./localization.drawio.svg)

| State        | Description                                                        |
| ------------ | ------------------------------------------------------------------ |
|              | 自己位置が未推定、もしくは、何らかの原因で信頼できなくなった状態。 |
| Initializing | 自己位置を推定している状態。                                       |
|              | 自己位置が推定できている状態。                                     |
