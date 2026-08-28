# Compatibility Matrix

| Feature | OpenAI/Codex-style skills | Claude-style projects/skills | Gemini-style agent contexts | Generic file-capable agent |
| --- | --- | --- | --- | --- |
| Root `SKILL.md` instructions | Native pattern | Adaptable | Adaptable | Read directly |
| YAML trigger metadata | Native pattern | Adapter may be needed | Adapter may be needed | Optional parser |
| Bundled references | Supported | Supported | Supported | Supported if local files are readable |
| Python validation scripts | Supported with runtime | Supported with runtime | Supported with runtime | Runtime required |
| R recipe execution | Runtime required | Runtime required | Runtime required | R runtime required |
| GitHub Actions validation | Repository-level | Repository-level | Repository-level | Repository-level |

“Adaptable” means the skill's operational instructions remain usable, but the target platform may require a wrapper, manifest, or different installation path.
