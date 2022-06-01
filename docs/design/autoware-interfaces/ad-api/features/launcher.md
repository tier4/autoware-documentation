# Launcher API

## Launcher State

![launcher-state](./launcher-state.drawio.svg)

| State       | Description                                                                             |
| ----------- | --------------------------------------------------------------------------------------- |
| READY       | Autoware は起動していません。バージョンの変更やファイルの更新などを行うことができます。 |
| NOT_READY   | Autoware のバージョン変更やファイルの更新、再起動などを行っています。                   |
| RUNNING     | Autoware が起動しています。起動中の詳細な状態は各種ステートを参照してください。         |
| TERMINATING | Autoware を終了しています。                                                             |

## Sequence

## Related API

- /api/launcher/state
- /api/launcher/request
