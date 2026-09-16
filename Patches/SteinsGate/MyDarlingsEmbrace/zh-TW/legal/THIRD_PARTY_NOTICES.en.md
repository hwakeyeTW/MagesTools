# Third-party notices

This file records third-party projects and components materially relevant to the public Taiwan Traditional Chinese localization module and its tooling/build lineage.

It is an attribution/provenance document, not a replacement for the original license texts.

## MagesTools / EasyPatcher / MagesLib

Upstream project:

- Project: **MagesTools**
- Repository: <https://github.com/fengberd/MagesTools>
- Original author/copyright notice: `Copyright (c) 2020 FENGberd`
- License: **MIT License**

This repository, <https://github.com/hwakeyeTW/MagesTools>, is a fork of that project. The fork retains the upstream tooling lineage while adding Taiwan Traditional Chinese EasyPatcher UI work, Steam installation-path detection, and game-specific localization-module maintenance material.

A copy of the upstream MIT license is preserved at [`licenses/MAGES_TOOLS_MIT.txt`](licenses/MAGES_TOOLS_MIT.txt).

The localization module relies on EasyPatcher and MagesLib for patch application and MAGES-format handling. Exact accepted binary/tooling identities for the v1.0.0 release are recorded separately in `../authority/TOOLING_REFERENCE.json`; machine-readable release authority should not be inferred from this human-readable notice.

## fastJSON

`fastJSON.dll` is used as a JSON dependency by the EasyPatcher/MagesTools software lineage and is inherited from the original MagesTools distribution.

For this documentation draft, the exact binary-version provenance and corresponding historical license notice for the inherited DLL have **not yet been independently established from the binary itself**. This file therefore intentionally does not assign a new or inferred license to that specific historical binary merely from the current state of another upstream repository.

Before this documentation branch is merged, the preferred closure is one of:

1. establish the exact inherited binary provenance/license and record it here; or
2. preserve the upstream-distribution attribution explicitly without overstating provenance that has not been verified.

This uncertainty concerns attribution documentation only; it does not change the accepted v1.0.0 module binary identity.

## GenYo Gothic / 源樣黑體

Font source used by the localization project's font-generation/maintenance workflow includes:

- Font family/project: **GenYo Gothic / 源樣黑體**
- Upstream repository: <https://github.com/ButTaiwan/genyog-font>
- Maintainer/project author: **ButTaiwan**
- Relevant build source used by this project: `GenYoGothic2TW-M.otf`
- License: **SIL Open Font License 1.1**

The GenYo Gothic project states that the family is derived from Adobe **Source Han Sans / 思源黑體** and is distributed under the SIL Open Font License 1.1.

The module's normal public game distribution contains generated game font textures rather than redistributing the source OTF as a general end-user module file.

A copy of the upstream OFL text is preserved at [`licenses/GENYO_GOTHIC_OFL-1.1.txt`](licenses/GENYO_GOTHIC_OFL-1.1.txt).

## Source Han Sans lineage

The OFL text shipped by the GenYo Gothic upstream records:

`Copyright 2014-2019 Adobe (http://www.adobe.com/), with Reserved Font Name 'Source'.`

Source Han Sans / Source naming, copyright, reserved-font-name requirements, and derivative-font conditions remain governed by the applicable SIL Open Font License terms.

## OpenAI GPT-5.6 Sol

OpenAI GPT-5.6 Sol was used as the primary language-model tool in substantial portions of the localization, rewriting, review assistance, consistency analysis, and project-maintenance workflow.

Its use is disclosed for process transparency. OpenAI is not represented as an author, publisher, sponsor, or endorser of the original game or this fan-localization module.

See [`../docs/LOCALIZATION_METHODOLOGY.md`](../docs/LOCALIZATION_METHODOLOGY.md) for the project's AI-assisted localization methodology and acceptance boundaries.

## Original game materials

Original *STEINS;GATE* game materials and official localized text are not third-party open-source dependencies of this repository and are not relicensed by the notices above. Their rights remain with their respective rights holders. See [`NOTICE.en.md`](NOTICE.en.md).
