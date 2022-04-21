# Route

## Related API

- /api/v0/route/state
- /api/v0/route/clear
- /api/v0/route/set
- /api/v0/route/data
- /api/v0/route/lanelet/set
- /api/v0/route/lanelet/data

## Route State

ルートに関する状態遷移。目的地へのルートが設定されているかを管理する。

![route-state](./route-state.drawio.svg)

| State    | Description                                        |
| -------- | -------------------------------------------------- |
| UNSET    | ルートが設定されていない状態。                     |
| SET      | ルートを設定されている状態。                       |
| CHANGING | ルートを走りながら別のルートを切り替えている状態。 |
| ARRIVED  | ルートの終点まで到着した状態。                     |
