# Intonate – Roadmap

This document outlines the phased development plan for the Intonate project, transitioning from a working prototype to a mature, extensible SSML generation tool.

---

## ✅ Completed (v1.0)
- Markdown to SSML transformation via YAML rule engine
- CLI support with `--input`, `--config`, `--output` arguments
- `<speak>` tag wrapping
- Rule tagging for headings, bold, italic, emphasis
- GitHub repo initialized with README and basic structure

---

## 🔹 Upcoming Milestones

### 🧱 v1.1 – Core Stability & Profile Support
- [ ] Add support for `core` vs `extended` SSML profiles
- [ ] Validate YAML rules (regex compilation, tag format)
- [ ] Output warnings for invalid or unused rules
- [ ] Add CLI flag for "profile=core|extended"
- [ ] Catch untaggable content and output as-is with note

### 🛠️ v1.2 – Authoring Controls
- [ ] Add support for `<sub>` element
- [ ] Add support for `<phoneme>` element (IPA only)
- [ ] Add support for `<lang>` element
- [ ] Allow metadata overrides in Markdown (YAML frontmatter or comment block)
- [ ] Improve CLI feedback for tagged vs untouched lines

### 🔍 v1.3 – Structural Validation
- [ ] Add validator module to check for illegal SSML nesting
- [ ] Identify known restrictions (e.g., `<sub>` can't contain `<audio>`, `<phoneme>` is text-only)
- [ ] Raise CLI warnings/errors on structural violations
- [ ] Optional: validate final SSML output using `xml.etree.ElementTree`

---

## 🧪 Ideas for Future Releases
- SSML preview window (VS Code plugin or CLI audio playback)
- Live "linting" of Markdown input for SSML conflicts
- Voice metadata (e.g., emotion, role) via comments or shorthand
- Batch processing of multiple `.md` files
- ElevenLabs API integration (auto-render after export)

---

## 🗂️ Notes
- Refer to W3C SSML 1.1 spec for canonical tag usage and constraints
- Use `synthesis.xsd` schema URL for reference and future validation goals
- Maintain `summary.txt` as a living compatibility overview

---

> This roadmap is versioned. For milestone completion history, see Git commit logs.
