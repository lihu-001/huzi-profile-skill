# X avatar and banner safe zones

Read this before generating profile images.

## Why default renders fail

- Portrait generate = extra bars above and below a circular motif. Not 1-1.
- Landscape generate = typically 16-9. X banner is 3-1 (three times wider than tall). A 16-9 file looks like a tall strip on the profile and shoves content into the avatar.
- The avatar is a separate layer X draws on top of the banner. Anything in the overlap is gone on the live profile even if the PNG looks fine in chat.

## Mandatory canvas sizes

| Asset | Canvas | Ratio | Command |
| --- | --- | --- | --- |
| Avatar | 1408 x 1408 | 1-1 | convert -size 1408x1408 xc:'#111111' /home/workdir/artifacts/x-avatar-1x1.png |
| Banner | 1500 x 500 | 3-1 | convert -size 1500x500 xc:'#111111' /home/workdir/artifacts/x-banner-3x1.png |

Paint with render_edited_image on the read_file id of that canvas. Keep the canvas ratio. Do not ask the model to "look square" inside a portrait frame.

## Banner coordinates on a 1500 x 500 file

Origin is top-left.

Focal-content exclusion zones

- Avatar disk on web — roughly a 200-220 px circle centered near x 110, y 390. Check with a modest padded circle
- Mobile vertical crop — y 0-90 and y 410-500

These zones are not blank-canvas requirements. Backgrounds, paper grain, grids, rules, color fields, and non-critical decoration should continue through them. Keep type, logos, faces, and irreplaceable focal objects outside them.

Default type band

- x 570-1380
- y 110-390

Preferred type block

- x 620-1100
- y 160-340

Preferred focal motif

- x 1100-1450
- y 120-380

These are defaults, not a universal right-half template. A style may use another composition when the text and focal content remain clear of the avatar circle and mobile crop edges. The visual language must span the full 1500 px width.

## Prompt fragments (paste)

Avatar
Keep this exact 1-1 square canvas. Fill the frame. No letterbox, no 2-3 portrait. Center the emblem so a circular crop keeps the whole motif. Letters nearly reach the left and right of the circle. Never write 84, 86, percent, or px next to the brand name.

Banner
Keep this exact 3-1 canvas (three times wider than tall). No 16-9, no added bars. Carry the style language across the full width. The bottom-left avatar circle may cover background and non-critical decoration, but never type, a face, a logo, or the key focal object. Keep type out of the top and bottom fifths so mobile crops cannot cut letters. Do not default to a blank-left/right-full composition.

## Check before sending to the user

- Avatar file reads as width == height
- Banner file reads as width == 3 * height (allow 1 percent)
- Cover check — place a roughly 220 px circle near x 110, y 390. If it covers type or the key focal object, reject and repaint; covering continuous background or non-critical texture is acceptable
- Type contrast — every letter of the banner line and of HUZI reads against the local field (references/design-bar.md)


## Avatar fill

The circular crop is the frame. Content must nearly fill it.

- Mark width ≈ 0.84-0.90 of canvas
- Quiet gutter ≈ 5-9 percent on all sides after the circle cuts the corners
- Fail: a 30 percent word on a 100 percent field (Garden and Macro badges did this)
- Pass: Night-editor torn ring and Indie pixel HUZI — type is the picture

## Profile preview card coordinates (749 x 465)

When compositing the final in-situ preview card for user inspection:

| Element | X | Y | Dimensions / Radius | Style / Color |
| --- | --- | --- | --- | --- |
| Canvas | 0 | 0 | 749 x 465 | Background `#000000` |
| Banner | 0 | 0 | 749 x 250 | Scaled from 1500x500 (exact 3:1) |
| Profile panel | 0 | 250 | 749 x 215 | `#000000` |
| Avatar border | 19 | 158 | d=176 px, r=88 px, center (107, 246) | Circle `#000000`, 4 px stroke |
| Avatar mask | 23 | 162 | d=168 px, r=84 px, center (107, 246) | Antialiased circular crop of 1:1 avatar |
| Tip button ($) | 516 | 266 | 44 x 44 px, r=22 px | Circular outline `#536471`, `$`, centered |
| Edit button | 560 | 266 | 166 x 44 px, r=22 px pill | Outline `#536471`, bold text `#EFF3F4` |
| Display name | 18 | 362 | Bold 21 px | Text `#EFF3F4` |
| Verified badge | name_end + 6 | 362 (centered) | 20 x 20 px | Scalloped circle `#1D9BF0`, white checkmark |
| Handle | 18 | 394 | Regular 15 px | Text `#71767B` |
| Bio | 18 | 430 | Regular 15 px, line-height 20 px | Text `#EFF3F4`, wrap at 710 px |
