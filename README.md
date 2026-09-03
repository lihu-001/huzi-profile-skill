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

## Port the image pipeline

`SKILL.md` names Grok tools (`render_edited_image`, `read_file`) and ImageMagick `convert`. On another host:

- Still lock canvases to **1408×1408** (avatar) and **1500×500** (banner).
- If there is no ImageMagick, create those canvases any other way, then edit in place.
- If there is only text-to-image, demand those exact ratios in the prompt and reject 16:9 or portrait outputs.
- Never treat a default landscape generate as an X banner.

Rules that must survive the port: full-width banner design with only the bottom-left avatar circle excluding type and focal objects, avatar mark nearly filling the circle, banner line taken from the bio, style number from `references/world-styles.md`.


## Deliverable & Profile Preview

Whenever a profile pack is generated, the skill produces both the standalone upload assets AND the combined in-situ profile preview card (749×465):

1. **`profile-preview.png` (749×465)**: Assembled X desktop dark-mode preview card combining the banner, overlapping circular avatar, verified badge, buttons ("编辑个人资料", "$"), display name, handle, and bio.
2. **`banner.png` (1500×500)**: Clean 3:1 banner for upload.
3. **`avatar.png` (1408×1408)**: 1:1 circular-safe avatar for upload.

The card can be composed automatically using the bundled Python script:
```bash
python compose_preview.py --banner banner.png --avatar avatar.png --name "HUZI" --handle "@lihu9048" --bio "学习AI，分享AI" --out profile-preview.png
```
## How the user picks a style

Name a number, English name, or Chinese name: `用 01 Swiss`, `要包豪斯`, `封面用第 25 套`.

Or dump the catalog:

- `对照全部风格`
- `输出全部 50 套封面`
- `all styles`

Generate 1500×500 banners in batches of ten. Avatars only after a pick.

Catalog previews live in `assets/` — `01-xxx.png` is style 01, `02-xxx.png` is style 02, and so on. Runtime packs are still generated in chat.

## 50 world styles

| # | Preview | Name | What you should recognize | Fits |
|---|---|---|---|---|
| 01 | <img src="assets/01-swiss.png" alt="01 Swiss" width="280"> | Swiss | grid, flush grotesque | product notes |
| 02 | <img src="assets/02-bauhaus.png" alt="02 Bauhaus" width="280"> | Bauhaus | circle, bar, square | studio, course |
| 03 | <img src="assets/03-constructivism.png" alt="03 Constructivism" width="280"> | Constructivism | diagonal industrial bars | manifesto |
| 04 | <img src="assets/04-de-stijl.png" alt="04 De Stijl" width="280"> | De Stijl | H/V + RGB blocks | systems |
| 05 | <img src="assets/05-new-typography.png" alt="05 New Typography" width="280"> | New Typography | heavy rules, asymmetric | editorial |
| 06 | <img src="assets/06-art-nouveau.png" alt="06 Art Nouveau" width="280"> | Art Nouveau | whiplash plant line | decorative, rare |
| 07 | <img src="assets/07-art-deco.png" alt="07 Art Deco" width="280"> | Art Deco | chevron, gold/black | event |
| 08 | <img src="assets/08-arts-and-crafts.png" alt="08 Arts and Crafts" width="280"> | Arts and Crafts | woodcut border | craft, press |
| 09 | <img src="assets/09-vienna-secession.png" alt="09 Vienna Secession" width="280"> | Vienna Secession | gold grid, black field | design firm |
| 10 | <img src="assets/10-futurism.png" alt="10 Futurism" width="280"> | Futurism | slashing speed type | tech manifesto |
| 11 | <img src="assets/11-dada.png" alt="11 Dada" width="280"> | Dada | ransom newsprint | critique |
| 12 | <img src="assets/12-suprematism.png" alt="12 Suprematism" width="280"> | Suprematism | black square, red plane | concept |
| 13 | <img src="assets/13-sachplakat.png" alt="13 Sachplakat" width="280"> | Sachplakat | one giant object | tools, workflows |
| 14 | <img src="assets/14-streamline.png" alt="14 Streamline" width="280"> | Streamline | chrome curve | machine era |
| 15 | <img src="assets/15-heroic-realism.png" alt="15 Heroic Realism" width="280"> | Heroic Realism | monument silhouette | campaign |
| 16 | <img src="assets/16-corporate-modern.png" alt="16 Corporate Modern" width="280"> | Corporate Modern | one mark + big word | one-person firm |
| 17 | <img src="assets/17-mid-century.png" alt="17 Mid-century" width="280"> | Mid-century | organic color fields | popular |
| 18 | <img src="assets/18-ulm.png" alt="18 Ulm" width="280"> | Ulm | gray modules, spec line | R&D |
| 19 | <img src="assets/19-crouwel.png" alt="19 Crouwel" width="280"> | Crouwel | tight tracking, number grid | information design |
| 20 | <img src="assets/20-lubalin.png" alt="20 Lubalin" width="280"> | Lubalin | tight phototype, complete word | editorial |
| 21 | <img src="assets/21-pop-art.png" alt="21 Pop Art" width="280"> | Pop Art | Ben-Day, comic type | pop critique |
| 22 | <img src="assets/22-psychedelic.png" alt="22 Psychedelic" width="280"> | Psychedelic | molten letters | music-adjacent |
| 23 | <img src="assets/23-push-pin.png" alt="23 Push Pin" width="280"> | Push Pin | flat historic pastiche | editorial illustration |
| 24 | <img src="assets/24-polish-poster.png" alt="24 Polish Poster" width="280"> | Polish Poster | painted metaphor | film, deep poster |
| 25 | <img src="assets/25-japanese-modern.png" alt="25 Japanese Modern" width="280"> | Japanese Modern | huge red disk | international mark |
| 26 | <img src="assets/26-wood-type.png" alt="26 Wood type" width="280"> | Wood type | oversized complete letters, print shift | press, poster |
| 27 | <img src="assets/27-punk-diy.png" alt="27 Punk DIY" width="280"> | Punk DIY | xerox, stencil | independent |
| 28 | <img src="assets/28-new-wave.png" alt="28 New Wave" width="280"> | New Wave | broken Swiss grid | experimental type |
| 29 | <img src="assets/29-memphis.png" alt="29 Memphis" width="280"> | Memphis | pink lime terrazzo | playful, costume risk |
| 30 | <img src="assets/30-deconstructivism.png" alt="30 Deconstructivism" width="280"> | Deconstructivism | fractured layers | academic |
| 31 | <img src="assets/31-emigre.png" alt="31 Emigre" width="280"> | Emigre | bitmap display | 90s magazine |
| 32 | <img src="assets/32-grunge.png" alt="32 Grunge" width="280"> | Grunge | overprint dirt | 90s print |
| 33 | <img src="assets/33-maximalism.png" alt="33 Maximalism" width="280"> | Maximalism | dense but readable | culture account |
| 34 | <img src="assets/34-brutalism.png" alt="34 Brutalism" width="280"> | Brutalism | type cast in concrete | anti-gloss |
| 35 | <img src="assets/35-wabi-sabi.png" alt="35 Wabi-sabi" width="280"> | Wabi-sabi | stained paper, broken ink | slow object |
| 36 | <img src="assets/36-bass.png" alt="36 Bass" width="280"> | Bass | cut-paper planes, condensed title | film, campaign |
| 37 | <img src="assets/37-superflat.png" alt="37 Superflat" width="280"> | Superflat | no depth, no mascot | graphic planes |
| 38 | <img src="assets/38-op-art.png" alt="38 Op Art" width="280"> | Op Art | vibrating B/W field | optical, no figures |
| 39 | <img src="assets/39-concrete.png" alt="39 Concrete" width="280"> | Concrete | squares as proportion | structure |
| 40 | <img src="assets/40-agitprop.png" alt="40 Agitprop" width="280"> | Agitprop | red bar, bold italic, full words | critique, culture |
| 41 | <img src="assets/41-flat.png" alt="41 Flat Design" width="280"> | Flat Design | UI blocks | product |
| 42 | <img src="assets/42-material.png" alt="42 Material Design" width="280"> | Material Design | stacked sheets | product |
| 43 | <img src="assets/43-skeuomorphism.png" alt="43 Skeuomorphism" width="280"> | Skeuomorphism | physical plate | object |
| 44 | <img src="assets/44-glassmorphism.png" alt="44 Glassmorphism" width="280"> | Glassmorphism | frosted panel, sharp type | must stay readable |
| 45 | <img src="assets/45-neumorphism.png" alt="45 Neumorphism" width="280"> | Neumorphism | same-color relief | soft UI |
| 46 | <img src="assets/46-y2k.png" alt="46 Y2K" width="280"> | Y2K | chrome bubble type | revival, slop risk |
| 47 | <img src="assets/47-synthwave.png" alt="47 Synthwave" width="280"> | Synthwave | purple-cyan horizon grid | wallpaper risk |
| 48 | <img src="assets/48-acid.png" alt="48 Acid Graphics" width="280"> | Acid Graphics | toxic melt type | club |
| 49 | <img src="assets/49-neo-brutalism.png" alt="49 Neo-brutalism" width="280"> | Neo-brutalism | system font, thick frame | anti-brand gloss |
| 50 | <img src="assets/50-risograph.png" alt="50 Risograph" width="280"> | Risograph | fluorescent two-color overprint | zine, studio print |

One-person AI-media defaults: 01, 02, 03, 13, 16, 18, 19, 20, 25, 34.

## Shorter studio textures

`references/style-packs.md` has twenty job textures (Studio plate, Clear terminal, …). A world-style number wins when both are named. Do not mix Swiss and Memphis on one account.

## Hard specs

- Avatar 1408×1408, letters almost fill the circular crop
- Banner 1500×500, full-width visual language; keep type and focal objects clear of the bottom-left avatar circle
- Type must contrast the local field (`references/design-bar.md`)
- Never ship a default landscape generate as the banner

Details: `SKILL.md`, `references/safe-zones.md`, `references/design-bar.md`.
