# Contributing

Thank you for improving Visual UI Production.

## Before opening a pull request

1. Keep the approval gates and non-destructive asset rules intact.
2. Do not include private screenshots, real client data, local absolute paths,
   generated drafts, secrets, licensed fonts, or unlicensed media.
3. Add or update an anonymous example when behavior changes.
4. Run:

   ```bash
   python -m pip install -r requirements.txt
   python -m unittest discover -s tests -v
   python tools/package_skill.py
   ```

5. Describe the user-visible behavior changed and the validation performed.

## Documentation

Use relative links inside the skill package. Keep exact UI labels and commands
in code blocks. Examples must be synthetic and must not imply endorsement by a
real company, customer, or project.

## Versioning

This repository follows semantic versioning. Workflow or compatibility breaks
require a major version; backwards-compatible capabilities use a minor version;
documentation and compatible fixes use a patch version.
