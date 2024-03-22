# /api/external/set/rosbag_record

## Classification

- Behavior: Service
- DataType: tier4_external_api_msgs/srv/SetRosbagRecord

## Description

rosbag 記録の開始/停止を行う。

| Mode     | record |
| -------- | -------|
| 記録開始 | false  |
| 記録停止 | true   |

## Requirement

現在の rosbag record 動作モード(`recording_type`)が「手動記録」(`manual`)の時で、本サービスリスエクストを受信した時は、rosbag 記録の開始または停止を行うこと。

## Remarks

`recording_type`の変更方法

`/etc/autoware_logging_suite/logpacker/logpacker_config.yaml`<br>
`recording_type`の部分を変更する。設定可能な値は、`manual`, `auto`である。

```yaml
rosbag:
  # If you use another file for rosbag configuration, define its file path. When not defined, this file will be used.
  # params_file: "{{ logpacker_config_dir }}/rosbag_params.yaml"
  recording_type: "manual"
```
