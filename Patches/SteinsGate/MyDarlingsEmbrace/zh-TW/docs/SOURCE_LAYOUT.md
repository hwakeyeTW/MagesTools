# Source layout

This localization module uses a layered repository structure so that runtime patch data, machine-readable authority, maintenance implementation, human-facing documentation, and legal/third-party notices do not collapse into one README.

## Public module tree

- `patch/berd/` — current public patch data consumed by EasyPatcher.
- `docs/` — human-readable localization methodology, credits, maintenance, reproducibility, terminology, and source-layout documentation.
- `legal/` — game-rights notice, third-party attribution, and copied license texts required for clear provenance.
- `authority/` — machine-readable release, private-source, tooling, and path bindings.
- `maintenance/` — repository-native maintenance implementations and preserved validation references.
- `milestones/` — immutable selected evidence for accepted milestones.

The user-facing project is described as a **localization module / 中文化模組**. Existing technical paths and implementation names such as `Patches/`, `patch/berd/`, EasyPatcher, and already-published artifact names containing `Patch` remain unchanged.

## Source-corpus boundary

Private JP / official EN / alignment / recovered-source corpora are stored in `hwakeyeTW/MagesTranslationSources` under the matching series/game/locale path and are referenced through the module's authority metadata.

The public repository intentionally does not reproduce the complete official Japanese, English, or other official-language corpora used for source comparison and terminology work.

The full frozen B-postfix maintenance archive remains external/archive-only and is not copied wholesale into either Git history.

## Human-readable provenance

Translation source priority and AI usage disclosure are documented in [`LOCALIZATION_METHODOLOGY.md`](LOCALIZATION_METHODOLOGY.md).

Original-work, tooling, font, and community acknowledgements are documented in [`CREDITS.md`](CREDITS.md).

Rights and third-party licensing information are documented under [`../legal/`](../legal/).
