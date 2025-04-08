# Discord Account Creator (via Microsoft Account)

This Python script automates the creation of Discord accounts by first creating a Microsoft (Outlook/Hotmail) account and then using that session to register on Discord. It uses **Brave Browser** and incorporates various anti-detection techniques to mimic human behavior.

**Disclaimer:** This script is for educational purposes only. Automated account creation may violate the Terms of Service of Discord and Microsoft. Use responsibly and at your own risk. Excessive use may lead to IP blocks or account flags.

## Features

*   **Microsoft Account Creation:** Automates signup on signup.live.com.
*   **Discord Registration:** Uses the created Microsoft account session (email) to register on Discord.
*   **Automatic Outlook Login Attempt:** Tries to log into Outlook automatically if needed for verification.
*   **Automatic Discord Email Verification:** Attempts to find and click the Discord verification link in the Outlook inbox.
*   **Anti-Detection Techniques:**
    *   Random User-Agent selection from a list.
    *   Random delays between actions.
    *   Human-like typing simulation (including errors and pauses).
    *   Human-like mouse movement simulation for clicks.
    *   Randomized browser profile variations (fonts, timezone, platform, CPU cores, etc.).
    *   Disables WebRTC and other potential fingerprinting vectors.
    *   Fixed window size (1280x720).
*   **Error Handling:**
    *   Detects if a generated Microsoft email is already taken and retries with a new one.
    *   Saves screenshots upon encountering errors.
    *   **Leaves browser open on error:** If an error occurs during any step, the script pauses and keeps the browser open, allowing you to inspect the page. Press Enter in the terminal to acknowledge the error and stop the current account attempt.
*   **Manual Fallback/Steps Required:**
    *   **CAPTCHA Solving:** The script detects CAPTCHAs on Microsoft/Discord signup and Outlook login, requiring manual solving.
    *   **Outlook Login Failure:** If automatic Outlook login fails (e.g., due to 2FA), manual login may be needed.
    *   **Microsoft Email Verification:** May require manual checks in Outlook if automated steps fail.
    *   **Discord Email Verification:** Falls back to manual verification if the automated process fails (email not found, link error, etc.).
*   **Output:** Saves successfully created account credentials (Microsoft email used and the fixed password) to `genned.txt` in the format: `email password`.

## Prerequisites

*   Python 3.x
*   **Brave Browser** installed (tested with default location: `C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe`).
*   **`chromedriver`** compatible with your installed Brave/Chromium version. Download from the [Chrome for Testing availability dashboard](https://googlechromelabs.github.io/chrome-for-testing/) and ensure it's in your system's PATH or in the same directory as the script.
*   Required Python packages.

## Installation

1.  **Clone the repository or download the script.**
2.  **Install dependencies:**
    ```bash
    pip install selenium
    ```
3.  **Download `chromedriver`** and place it appropriately.
4.  **Verify Brave Path:** Ensure the `brave_path` variable in the `setup_driver` method points to your actual Brave installation if it's non-standard.

## Usage

1.  **Configure (Optional):** Modify the fixed password (`self.password`) or the number of accounts to create (`creator.run(10)`) at the bottom of the script.
2.  **Run the script:**
    ```bash
    python discord_account_creator.py
    ```
3.  **Interact when prompted:**
    *   Solve CAPTCHAs in the Brave browser when detected.
    *   Perform manual login/verification steps if the automated attempts fail and the script prompts you.
    *   Press Enter in the terminal to continue after manual steps or to acknowledge errors.

## Output File (`genned.txt`)

Successfully created accounts are appended to `genned.txt` with the following format:

```
microsoft_email@domain.com YourFixedPassword
another_email@domain.com YourFixedPassword
```

## Notes

*   The script uses a fixed password (`BOys552@kk_`). Change it in the `__init__` method if desired.
*   Random delays are used between steps, and a longer random delay (1-3 minutes) is added between creating each account.
*   Browser sessions remain open on errors or for manual steps. Ensure you press Enter in the terminal when prompted.
