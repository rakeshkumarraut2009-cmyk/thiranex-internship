import re
import random
import string

# ============================================================
#   PASSWORD STRENGTH ANALYZER
#   Project 1 - Thiranex Cyber Security Internship
#   Intern: Rakesh Kumar Raut | ID: THX-MAY2226-591
# ============================================================

def check_password_strength(password):
    score = 0
    feedback = []

    print("\n--- Checking Password ---")
    print(f"Password: {password}")
    print("-" * 35)

    # 1. Length check
    if len(password) >= 12:
        score += 2
        print("[✓] Length is 12+ characters (Strong)")
    elif len(password) >= 8:
        score += 1
        print("[~] Length is 8-11 characters (Moderate)")
        feedback.append("Use at least 12 characters for stronger password")
    else:
        print("[✗] Length is less than 8 characters (Weak)")
        feedback.append("Password must be at least 8 characters long")

    # 2. Uppercase check
    if re.search(r'[A-Z]', password):
        score += 1
        print("[✓] Contains uppercase letters")
    else:
        print("[✗] No uppercase letters found")
        feedback.append("Add uppercase letters (A-Z)")

    # 3. Lowercase check
    if re.search(r'[a-z]', password):
        score += 1
        print("[✓] Contains lowercase letters")
    else:
        print("[✗] No lowercase letters found")
        feedback.append("Add lowercase letters (a-z)")

    # 4. Number check
    if re.search(r'[0-9]', password):
        score += 1
        print("[✓] Contains numbers")
    else:
        print("[✗] No numbers found")
        feedback.append("Add numbers (0-9)")

    # 5. Special character check
    if re.search(r'[!@#$%^&*()_+\-=\[\]{};\':"\\|,.<>\/?]', password):
        score += 1
        print("[✓] Contains special characters")
    else:
        print("[✗] No special characters found")
        feedback.append("Add special characters (!@#$%^&*)")

    # 6. Common password check
    common_passwords = [
        "password", "123456", "password123", "admin", "letmein",
        "welcome", "monkey", "dragon", "qwerty", "abc123"
    ]
    if password.lower() in common_passwords:
        score -= 2
        print("[✗] This is a very common password!")
        feedback.append("Avoid common passwords like 'password', '123456'")
    else:
        print("[✓] Not a common password")

    # 7. Repeated characters check
    if re.search(r'(.)\1{2,}', password):
        score -= 1
        print("[✗] Contains repeated characters (e.g. aaa, 111)")
        feedback.append("Avoid repeating the same character 3+ times")
    else:
        print("[✓] No repeated character patterns")

    print("-" * 35)

    # Strength result
    if score <= 1:
        strength = "VERY WEAK ❌"
        color_hint = "Change this password immediately!"
    elif score == 2:
        strength = "WEAK ⚠️"
        color_hint = "This password needs improvement."
    elif score == 3:
        strength = "FAIR 🟡"
        color_hint = "Decent, but can be stronger."
    elif score == 4:
        strength = "STRONG 🟢"
        color_hint = "Good password!"
    else:
        strength = "VERY STRONG ✅"
        color_hint = "Excellent password!"

    print(f"\nScore  : {max(score, 0)} / 6")
    print(f"Result : {strength}")
    print(f"Tip    : {color_hint}")

    if feedback:
        print("\n--- Suggestions to Improve ---")
        for i, tip in enumerate(feedback, 1):
            print(f"  {i}. {tip}")

    return score


def generate_strong_password(length=14):
    upper = random.choices(string.ascii_uppercase, k=2)
    lower = random.choices(string.ascii_lowercase, k=4)
    digits = random.choices(string.digits, k=3)
    symbols = random.choices("!@#$%^&*", k=2)
    rest = random.choices(string.ascii_letters + string.digits, k=length - 11)
    all_chars = upper + lower + digits + symbols + rest
    random.shuffle(all_chars)
    return ''.join(all_chars)


def main():
    print("=" * 40)
    print("  PASSWORD STRENGTH ANALYZER")
    print("  Thiranex Cyber Security Internship")
    print("  Intern: Rakesh Kumar Raut")
    print("=" * 40)

    while True:
        print("\nOptions:")
        print("  1. Check a password")
        print("  2. Generate a strong password")
        print("  3. Exit")

        choice = input("\nEnter choice (1/2/3): ").strip()

        if choice == '1':
            password = input("Enter password to check: ")
            if not password:
                print("No password entered!")
                continue
            check_password_strength(password)

        elif choice == '2':
            pw = generate_strong_password()
            print(f"\n[✓] Generated Strong Password: {pw}")
            print("(Save this password somewhere safe!)")

        elif choice == '3':
            print("\nThank you! Goodbye.")
            break

        else:
            print("Invalid choice. Please enter 1, 2, or 3.")


if __name__ == "__main__":
    main()