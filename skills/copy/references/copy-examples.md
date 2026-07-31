# Microcopy — before/after library

Concrete pairs. Each one shows a single move. Read the principle — apply it everywhere.

---

## Errors

**No connection:**
- before: "Network error. Please try again later."
- after: "No connection — your changes weren't saved. Retry →"

**Invalid input:**
- before: "Invalid email format."
- after: "Check the address — looks like the @ is missing"

**Server not responding:**
- before: "Internal Server Error (500)"
- after: "The server isn't responding. Refresh the page — that usually helps. If it doesn't, we already know."

**No access:**
- before: "Forbidden. You do not have permission to access this resource."
- after: "No access. Ask the owner for permission, or sign in with a different account."

**Upload failed:**
- before: "Upload failed."
- after: "The file didn't upload — it's 24 MB and the limit is 10 MB. Shrink it and try again."

**Form:**
- before: "The 'Phone' field is filled in incorrectly."
- after: "Enter the phone as +1 900 000 0000"

---

## Buttons

| before | after | why |
|----|-------|--------|
| "Confirm" | "Pay $1,200" | names the action and the consequence |
| "Yes" | "Delete message" | doesn't require reading the question |
| "Submit form" | "Send request" | concrete object |
| "OK" | "Got it" / "Close" | OK means nothing |
| "No" | "Keep" / "Cancel" | names what will happen |
| "Save and exit" | "Save" (then exit automatically) | drop two actions merged into one |
| "Click here" (link) | "Open settings" | names the destination |
| "Learn more" | "Read the delivery terms" | concrete |

---

## Empty states

| Context | before | after |
|----------|----|-------|
| Task list | (empty) | "No tasks yet. Create the first one →" |
| Search with no results | "Nothing found" | "Nothing for 'concrete'. Try 'building materials', or clear the filters." |
| Purchase history | "History is empty" | "You haven't bought anything yet. Go to the catalog →" |
| Notifications | "No notifications" | "All caught up" (when it's good news) |
| Inbox | "No messages" | "Inbox zero. Get on with your day." |
| Favorites | "Your favorites list is empty" | "Add items to favorites — they'll show up here." |

---

## Onboarding and permissions

**Microphone request:**
- before: "The app requires access to your microphone to function."
- after: "Allow the mic — without it the app can't record your note."

**Location request:**
- before: "We need your location."
- after: "Allow location so we can show the nearest stores."

**First screen:**
- before: "Welcome to TaskFlow! We're glad you're here. TaskFlow is a powerful task-management tool."
- after: "Where do we start? Create a task →" or just the task-creation screen.

---

## Confirmations

**Deletion:**
- before: "Are you sure you want to delete this item? This action cannot be undone." [Yes] [No]
- after: "Delete the file 'Contract_final.pdf'? You won't be able to recover it." [Delete file] [Keep]

**Subscription cancellation:**
- before: "Confirm subscription cancellation." [Confirm] [Cancel]
- after: "Cancel your Pro subscription? Access to advanced features ends June 15." [Cancel subscription] [Keep Pro]

**Leave without saving:**
- before: "Changes not saved. Leave the page?" [Yes] [No]
- after: "Leave without saving? Your changes will be lost." [Leave] [Save and leave]

---

## Success and status

| Situation | before | after |
|----------|----|-------|
| Save | "Data saved successfully!" | ✓ Saved |
| Send | "Your message has been sent successfully." | "Sent" |
| File upload | "Upload completed successfully!" | "Uploaded: contract.pdf" |
| Payment | "Payment processed." | "Paid. Receipt is on its way to your email." |
| Deletion | (the item just disappears) | "Deleted. Undo →" (toast) |
| First achievement | "Congratulations! You've completed your first step!" | "First step — done." |

---

## Loading

| before | after |
|----|-------|
| "Loading…" (no specifics) | "Loading your documents…" |
| (spinner with no text) | "Connecting to the server…" |
| "Processing data. Please wait." | "Analyzing — usually 5–10 seconds." |
| "0%" (hanging) | skeleton screen with no text |

---

## Voice and tone — variants of one fact

Fact: a submitted form field failed validation.

| Tone | Text |
|-----|-------|
| Neutral | "Didn't go through. Try again." |
| Supportive | "Almost — one more time." |
| Direct, no blame | "Not accepted. Again →" |
| Too soft (avoid) | "Don't worry! That's totally normal — give it another little try! 😊" |
| Too harsh (avoid) | "Error. Field invalid." |

Rule: warm means direct and human, not babying.
