# skills.md · ToolTammy

Platform: https://skills.md  
CLI: `@hasna/skills` (needs bun)

## Setup (done on nico profile)
- bun → `~/.bun/bin/bun`
- skills → `~/.npm-global/bin/skills`
- PATH wired in `~/.bashrc`

## Auth
```bash
skills login --device
# open verification URL, enter code
skills login --poll
skills whoami
```

## Tammy first runs (after credits)
```bash
skills run --remote --yes --wait logo-design --brief "ToolTammy AI agent girl" --brand "ToolTammy" --palette "hot pink,black,white" --variations 4
skills run --remote --yes --wait short-video-pack --brief "crush-worthy Tammy talking-head tips reel"
```
