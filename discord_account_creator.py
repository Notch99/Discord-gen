from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import time
import random
import string
import json
import os
from datetime import datetime
from selenium.webdriver.support.ui import Select
import math

class DiscordAccountCreator:
    def __init__(self):
        self.email = None
        self.password = "BOys552@kk_"  # Fixed password
        self.accounts_created = 0  # Counter for successful accounts
        self.method = 1  # Default method
        self.user_agents = [
            # Windows + Chrome
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36",
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36",
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36",
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36",
            # Windows + Firefox
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:99.0) Gecko/20100101 Firefox/99.0",
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:100.0) Gecko/20100101 Firefox/100.0",
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:101.0) Gecko/20100101 Firefox/101.0",
            # Windows + Edge
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36 Edg/99.0.1150.55",
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36 Edg/100.0.1185.39",
            # macOS + Safari
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 12_3_1) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.3 Safari/605.1.15",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 12_4) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.4 Safari/605.1.15",
            # macOS + Chrome
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 12_3_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36",
            # Mobile - Android
            "Mozilla/5.0 (Linux; Android 12; SM-G991U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.61 Mobile Safari/537.36",
            "Mozilla/5.0 (Linux; Android 12; Pixel 6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.61 Mobile Safari/537.36",
            # Mobile - iOS
            "Mozilla/5.0 (iPhone; CPU iPhone OS 15_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.4 Mobile/15E148 Safari/604.1",
            "Mozilla/5.0 (iPhone; CPU iPhone OS 15_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/101.0.4951.58 Mobile/15E148 Safari/604.1",
        ]
        
        # Different screen resolutions
        self.screen_resolutions = [
            (1366, 768),   # Most common laptop
            (1920, 1080),  # Full HD
            (1440, 900),   # MacBook
            (1536, 864),   # Common laptop
            (1280, 720),   # HD
            (1680, 1050),  # Common desktop
            (1600, 900),   # Common laptop
            (2560, 1440),  # QHD
            (1280, 800),   # Old MacBook
            (1920, 1200),  # 16:10 desktop
        ]
        
        # Different hardware concurrency (CPU cores) values
        self.cpu_cores = [2, 4, 6, 8, 12, 16]
        
        # Multiple browser profiles to randomize
        self.profile_variations = {
            'fonts': ['Arial', 'Helvetica', 'Times New Roman', 'Courier New', 'Verdana', 'Georgia'],
            'languages': ['en-US', 'en-GB', 'en-CA', 'de-DE', 'fr-FR', 'es-ES', 'it-IT'],
            'timezones': ['America/New_York', 'Europe/London', 'Europe/Berlin', 'Asia/Tokyo', 'Australia/Sydney'],
            'platforms': ['Win32', 'MacIntel', 'Linux x86_64'],
            'color_depths': [24, 30, 48],
            'device_memories': [2, 4, 8, 16],
        }
        
    def get_random_proxy(self):
        """Get a random residential proxy from the list."""
        if not self.residential_proxies:
            print("No residential proxies configured. Running without proxy.")
            return None
        
        return random.choice(self.residential_proxies)
    
    def get_random_resolution(self):
        """Get a random screen resolution."""
        return random.choice(self.screen_resolutions)
    
    def get_random_cpu_cores(self):
        """Get a random number of CPU cores."""
        return random.choice(self.cpu_cores)
        
    def get_random_profile_variation(self):
        """Get random browser profile details."""
        return {
            'font': random.choice(self.profile_variations['fonts']),
            'language': 'en-US',  # Fixed language
            'timezone': random.choice(self.profile_variations['timezones']),
            'platform': random.choice(self.profile_variations['platforms']),
            'color_depth': random.choice(self.profile_variations['color_depths']),
            'device_memory': random.choice(self.profile_variations['device_memories']),
        }
        
    def setup_driver(self, user_agent=None):
        print("Setting up Brave browser...") # Changed browser name
        options = ChromeOptions() 
        
        # --- SET BRAVE BROWSER LOCATION --- 
        # Adjust this path if your Brave installation is different
        brave_path = "C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe"
        if os.path.exists(brave_path):
             options.binary_location = brave_path
             print(f"Using Brave binary location: {brave_path}")
        else:
             print(f"Warning: Brave binary not found at {brave_path}. Using default Chrome/Chromium installation.")
             # Script might use standard Chrome if Brave isn't found here.
        
        # Get random profile variations
        profile = self.get_random_profile_variation()
        cpu_cores = self.get_random_cpu_cores()
        
        print(f"Using profile variations: {profile}")
        print(f"Using CPU cores: {cpu_cores}")
        
        # Basic options
        options.add_argument("--disable-blink-features=AutomationControlled")
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        options.add_experimental_option("useAutomationExtension", False)
        
        # Remove automated test flag
        options.add_argument("--disable-infobars")
        options.add_argument("--disable-notifications")
        
        # Set window size to match Discord's size
        options.add_argument("--window-size=1280,720")
        
        # Anti-detection measures
        options.add_argument("--disable-webrtc")
        options.add_argument("--disable-features=CalculateNativeWinOcclusion")
        options.add_argument("--disable-features=IsolateOrigins,site-per-process")
        options.add_argument("--disable-site-isolation-trials")
        options.add_argument("--disable-web-security")
        options.add_argument("--disable-3d-apis")
        options.add_argument("--disable-accelerated-2d-canvas")
        options.add_argument("--disable-accelerated-jpeg-decoding")
        options.add_argument("--disable-accelerated-mjpeg-decode")
        options.add_argument("--disable-accelerated-video-decode")
        options.add_argument("--disable-gpu-compositing")
        options.add_argument("--disable-d3d11")
        
        # Set custom permissions
        prefs = {
            "profile.default_content_setting_values": {
                "geolocation": 2,
                "notifications": 2,
                "media_stream_mic": 2,
                "media_stream_camera": 2,
                "midi_sysex": 2
            },
            "profile.managed_default_content_settings": {
                "plugins": 1
            },
            "intl.accept_languages": profile['language'],
            "credentials_enable_service": False,
            "profile.password_manager_enabled": False
        }
        options.add_experimental_option("prefs", prefs)
        
        # Set custom User Agent if provided
        if user_agent:
            print(f"Using User Agent: {user_agent}")
            options.add_argument(f"user-agent={user_agent}")
        
        # Add language and timezone options
        options.add_argument(f"--lang={profile['language']}")
        options.add_argument(f"--timezone={profile['timezone']}")
        
        # Add audio output options
        options.add_argument("--disable-audio-output")
        options.add_argument("--mute-audio")
        
        try:
            driver = webdriver.Chrome(options=options)
            print("ChromeDriver initialized.")
        except Exception as e:
            print(f"Error initializing ChromeDriver: {e}")
            print("Ensure chromedriver is installed and accessible in your PATH.")
            print("Download from: https://googlechromelabs.github.io/chrome-for-testing/")
            raise
        
        # Set window size and position
        driver.set_window_size(1280, 720)
        driver.set_window_position(0, 0)  # Position at top-left corner
        
        # Modify navigator properties
        driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
            "source": f"""
                Object.defineProperty(navigator, 'webdriver', {{
                    get: () => undefined
                }});
                
                Object.defineProperty(navigator, 'plugins', {{
                    get: () => [
                        {{
                            0: {{
                                type: "application/pdf",
                                suffixes: "pdf",
                                description: "Portable Document Format"
                            }},
                            name: "PDF Viewer",
                            description: "Portable Document Format",
                            filename: "internal-pdf-viewer"
                        }}
                    ]
                }});
                
                Object.defineProperty(navigator, 'hardwareConcurrency', {{
                    get: () => {cpu_cores}
                }});
                
                Object.defineProperty(navigator, 'language', {{
                    get: () => '{profile['language']}'
                }});
                
                Object.defineProperty(navigator, 'platform', {{
                    get: () => '{profile['platform']}'
                }});
                
                Object.defineProperty(navigator, 'deviceMemory', {{
                    get: () => {profile['device_memory']}
                }});
                
                // Remove automation flags
                window.chrome = undefined;
                window.navigator.chrome = undefined;
                window.navigator.webdriver = undefined;
                
                // Add random noise to timing functions
                const originalGetTime = Date.prototype.getTime;
                Date.prototype.getTime = function() {{
                    return originalGetTime.call(this) + Math.floor(Math.random() * 10);
                }};
                
                // Modify performance timing
                const originalNow = performance.now;
                performance.now = function() {{
                    return originalNow.call(this) + Math.random() * 10;
                }};
                
                // Force Discord window size
                const style = document.createElement('style');
                style.textContent = `
                    body {{
                        width: 1280px !important;
                        height: 720px !important;
                        overflow: hidden !important;
                        position: fixed !important;
                        top: 0 !important;
                        left: 0 !important;
                    }}
                    #app-mount {{
                        width: 1280px !important;
                        height: 720px !important;
                        position: fixed !important;
                        top: 0 !important;
                        left: 0 !important;
                    }}
                    .app {{
                        width: 1280px !important;
                        height: 720px !important;
                        position: fixed !important;
                        top: 0 !important;
                        left: 0 !important;
                    }}
                `;
                document.head.appendChild(style);
                
                // Prevent window resizing
                window.addEventListener('resize', function() {{
                    window.resizeTo(1280, 720);
                    document.body.style.width = '1280px';
                    document.body.style.height = '720px';
                    document.body.style.overflow = 'hidden';
                    document.body.style.position = 'fixed';
                    document.body.style.top = '0';
                    document.body.style.left = '0';
                    
                    const appMount = document.getElementById('app-mount');
                    if (appMount) {{
                        appMount.style.width = '1280px';
                        appMount.style.height = '720px';
                        appMount.style.position = 'fixed';
                        appMount.style.top = '0';
                        appMount.style.left = '0';
                    }}
                    
                    const app = document.querySelector('.app');
                    if (app) {{
                        app.style.width = '1280px';
                        app.style.height = '720px';
                        app.style.position = 'fixed';
                        app.style.top = '0';
                        app.style.left = '0';
                    }}
                }});
            """
        })
        
        return driver
    
    def get_random_user_agent(self):
        """Generate a random User Agent from the predefined list."""
        return random.choice(self.user_agents)
    
    def generate_random_email(self):
        # Add more variety to emails
        username_styles = [
            # Simple random letters and numbers
            lambda: ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(random.randint(7, 12))),
            # Name-based (firstName.lastName format)
            lambda: random.choice(['john', 'jane', 'mike', 'sarah', 'david', 'emma', 'alex', 'lisa']) + 
                    '.' + 
                    random.choice(['smith', 'johnson', 'williams', 'brown', 'jones', 'miller', 'davis', 'garcia']) +
                    (random.choice(['', str(random.randint(1, 99))]) if random.random() < 0.4 else ''),
            # Word combinations
            lambda: random.choice(['cool', 'super', 'awesome', 'tech', 'game', 'pro', 'dev', 'web']) +
                    random.choice(['user', 'player', 'master', 'guru', 'fan', 'star', 'king', 'ninja']) +
                    str(random.randint(0, 9999)) if random.random() < 0.6 else '',
        ]
        
        # Select a random style for this email
        style = random.choice(username_styles)
        return style()  # Return only username without @mail.io
    
    def generate_random_username(self):
        # Add more variety to usernames
        username_styles = [
            # Simple random letters and numbers
            lambda: ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(random.randint(8, 15))),
            # Gaming-style username
            lambda: random.choice(['xX', '', 'Pro', 'The']) +
                    random.choice(['Gamer', 'Ninja', 'Wizard', 'Dragon', 'Shadow', 'Ghost', 'Legend', 'Cool']) +
                    random.choice(['', 'Xx', str(random.randint(0, 9999))]),
            # Word combinations
            lambda: random.choice(['epic', 'dark', 'fast', 'crazy', 'mad', 'silent', 'toxic', 'swift']) +
                    random.choice(['wolf', 'eagle', 'shark', 'rider', 'killer', 'sniper', 'slayer', 'hunter']) +
                    (str(random.randint(0, 999)) if random.random() < 0.7 else ''),
        ]
        
        # Select a random style for this username
        style = random.choice(username_styles)
        return style()
    
    def generate_random_display_name(self, style=None):
        # Add more variety to display names
        name_styles = {
            # Capitalized word
            'capital': lambda: ''.join(random.choice(string.ascii_lowercase) for _ in range(random.randint(5, 8))).capitalize(),
            # Real-looking name
            'real': lambda: random.choice([
                'James', 'John', 'Robert', 'Michael', 'William', 'David', 'Joseph', 'Charles',
                'Mary', 'Patricia', 'Jennifer', 'Linda', 'Elizabeth', 'Barbara', 'Susan', 'Jessica',
                'Alex', 'Jordan', 'Taylor', 'Casey', 'Riley', 'Avery', 'Quinn', 'Morgan'
            ]),
            # Fun nickname
            'fun': lambda: random.choice([
                'Spark', 'Blaze', 'Shadow', 'Frost', 'Storm', 'Sunny', 'Star', 'Luna',
                'Ocean', 'Sky', 'Thunder', 'Flash', 'Wolf', 'Eagle', 'Phoenix', 'Tiger'
            ]),
        }

        # Select a specific style if provided and valid, otherwise random
        if style and style in name_styles:
            selected_style = name_styles[style]
            print(f"Using display name style: {style}") # Optional: log which style is used
        else:
            selected_style = random.choice(list(name_styles.values()))
            print("Using random display name style.") # Optional: log random selection

        return selected_style()
    
    def random_delay(self, min_seconds=1, max_seconds=5):
        """Add a random delay between actions to appear more human-like."""
        delay = random.uniform(min_seconds, max_seconds)
        print(f"Waiting for {delay:.2f} seconds...")
        time.sleep(delay)
    
    def simulate_typing_error(self, element, text):
        """Simulate human typing with occasional errors that get corrected."""
        for i, char in enumerate(text):
            # 15% chance to make a typing error
            if random.random() < 0.15 and i < len(text) - 1:
                # Type a wrong character
                wrong_char = random.choice(string.ascii_lowercase + string.digits)
                print(f"Simulating typing error: typing '{wrong_char}' instead of '{char}'")
                element.send_keys(wrong_char)
                self.random_delay(0.1, 0.3)  # Short delay after mistake
                
                # Delete the wrong character
                element.send_keys(Keys.BACKSPACE)
                self.random_delay(0.2, 0.4)  # Delay after deleting
            
            # Type the correct character
            element.send_keys(char)
            time.sleep(random.uniform(0.05, 0.2))  # Random delay between keystrokes
            
            # 5% chance to pause in the middle of typing (as if thinking)
            if random.random() < 0.05 and i > 0 and i < len(text) - 1:
                self.random_delay(0.5, 1.5)
        
        # Random delay after typing is complete
        self.random_delay(0.5, 2)
    
    def human_type(self, element, text):
        """Type like a human with random delays between keystrokes."""
        # 70% chance to use error simulation, 30% chance to just type normally
        if random.random() < 0.7:
            self.simulate_typing_error(element, text)
        else:
            for char in text:
                element.send_keys(char)
                # Very small random delay between keystrokes (50ms to 200ms)
                time.sleep(random.uniform(0.05, 0.2))
            
            # Random delay after typing
            self.random_delay(0.5, 2)
    
    def move_mouse_humanly(self, driver, element):
        """Simulate human-like mouse movement towards an element."""
        action = ActionChains(driver)
        
        # Get current mouse position (if possible, otherwise assume 0,0)
        try:
            # This is a bit tricky and might not be standard Selenium
            # We might need JS execution or rely on last known position
            # For now, let's move from a slight offset from the element
            start_x, start_y = element.location['x'] - random.randint(50, 150), element.location['y'] - random.randint(50, 150)
        except:
            start_x, start_y = 0, 0 # Fallback
        
        # Get target element position
        target_x = element.location['x'] + random.randint(0, element.size['width'] // 2) # Add slight random offset
        target_y = element.location['y'] + random.randint(0, element.size['height'] // 2)
        
        # Calculate distance and steps
        distance = math.sqrt((target_x - start_x)**2 + (target_y - start_y)**2)
        num_steps = max(5, int(distance / random.randint(50, 100))) # More steps for longer distances
        
        print(f"Moving mouse towards element ({num_steps} steps)...")
        action.move_by_offset(start_x, start_y) # Move to start offset if needed (simulated)
        
        current_x, current_y = start_x, start_y
        for i in range(num_steps):
            step_progress = (i + 1) / num_steps
            
            # Add randomness/curvature to path
            noise_x = random.uniform(-15, 15) * (1 - step_progress) # More noise at the beginning
            noise_y = random.uniform(-15, 15) * (1 - step_progress)
            
            # Interpolate position
            interp_x = start_x + (target_x - start_x) * step_progress + noise_x
            interp_y = start_y + (target_y - start_y) * step_progress + noise_y
            
            move_x = interp_x - current_x
            move_y = interp_y - current_y
            
            # Add small random pauses during movement
            step_duration = random.uniform(0.01, 0.05)
            action.pause(step_duration) 
            action.move_by_offset(move_x, move_y)
            
            current_x, current_y = interp_x, interp_y
            
        # Perform the move
        try:
            action.perform()
            self.random_delay(0.2, 0.5) # Small pause after moving
        except Exception as e:
            print(f"Error performing mouse move: {e}")
            # Fallback: try moving directly to the element if human-like fails
            try:
                ActionChains(driver).move_to_element(element).perform()
            except Exception as fallback_e:
                print(f"Fallback mouse move failed: {fallback_e}")

    def click_element_humanly(self, driver, element):
        """Move mouse humanly to the element and then click."""
        try:
            # 1. Move mouse towards the element
            self.move_mouse_humanly(driver, element)
            
            # 2. Add a very short random pause before clicking
            self.random_delay(0.1, 0.4)
            
            # 3. Click the element
            print(f"Clicking element...")
            element.click()
            
            # 4. Add a short random pause after clicking
            self.random_delay(0.3, 0.8)
            
        except Exception as e:
            print(f"Error during human-like click: {e}. Trying standard click.")
            driver.save_screenshot("human_click_error.png")
            # Fallback to standard click if human-like fails
            try:
                element.click()
                self.random_delay(0.5, 1)
            except Exception as fallback_e:
                print(f"Standard fallback click also failed: {fallback_e}")
                driver.save_screenshot("standard_click_error.png")
                raise fallback_e # Re-raise the exception if standard click fails too

    def save_account_details(self, username, email, password):
        # Format: email password
        # Email should be the full Microsoft email used (e.g., something@outlook.com or something@hotmail.com)
        # Although the script doesn't explicitly add @outlook.com anymore, 
        # the self.email used should contain it if the Microsoft signup process requires it.
        # If Microsoft signup *doesn't* require a domain, self.email will just be the username part.
        # We save whatever self.email contains at the point of calling this function.
        details = f"{email} {password}"
        
        try:
            with open("genned.txt", "a") as file:
                file.write(details + "\n")
            # Increment the account counter (This seems to be handled in create_discord_account now, maybe remove duplicate? Check usage)
            # self.accounts_created += 1 # Duplicated in create_discord_account, remove here?
            print(f"Account details saved to genned.txt: {details}")
            # print(f"Total accounts created: {self.accounts_created}") # Also duplicated
        except Exception as e:
            print(f"Error saving account details: {e}")
    
    def create_microsoft_account(self):
        """Create a Microsoft account and verify it."""
        print("Starting Microsoft account creation...")
        max_retries = 3 # Keep retries for the whole process, but stop attempt on step failure
        retry_count = 0
        driver = None # Define driver outside the loop to manage its state
        
        while retry_count < max_retries:
            try:
                # Only set up a new driver if one isn't already open from a previous failed step in this attempt
                if driver is None:
                    user_agent = self.get_random_user_agent()
                    driver = self.setup_driver(user_agent=user_agent)

                # Open Microsoft signup page if not already on it (handles retries better)
                if "signup.live.com" not in driver.current_url:
                    microsoft_signup_url = "https://signup.live.com/signup?lcid=1033&wa=wsignin1.0&rpsnv=13&ct=1617845096&rver=7.0.6737.0&wp=MBI_SSL&wreply=https%3a%2f%2foutlook.live.com%2fowa%2f%3fnlp%3d1%26signup%3d1%26RpsCsrfState%3d4b76f637-0e5e-0d3e-5b9b-8a6d5a9f3a7e&id=292841&CBCXT=out&lw=1&fl=dob%2cflname%2cwld&cobrandid=90015&lic=1&uaid=7f481e2b4b57419ab5a9e5d6c1e3a3b0"
                    print(f"Navigating to: {microsoft_signup_url}")
                    driver.get(microsoft_signup_url)
                    self.random_delay(3, 5)

                # Generate random email for Microsoft (only if not already set in this attempt)
                if not self.email:
                    self.email = self.generate_random_email()
                self.password = "BOys552@kk_"  # Use the fixed password

                # Input email
                try:
                    print("Looking for email input field...")
                    email_input = WebDriverWait(driver, 10).until(
                        EC.visibility_of_element_located((By.XPATH, "//*[@id='usernameInput']"))
                    )
                    # Clear field only if needed (e.g., if retrying after email taken)
                    # email_input.clear() 
                    self.click_element_humanly(driver, email_input)
                    self.random_delay(0.5, 1)
                    self.human_type(email_input, self.email)
                    print(f"Entered Microsoft email: {self.email}")
                    self.random_delay(1, 2)
                except Exception as e:
                    print(f"Email input error: {str(e)}")
                    driver.save_screenshot("microsoft_email_error.png")
                    print("Browser left open for inspection.")
                    input("Press Enter to stop this attempt...")
                    return None # Stop this account attempt

                # Click Next button
                try:
                    next_button = WebDriverWait(driver, 5).until(
                        EC.element_to_be_clickable((By.XPATH, "//*[@id='nextButton']"))
                    )
                    self.click_element_humanly(driver, next_button)
                    print("Clicked Next button after email")
                    # --- Check if email is already taken ---
                    try:
                        error_message_xpath = "//*[contains(text(), 'is already a Microsoft account')]"
                        WebDriverWait(driver, 3).until(
                            EC.visibility_of_element_located((By.XPATH, error_message_xpath))
                        )
                        # Email is taken!
                        old_email = self.email
                        print(f"Email {old_email} is already taken. Generating a new one.")
                        driver.save_screenshot(f"microsoft_email_taken_{old_email}.png")
                        
                        # Generate and set the new email IMMEDIATELY
                        self.email = self.generate_random_email()
                        print(f"Generated new email: {self.email}")
                        
                        # Find the input again, clear it, and type the NEW email
                        try:
                            email_input = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, "//*[@id='usernameInput']")))
                            # Use JS to clear if standard clear fails sometimes
                            driver.execute_script("arguments[0].value='';", email_input) 
                            # email_input.clear() # Standard clear as fallback/alternative
                            self.random_delay(0.5, 1) # Pause after clearing
                            self.human_type(email_input, self.email) # Type the new email
                            print(f"Re-entered new email: {self.email}")
                            # Let the code proceed to click 'Next' again naturally
                        except Exception as e_retry_input:
                            print(f"Error trying to clear/re-enter new email: {e_retry_input}")
                            # If we can't re-enter, this attempt is likely doomed
                            print("Browser left open for inspection.")
                            input("Press Enter to stop this attempt...")
                            return None # Stop this account attempt

                    except TimeoutException:
                        # Error message did not appear within 3 seconds, email is likely okay
                        print("Email seems available. Proceeding to password.")
                        # No action needed here, just proceed
                        pass
                except Exception as e:
                    print(f"Next button click error (after email): {str(e)}")
                    driver.save_screenshot("microsoft_next_email_error.png")
                    print("Browser left open for inspection.")
                    input("Press Enter to stop this attempt...")
                    return None
                
                # --- Enter Password, Names, DOB steps follow ---
                # (Add similar error handling: remove driver.quit, add input prompt, return None)

                # Example for Password:
                try:
                    password_input = WebDriverWait(driver, 10).until(
                        EC.visibility_of_element_located((By.XPATH, "//*[@id='Password']"))
                    )
                    self.click_element_humanly(driver, password_input)
                    self.random_delay(0.5, 1)
                    self.human_type(password_input, self.password)
                    print("Entered password")
                    self.random_delay(1, 2)
                except Exception as e:
                    print(f"Password input error: {str(e)}")
                    driver.save_screenshot("microsoft_password_error.png")
                    print("Browser left open for inspection.")
                    input("Press Enter to stop this attempt...")
                    return None

                # Click Next button after password
                try:
                    next_button = WebDriverWait(driver, 5).until(
                        EC.element_to_be_clickable((By.XPATH, "//*[@id='nextButton']"))
                    )
                    self.click_element_humanly(driver, next_button)
                    print("Clicked Next button after password")
                    self.random_delay(2, 3)
                except Exception as e:
                    print(f"Next button click error (after password): {str(e)}")
                    driver.save_screenshot("microsoft_next_password_error.png")
                    print("Browser left open for inspection.")
                    input("Press Enter to stop this attempt...")
                    return None

                # Enter first name and last name
                try:
                    first_name = self.generate_random_display_name(style='real')
                    last_name = self.generate_random_display_name(style='real')
                    first_name_input = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//*[@id='firstNameInput']")))
                    self.click_element_humanly(driver, first_name_input)
                    self.random_delay(0.5, 1)
                    self.human_type(first_name_input, first_name)
                    print(f"Entered first name: {first_name}")
                    self.random_delay(1, 1.5)
                    last_name_input = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, "//*[@id='lastNameInput']")))
                    self.click_element_humanly(driver, last_name_input)
                    self.random_delay(0.5, 1)
                    self.human_type(last_name_input, last_name)
                    print(f"Entered last name: {last_name}")
                    self.random_delay(1, 2)
                except Exception as e:
                    print(f"Name input error: {str(e)}")
                    driver.save_screenshot("microsoft_name_error.png")
                    print("Browser left open for inspection.")
                    input("Press Enter to stop this attempt...")
                    return None
                
                # Click Next button after name
                try:
                    next_button = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='nextButton']")))
                    self.click_element_humanly(driver, next_button)
                    print("Clicked Next button after name")
                    self.random_delay(2, 3)
                except Exception as e:
                    print(f"Next button click error (after name): {str(e)}")
                    driver.save_screenshot("microsoft_next_name_error.png")
                    print("Browser left open for inspection.")
                    input("Press Enter to stop this attempt...")
                    return None

                # Enter birth date
                try:
                    birth_month_dropdown = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, "//*[@id='BirthMonth']")))
                    select_month = Select(birth_month_dropdown)
                    month_value = str(random.randint(1, 12))
                    select_month.select_by_value(month_value)
                    print(f"Selected birth month: {month_value}")
                    self.random_delay(1, 1.5)
                    birth_day_input = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, "//*[@id='BirthDay']")))
                    self.click_element_humanly(driver, birth_day_input)
                    self.random_delay(0.5, 1)
                    day_value = str(random.randint(1, 28))
                    self.human_type(birth_day_input, day_value)
                    print(f"Entered birth day: {day_value}")
                    self.random_delay(1, 1.5)
                    birth_year_input = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, "//*[@id='BirthYear']")))
                    self.click_element_humanly(driver, birth_year_input)
                    self.random_delay(0.5, 1)
                    year_value = str(random.randint(1990, 2000))
                    self.human_type(birth_year_input, year_value)
                    print(f"Entered birth year: {year_value}")
                    self.random_delay(1, 2)
                except Exception as e:
                    print(f"Birth date input error: {str(e)}")
                    driver.save_screenshot("microsoft_birthdate_error.png")
                    print("Browser left open for inspection.")
                    input("Press Enter to stop this attempt...")
                    return None
                
                # Click Next button after birth date
                try:
                    next_button = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='nextButton']")))
                    self.click_element_humanly(driver, next_button)
                    print("Clicked Next button after birth date")
                    self.random_delay(3, 5)
                except Exception as e:
                    print(f"Next button click error (after birth date): {str(e)}")
                    driver.save_screenshot("microsoft_next_birthdate_error.png")
                    print("Browser left open for inspection.")
                    input("Press Enter to stop this attempt...")
                    return None

                # --- CAPTCHA Handling ---
                try:
                    captcha_iframe = WebDriverWait(driver, 5).until(
                        EC.presence_of_element_located((By.CSS_SELECTOR, "iframe[title*='CAPTCHA']"))
                    )
                    print("CAPTCHA detected! Please solve it manually.")
                    # We don't switch frames automatically, user needs to interact
                    print("Browser left open for manual CAPTCHA solving.")
                    input("Press Enter after solving the CAPTCHA to continue...")
                    # No need to switch back if we didn't switch in
                    print("Continuing after manual CAPTCHA solving attempt...")
                    self.random_delay(2, 4)
                except TimeoutException:
                    print("No CAPTCHA detected, or timed out waiting.")
                except Exception as e:
                    print(f"Error during CAPTCHA check: {e}")
                    print("Browser left open for inspection.")
                    input("Press Enter to acknowledge CAPTCHA check error and continue...")
                
                # --- Verification Step ---
                print("Checking if Microsoft account creation was successful...")
                try:
                    WebDriverWait(driver, 20).until(EC.url_contains("outlook.live.com"))
                    print("Microsoft account creation seems successful.")
                    print("\nPlease manually check the Microsoft inbox for any verification emails.")
                    print("Complete any required verification steps in the browser.")
                    print("Browser left open for manual verification.")
                    input("Press Enter after completing manual verification (if any) to continue to Discord...")
                    return driver # SUCCESS! Return the driver
                except TimeoutException:
                    print("Failed to confirm Microsoft account creation (Timeout waiting for outlook.live.com URL).")
                    driver.save_screenshot("microsoft_creation_failed.png")
                    print("Browser left open for inspection.")
                    input("Press Enter to stop this attempt...")
                    return None
                except Exception as e:
                    print(f"Error verifying Microsoft account creation: {e}")
                    driver.save_screenshot("microsoft_verification_error.png")
                    print("Browser left open for inspection.")
                    input("Press Enter to stop this attempt...")
                    return None
                    
            except Exception as e:
                print(f"An unexpected error occurred during Microsoft account creation attempt: {str(e)}")
                if driver:
                    try:
                        driver.save_screenshot(f"microsoft_unexpected_error_{retry_count}.png")
                    except: pass
                print("Browser left open (if initialized) for inspection.")
                input("Press Enter to stop this attempt...")
                # Don't increment retry_count here, just stop the attempt
                return None # Stop this attempt

        # This part is reached only if the while loop finishes (max_retries reached)
        print("Failed to create Microsoft account after multiple retries.")
        # Ensure driver is closed if it exists after all retries fail
        if driver:
             try:
                 driver.quit()
             except: pass
        return None # Indicate overall failure

    def create_discord_account(self, driver, username=None, display_name=None):
        """Create a Discord account using the provided driver session."""
        if not driver:
            print("Driver not initialized. Cannot create Discord account.")
            return False
        
        print("Starting Discord account creation process...")
        
        # Generate random details if not provided
        if not username: username = self.generate_random_username()
        if not display_name: display_name = self.generate_random_display_name()
        if not self.email: 
             print("Error: Microsoft email not set before Discord registration.")
             return False

        try:
            print("Opening Discord registration page...")
            driver.execute_script("window.open('https://discord.com/register', '_blank');")
            self.random_delay(2, 3)
            driver.switch_to.window(driver.window_handles[-1])
            self.random_delay(3, 5)
            
            print(f"Using Email: {self.email}")
            print(f"Using Username: {username}")
            print(f"Using Display Name: {display_name}")
            print(f"Using Password: {self.password}")
            
            # --- Input Email ---
            try:
                email_input = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.NAME, "email")))
                self.click_element_humanly(driver, email_input)
                self.human_type(email_input, self.email)
                print("Entered email into Discord form.")
                self.random_delay(1, 2)
            except Exception as e:
                print(f"Error entering email on Discord: {e}")
                driver.save_screenshot("discord_email_error.png")
                print("Browser left open for inspection.")
                input("Press Enter to stop this Discord attempt...")
                return False 

            # --- Input Display Name ---
            try:
                display_name_input = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.NAME, "global_name")))
                self.click_element_humanly(driver, display_name_input)
                self.human_type(display_name_input, display_name)
                print("Entered display name.")
                self.random_delay(1, 2)
            except Exception as e:
                print(f"Error entering display name: {e}")
                driver.save_screenshot("discord_displayname_error.png")
                print("Browser left open for inspection.")
                input("Press Enter to stop this Discord attempt...")
                return False # Treat as fatal for now
            
            # --- Input Username ---
            try:
                username_input = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.NAME, "username")))
                self.click_element_humanly(driver, username_input)
                self.human_type(username_input, username)
                print("Entered username.")
                self.random_delay(1, 2)
            except Exception as e:
                print(f"Error entering username: {e}")
                driver.save_screenshot("discord_username_error.png")
                print("Browser left open for inspection.")
                input("Press Enter to stop this Discord attempt...")
                return False 

            # --- Input Password ---
            try:
                password_input = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.NAME, "password")))
                self.click_element_humanly(driver, password_input)
                self.human_type(password_input, self.password)
                print("Entered password.")
                self.random_delay(1, 2)
            except Exception as e:
                print(f"Error entering password: {e}")
                driver.save_screenshot("discord_password_error.png")
                print("Browser left open for inspection.")
                input("Press Enter to stop this Discord attempt...")
                return False 

            # --- Input Date of Birth (Attempting Text Input Again) ---
            try:
                print("Entering date of birth as text input...")
                
                # Generate DOB values
                month_value = str(random.randint(1, 12))
                day_value = str(random.randint(1, 28))
                year_value = str(random.randint(1990, 2000))

                # --- Input Month ---
                # NOTE: Selectors are guesses. Adjust if they fail.
                try:
                    # Try various common attributes
                    month_input_selector = "input[placeholder*='Month'], input[aria-label*='Month'], input[name*='month']"
                    month_input = WebDriverWait(driver, 10).until(
                        EC.visibility_of_element_located((By.CSS_SELECTOR, month_input_selector))
                    )
                    self.click_element_humanly(driver, month_input) # Click first
                    month_input.send_keys(Keys.CONTROL + "a") # Select all
                    month_input.send_keys(Keys.DELETE) # Clear field
                    self.human_type(month_input, month_value)
                    print(f"Typed month: {month_value}")
                    self.random_delay(0.5, 1.5)
                except Exception as e_month:
                    print(f"Error typing month: {e_month}")
                    driver.save_screenshot("discord_dob_month_type_error.png")
                    print("Browser left open for inspection.")
                    input("Press Enter to stop this Discord attempt...")
                    return False

                # --- Input Day ---
                try:
                    day_input_selector = "input[placeholder*='Day'], input[aria-label*='Day'], input[name*='day']"
                    day_input = WebDriverWait(driver, 5).until(
                         EC.visibility_of_element_located((By.CSS_SELECTOR, day_input_selector))
                    )
                    self.click_element_humanly(driver, day_input)
                    day_input.send_keys(Keys.CONTROL + "a") 
                    day_input.send_keys(Keys.DELETE)
                    self.human_type(day_input, day_value)
                    print(f"Typed day: {day_value}")
                    self.random_delay(0.5, 1.5)
                except Exception as e_day:
                    print(f"Error typing day: {e_day}")
                    driver.save_screenshot("discord_dob_day_type_error.png")
                    print("Browser left open for inspection.")
                    input("Press Enter to stop this Discord attempt...")
                    return False
                
                # --- Input Year ---
                try:
                    year_input_selector = "input[placeholder*='Year'], input[aria-label*='Year'], input[name*='year']"
                    year_input = WebDriverWait(driver, 5).until(
                        EC.visibility_of_element_located((By.CSS_SELECTOR, year_input_selector))
                    )
                    self.click_element_humanly(driver, year_input)
                    year_input.send_keys(Keys.CONTROL + "a")
                    year_input.send_keys(Keys.DELETE)
                    self.human_type(year_input, year_value)
                    print(f"Typed year: {year_value}")
                    self.random_delay(1, 2)
                except Exception as e_year:
                    print(f"Error typing year: {e_year}")
                    driver.save_screenshot("discord_dob_year_type_error.png")
                    print("Browser left open for inspection.")
                    input("Press Enter to stop this Discord attempt...")
                    return False

            except Exception as e:
                # This catches potential errors even before finding the first field
                print(f"General error during date of birth text input: {e}")
                driver.save_screenshot("discord_dob_text_input_error.png")
                print("Browser left open for inspection.")
                input("Press Enter to stop this Discord attempt...")
                return False
            
            # --- Terms Checkbox ---
            try:
                terms_checkbox = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[type='checkbox'][class*='inputCheckbox']")))
                if not terms_checkbox.is_selected():
                     self.click_element_humanly(driver, terms_checkbox) # JS click might be safer here too
                     # driver.execute_script("arguments[0].click();", terms_checkbox)
                     print("Checked terms and conditions.")
                else: print("Terms checkbox already checked.")
                self.random_delay(1, 2)
            except Exception as e:
                 print(f"Error interacting with terms checkbox: {e}")
                 driver.save_screenshot("discord_terms_error.png")
                 print("Browser left open for inspection.")
                 input("Press Enter to stop this Discord attempt...")
                 return False # Treat as fatal

            # --- Click Continue Button ---
            try:
                continue_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']")))
                self.click_element_humanly(driver, continue_button)
                # driver.execute_script("arguments[0].click();", continue_button) # JS click if needed
                print("Clicked Continue button.")
                self.random_delay(5, 8)
            except Exception as e:
                print(f"Error clicking Continue button: {e}")
                driver.save_screenshot("discord_continue_error.png")
                print("Browser left open for inspection.")
                input("Press Enter to stop this Discord attempt...")
                return False

            # --- CAPTCHA Handling ---
            try:
                captcha_iframe = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "iframe[title='Main content']")))
                print("CAPTCHA detected on Discord! Please solve it manually.")
                print("Browser left open for manual CAPTCHA solving.")
                input("Press Enter after solving the Discord CAPTCHA to continue...")
                print("Continuing after manual Discord CAPTCHA attempt...")
                self.random_delay(3, 5)
            except TimeoutException:
                print("No Discord CAPTCHA detected or timed out waiting.")
            except Exception as e:
                print(f"Error during Discord CAPTCHA check: {e}")
                print("Browser left open for inspection.")
                input("Press Enter to acknowledge CAPTCHA check error and continue...")

            # --- Automatic Email Verification via Outlook ---
            verification_success = self.verify_discord_email_via_outlook(driver)

            if verification_success:
                print("Automatic email verification successful or link clicked.")
            else:
                print("\nAutomatic email verification failed or timed out.")
                print("Please check the Microsoft inbox manually for the Discord verification email and click the link.")
                print("Browser session remains open for manual verification.")
                input("Press Enter here in the terminal once you have manually verified (if needed) and are ready to save details...")

            # --- Save Account Details (Moved after verification attempt) ---
            print("\nProceeding to save account details...")
            self.save_account_details(username, self.email, self.password)
            self.accounts_created += 1
            # print(f"Account {self.accounts_created} details saved.") # save_account_details prints this
            
            print("\n--- IMPORTANT --- ")
            print("Account details saved. Browser session remains open for any final checks.")
            input("Press Enter here in the terminal once you are done and ready to close this browser session...")
            return True # Indicate success

        except Exception as e:
            print(f"An unexpected error occurred during Discord account creation: {str(e)}")
            if driver:
                 try: driver.save_screenshot("discord_unexpected_error.png")
                 except: pass
            print("Browser left open (if initialized) for inspection.")
            input("Press Enter to acknowledge the error and stop this Discord attempt...")
            return False
        # NO finally block needed here, run() handles closing

    def verify_discord_email_via_outlook(self, driver):
        """Attempts to automatically verify the Discord email by checking Outlook.
           Returns True if verification link was likely clicked, False otherwise.
        """
        print("\nAttempting automatic Discord email verification via Outlook...")
        max_email_wait_time = 120 # seconds to wait for email
        check_interval = 10 # seconds between checks
        start_time = time.time()
        outlook_tab_handle = driver.window_handles[0] # Assume Outlook is the first tab
        original_tab = driver.current_window_handle
        
        try:
            # --- Check Login Status and Attempt Login ---
            try:
                print("Checking Outlook login status...")
                # Check if we are already in the inbox
                if "outlook.live.com/mail" not in driver.current_url:
                    print("Not logged into Outlook inbox. Attempting login...")
                    # Navigate to login page if not already there
                    if "login.live.com" not in driver.current_url:
                        driver.get("https://login.live.com")
                        self.random_delay(3, 5)

                    # --- Enter Email ---
                    try:
                        email_field = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.NAME, "loginfmt")))
                        self.click_element_humanly(driver, email_field)
                        self.human_type(email_field, self.email)
                        print(f"Entered email {self.email} into login form.")
                        next_button = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.ID, "idSIButton9")))
                        self.click_element_humanly(driver, next_button)
                        print("Clicked Next after email on login page.")
                        self.random_delay(2, 4)
                    except Exception as e_login_email:
                        print(f"Error entering email during Outlook login: {e_login_email}")
                        raise Exception("Outlook login failed at email step.") # Use raise to trigger main failure

                    # --- Enter Password ---
                    try:
                        password_field = WebDriverWait(driver, 15).until(EC.visibility_of_element_located((By.NAME, "passwd")))
                        self.click_element_humanly(driver, password_field)
                        self.human_type(password_field, self.password)
                        print("Entered password into login form.")
                        signin_button = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.ID, "idSIButton9"))) # Often same ID
                        self.click_element_humanly(driver, signin_button)
                        print("Clicked Sign in after password.")
                        self.random_delay(3, 6)
                    except Exception as e_login_pass:
                        print(f"Error entering password/signing in during Outlook login: {e_login_pass}")
                        raise Exception("Outlook login failed at password step.")

                    # --- Handle "Stay signed in?" ---
                    try:
                        WebDriverWait(driver, 15).until(
                            EC.any_of(
                                EC.element_to_be_clickable((By.ID, "idBtn_Back")), # "No" button
                                EC.url_contains("outlook.live.com/mail") # Or successful redirect
                            )
                        )
                        if "login.live.com" in driver.current_url: # Check if prompt is still visible
                             no_button = driver.find_element(By.ID, "idBtn_Back")
                             print("Clicking 'No' on 'Stay signed in?' prompt.")
                             self.click_element_humanly(driver, no_button)
                             self.random_delay(3, 5)
                    except TimeoutException:
                         print("Did not find 'Stay signed in?' prompt or redirect to inbox quickly.")
                    except Exception as e_stay_signed:
                        print(f"Error handling 'Stay signed in?' prompt: {e_stay_signed}")

                    # --- Final Check for Inbox URL ---
                    try:
                        WebDriverWait(driver, 20).until(EC.url_contains("outlook.live.com/mail"))
                        print("Successfully logged into Outlook.")
                    except TimeoutException:
                        print("Failed to reach Outlook inbox after login attempt.")
                        driver.save_screenshot("outlook_login_fail_redirect.png")
                        raise Exception("Outlook login failed, couldn't reach inbox.")
                else:
                    print("Already logged into Outlook.")

                # --- Proceed with checking emails (existing logic) ---
                # (The rest of the email checking while loop goes here)

            except Exception as e:
                print(f"An unexpected error occurred during automatic email verification (incl. login): {e}")
                # ... (rest of existing except block) ...

            while time.time() - start_time < max_email_wait_time:
                print("Refreshing Outlook inbox and searching for Discord verification email...")
                driver.refresh()
                self.random_delay(5, 7) # Wait for refresh and emails to load
                
                try:
                    # Find the Discord email - adjust selector based on actual Outlook HTML
                    # Look for an item with aria-label containing sender/subject
                    discord_email_selector = "div[role='option'][aria-label*='Discord'][aria-label*='Verify']"
                    discord_email_item = WebDriverWait(driver, check_interval - 2).until(
                        EC.element_to_be_clickable((By.CSS_SELECTOR, discord_email_selector))
                    )
                    
                    print("Found potential Discord verification email. Clicking it...")
                    self.click_element_humanly(driver, discord_email_item)
                    self.random_delay(3, 5) # Wait for email content to load
                    
                    # --- Find and Click Verification Link --- 
                    try:
                        # Find the iframe containing the email body (if Outlook uses one)
                        # Adjust selector if needed
                        iframe_selector = "iframe[aria-label='Message body']"
                        WebDriverWait(driver, 10).until(EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR, iframe_selector)))
                        print("Switched to email body iframe.")
                        
                        # Find the verification link - adjust selector based on actual link
                        verify_link_selector = "a[href*='discord.com/verify'][href*='token=']"
                        verify_link = WebDriverWait(driver, 10).until(
                            EC.element_to_be_clickable((By.CSS_SELECTOR, verify_link_selector))
                        )
                        verify_url = verify_link.get_attribute('href')
                        print(f"Found verification link: {verify_url}")
                        
                        # Switch back to default content before opening link in new tab
                        driver.switch_to.default_content()
                        
                        # Open link in a new tab
                        print("Opening verification link in new tab...")
                        driver.execute_script(f"window.open('{verify_url}', '_blank');")
                        self.random_delay(2, 4)
                        driver.switch_to.window(driver.window_handles[-1]) # Switch to the new verification tab
                        print("Switched to verification tab.")
                        self.random_delay(5, 8) # Wait for verification page to process

                        # Optional: Check for success message on verification page
                        # try:
                        #     WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//*[contains(text(), 'Email verified')]")))
                        #     print("Verification page indicates success.")
                        # except:
                        #     print("Could not confirm success message on verification page, but link was clicked.")
                            
                        print("Automatic Discord email verification attempted successfully.")
                        # Close the verification tab
                        driver.close()
                        # Switch back to the original Discord tab (might need adjustment)
                        driver.switch_to.window(original_tab if original_tab in driver.window_handles else driver.window_handles[-1])
                        return True
                        
                    except Exception as e_link:
                        print(f"Error finding/clicking verification link within email: {e_link}")
                        driver.switch_to.default_content() # Ensure we switch back if iframe failed
                        break # Stop trying if we can't process the email
                        
                except TimeoutException:
                    print(f"Discord email not found yet. Waiting {check_interval}s...")
                    # time.sleep(check_interval) # Handled by loop and WebDriverWait timeout
                except Exception as e_find:
                    print(f"Error searching for Discord email item: {e_find}")
                    break # Stop trying if there's an error finding emails

            print("Timed out waiting for Discord verification email in Outlook.")
            driver.switch_to.window(original_tab if original_tab in driver.window_handles else driver.window_handles[-1]) # Switch back before failing
            return False
            
        except Exception as e:
            print(f"An unexpected error occurred during automatic email verification: {e}")
            try:
                 # Attempt to switch back to original tab on error
                 driver.switch_to.window(original_tab if original_tab in driver.window_handles else driver.window_handles[-1])
            except: pass
            return False

    def run(self, num_accounts):
        print(f"Attempting to create {num_accounts} Discord accounts using Microsoft/Outlook.")
        
        successful_creations = 0
        for i in range(num_accounts):
            print(f"\n--- Starting Account Creation {i+1}/{num_accounts} ---")
            driver = None 
            self.email = None # Ensure email is reset for each new account attempt
            account_success = False
            try:
                # 1. Create Microsoft Account
                driver = self.create_microsoft_account()
                
                if driver:
                    print("Microsoft account process completed. Proceeding to Discord.")
                    # 2. Create Discord Account using the same browser session
                    username = self.generate_random_username() 
                    display_name = self.generate_random_display_name()
                    account_success = self.create_discord_account(driver, username=username, display_name=display_name)
                    
                    if account_success:
                        successful_creations += 1
                        print(f"Successfully completed process for Discord account {i+1}. Browser closing after your final Enter press.")
                    else:
                        print(f"Failed during Discord creation steps for account {i+1}. Browser left open.")
                else:
                    print(f"Failed during Microsoft creation steps for attempt {i+1}. Browser potentially left open.")
                    # Driver might be None or already closed by user input in create_microsoft_account

            except Exception as e:
                print(f"An unexpected error occurred in the main run loop for account {i+1}: {str(e)}")
                if driver:
                    print("Browser left open due to main loop error.")
                    input("Press Enter to acknowledge the main loop error...")
                # No automatic driver quit here

            finally:
                # REMOVED automatic driver.quit() from here.
                # Browser is closed by user pressing Enter in input() prompts 
                # (either on success in create_discord_account or on error in either function).
                if driver and account_success: # Only close if successful *and* user pressed Enter
                    try: 
                        driver.quit()
                        print("Browser closed successfully after user confirmation.")
                    except Exception as eq:
                        print(f"Error trying to close browser after success: {eq}")
                elif driver and not account_success:
                    print(f"Browser for account {i+1} remains open due to failure. Please close it manually when done inspecting.")
                
                # Add a longer delay between account creations
                if i < num_accounts - 1: 
                    delay = random.uniform(60, 180)
                    print(f"Waiting for {delay:.2f} seconds before next account attempt... ({i+2}/{num_accounts})" )
                    time.sleep(delay)

        print(f"\n--- Run Complete ---")
        print(f"Attempted {num_accounts} accounts. Successfully processed: {successful_creations}.")

if __name__ == "__main__":
    creator = DiscordAccountCreator()
    creator.run(10)
