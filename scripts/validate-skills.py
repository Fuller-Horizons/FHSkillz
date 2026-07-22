#!/usr/bin/env python3
import os
import re
import sys
import yaml

def validate_skill_file(filepath):
    print(f"Validating: {filepath}")
    errors = []

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Check frontmatter only for SKILL.md
    if os.path.basename(filepath) == "SKILL.md":
        frontmatter_match = re.match(r'^---\s*\n(.*?)\n---\s*\n', content, re.DOTALL)
        if not frontmatter_match:
            errors.append("Missing or invalid YAML frontmatter (must start and end with ---).")
            return errors

        try:
            metadata = yaml.safe_load(frontmatter_match.group(1))
        except Exception as e:
            errors.append(f"Failed to parse YAML frontmatter: {e}")
            return errors

        if not metadata:
            errors.append("YAML frontmatter is empty.")
            return errors

        if 'name' not in metadata or not metadata['name']:
            errors.append("Frontmatter is missing the 'name' field.")
        elif not re.match(r'^[a-z0-9-]+$', metadata['name']):
            errors.append(f"Skill name '{metadata['name']}' must be lowercase-hyphenated [a-z0-9-].")

        if 'description' not in metadata or not metadata['description']:
            errors.append("Frontmatter is missing the 'description' field.")

    # Check file:/// links — but ignore illustrative examples inside code spans
    # or fenced code blocks (docs legitimately show file URLs as an anti-pattern).
    link_scan = re.sub(r'```.*?```', '', content, flags=re.DOTALL)  # fenced blocks
    link_scan = re.sub(r'`[^`]*`', '', link_scan)                   # inline code spans
    file_links = re.findall(r'file:///([^\s\)\"\>]+)', link_scan)
    for link in file_links:
        from urllib.parse import unquote
        clean_path = unquote(link)

        if clean_path.startswith('/') and len(clean_path) > 2 and clean_path[2] == ':':
            clean_path = clean_path[1:]

        if '#' in clean_path:
            clean_path = clean_path.split('#')[0]

        if any(p in clean_path for p in ["path/or/url", "path/to/", "absolute/path/"]) or clean_path == "path":
            continue

        if not os.path.exists(clean_path):
            errors.append(f"Broken link: {link} (resolved path does not exist: {clean_path})")

    # Check JSON syntax and schema validity in markdown code blocks
    import json
    json_blocks = re.findall(r'```json\s*\n(.*?)\n```', content, re.DOTALL)
    for idx, block in enumerate(json_blocks):
        try:
            obj = json.loads(block)
            if isinstance(obj, dict) and ("$schema" in obj or "properties" in obj or "type" in obj):
                valid_types = {"string", "number", "integer", "boolean", "object", "array", "null"}
                if "properties" in obj and isinstance(obj["properties"], dict):
                    for prop, details in obj["properties"].items():
                        if isinstance(details, dict) and "type" in details:
                            if details["type"] not in valid_types:
                                errors.append(f"Invalid JSON Schema in block #{idx + 1}: Property '{prop}' has invalid type '{details['type']}'.")
        except Exception as e:
            errors.append(f"Invalid JSON syntax in code block #{idx + 1}: {e}")

    return errors

def run_toolkit_checks(repo_root):
    """Release-loop wiring (0.23.0): run the jail-py-toolkit / jail-py-lab
    machine checks on every validation run, not only on request.
    Checks: (1) every bundled script byte-compiles; (2) jail-py-toolkit's
    validate-skill-structure.py passes on every skills/* directory."""
    import py_compile
    import subprocess
    errors = []
    skills_dir = os.path.join(repo_root, "skills")
    # 1 — all bundled scripts compile
    for skill in ("jail-py-toolkit", "jail-py-lab"):
        sdir = os.path.join(skills_dir, skill, "scripts")
        if not os.path.isdir(sdir):
            errors.append(f"missing companion scripts dir: {sdir}")
            continue
        for f in sorted(os.listdir(sdir)):
            if f.endswith(".py"):
                try:
                    py_compile.compile(os.path.join(sdir, f), doraise=True)
                except py_compile.PyCompileError as e:
                    errors.append(f"{skill}/{f}: {e.msg}")
    # 2 — structural lint of every skill dir via the toolkit
    lint = os.path.join(skills_dir, "jail-py-toolkit", "scripts",
                        "validate-skill-structure.py")
    if os.path.isfile(lint) and os.path.isdir(skills_dir):
        for d in sorted(os.listdir(skills_dir)):
            path = os.path.join(skills_dir, d)
            if os.path.isdir(path):
                r = subprocess.run([sys.executable, lint, path],
                                   capture_output=True, text=True)
                if r.returncode != 0:
                    errors.append(f"structure lint failed for skills/{d}: "
                                  f"{(r.stdout + r.stderr).strip()[:200]}")
    return errors


def main():
    target = sys.argv[1] if len(sys.argv) > 1 else os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    all_errors = {}
    if os.path.isdir(target):
        for root, _, files in os.walk(target):
            for file in files:
                if file.endswith(".md"):
                    filepath = os.path.join(root, file)
                    errs = validate_skill_file(filepath)
                    if errs:
                        all_errors[filepath] = errs
    elif os.path.isfile(target):
        errs = validate_skill_file(target)
        if errs:
            all_errors[target] = errs

    if os.path.isdir(target):
        toolkit_errors = run_toolkit_checks(target)
        if toolkit_errors:
            all_errors["[jail-py-toolkit release checks]"] = toolkit_errors
        else:
            print("[toolkit] machine checks passed (script compile + structure lint)")

    if all_errors:
        print("\n[!] Validation Failed with Errors:")
        for path, errs in all_errors.items():
            print(f"\nFile: {path}")
            for err in errs:
                print(f"  - {err}")
        sys.exit(1)
    else:
        print("\n[+] Validation Succeeded! All checks passed.")
        sys.exit(0)

if __name__ == "__main__":
    main()
