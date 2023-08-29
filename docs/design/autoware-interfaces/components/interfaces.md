# Interfaces

## Overview

インターフェース変更により意図せずAutowareや周辺ツールが動かなくなってしまうのを防ぐため、下記の条件に該当するインターフェースを更新する際は slack にて通知を行い関係者と対応方針を相談してください。

- [autoware_msgs](https://github.com/autowarefoundation/autoware_msgs) や [autoware_auto_msgs](https://github.com/tier4/autoware_auto_msgs) に依存するインターフェース
- このページに記載されたインターフェース

内部で使用される [tier4_autoware_msgs](https://github.com/tier4/tier4_autoware_msgs) などのインターフェースに依存がある場合、通知が必要性を明示するため、このページにインターフェースを追加する PR を作成してください。インターフェースの提供者はレビューを行い、そのインターフェースを外部から使用して問題ないか判断してください。

- 公開インターフェースは [autoware_msgs](https://github.com/autowarefoundation/autoware_msgs) に配置するのが望ましいため、適宜移行してください。
- 逆に非公開のインターフェースは [autoware_msgs](https://github.com/autowarefoundation/autoware_msgs) や [autoware_auto_msgs](https://github.com/tier4/autoware_auto_msgs) に配置しないでください。

## Topics and services

| Name | Description |
| ---- | ----------- |

## System files

| Path                         | Description          |
| ---------------------------- | -------------------- |
| lanelet2_map.osm             | レーンレット         |
| pointcloud_map.pcd           | 点群地図             |
| pointcloud_map_metadata.yaml | 点群地図のメタデータ |
| map_projector_info.yaml      | 地図の射影情報       |

## Parameter files

| Path | Description |
| ---- | ----------- |
