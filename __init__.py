from aqt import mw
from aqt.qt import QMessageBox
from aqt import gui_hooks
import datetime

# === LOAD CONFIG ===
config = mw.addonManager.getConfig(__name__) or {}
DECKS_CONFIG = config.get("decks", {})
SHOW_POPUP = config.get("show_popup", True)  # default: show popup

if not DECKS_CONFIG:
    if SHOW_POPUP:
        QMessageBox.information(mw, "AutoSuspend", "[AutoSuspend] No decks defined in config.")
else:
    def suspend_old_cards():
        col = mw.col
        total_suspended = 0
        deck_summaries = []

        existing_decks = set(col.decks.all_names())

        for deck_name, suspend_days in DECKS_CONFIG.items():
            if deck_name not in existing_decks:
                deck_summaries.append(f"Skipped '{deck_name}' (not in this profile)")
                continue

            cutoff_time = datetime.datetime.now() - datetime.timedelta(days=suspend_days)
            cutoff_ts = int(cutoff_time.timestamp())

            # Parameterized query for safety
            query = """
                SELECT c.id
                FROM cards c
                JOIN decks d ON c.did = d.id
                WHERE d.name = ?
                  AND (c.id / 1000) < ?
                  AND c.queue != -1
            """
            cids = col.db.list(query, deck_name, cutoff_ts)
            count = len(cids)

            if count:
                col.sched.suspend_cards(cids)
                col.reset()
                mw.reset()
                deck_summaries.append(
                    f"In '{deck_name}': {count} card{'s' if count != 1 else ''} suspended after {suspend_days} day{'s' if suspend_days != 1 else ''}"
                )
                total_suspended += count
            else:
                deck_summaries.append(f"No cards to suspend in '{deck_name}'")

        # Final summary
        msg_lines = ["[AutoSuspend] Run summary:"]
        msg_lines += deck_summaries
        msg_lines.append(f"Total: {total_suspended} card{'s' if total_suspended != 1 else ''} suspended")
        msg = "\n".join(msg_lines)

        print(msg)
        if SHOW_POPUP:
            QMessageBox.information(mw, "AutoSuspend", msg)

    # === TRIGGER ONLY AFTER SYNC ===
    gui_hooks.sync_did_finish.append(suspend_old_cards)
