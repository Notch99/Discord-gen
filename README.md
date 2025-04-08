# Discord Account Creator (via Microsoft Account)

This Python script automates the creation of Discord accounts by first creating a Microsoft (Outlook/Hotmail) account and then using that session to register on Discord. It incorporates various anti-detection techniques to mimic human behavior.

**Disclaimer:** This script is for educational purposes only. Automated account creation may violate the Terms of Service of Discord and Microsoft. Use responsibly and at your own risk. Excessive use may lead to IP blocks or account flags.

## Features

*   **Microsoft Account Creation:** Automates signup on signup.live.com.
*   **Discord Registration:** Uses the created Microsoft account session (email) to register on Discord.
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
*   **Manual Steps Required:**
    *   **CAPTCHA Solving:** The script detects CAPTCHAs on both Microsoft and Discord signup pages and pauses, requiring manual user intervention to solve them. The browser remains open for this.
    *   **Microsoft Email Verification:** The script pauses after successful Microsoft account creation, prompting the user to manually check the Microsoft inbox (Outlook/Hotmail) for any verification emails and complete necessary steps before proceeding to Discord.
    *   **Discord Email Verification:** After Discord registration, the script prompts the user to manually check the Microsoft inbox again for the Discord verification email and click the link.
*   **Output:** Saves successfully created account credentials (Microsoft email used and the fixed password) to `genned.txt` in the format: `email password`.

## Prerequisites

*   Python 3.x
*   Microsoft Edge browser installed.
*   `msedgedriver` compatible with your Edge version. Download from [Microsoft Edge Driver page](https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/) and ensure it's in your system's PATH or in the same directory as the script.
*   Required Python packages.

## Installation

1.  **Clone the repository or download the script.**
2.  **Install dependencies:**
    ```bash
    pip install selenium
    ```
    (Or use `pip install -r requirements.txt` if one is provided).
3.  **Download `msedgedriver`** and place it appropriately.

## Usage

1.  **Configure (Optional):** You can modify the fixed password (`self.password`) or the number of accounts to create at the bottom of the script.
2.  **Run the script:**
    ```bash
    python discord_account_creator.py
    ```
3.  **Interact when prompted:**
    *   Solve CAPTCHAs in the browser when detected.
    *   Perform manual email verification steps for Microsoft and Discord when prompted.
    *   Press Enter in the terminal to continue after manual steps or to acknowledge errors.

## Output File (`genned.txt`)

Successfully created accounts are appended to `genned.txt` with the following format:

```
microsoft_email@domain.com YourFixedPassword
another_email@domain.com YourFixedPassword
```

## Notes

*   The script uses a fixed password (`BOys552@kk_`). Change it in the `__init__` method if desired.
*   The number of accounts to create is set in the `if __name__ == "__main__":` block (default is 10).
*   Random delays are used between steps, and a longer random delay (1-3 minutes) is added between creating each account to reduce detection.
*   Browser sessions remain open on errors or for manual steps. Ensure you press Enter in the terminal when prompted.
