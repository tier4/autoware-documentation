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

## Fail Safe State

車両の異常に関わる状態を管理する。

![fail-safe-state](./fail-safe.drawio.svg)

| State            | Description                              |
| ---------------- | ---------------------------------------- |
| Normal           | 正常状態                                 |
| Takeover Request | 正常だが異常の可能性が高くなっている状態 |
| MRM Operating    | 異常があり MRM を動作させている状態      |
| MRM Succeeded    | 異常があり MRM が成功した状態            |
| MRM Failed       | 異常があり MRM が失敗した状態            |

## Moving State

車両の速度に関する状態遷移。

![moving-state](./moving.drawio.svg)

| State        | Description        |
| ------------ | ------------------ |
| Stopped      | 停止中             |
| Starting     | 発車確認中         |
| Moving       | 移動中             |
| Decelerating | 停止に向けて減速中 |

## Localization State

位置推定に関する状態遷移。車両の位置を推定されているかを管理する。

![localization-state](./localization.drawio.svg)

| State        | Description                                                        |
| ------------ | ------------------------------------------------------------------ |
| Uncertain    | 自己位置が未推定、もしくは、何らかの原因で信頼できなくなった状態。 |
| Initializing | 自己位置を推定している状態。                                       |
| Estimated    | 自己位置が推定できている状態。                                     |

## Vehicle Info

| Name          | Type  | Description      |
| ------------- | ----- | ---------------- |
| position      | Twist | 位置、角度       |
| velocity      | Twist | 速度、角速度     |
| acceleration  | Twist | 加速度、角加速度 |
| blinker       | Enum  | ウィンカー       |
| hazard        | Enum  | ハザード         |
| gear          | Enum  | ギア             |
| fuel.value    | float | 燃料（残量）     |
| fuel.capacity | float | 燃料（最大）     |
