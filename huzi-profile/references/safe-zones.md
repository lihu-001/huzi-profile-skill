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

Dead zones (must be empty of type and focal art)

- Left gutter — x 0-480 (32 percent)
- Avatar disk on web — roughly a 200-220 px circle centered near x 110, y 390. Pad to a box x 0-420, y 220-500
- Mobile vertical crop — y 0-90 and y 410-500

Live band (all titles, subtitles, globes, trails)

- x 570-1380
- y 110-390

Preferred type block

- x 620-1100
- y 160-340

Preferred motif (network, landscape, object)

- x 1100-1450
- y 120-380

## Prompt fragments (paste)

Avatar
Keep this exact 1-1 square canvas. Fill the frame. No letterbox, no 2-3 portrait. Center the emblem so a circular crop keeps the whole motif. Letters nearly reach the left and right of the circle. Never write 84, 86, percent, or px next to the brand name.

Banner
Keep this exact 3-1 canvas (three times wider than tall). No 16-9, no added bars. Leave the left third empty. Leave the bottom-left quarter empty for the circular avatar. Keep all type and focal objects inside the middle-right live band. Keep type out of the top and bottom fifths so mobile crops cannot cut letters.

## Check before sending to the user

- Avatar file reads as width == height
- Banner file reads as width == 3 * height (allow 1 percent)
- Cover mock in your head — drop a circle on the bottom-left. If it covers a letter or a globe, reject and repaint


## Avatar fill

The circular crop is the frame. Content must nearly fill it.

- Mark width ≈ 0.84-0.90 of canvas
- Quiet gutter ≈ 5-9 percent on all sides after the circle cuts the corners
- Fail: a 30 percent word on a 100 percent field (Garden and Macro badges did this)
- Pass: Night-editor torn ring and Indie pixel HUZI — type is the picture
