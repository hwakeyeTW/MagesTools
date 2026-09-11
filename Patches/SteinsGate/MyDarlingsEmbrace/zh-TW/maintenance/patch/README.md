# Postfix canonical patch maintenance

This directory is the repository-native successor of the frozen B-postfix canonical patch-maintenance lane.

The canonical packer consumes:

- exact public game files under `../../patch/berd/`;
- an externally supplied tool-shell directory containing the exact accepted EasyPatcher/MagesLib/fastJSON binaries.

Tool binaries are intentionally **not vendored** in this game directory. See `../../authority/TOOLING_REFERENCE.json`.

With the exact accepted tool shell, the builder must reproduce production candidate `edbd65e66eb9e650be0cbe8a3763cd669eb7f1a15b0e7005148d993431a26219`.

Files under `reference/` are retained historical validation references and are not the current release authority.
