# Informational Style Canon — Reference

Depth beyond the rules in SKILL.md. Source — Maxim Ilyahov, Ludmila Sarycheva, «Пиши, сокращай» (*Write, Shorten*), 4th ed., 2024. Open this when you need an exact quote, a breakdown of a specific technique, or a before/after example from the primary source.

Quotes and example UI strings stay in Russian — they're the author's exact wording and concrete specimens, not prose to translate. The explanatory text around them is English.

**Table of contents:**
- [The Three Criteria](#the-three-criteria-of-informational-style) · [Useful Action](#useful-action-goal-tasks)
- [Stop-Words](#stop-words--five-groups) · [Канцелярит and Verbs](#канцелярит-and-verbs)
- [Organizing Longer Text: Instruction](#organizing-longer-text-instruction) · [Paragraph](#paragraph) · [Tone and Fakeness](#tone-and-fakeness)
- [Sources](#sources)

⚠️ The book also covers genres beyond the interface (press releases, cold email, slide decks, landing pages) — that's content-marketing/copywriting territory, not microcopy. Only what transfers directly to a button, an error, an empty state, a tooltip is kept here.

---

## The Three Criteria of Informational Style

Not "just shorter" — three separate, checkable properties:

Ilyahov and Sarycheva frame информационный стиль not as a house style but as a **set of techniques for improving business text** — something you apply and check, not a taste you have.

- **Кратко (Brief)** — no wasted words, but never at the expense of meaning.
- **Ясно (Clear)** — the thought lands immediately, not after decoding.
- **Убедительно (Convincing)** — people listen and act on it.

Four levels at which a text can fail (check in this order — largest to smallest):
1. **Useful action** — the text promises a benefit and delivers it.
2. **Words** — no word the reader trips over.
3. **Sentences and paragraphs** — something for the eye to grab onto, no fog.
4. **Structure and delivery** — help solve the text's task rather than get in its way.

**Criterion:** if a text "isn't working," check top-down — useful action first, words second. Grooming stop-words in a text with zero useful action is fixing the wrong layer.

---

## Useful Action, Goal, Tasks

A three-part support structure answering three different questions — the ones most often confused:

- **Полезное действие (useful action)** — the reader's own reason to read this. It answers *why would they want to?*, and it is a promise made to them, not a description of the text.
- **Цель (goal)** — the author's side, kept internal: what should be different in the reader's picture of the world afterwards. Where the text is going.
- **Задачи (tasks)** — the concrete moves that get there. Goal is *where*, tasks are *how*.

The three get confused constantly, and the confusion always runs the same way: an author states their own goal and calls it the reader's useful action.

**Informing is not a useful action.** Nobody wants to be informed for its own sake; information is wanted in service of something — solving a problem, or feeling something. Direct application to an interface: a screen that just "displays data" never answers "why should I look at this right now" — a good error, empty state, or onboarding line always does.

**Criterion:** for any interface string — "why would the user themselves want to read this?" If the answer is "to stay informed," that's informing, not usefulness, and the line should be reformulated around a decision or an action.

---

## Stop-Words — Five Groups

**Стоп-слова (stop-words)** are words and phrases that come out with no loss of meaning — the book's list of names for them is all waste: junk, chaff, slag, scale.

And the limit is stated in the same breath, which is the part usually dropped when this gets repeated: removing them makes a text **cleaner. Not more interesting, not more useful — cleaner.** Cutting stop-words from a text with no useful action produces clean nothing.

An important caveat — this isn't mechanically crossing words off a list. A stop-word is a **flag, not a verdict**: it forces the choice between what the sentence needs and what it merely carries. Read it as *something here might be off*, then decide.

**1. Вводные конструкции (Parenthetical constructions)** — anything introduced by paired commas, dashes, or parentheses, usually removable without loss: the-obvious ("не секрет, что…" — "it's no secret that…"), hedges («по-моему», «если честно», «точнее»), verbal numbering («во-первых»), parentheses («Всё, что стоит в скобках, намекает своим видом, что оно неважно» — "anything in parentheses signals by its very form that it's unimportant"), «кстати» ("by the way" — «слова "кстати" и "к слову" выдают неуверенность автора», "these words betray the author's own uncertainty").

**2. Неопределённое (Vagueness)** — words that flag imprecision where precision either isn't needed or is exactly what's needed (примерно, около, более, некий, какой-то — roughly, about, more than, some, some kind of). «Слова вроде "более", "около", "примерно" и "не менее" не делают текст более понятным.» ("Words like 'more than,' 'about,' 'roughly' don't make a text clearer.") Example: «Более 10 лет производим товары» → «Производим товары с 2012 года» ("We've made goods for over 10 years" → "We've made goods since 2012").

**3. Заумные слова (Overwrought/jargon words)** — smart-sounding synonyms chosen to seem clever rather than to be precise: «Мы говорим о заумности, которую используют, чтобы казаться умнее» ("We're talking about the kind of jargon used to seem smarter") — not to be confused with real domain terms, which should stay.

**4. Навязанные оценки (Imposed judgments)** — a subjective characterization standing in for a fact (tasty, reliable, high-quality, powerful). Core claim: **«Факты сильнее оценок.»** ("Facts beat judgments.") "False sense of work done": a text loaded with judgments gives the author an illusion of having written something convincing — the illusion is false. An **усилитель** (intensifier) is "a judgment stacked on another judgment" (maximally favorable, absolutely free) — almost always removable at no cost to meaning. Test: cover the company/product name — do the judgments and intensifiers still work without it? If not, it's not a judgment, it's empty noise.

**5. Штампы (Stock phrases)** — a phrase «которая переходит из одного текста в другой в одном и том же виде» ("that moves from one text to another in the exact same form") — team of professionals, wide range, individual approach. The author's own metaphor: **«Штампы — это корм для кота, который предсказуемо лежит на одном месте.»** ("Stock phrases are cat food that predictably sits in the same spot.") Test for a stock phrase: try swapping one word in the combination — if it breaks into nonsense, it was a stock phrase (a Russian example: «хранительница гаража» — "keeper of the garage," sounds absurd precisely because the original «хранительница очага», "keeper of the hearth," was a dead stock phrase, not a living one).

**Criterion (for all five groups at once):** can the word be crossed out without losing meaning? Yes → cross it out. Does the word only "work" propped up by the surrounding brand/context, with none of its own substance? Check the same way for UI copy: does the button/error wording still work with the brand context stripped away?

🚩 A judgment standing in for a fact in an interface ("Fast loading!" instead of an actual time) · an intensifier on nothing ("absolutely free" instead of "free") · an unexamined stock phrase ("team of professionals" in a job listing).

---

## Канцелярит and Verbs

*Канцелярит* — bureaucratese: the disease of turning simple actions into abstract, faceless processes. No single English word covers it; "officialese" or "red-tape language" gets close.

**State verbs instead of action verbs** — «глагол обозначает не действие, а состояние или его изменение» ("the verb names a state or its change, not an action") — быть, являться, находиться, предполагать, указывать (to be, to constitute, to be located, to presuppose, to indicate). If a real action is hiding behind a state verb, bring it back.

**Turn nominalizations back into verbs.** Marker: «осуществлять / реализовывать / проводить / обеспечивать» ("to carry out / to implement / to conduct / to ensure") sitting next to a noun. «Компания осуществляет поставку оборудования» → «Компания поставляет оборудование» ("The company carries out the delivery of equipment" → "The company delivers equipment").

**Passive voice → active.** «Ваше заявление было рассмотрено комитетом» → «Комитет рассмотрел ваше заявление» ("Your application was reviewed by the committee" → "The committee reviewed your application"). Caveat: switching voice can shift which noun is the sentence's main character — check that meaning didn't get lost along with the passive.

**Cinematic sentences — the formula "person + does + this."** «В фильме должны участвовать люди, которые будут совершать действия. Чем больше в тексте людей и действий, тем яснее.» ("A film needs people in it who perform actions. The more people and actions in the text, the clearer it is.") Direct application to errors and empty states: not «Данные отсутствуют» ("Data absent" — no hero, no action), but «Вы ещё не добавили контактов» ("You haven't added contacts yet" — the hero is the user, the action is what they haven't done).

**Six techniques against канцелярит** (the order matters — this is a decompression sequence, not a menu):
1. **Сначала суть, потом причина (Point first, reason second)** — put the hero and the action next to each other, near the sentence's start, with no qualifiers wedged between them.
2. **«Мама мыла раму» ("Mom washed the frame")** — a simple subject plus a simple predicate, no clutter.
3. **Deeds, not processes** — «Обеспечение безопасности» → «Арестовали хулиганов» ("Ensuring security" → "Arrested the troublemakers").
4. **Enumerations → a list** — three or more parallel items get formatted as a list, not dragged through a single sentence.
5. **A useful heading** — the heading names the substance, not its own importance («Уважаемые жильцы!» → «Отключение горячей воды», "Dear residents!" → "Hot water shutoff").
6. **Active care** — don't just inform, help: «Во избежание самопроизвольного перемещения предметов личного багажа убедительная просьба…» → «Придерживайте сумки, чтобы они не катались по вагону» ("To prevent the spontaneous displacement of personal luggage items, kindly…" → "Hold onto your bags so they don't roll around the car").

> **«Канцелярит ворует ваши деньги и время.»** ("Канцелярит steals your money and your time.")
> **«Не информировать, а помогать.»** ("Not to inform — to help.")

**When to keep канцелярит** — the book explicitly carves out an exception: legal/regulatory wording, where a term's precision outweighs liveliness, shouldn't be simplified at the risk of misstating an obligation. In an interface, this covers consent text and legal notices — don't confuse those with an ordinary error or tooltip.

**Criterion:** the four-step decompression algorithm for any bureaucratic sentence — 1) is there a real action hiding behind a state verb? 2) who performs it — a hero, or a vague "is being carried out"? 3) put the hero and the action next to each other, no insertions between them; 4) move that pair toward the start of the sentence.

🚩 "Data was not processed by the system" (passive voice, no hero, no cause) instead of "Couldn't process the data — check the format" · an address-heading instead of a substance-heading on a notification · legal канцелярит where a human error message was needed (and the reverse — an over-simplified consent notice where precise legal wording was required).

---

## Organizing Longer Text: Instruction

Relevant to `buro:copy` specifically for multi-step onboarding sequences and step-by-step help articles — this is the one organizing pattern from the book's structure chapter that transfers directly to UI text, unlike the surrounding genre patterns (news, story, digest, review), which don't.

> «Инструкция — для решения задачи нужно совершить некие действия в определённой последовательности.»
> ("Instruction — solving the task requires performing certain actions in a specific order.")

**Three aspects to track for any instruction** — hronology, context, visualization:
- **Chronology** — «Действия в инструкции должны перечисляться в том порядке, в котором совершаются» ("actions in an instruction must be listed in the order they're actually performed") — never reordered for narrative effect the way a "hook, then flashback" story might be.
- **Context** — the reader needs to know *why* a step matters before being asked to do it, not after.
- **Visualization** — a step the reader can't picture (or see, via a screenshot/icon) is a step they'll get wrong or skip.

**Modules as a structural unit** (from the same organizing-text material, applicable to a settings page or FAQ broken into sections): a module is «законченный рассказ о чём-то одном… самостоятельная единица смысла, его можно читать в отрыве от остальных» ("a complete account of one single thing… a self-contained unit of meaning, readable in isolation from the rest"). A help article or a settings screen split into named sections should pass the same test a magazine module does: can each section stand alone if the reader jumps straight to it?

**Criterion:** for a multi-step onboarding flow or help article — does each step name the action in the order it's actually performed, with the reason given before the step rather than after? And can a reader who jumps to step 4 directly still understand what to do, or does it silently depend on having read steps 1–3?

🚩 A tutorial sequence reordered for "narrative flow" rather than execution order — the reader now has to hold a step in memory before it's relevant. · A help-article section that only makes sense if read start to finish, defeating the point of splitting it into sections at all.

---

## Paragraph

Applies to any UI text longer than one line — help copy, an onboarding paragraph, an expanded description in settings.

**Paragraph structure** — three parts: «называет главную мысль; раскрывает её; подводит итог» ("states the main idea; unpacks it; wraps it up"). One-topic rule: one paragraph, one idea, read "in a single breath."

**Paragraph autonomy** — the first sentence should be self-contained, never starting with "for example" or "although" (words that require preceding context a paragraph read in isolation may not have). **Autonomy test:** read only the first sentence of every paragraph in sequence — if the overall picture is clear from just those, the paragraphs are built correctly.

**The last sentence** of a paragraph wraps up and bridges to the next one — it doesn't just trail off mid-thought.

**Digression test:** for any inserted detail, ask "does this deserve its own paragraph?" If yes — it's important, keep it as a full paragraph. If it's just a passing aside — cut it without regret rather than leaving it as a stray tail hanging off someone else's paragraph.

**Criterion:** does a paragraph's first sentence read as meaningful with nothing above it? No → the paragraph isn't autonomous, and it will fall apart under selective reading (which is almost always how UI text actually gets read).

---

## Tone and Fakeness

Extends the "Voice and tone" section in SKILL.md with the primary source's definitions.

**Тональность (tone)** is the part of a text the reader never audits. Content gets evaluated and argued with; tone is absorbed. The book's comparison is film music — few viewers notice it, every viewer feels the mood it sets.

Four ingredients of tone: subject matter, the author's attitude toward themselves and others, empathy, and erudition/life experience. The author's own conclusion: "words and jokes are born on their own, as a consequence of internal attitudes" — meaning tone can't be pasted on top in a separate editing pass if the underlying attitude doesn't match it.

**Fakeness (Фальшь)** — the central concept for interface text that tries to sound "more human" than it actually is:

**The best tone is the author's own.** Fakeness appears in two places, both mechanical: where the author performs someone they are not, and where ingratiation is used to cover a self-interested motive. The book's observation on the second is the useful one for product work — readers are fine with being sold to, and not fine with being handled.

**Fakeness test:** does the message try to sound friendlier, more excited, or more humble than the actual situation calls for (an error, a payment, a rejection)? The gap between the moment's real emotional temperature and the text's put-on tone — that gap is fakeness, and the reader registers it before the content, every time.

🚩 An excited tone on an action the user isn't happy about (a payment, a deletion, a decline) · an apologetic tone where a plain statement of fact was needed · a joke on an error screen — irony on a negative event always reads as fake, never as lightness.

---

## Sources

Maxim Ilyahov, Ludmila Sarycheva, *Пиши, сокращай. Как создавать сильный текст* (*Write, Shorten*), 4th ed. (Alpina Publisher, 2024) · supplementary materials and video course — sokratil.ru/electro
