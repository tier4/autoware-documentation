# /api/autoware/get/rosbag_record

## Classification

- Behavior: Topic
- DataType: tier4_external_api_msgs/msg/RosbagRecordStatus

## Description

rosbag 記録状態を取得する。

| Mode                            | status                  |
| ------------------------------- | ----------------------- |
| 初期化中                        | 0: INITIALIZING         |
| 車両情報受信待ち                | 1: WAITING_VEHICLE_INFO |
| rosbag record開始条件の成立待ち | 2: READY                |
| rosbag record動作中             | 3: RECORDING            |
| エラー発生中                    | 4: ERROR                |

## Requirement

現在のrosbag 記録状態を提供すること。

## Remarks

エラー発生中(4: ERROR)となる条件

- 設定が不正の時
- disk容量が足りない
- rosbag record中にディスクが接続されてない状態になった時(書き込み先のフォルダが存在しない）
