# AutoSuspend

**Automatically suspend old cards in Anki after a specified number of days.**  

AutoSuspend helps reduce daily review load by suspending cards in specified decks once they reach a set age.

---

## Context

For context, I'm learning Japanese and I made this add-on for myself as I was getting tired of daily endless Anki reviews (1h+). All the time I'm spending reviewing old cards could be better spent immersing and hence being exposed to words **while enjoying content**. Of course, Anki is great and it works but I'm a bit sick of it now after years of use. The idea behind this add-on is to help me learn new words by reviewing them but only in a limited time window (1 week) such that I don't get overwhelmed by too many reviews. I see it as a little help to be more familiar with new words. After that, I can just encounter them in the wild and learn them naturally. It's ok if I forget them after a week, the idea is to focus on being exposed to words in context rather than memorizing them in Anki forever. If I get enough immersion, daily life is actually the most enjoyable SRS!

I was inspired by [MattVsJapan's video](https://youtu.be/u3sqHvdpBwM?si=JnWrAofiknKpGEuN) to make this add-on.


---

## Features

- Suspend cards automatically after a configurable number of days.
- Target specific decks individually with their own thresholds.
- Optional pop-up summary after each sync.
- Triggered **after each sync**

---

## Installation

1. Download the add-on folder into your Anki `addons21` directory. For example:  
   `~/Library/Application Support/Anki2/addons21/AutoSuspend`
2. Restart Anki.
3. Configure the add-on by editing `config.json` in the add-on folder. Go to "Tools" -> "Add-ons" -> "AutoSuspend" -> "Config"

---

## Configuration

Edit `config.json` like this:

```json
{
  "decks": {
    "Japanese tmp": 7,
    "French": 14
  },
  "show_popup": true
}
```

- Key = deck name exactly as it appears in Anki.
- Value = number of days after which cards will be suspended.
- show_popup = true to display a summary pop-up after each sync, false to disable it.

Only decks listed here will be affected.

## Usage

- The add-on runs automatically after every sync.
- Suspended cards will no longer appear in reviews until manually unsuspended.
- If a deck does not exist in the current profile, it will be skipped safely.
