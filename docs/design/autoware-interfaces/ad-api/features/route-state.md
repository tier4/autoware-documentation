# Route

## Related API

- {{ adapi("/api/v1/route/state") }}
- {{ adapi("/api/v1/route/clear") }}
- {{ adapi("/api/v1/route/set") }}
- {{ adapi("/api/v1/route/data") }}
- {{ adapi("/api/v1/route/lanelet/set") }}
- {{ adapi("/api/v1/route/lanelet/data") }}

## Route State

ルートに関する状態遷移。目的地へのルートが設定されているかを管理する。

![route-state](./route-state.drawio.svg)

| State    | Description                                        |
| -------- | -------------------------------------------------- |
| UNSET    | ルートが設定されていない状態。                     |
| SET      | ルートを設定されている状態。                       |
| CHANGING | ルートを走りながら別のルートを切り替えている状態。 |
| ARRIVE   | ルートの終点まで到着した状態。                     |
