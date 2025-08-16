import re

def check_strength(password):
    score = 0
    feedback = []

    # Criteria checks
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Make it at least 8 characters long.")

    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("Add uppercase letters.")

    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("Add lowercase letters.")

    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("Include some numbers.")

    if re.search(r"[!@#$%^&*()_+\-=\[\]{};':\"\\|,.<>\/?]", password):
        score += 1
    else:
        feedback.append("Use special characters.")

    # Strength rating
    levels = {
        0: ("Very Weak", "❌"),
        1: ("Weak", "⚠️"),
        2: ("Moderate", "🟡"),
        3: ("Strong", "🟢"),
        4: ("Very Strong", "✅"),
        5: ("Excellent", "💪")
    }

    rating, icon = levels[score]
    return rating, icon, feedback

def main():
    print("🔐 Password Strength Tester 🔐")
    password = input("Enter a password to test: ")
    
    rating, icon, feedback = check_strength(password)
    
    print(f"\nStrength: {rating} {icon}")
    
    if feedback:
        print("\nSuggestions to improve:")
        for tip in feedback:
            print(f"- {tip}")
    else:
        print("✅ Your password looks great!")

if __name__ == "__main__":
    main()