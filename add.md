Update my existing PWA app called "Semicolon Ai" by adding an install-gate experience without breaking the current app design, routes, features, or backend logic.

Important context:
- This is an existing working app, not a new project
- Keep the current UI style, branding, color theme, routing structure, authentication flow, and existing functionality
- Only add the new install-required behavior and related UI
- Do not rebuild the whole app from scratch
- Do not remove any existing pages or features
- Integrate the new logic cleanly into the current codebase

Goal:
The main app should only be fully usable when opened as an installed PWA in standalone mode. If users open the app in a normal browser, they should see a branded install-required screen or be redirected to an install page, while protected app sections remain inaccessible until the PWA is installed and launched from the home screen.

Required behavior:
1. Detect whether the app is running in standalone mode
2. If the app is running in standalone mode:
   - allow users to access the existing app normally
   - keep all current pages and app flows working
3. If the app is NOT running in standalone mode:
   - block access to protected sections of the existing app
   - show an install-required screen that matches the current Semicolon Ai design
   - allow access only to selected public pages if needed, such as home, about, contact, privacy, terms, or install page
4. If a user tries to open protected routes in browser mode, redirect them to the install page
5. Keep this as a UX gate, not security. Do not pretend it is backend protection
6. Add comments in the code explaining what is happening and where to customize route protection later

Design requirements:
- The new install gate must match the current design system of my app
- Reuse existing fonts, colors, spacing, components, buttons, cards, and branding wherever possible
- The install-required page should feel like part of the same app, not a separate template
- Keep the UI modern, clean, mobile-friendly, and polished
- Add a strong heading like:
  "Install Semicolon Ai to continue"
- Add short supporting text about better app experience after installation
- Add an install button
- Add fallback manual install instructions for Android Chrome and iPhone Safari
- Add optional feature preview cards from the existing app if useful
- Add subtle animation only if it matches the current app style

Technical requirements:
- Do not replace the current app architecture unless absolutely needed
- Work inside the existing framework and project structure
- Create a reusable utility or helper function to detect standalone mode using:
  - window.matchMedia('(display-mode: standalone)').matches
  - window.navigator.standalone for iOS fallback
- Handle beforeinstallprompt properly
- Save the deferred install prompt and trigger it from a custom install button when available
- If install prompt is not available, show manual instructions
- Add route guarding or middleware-like logic for protected routes depending on the framework
- Keep existing authentication, API calls, and Firebase logic untouched unless needed for integration
- Ensure the app still works properly after installation
- Keep changes modular and easy to maintain

Implementation details:
- Add a reusable component such as:
  - InstallGate
  - InstallButton
  - InstallRequiredPage
- Add helper file for standalone detection
- Add protected route logic that can be applied to routes like:
  - /app
  - /dashboard
  - /tools
  - /chat
  - /profile
  - or equivalent existing private routes in my app
- Allow public pages to remain accessible if desired
- If my app already has a landing page, integrate the install CTA into it instead of making a disconnected screen
- If my app already uses a layout system, wrap protected content inside the install gate cleanly
- Preserve existing loading, navigation, and error handling patterns

PWA requirements:
- Review the existing manifest and service worker setup
- Improve them only if necessary for proper installability
- Ensure manifest, icons, display mode, theme color, and installability settings are correct
- Do not break the existing PWA setup

User experience:
- In browser mode:
  - show install-required experience
  - hide or block main app content
  - redirect protected routes to install page
- In standalone mode:
  - allow full normal use of the app
- Make the experience smooth on mobile devices
- Show a helpful message if the browser does not support install prompt events

Output expected:
- Modify the existing app, do not generate a totally fresh app
- Show exactly which files should be added or updated
- Generate production-ready code for the required changes
- Keep the code clean, well-structured, and commented
- Avoid unnecessary rewrites

Extra instruction:
Before coding, first analyze the current project structure and identify the best integration points for:
- standalone mode detection
- install prompt handling
- protected route gating
- install page UI
Then implement the feature in the least disruptive way possible.





Important: make minimal but high-quality changes, and preserve the current Semicolon Ai app experience as much as possible.