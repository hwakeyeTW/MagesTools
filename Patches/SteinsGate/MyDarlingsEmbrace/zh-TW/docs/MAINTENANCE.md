# Maintenance policy

The 2026-09-10 milestone is byte-frozen. Editing a current authority file creates a successor candidate; do not silently overwrite milestone identities.

- Editing `patch/berd/script.json` invalidates the current script/release binding and requires bounded rebuild/revalidation appropriate to the change.
- Editing `patch/berd/system.json` or font machinery requires system/font impact validation.
- Editing `patch/berd/meta.json` changes the production ZIP identity even if gameplay text is unchanged.
- Tool-source changes do not automatically prove byte identity to the previously accepted EasyPatcher binary; see `TOOLING_REFERENCE.json`.
- Frozen milestone ZIPs are evidence and must never be edited/repacked under the same name/hash authority.
