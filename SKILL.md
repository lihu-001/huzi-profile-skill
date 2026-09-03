---
name: huzi-profile
description: Build a complete X (Twitter) new-user profile pack — display name, handle, bio, avatar, banner, and in-situ 749x465 profile preview card. Use when the user runs /huzi-profile, or asks for X or Twitter profile setup, 取名, 简介, 头像, 封面, 预览, handle ideas, style number 01-50, 对照风格, or a personal brand kit. Design from the personal IP goal first. Banner before avatar. Aim at award-level identity (D and AD / ADC / JAGDA methods), not stock moodboards. Always produce true 1-1 avatars, 3-1 banners with safe zones, and the assembled profile preview card (749x465).
---

# HUZI Profile

Create a coherent X identity pack. Start from the personal IP goal. Name, handle, bio, and images are expressions of that goal, not a moodboard.

## IP first (do this before any style)

Write one sentence the account must be famous for in 90 days.
Template — I am the person who [proof they publish] for [who] so they can [result].

Derive from that sentence

- Proof type — tutorials, teardown, essays, builds, opinions, diary
- Vessel — personal diary, face-IP, or one-person company (the name is the firm)
- Audience language and geography
- What the mark must signal at 40px — a maker, a writer, an operator, a performer, a studio
- What the mark must never signal — a shop they do not run (fashion house, restaurant, game studio, temple, crypto temple) unless that is the actual IP

Do not pick a style pack until this sentence exists. Style packs are textures for the IP, not costumes.

## Order of making (mandatory)

1. IP sentence and bio.
2. Banner line cut from the bio (3-8 words).
3. One master method from references/masters.md — a way of working, not a logo to copy.
4. Design the 1500x500 banner first. It must carry the offer.
5. Derive the 1408x1408 avatar from the banner's design language — same method, type cut, color system, and spatial idea. Do not invent a second system. Do not confuse language with photocopying the banner's wood or paper.
   Two packs that both output black HUZI on cream have lost the style. Clear terminal must still be a grid + caret. Field folio must still be an annotated sheet. Protocol kitchen must still be one quiet object. The name stays HUZI; the style must still be readable with the name covered.
6. Paint a wordless ground first. Set the banner line and the HUZI mark in a later pass (code or a second edit), not inside the image-model prompt. Accidental readable words on the ground are a defect. Type cut and ink follow the style.
7. Type contrast — read references/design-bar.md. If a letter collides with the local field, recast only the type ink, then re-inspect. Do not add a generic plate.
8. Stunning test — hide the name. Would a design jury remember one decision (one cut of type, one material, one spatial idea)? If it only looks tidy, redo.
9. Assemble composite profile preview card (749x465) — combine the 3-1 banner, circular avatar, display name, verified badge, handle, bio, and X action buttons into the final preview image via `compose_preview.py` (or Python PIL). Deliver this composite preview directly in chat for user review.

Read references/masters.md before prompting images.

## First collect (ask only what is missing)

- IP sentence above
- Purpose — personal creator, brand, alt
- Audience and language
- Face on camera or mark-only
- Constraints — no CJK on images, no face, must include a wordmark, etc.

If they only want options, write 3 different IP sentences and one pack each. Do not stall on vibe adjectives.

## Specs

- Display name — max 50 characters
- Handle — 4-15 characters, letters numbers underscore
- Bio — max 160 characters
- Avatar upload — square 400x400 or larger, displayed as a circle
- Banner upload — 1500x500, exact 3-1
- Profile preview card — 749x465 (exact X dark-mode layout matching in-situ profile preview)
- Default output directory — `.huzi-profile/` under the current workspace. All generated deliverables (`profile-preview.png`, `banner.png`, `avatar.png`) default to this directory.

## Hard rule — never trust default image orientations

`render_generated_image` only exposes portrait or landscape. Portrait is not 1-1. Landscape is usually ~16-9, not 3-1. Using those outputs as final X assets is a defect.

Always manufacture the canvas first, then paint onto it.

### Avatar canvas (mandatory)

```bash
convert -size 1408x1408 xc:'#111111' .huzi-profile/avatar.png
```

`read_file` that PNG to get an image_id. Then `render_edited_image` onto that id. The prompt must say keep this exact square 1-1 canvas, fill the frame, no letterbox bars.

Motif scale is mandatory. The mark must fill the circle, not sit as a badge in a field.

- Occupies 82-90 percent of the square width and height
- After X's circular crop, a 6-10 percent quiet margin remains — slightly smaller than the avatar, never half-size
- A tiny letter in a huge empty field is a defect. Redo it
- No decorative wreaths, cameo faces, or nested circles that shrink the word

No tiny text besides the mark. Type contrast in references/design-bar.md is mandatory; 40px is the avatar check size.
When writing the image prompt, never put a percentage, pixel size, or the words inner/circle-safe next to the brand name. The model will typeset those numbers (HUZI 86). Describe fill as: the letters nearly reach the circular crop on left and right, only a thin margin remains.

### Banner canvas (mandatory)

```bash
convert -size 1500x500 xc:'#111111' .huzi-profile/banner.png
```

`read_file` that PNG. Then `render_edited_image` onto that id. The prompt must say keep this exact 3-1 canvas, no added bars, no 16-9 scene.

If the edit comes back taller than 1-3 of width, discard and rerun on a fresh 1500x500 canvas. Do not ship it.

Full safe-zone math is in references/safe-zones.md. Read it before writing any banner prompt.
### Profile preview card canvas (mandatory)

After generating the 1500x500 banner and 1408x1408 avatar, assemble them into the 749x465 profile preview card so the user can directly see how their identity looks on X:

```bash
python compose_preview.py \
  --banner .huzi-profile/banner.png \
  --avatar .huzi-profile/avatar.png \
  --name "HUZI" \
  --handle "@lihu9048" \
  --bio "学习AI，分享AI" \
  --out .huzi-profile/profile-preview.png

Card layout specs (749 x 465):
- Banner area: top 749 x 250 (exact 3:1 ratio).
- Profile background: `#000000` (y 250..465).
- Avatar cutout: center `(107, 246)`, inner circular avatar radius 84 px (diameter 168 px), outer `#000000` border radius 88 px (thickness 4 px, cutting into banner).
- Action buttons (top right): circular tip button (`$`) at `(516, 266)`, pill button ("编辑个人资料") at `(560, 266)` with `#536471` outline.
- User metadata (bottom left):
  - Display name: bold `#EFF3F4`, font 21 px, at `(18, 362)`.
  - Verified badge: Twitter blue `#1D9BF0` scalloped badge + white checkmark, vertically centered beside name.
  - Handle: regular `#71767B`, font 15 px, at `(18, 394)`.
  - Bio: regular `#EFF3F4`, font 15 px, at `(18, 430)`, auto-wrapped to 710 px width.


## Banner overlap — web and mobile

X composites the circular avatar onto the banner. Web pins it to the bottom-left. Mobile also covers the bottom-left and crops extra from the top and bottom edges.

Treat the avatar overlap as a focal-content exclusion zone, not a blank canvas region. Backgrounds, texture, grids, rules, color fields, and non-critical decoration should continue across the full banner. Keep type, logos, faces, and irreplaceable focal objects outside the avatar circle and mobile crop edges.

- Avatar exclusion circle — approximately 220 px diameter, centered near x 110, y 390 on a 1500x500 banner; use a modest padded circle for checks
- Dead vertical edges — top 18 percent and bottom 18 percent for type and focal objects only
- Type band — horizontal 38–92 percent, vertical 22–78 percent by default; another position is allowed when the chosen style demands it and the avatar circle stays clear
- Full canvas — visual language must span all 1500 pixels; the left side must not become a generic blank third

Compose each style by its own rules. Never reuse a mechanical left-empty/right-full template. Do not repeat the avatar wordmark in the banner; the avatar already carries the name.

## Output format

Write the bio before the banner. The banner line must be a compression of that bio, not a new slogan.

1. IP sentence
2. Display name + character count
3. 3 handles, one preferred
4. Bio + character count
5. Banner line — 3 to 8 words copied or tightly cut from the bio. A stranger reading only the cover must recognize the same claim.
6. Pin suggestion
7. Banner brief first — live band, dead zones, bio line, which master method
8. Avatar brief — how it is derived from the banner
9. Shared hex palette
10. Assembled profile preview image (`.huzi-profile/profile-preview.png`, 749x465) — primary composite deliverable for user preview, displaying banner, avatar, name, handle, bio, and verified badge in situ.
11. Production upload assets via the canvas pipeline: `.huzi-profile/banner.png` (1500x500) and `.huzi-profile/avatar.png` (1408x1408 square).

Max 5 packs. Prefer 3.

## Naming, bio, handles

- Display name is the brand. Handle is the URL.
- Chinese users — CJK display name plus Latin handle, or bilingual like HUZI 虎子.
- x_user_search the top handles. Do not claim a handle is free if an exact username exists.
- Bio does one job. Specific beats vague. 0-2 emoji. Count after writing.
- Do not impersonate living public figures.

Style menus live in README.md (user-facing 50-style table) and references/world-styles.md (how to generate each number). Studio textures stay in references/style-packs.md.

## Visual system

Read references/design-bar.md.

Avatar is the IP mark (name / plate). Banner is the bio made visible — same claim, same words or the same three proof-objects. Same 3-5 hexes. If you hide the bio, the cover must still say what the account publishes.

Map IP to materials from the work itself

- Operator / workflow creator — paper, ink, a single tool, a wordmark that looks like a column masthead
- One-person company — letterhead, studio plate, visiting-card wordmark. The name is the firm. Not a clothing label, not a corporate gradient orb.
- Writer / editor — type on paper, lamp, annotated sheet
- Builder / engineer — graphite, one instrument
- Performer / face-IP — a real still of them, not a costume

Never dress the account as a product the person does not sell.

Invented marks — generate freely. Real named people — image-gen-edit skill.

## Style choice (after IP)

User may pick by number (01-50), English name, or Chinese name. Catalog is README.md plus references/world-styles.md.

If they say 对照 / 全部风格 / all styles, generate catalog banners only, ten per batch, 3-1 canvas, label numbers in chat. Do not emit 50 avatars until they pick.

If they pick one number, that language wins. Derive the avatar from it. Do not mix a second catalog style on the same account.

Studio textures in references/style-packs.md are the short recipe book. World-style number overrides a texture when both are named.

## What not to do

- Do not ship portrait avatars or 16-9 banners
- Do not put banner type or focal objects inside the bottom-left avatar circle or the top/bottom 18 percent; backgrounds and non-critical style elements must continue across the full width
- Do not generate 20 name lists with no visuals
- Do not use copyrighted character likenesses
- Do not export Word/PDF unless asked
- Do not ship generic AI-media slop (neural globes, particle trails, rain neon, gold serif on navy, lens flare)
- Do not costume the IP as fashion, food, gaming, or luxury goods unless that is what they publish
- Do not ship a banner whose line could sit on any other studio — it must match this bio
- Do not ship an avatar whose mark is a small island in empty space
- Do not ship two packs that share the same silhouette (black HUZI on cream). Design language must identify the pack with the name covered
- Do not ship type whose ink matches the local field, and do not hide the collision under a generic plate. Recast only the type ink (references/design-bar.md)
- Do not stop before delivering the assembled profile preview card (749x465). The user must see the full in-situ profile layout (banner + avatar + text + buttons) combined before uploading.
