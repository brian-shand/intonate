# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/), and this project adheres to [Semantic Versioning](https://semver.org/).

---

## [v1.1.1] – 2025-06-08

### Added
- Rule usage tracking and unused rule reporting
- Validation for regex compilation and tag structure
- Fallback handling for discarded content (e.g., missing `\1`)
- Support for `core` vs `extended` profile filtering

### Fixed
- False positives in unused rule reporting
- Over-escaped regex strings in YAML

### Improved
- CLI feedback for applied rules and tagging results
- Developer visibility with rule-by-rule debug logs

---

## [v1.1.0] – Unreleased

> Internal version milestone prior to fallback and validation additions.
