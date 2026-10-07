# ZAD Train — final edit (overlay pass)

Source: the assembled 1080×1080 edit (58.7 s). It plays untouched underneath everything:
structure, transitions and backgrounds are not changed. Times below come from the word-level
`transcript.json`.

## 2026-10-07 — Round 3 notes (square format kept)

- **Challenge** and **ZAD Train transforms** panels moved to the top (y=112), above the
  speaker's head; the transforms panel was compacted to ~210 px high to fit.
- **Demo:** narration-repeating headings removed (read as a second voice-over), so the
  product recordings play alone in a larger centred window (912×570). Audio analysis of the
  source found a single voice in this section (no echo, no recording audio mixed in).
- **Phone shot at ~40 s removed:** the demo now covers the speaker until the phone shot ends
  (40.47 s) and fades out over the normal framing (host 28.3 s → 40.75 s; `demo.mp4` 12.5 s).
- **Platform supports:** points appear with no fade or movement, on his hand gestures:
  finger raised 48.6 s, hand flicks forward 50.0 s, hand drops 51.6 s.
- **With ZAD Train:** panel moved to the top; lines appear with no motion on the gestures:
  pointing sweep 54.8 s, hand to chin 56.1 s, finger raised 57.2 s.

## Visual system

- Inter 400/700, navy ink `#0E1A2B`, ZAD green accent `#17603E` (kickers, icons) and the
  brand green `#0F2F1E` (from the logo) for filled pills, checks and the demo background.
- White panels (radius 22, soft shadow), anchored bottom inside the 80% title-safe box, so the
  speaker's face stays clear.
- Motion: soft fade + 12–24 px slide, 0.4–0.5 s, `power2.out`. No bounce, no kinetic type.
- ZAD logo: white wordmark, top centre, 34 px high, the whole video (`compositions/logo.html`,
  `assets/zad-logo-white.png`, cut from the supplied logo).

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

Speaker hidden. `assets/demo/demo.mp4` (12 s, 1600×1000, muted) is cut from the supplied ZAD Train
recordings by `build-demo.sh`, cropped to the clean UI so the recordings' own marketing captions
never show. Crossfades land on the sentence boundaries.

| Step | Narration                                                        | Recording → shots                                                       | Window      |
| ---- | ---------------------------------------------------------------- | ----------------------------------------------------------------------- | ----------- |
| 1    | "A machine manual can become a learning module."                 | `Untitled_design`: PDF manual uploaded → generated course modules       | 0 – 2.7 s   |
| 2    | "A maintenance procedure can become a step-by-step training."    | `download_6`: feedback on the Hydraulic System Health slide → visual guide | 2.7 – 6.3 s |
| 3    | "An internal process can become structured content for onboarding or skills development." | `download_4`: course library → beginner-operator course setup | 6.3 – 12 s |

`Untitled_design_1` and `download_5` match `Untitled_design` and `download_4` visually and are not used.

## Rebuilding

Demo clip: `./build-demo.sh <Untitled_design.mp4> <download_6.mp4> <download_4.mp4>`.

`assets/source.mp4` is the source edit re-encoded with a keyframe every 30 frames (not
committed; large media is gitignored):

```bash
ffmpeg -y -i <source>.mp4 -c:v libx264 -crf 18 -g 30 -keyint_min 30 -pix_fmt yuv420p \
  -movflags +faststart -c:a aac -b:a 192k assets/source.mp4
```
