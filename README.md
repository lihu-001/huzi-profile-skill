# huzi-profile

Open skill for an X (Twitter) new-account pack: display name, handle, bio, 1:1 avatar, 3:1 banner. Write the personal IP sentence first, then pick a style.

License: MIT (`LICENSE`).

## Layout (Agent Skills spec)

The repository root is the skill directory:

```
huzi-profile/
├── SKILL.md
├── README.md
├── LICENSE
├── compose_preview.py
├── assets/
└── references/
    ├── world-styles.md
    ├── style-packs.md
    ├── safe-zones.md
    ├── design-bar.md
    └── masters.md
```

## Install on another agent

Clone this repository directly to the host's skill directory as `huzi-profile`, then load the root `SKILL.md`. Claude/Codex commonly use `skills/` or `.agents/skills/`; Grok commonly uses `.grok/skills/`.

Allow on-demand reads of `references/*.md` and bundled previews from `assets/`.

No binaries ship with this skill. Image tools differ by host.

## Recommended image host

Prefer **Codex** or **Grok** for avatars and banners. Both can lock the 1408×1408 / 1500×500 canvases and paint onto them.

If neither host is available, fall back to **AutoGLM** text-to-image. AutoGLM quality is substantially worse than Codex and Grok — weaker type, less reliable 1-1 / 3-1 frames, more retries. Still demand those exact ratios and reject 16:9 or portrait outputs.

## Port the image pipeline

`SKILL.md` names Grok tools (`render_edited_image`, `read_file`) and ImageMagick `convert`. On another host:

- Still lock canvases to **1408×1408** (avatar) and **1500×500** (banner).
- If there is no ImageMagick, create those canvases any other way, then edit in place.
- If there is only text-to-image, demand those exact ratios in the prompt and reject 16:9 or portrait outputs.
- Never treat a default landscape generate as an X banner.

Rules that must survive the port: full-width banner design with only the bottom-left avatar circle excluding type and focal objects, avatar mark nearly filling the circle, banner line taken from the bio, style number from `references/world-styles.md`.


## Deliverable & Profile Preview

Whenever a profile pack is generated, the skill produces both the standalone upload assets AND the combined in-situ profile preview card (749×465), saved by default to `.huzi-profile/`:

1. **`.huzi-profile/profile-preview.png` (749×465)**: Assembled X desktop dark-mode preview card combining the banner, overlapping circular avatar, verified badge, buttons ("编辑个人资料", "$"), display name, handle, and bio. Multiple styles use `.huzi-profile/{nn}-{slug}-preview.png` (example: `01-swiss-preview.png`).
2. **`.huzi-profile/banner.png` (1500×500)**: Clean 3:1 banner for upload.
3. **`.huzi-profile/avatar.png` (1408×1408)**: 1:1 circular-safe avatar for upload.

The card can be composed automatically using the bundled Python script (defaults read from and write to `.huzi-profile/`). Pass the display name, handle, and bio collected this turn — do not keep the script's example identity:
```bash
python compose_preview.py --name "<display name>" --handle "<handle>" --bio "<bio>"
```
## How the user picks a style

Name a number, English name, or Chinese name: `用 01 Swiss`, `要包豪斯`, `封面用第 13 套`.

Or dump the catalog:

- `对照全部风格`
- `输出全部封面`
- `all styles`

Generate 1500×500 banners in batches of ten. Avatars only after a pick.

Catalog style numbers and names live in the table below. Runtime packs are generated in chat.

## World styles

| # | Name | What you should recognize | Fits |
|---|---|---|---|
| 01 | Swiss | grid, flush grotesque | product notes |
| 02 | Bauhaus | circle, bar, square | studio, course |
| 05 | New Typography | heavy rules, asymmetric | editorial |
| 06 | Art Nouveau | whiplash plant line | decorative, rare |
| 07 | Art Deco | chevron, gold/black | event |
| 08 | Arts and Crafts | woodcut border | craft, press |
| 09 | Vienna Secession | gold grid, black field | design firm |
| 11 | Dada | ransom newsprint | critique |
| 12 | Suprematism | black square, red plane | concept |
| 13 | Sachplakat | one giant object | tools, workflows |
| 28 | New Wave | broken Swiss grid | experimental type |
| 29 | Memphis | pink lime terrazzo | playful, costume risk |
| 42 | Material Design | stacked sheets | product |
| 45 | Neumorphism | same-color relief | soft UI |

One-person AI-media defaults: 01, 02, 13.

## Shorter studio textures

`references/style-packs.md` has twenty job textures (Studio plate, Clear terminal, …). A world-style number wins when both are named. Do not mix Swiss and Memphis on one account.

## Hard specs

- Avatar 1408×1408, letters almost fill the circular crop
- Banner 1500×500, full-width visual language; keep type and focal objects clear of the bottom-left avatar circle
- Type must contrast the local field (`references/design-bar.md`)
- Never ship a default landscape generate as the banner

Details: `SKILL.md`, `references/safe-zones.md`, `references/design-bar.md`.
