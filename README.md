# Al-Hayat — al-Tariqah al-Asriyah teaching companion

A complete static GitHub Pages repository for the supplied Part 1 and Part 2 scans of **الطريقة العصرية في تعليم اللغة العربية**, by Dr. Abdul Razzaq Iskandar.

Teaching presentation prepared by **Dr. Imran Hayat**, الحیات مرکز علوم اسلامیہ.

## Use and deploy

1. Extract this ZIP. Upload the files and folders **inside it** to your repository root.
2. In GitHub **Settings → Pages**, deploy from your main branch and the root folder.
3. Keep `index.html`, `data`, `fonts`, and `sources` in their supplied relative locations.

No build, server, API key, database, account or CDN is required. You may open `index.html` locally; browser-local storage behavior can vary under `file://`. GitHub Pages is the intended hosting environment. An empty `.nojekyll` file is included.

## Coverage

- Part 1: all 75 lessons.
- Part 2: all 42 lessons.
- All 311 original PDF pages are available as on-demand page images.
- Original numbered exercises, translations, grammar identification, verb transformations, parsing, dictation, numeric expressions, sentence ordering, letters and composition have page-linked worked answers.
- Dictation lessons include the original word/sentence material and spelling guidance. The final Quran reading sections are identified as reading material rather than fabricated numbered exercises.
- Additional learning material is separately labelled: 117 concise lesson guides, editorial examples, 234 MCQs and 351 written-practice prompts.
- Vocabulary cards provide selected contextual Arabic/Urdu/English meanings; the source pages retain the books' complete printed vocabulary tables. Repeated vocabulary across lessons is not counted as unique dictionary coverage.

See `COVERAGE.md` for every lesson's page range, group count and answer count. `TEACHER_KEY.md` contains the complete current worked-answer bank as readable text. `data/course.json` is authoritative; the website loads `data/course.js`.

Original exercises sometimes ask for personal answers, unrestricted composition, or an example sentence. Such answers are full models, not uniquely correct strings. The app lets learners compare meaning and grammar with a model rather than falsely marking every wording difference wrong. Multiple valid forms and inferred vocalizations are explained where relevant.

## Learning flow

Choose a part and lesson, then use:

1. **سبق سمجھیں** — core teaching point and a worked editorial example.
2. **الفاظ و معانی** — selected contextual vocabulary in Urdu and English.
3. **اصل مشقوں کے حل** — original tasks, writing area, hint, worked answer, explanation and self-review. Long exercise sets paginate at 12 answer components so every item remains reachable without an overwhelming page.
4. **خود آزمائیں** — additional MCQs with feedback and written recall exercises.
5. **اصل صفحہ** — source-image reader, page selection, previous/next, zoom, and the complete part including front matter.

Search includes lesson titles, teaching points, vocabulary and original solution text. Source links beside exercise groups open their exact original page. The coverage page lets teachers audit the supplied sequence.

## Reading and performance

- Urdu uses **Jameel Noori Nastaleeq**; Arabic examples use **Amiri**; English uses the system sans font.
- Installed Jameel is used via `local()`. The bundled Jameel was optimized while retaining all original Unicode mappings and shaping closure. Nafees is a compact fallback. Authors retain the font rights; attribution is retained in the font metadata.
- Jameel is approximately 7.2 MB, so its first download is still substantial. Text is immediately readable with a fallback while it loads; later visits may reuse cached files. No remote font service is used.
- Original source pages load only when opened; the homepage does not download 311 page images or construct hidden lesson exercises.
- Only one lesson panel is rendered at a time. Exercises paginate. Search text is normalized once and reused.
- Header height is CSS-owned, including the border. There is no resize-measurement feedback loop.
- Day/night follows the initial system preference and remembers the user's choice before first paint. Both palettes have explicit text, form, answer, feedback and example colors.
- Automatic progress, written drafts and self-review are stored under `al-hayat-asriyah-progress-v1`. Theme uses a separate key. The earlier Nahw project's progress is untouched. A storage failure does not block reading or practice.

## Edit and verify

Edit `data/course.json`, then regenerate derived files:

```sh
python scripts/sync-data.py
```

To run the developer checks:

```sh
npm ci
npm run check
```

The only npm dependency is for developer-side DOM tests; the deployed site does not use npm or fetch packages. Tests cover all 117 lessons, original exercise pagination, answer reveals, source-page paths, theme persistence, MCQ locking/retry, progress, blocked storage, safe escaping, joined-script font boundaries and representative contrast pairs.

Browser layout testing was unavailable in the authoring environment. DOM checks do not certify visual layout, assistive-technology behavior, or real network loading time. No measured live speed claim is made.

## Source and editorial identity

The two supplied scans identify the original books and author. Part 1 is the file named `attariqatul asriyah Part 1-share1.pdf`; the file named `الطریقۃ العصریۃ - Tareeqa tul Asria.pdf` is Part 2. Their SHA-256 hashes are retained in the metadata. The site attributes the books and distinguishes Dr. Imran Hayat's instructional presentation from the original authorship.

The source contents page in Part 2 contains some mismatched page references. Lesson boundaries were checked against the actual main lesson headings. Original page images remain available for comparison, including the original numbering.
