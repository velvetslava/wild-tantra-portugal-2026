# Wild Tantra review system

Status: working and tested end to end on 4 August 2026.

## Published page

https://olymarkes.github.io/wild-tantra-portugal-2026/

The page supports Russian and English review states. Review events use document ID `wild-tantra-portugal-2026`, so they can be filtered separately from Guthrie events in the shared archive.

## Where submitted notes go

Shared archive:

https://docs.google.com/spreadsheets/d/1lndxrU_GgkSgxifjhS3gotEKyhTTTIyZUgkKrv8-02Q/edit

Google Form receiver:

https://docs.google.com/forms/d/1DSpckSG937IGjLPwK5HknDXZo6sz06yZo7POaRhxuC4/edit#responses

Each saved block note, deleted local note, or saved general comment creates a separate immutable event. The payload includes the event ID, document ID, reviewer, language, action, block title, original excerpt, comment, suggested replacement, timestamp, page URL, and a JSON backup.

## Reliability behavior

- Text being typed is kept as a local draft.
- Saving records the note in local history immediately.
- Submitted events enter a local outbox and are sent to the shared archive.
- Failed events retry when the page loads again or the connection returns.
- The interface distinguishes local drafts, waiting-to-sync events, and synced events.
- The local JSON backup can be downloaded before clearing browser data.

The shared Google Sheet is a private write archive. Like the Guthrie implementation, the public page does not read the private Sheet back into another reviewer’s browser; doing so would require publishing review data or adding an authenticated read service.

## Verification

After changes to review code:

1. Test Russian and English modes.
2. Test desktop and mobile widths.
3. Save one clearly labelled system-test note.
4. Confirm its `Document:` value is `wild-tantra-portugal-2026` in the shared archive.
5. Confirm the page returns to the synced state.
6. Publish the updated `main` branch to GitHub Pages.

