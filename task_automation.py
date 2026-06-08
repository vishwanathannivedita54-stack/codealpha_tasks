import os
import re
import shutil

# ─────────────────────────────────────────────
# OPTION 1: Move all .jpg files to a new folder
# ─────────────────────────────────────────────
def move_jpg_files(source_folder=".", destination_folder="jpg_files"):
    os.makedirs(destination_folder, exist_ok=True)
    moved = 0

    for filename in os.listdir(source_folder):
        if filename.lower().endswith(".jpg"):
            src = os.path.join(source_folder, filename)
            dst = os.path.join(destination_folder, filename)
            shutil.move(src, dst)
            print(f"✅ Moved: {filename} → {destination_folder}/")
            moved += 1

    print(f"\n📁 Total .jpg files moved: {moved}")

# ─────────────────────────────────────────────
# OPTION 2: Extract all emails from a .txt file
# ─────────────────────────────────────────────
def extract_emails(input_file="input.txt", output_file="extracted_emails.txt"):
    if not os.path.exists(input_file):
        # Create a sample input file for demo purposes
        with open(input_file, "w") as f:
            f.write("""Hello, please contact us at support@example.com for help.
You can also reach john.doe@gmail.com or hr@company.org.
Invalid emails like @wrong or missing@.com will be ignored.
Feel free to email intern@codeAlpha.tech for internship queries.
""")
        print(f"📄 Sample '{input_file}' created for demo.")

    with open(input_file, "r") as f:
        content = f.read()

    # Regex pattern for valid email addresses
    email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    emails = re.findall(email_pattern, content)
    unique_emails = sorted(set(emails))

    if unique_emails:
        with open(output_file, "w") as f:
            f.write("Extracted Email Addresses\n")
            f.write("=" * 35 + "\n")
            for email in unique_emails:
                f.write(email + "\n")

        print(f"\n📧 Found {len(unique_emails)} unique email(s):")
        for email in unique_emails:
            print(f"   • {email}")
        print(f"\n✅ Saved to '{output_file}'")
    else:
        print("⚠️  No email addresses found.")

# ─────────────────────────────────────────────
# OPTION 3: Scrape title of a fixed webpage
# ─────────────────────────────────────────────
def scrape_webpage_title(url="https://www.python.org"):
    try:
        import urllib.request
        with urllib.request.urlopen(url) as response:
            html = response.read().decode("utf-8")

        match = re.search(r'<title>(.*?)</title>', html, re.IGNORECASE | re.DOTALL)
        if match:
            title = match.group(1).strip()
            print(f"\n🌐 Page Title: {title}")

            with open("webpage_title.txt", "w") as f:
                f.write(f"URL: {url}\nTitle: {title}\n")
            print("✅ Saved to 'webpage_title.txt'")
        else:
            print("⚠️  Could not find a title tag.")
    except Exception as e:
        print(f"❌ Error fetching page: {e}")

# ─────────────────────────────────────────────
# MAIN MENU
# ─────────────────────────────────────────────
def main():
    print("=" * 45)
    print("   🤖 Task Automation with Python Scripts")
    print("=" * 45)
    print("\nChoose a task to automate:")
    print("  1. Move all .jpg files to a new folder")
    print("  2. Extract email addresses from a .txt file")
    print("  3. Scrape the title of a webpage")

    choice = input("\nEnter choice (1/2/3): ").strip()

    if choice == "1":
        folder = input("Enter source folder path (press Enter for current folder): ").strip() or "."
        move_jpg_files(source_folder=folder)

    elif choice == "2":
        input_file = input("Enter .txt file name (press Enter for 'input.txt'): ").strip() or "input.txt"
        extract_emails(input_file=input_file)

    elif choice == "3":
        scrape_webpage_title()

    else:
        print("❌ Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()
