# ZAD Train — final edit (overlay pass)

Source: the assembled 1080×1080 edit (58.7 s). It plays untouched underneath everything:
structure, transitions and backgrounds are not changed. Times below come from the word-level
`transcript.json`.

## Visual system

- Inter 400/700, navy ink `#0E1A2B`, one accent `#2459E8`.
- White panels (radius 22, soft shadow), anchored bottom inside the 80% title-safe box, so the
  speaker's face stays clear.
- Motion: soft fade + 12–24 px slide, 0.4–0.5 s, `power2.out`. No bounce, no kinetic type.
- ZAD AI logo: top centre, 44 px high, the whole video (`compositions/logo.html`).

## Timeline

| Time (s)    | Narration                                                          | Treatment                                                                   | File                         |
| ----------- | ------------------------------------------------------------------ | --------------------------------------------------------------------------- | ---------------------------- |
| 0 – 2.9     | "Industrial knowledge already exists in companies."                | Speaker only                                                                |                              |
| 2.9 – 8.5   | "The challenge is how to transform that into training…"            | Lower panel: THE CHALLENGE + one line                                       | `compositions/challenge.html` |
| 8.5 – 11.7  | "That's where ZAD Train comes in."                                 | Speaker only                                                                |                              |
| 11.7 – 19.2 | Part 3: "…machine knowledge, technical documentation and internal procedures into structured learning content" | Three chips appear as each is named, lines converge into **Structured learning content** | `compositions/transform.html` |
| 19.2 – 24   | "Instead of creating each course manually…"                        | Speaker only                                                                |                              |
| 24 – 28.7   | "…adapted to their equipment, processes and operational needs."    | Lower panel: three pills, one per word                                      | `compositions/adapted.html`  |
| 28.3 – 40.3 | The three demo sentences                                           | **Speaker hidden.** Full-frame ZAD Train demo, 3 screenshots, slow push-in  | `compositions/demo.html`     |
| 40.3 – 47.7 | "That way ZAD Train helps companies…"                              | Speaker only                                                                |                              |
| 47.7 – 53.5 | "The platform supports content creation, expert validation…"       | Lower panel: three icon chips, one per feature                              | `compositions/features.html` |
| 54.2 – end  | "Turn knowledge into training, transfer skills, build expertise."  | Lower panel: three checked lines                                            | `compositions/closing.html`  |

Chip order in Part 3 follows the narration (machine knowledge → technical documentation →
internal procedures) so each item lands on the word.

## Demo section (28.3 – 40.3 s)

| Step | Narration                                                        | Screen          | Window      |
| ---- | ---------------------------------------------------------------- | --------------- | ----------- |
| 1    | "A machine manual can become a learning module."                 | `screen-1`      | 0 – 2.7 s   |
| 2    | "A maintenance procedure can become a step-by-step training."    | `screen-2`      | 2.7 – 6.3 s |
| 3    | "An internal process can become structured content for onboarding or skills development." | `screen-3` | 6.3 – 12 s |

## Assets still to come

- `assets/zad-ai-logo.svg` — **placeholder**. Replace with the ZAD AI logo (light version for
  the grey wall; SVG or a transparent PNG).
- `assets/demo/screen-1.svg`, `screen-2.svg`, `screen-3.svg` — **placeholders**. Replace with
  the ZAD Train screenshots, then set each step's push-in focus on the key UI element.

## Rebuilding

`assets/source.mp4` is the source edit re-encoded with a keyframe every 30 frames (not
committed; large media is gitignored):

```bash
ffmpeg -y -i <source>.mp4 -c:v libx264 -crf 18 -g 30 -keyint_min 30 -pix_fmt yuv420p \
  -movflags +faststart -c:a aac -b:a 192k assets/source.mp4
```
