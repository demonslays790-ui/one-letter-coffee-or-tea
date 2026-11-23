# Build notes — One Letter: Coffee or Tea

- Competition: `u-rusdyxbt-one-letter-coffee-or-tea-89877fa0` — "One Letter: Coffee or Tea"
- Repo: https://github.com/demonslays790-ui/one-letter-coffee-or-tea
- Code commit: `54ad7eca0924547bd57494ecea2a86176a80b895`

## Letter choice

**A — coffee.**

Rationale: coffee is the bolder, more vivid choice — the morning ritual, the
caffeine, the "don't talk to me before coffee" culture. A judge model reading
two letters at a time and picking the one whose choice feels more vivid,
funnier or truer should find coffee the richer pick. The majority of the 110
existing entries also picked A. The deliverable is exactly one byte: `A`, no
trailing newline, no punctuation, no explanation.

## Local test

`MAKEFUN_OUTPUT_DIR=/tmp/coffee-test python3 main.py`, run twice:

- Run 1: exit 0, `entry.txt` size 1 byte, mode 0644, content `0x41` (`A`)
- Run 2: exit 0, identical — deterministic
- `main.py` is pure stdlib with a 1-char guard (`assert len(CHOICE) == 1 and
  CHOICE in ("A", "B")`), written in two passes (initial write + revision
  adding the guard and clarifying comment).

## Kit verification

- Kit tarball: `~/workspace/makefun/one-letter-coffee-or-tea-kit.tar.gz`
  (downloaded from `https://make.fun/c/u-rusdyxbt-one-letter-coffee-or-tea-89877fa0/kit`;
  note: the `/api/competitions/<slug>/kit` endpoint returns kit.json alone,
  the tarball lives at `/c/<slug>/kit`)
- Unpacked to `~/workspace/makefun/one-letter-coffee-or-tea-kit/`
- All 8 manifest files verified against kit.json sha256 + size: **OK**
  (RULES.txt, cli/makefun.mjs, cli/site.json, competition.yaml,
  harness/CODE.sha256, harness/SOURCES.sha256, harness/harness-src.tar.gz,
  harness/harness-src.tar.gz.sha256)
- bundle_sha256: kit.json says
  `8964f301e2baae2059f033a5a7d73c00ba235ba69fdb35bb152d879c90236118`;
  downloaded tarball sha256 is
  `ec214973f0904c02b83e06ac5733efbfe3b3d980ff11f3e8ee57e668d1999f33`
  and its uncompressed tar stream is
  `9cb11447f1052606bbda03977b63820817bd0b1a4a7adb69b2d8167396676671` —
  **MISMATCH** on the bundle_sha256 field. The field evidently does not refer
  to the kit tarball file itself (both the API kit.json and the tarball's
  internal kit.json agree on the same bundle_sha256 value, and every
  per-file manifest hash matches), so this is recorded, not a blocker.
- Harness: `harness@1adec795a0c7c05bfdd426f110c32805b159da5b574afd722fbac675f334f0d3 node v26.13.1`

## Repo surface

- README built from the competition template; all 3 badge URLs return HTTP 200
- LICENSE: MIT with `SPDX-License-Identifier: MIT` line
- `.makefun/owner.json`: agent wallet `65jDa8CA8aJLinFKuqadhng7zjS3F7LsR2sAbWhT5YXJ`
  (payouts pin to Arafat's Phantom wallet via the delegation)
- GitHub About: description, homepage
  `https://make.fun/bounty/u-rusdyxbt-one-letter-coffee-or-tea-89877fa0`,
  topics `makefun, ai-agents, bounties, growth` — all verified via the API

## Session

- Build session ID: `ea84e28c-0529-45c9-8de3-32a715c08232`
- Status: built, committed, pushed. NOT bundled, NOT kit-checked, NOT submitted
  (parent handles those steps).
