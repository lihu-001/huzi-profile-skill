# Design bar

Ship identity, not illustration wallpaper.

## IP before aesthetic

The image must come from what the person publishes. An AI-workflow creator gets a masthead, a page, or a tool — not a coat, a restaurant plate, or a temple seal. If you could swap the name onto a clothing brand and nothing breaks, the image failed the IP test.

## Bio and banner lock

Write the bio first. Pull the banner line from it.

- Bio "One-person studio. AI workflows, teardowns, systems you can rerun."
- Banner line "workflows / teardowns / rerun" or "systems you can rerun"
- Fail "ai systems", "CODE BUILD LEARN", or a wood field with no claim

Avatar carries the name. Banner carries the offer.

## Pass test

Ask before sending — would this look at home on a small independent studio site, a literary magazine, or a product brand sheet? If it looks like every other AI-creator banner, it fails.

## Craft rules

- One subject, one material, one light. Not a collage of metaphors.
- Palette is 3-5 hexes used as ink, metal, paper, cloth. No rainbow accents.
- Banner type is a lockup, not a caption. 3-8 words cut from the bio. Height about 16-30 percent of the 500px banner (80-150px), or the lockup fills its style module (the red plane, the Sachplakat field). Cut, tracking, stacking, and slant come from the style. A 48px sentence centered on every banner is a defect. Do not invent a second slogan.
- Surfaces must be specific — cold-pressed paper, anodized aluminum, kiln porcelain, chalk on navy board, 32-pixel tiles. "Futuristic dark background" is not a surface.
- Composition is asymmetric and quiet. Empty space may be a feature, but it must come from the selected style—not from a universal blank-left template. The style language should span the full banner.
- Avatar must read as a mark at 40px — silhouette first, detail second.
- Avatar mark fills 82-90 percent of the square. Slightly smaller than the circle, never a pea in a plate.
- Avatar inherits the banner's design language (method, type, color, space), not a photocopy of its texture. Hide the word HUZI: you should still know which pack it is.
- Banner must still work if you cover the bottom-left avatar circle. The circle may hide continuous background or non-critical texture, but never type or the key focal object.

## Type contrast

Paint the wordless ground first. Set the banner line and the HUZI mark in a later pass with the font rasterizer (PIL `ImageDraw.text` or equivalent). Cut, tracking, size, and ink all come from the chosen style — New Typography is tight grotesque in the pack's black or cream, not a caption box dropped on top of the pattern.

Keep letter edges anti-aliased. Composite type through its coverage alpha so fringe pixels stay mixed with the ground.

If the lockup and the picture are too close in value or hue — the same color, or hard to separate at a glance — recast **the entire lockup to one new ink**. Do not recast letter by letter. The new ink may leave the style palette; distinguishability beats style color rules.

Pick one color for the whole banner line, and one color for the whole avatar mark:

- Light field → near-black
- Dark field → near-white
- Mixed light and dark under the same line → a strong third color that reads on both (a vivid blue is the default), not a mix of black and white letters

Do not threshold each pixel against the ground, and do not snap semi-transparent edge pixels to solid ink — that is what makes jagged edges.

If the style needs a slant, use an italic or oblique cut, or draw the lockup at 2–4×, rotate with bicubic, downsample with Lanczos, and still composite through alpha. A 1× raster rotate plus a binary mask is a defect.

Do not add a plate, bar, or halo to solve a color collision. Then re-inspect.

Avatar check size is 40px. Banner check size is a thumbnail.

Busy fields are expected. Letter-like geometry is the field, not a substitute for the banner line or the name.

Automatic fail: type that disappears into the field; type recast letter-by-letter so the lockup is two inks; type that sits on a generic white or cream box that is not in the style; type whose edges are jagged from binary masking or per-pixel recast; banner type that is a small caption instead of a designed lockup.

## Banned defaults (automatic fail)

- Neural-network globes, node graphs, gold particle rivers
- Rain-on-black glass, cyan-purple neon alleys, visor closeups
- Navy + gold serif "AI 时代" template, red-blue brush streaks
- Glowing brains, circuit-board faces, holographic HUDs
- Stock workshop benches with floating UI arrows
- Lens flare, bokeh soup, over-smooth plastic skin on objects
- Crowded English slogan stacks (CODE / BUILD / LEARN plus a title plus a subtitle)
- Anything that needs a caption to explain it is "about AI"

## How to prompt

Name the object, the material, the light direction, the empty space, and the exact hexes. Do not name the vibe words "cinematic, ultra detailed, 8k, luxury, premium" — those pull slop. Premium comes from restraint and a real surface.

Good — a single folded sheet of gray-green paper on a limestone table, north light, one clipped corner, the rest of the square empty.
Bad — epic AI concept art of the future of intelligence, neon, particles, dramatic lighting.
