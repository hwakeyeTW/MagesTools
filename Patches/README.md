# MAGES game localization modules

This tree contains game-specific localization module sources and maintenance metadata. Shared tooling such as EasyPatcher and MagesLib remains at repository level and is not vendored into each game.

User-facing documentation uses **module / 模組** for each complete fan-localization package. The existing `Patches/` directory name and technical terms such as patch data, `patch/berd/`, and EasyPatcher are retained as implementation terminology and stable repository paths.

## Layout

`Patches/<Series>/<Game>/<Locale>/`

Each game/locale directory owns its localization data, maintenance scripts, machine-readable authority metadata, human-readable documentation, legal/third-party notices, and selected milestone evidence.

## Current projects

- [`SteinsGate/`](SteinsGate/) — STEINS;GATE series localization modules.
  - [`MyDarlingsEmbrace/zh-TW/`](SteinsGate/MyDarlingsEmbrace/zh-TW/) — Taiwan Traditional Chinese localization module for *STEINS;GATE: My Darling's Embrace*.
