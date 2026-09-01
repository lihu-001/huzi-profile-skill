---
name: huzi-profile
description: Build a complete X (Twitter) new-user profile pack — display name, handle, bio, avatar, and banner. Use when the user runs /huzi-profile, or asks for X or Twitter profile setup, 取名, 简介, 头像, 封面, handle ideas, style number 01-50, 对照风格, or a personal brand kit. Design from the personal IP goal first. Banner before avatar. Aim at award-level identity (D and AD / ADC / JAGDA methods), not stock moodboards. Always produce true 1-1 avatars and 3-1 banners with safe zones.
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
6. Stunning test — hide the name. Would a design jury remember one decision (one cut of type, one material, one spatial idea)? If it only looks tidy, redo.

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

## Hard rule — never trust default image orientations

`render_generated_image` only exposes portrait or landscape. Portrait is not 1-1. Landscape is usually ~16-9, not 3-1. Using those outputs as final X assets is a defect.

Always manufacture the canvas first, then paint onto it.

### Avatar canvas (mandatory)

```bash
convert -size 1408x1408 xc:'#111111' /home/workdir/artifacts/x-avatar-1x1.png
```

`read_file` that PNG to get an image_id. Then `render_edited_image` onto that id. The prompt must say keep this exact square 1-1 canvas, fill the frame, no letterbox bars.

Motif scale is mandatory. The mark must fill the circle, not sit as a badge in a field.

- Occupies 82-90 percent of the square width and height
- After X's circular crop, a 6-10 percent quiet margin remains — slightly smaller than the avatar, never half-size
- A tiny letter in a huge empty field is a defect. Redo it
- No decorative wreaths, cameo faces, or nested circles that shrink the word

No tiny text besides the mark. High contrast at 40px.
When writing the image prompt, never put a percentage, pixel size, or the words inner/circle-safe next to the brand name. The model will typeset those numbers (HUZI 86). Describe fill as: the letters nearly reach the circular crop on left and right, only a thin margin remains.

### Banner canvas (mandatory)

```bash
convert -size 1500x500 xc:'#111111' /home/workdir/artifacts/x-banner-3x1.png
```

`read_file` that PNG. Then `render_edited_image` onto that id. The prompt must say keep this exact 3-1 canvas, no added bars, no 16-9 scene.

If the edit comes back taller than 1-3 of width, discard and rerun on a fresh 1500x500 canvas. Do not ship it.

Full safe-zone math is in references/safe-zones.md. Read it before writing any banner prompt.

## Banner overlap — web and mobile

X composites the circular avatar onto the banner. Web pins it to the bottom-left. Mobile also covers the bottom-left and crops extra from the top and bottom edges.

Treat these regions as dead. No type, logos, faces, globes, trails, or focal objects.

- Dead left — the left 32 percent of the width
- Dead bottom-left box — left 28 percent x bottom 55 percent (avatar sits here)
- Dead vertical edges — top 18 percent and bottom 18 percent (mobile crop)
- Live band — horizontal 38–92 percent, vertical 22–78 percent

Default type and motifs to the center-right of the live band. Never place a title where the user's screenshot problem happened — mid-left, overlapping the avatar.

Do not repeat the avatar wordmark on the left of the banner. The avatar already occupies that corner.

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
10. Generated assets via the canvas pipeline

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
- Do not put banner type or motifs in the left 32 percent or the top/bottom 18 percent
- Do not generate 20 name lists with no visuals
- Do not use copyrighted character likenesses
- Do not export Word/PDF unless asked
- Do not ship generic AI-media slop (neural globes, particle trails, rain neon, gold serif on navy, lens flare)
- Do not costume the IP as fashion, food, gaming, or luxury goods unless that is what they publish
- Do not ship a banner whose line could sit on any other studio — it must match this bio
- Do not ship an avatar whose mark is a small island in empty space
- Do not ship two packs that share the same silhouette (black HUZI on cream). Design language must identify the pack with the name covered
