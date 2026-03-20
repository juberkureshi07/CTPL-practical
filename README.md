# CTPL-practical

Scan the entire project for secrets and credentials. Ensure API keys, database service keys, and tokens are never exposed in frontend code or committed to the repository. Move all secrets to secure environment variables and ensure they are only used on the server.



Configure the application for secure deployment.
Enforce HTTPS, ensure secrets are stored securely, restrict direct database access from the public internet, and add logging for authentication attempts, API errors, and unusual traffic patterns so suspicious behavior can be detected.


Review all API endpoints and database queries. Ensure every request verifies the logged-in user owns the data being accessed. Prevent insecure direct object reference (IDOR) vulnerabilities by enforcing ownership checks before reading, modifying, or deleting any resource.


Act as a senior security engineer. Review the authentication system of this project and make it secure. Ensure passwords are securely hashed, sessions expire, email verification is enabled, password reset tokens expire, login attempts are rate limited, and authentication secrets are never exposed to the frontend. Refactor any insecure authentication logic.