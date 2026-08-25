import base64
import binascii
import os
import re
import sys
import time

# System-Check
if sys.version_info < (3, 8):
    sys.exit("❌ Dieses Skript benötigt mindestens Python 3.8.")

def sanitize_input(user_input: str) -> str:
    """Input Sanitization gegen bösartige Eingaben."""
    clean_text = re.sub(r'[^\w\s\-\?\.\!\@]', '', user_input)
    return clean_text.strip()

def print_slow(text: str, delay: float = 0.015):
    """Gibt Text Zeichen für Zeichen aus."""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def show_readme():
    """Liest die README.md sicher aus."""
    readme_path = "README.md"
    if not os.path.exists(readme_path) and os.path.exists("../README.md"):
        readme_path = "../README.md"

    print("\n" + "=" * 60)
    print(" 📄 README.md INHALT")
    print("=" * 60 + "\n")

    if os.path.exists(readme_path):
        try:
            from rich.console import Console
            from rich.markdown import Markdown
            console = Console()
            with open(readme_path, "r", encoding="utf-8") as f:
                console.print(Markdown(f.read()))
        except ImportError:
            with open(readme_path, "r", encoding="utf-8") as f:
                print(f.read())
    else:
        print("⚠️ README.md konnte im Hauptverzeichnis nicht gefunden werden.")

    print("\n" + "=" * 60)

def trigger_ninja_egg():
    """Geheimes Easter Egg: Hobbies."""
    print("\n" + "✨" * 30)
    print(" 🥷 UNLOCKED: HIDDEN EASTER EGG // SIDE QUESTS & PASSIONS")
    print("✨" * 30)
    print("🥷 Ninjutsu: Fokussiert, flexibel & immer einen Schritt voraus.")
    print("🎹 Klavier: Komplexe Strukturen harmonisch zusammenführen.")
    print("🍳 Kochen: Gute Zutaten + rezeptgenaue Architektur = Perfektion.")
    print("🕺 Tanzen: Rhythmus, Timing und perfekte Koordination.")
    print("🌿 Naturheilkunde: Ganzheitliche Problemlösung – Ursachen verstehen.")
    print("✨" * 30)

def trigger_beer_egg():
    """Geheimes Easter Egg: Zapfhahn."""
    print("\n" + "🍺" * 30)
    print(" 🍺 UNLOCKED: SOFTWARE BRAUEREI ZAPFHAHN")
    print("🍺" * 30)
    print("\nZapfe frischen Code & Kaffee/Bier...")
    for i in range(1, 4):
        time.sleep(0.4)
        print(f"   [🍺] Gläser gefüllt: {i * 33}%")
    time.sleep(0.3)
    print("\n✨ Prost! Bereit für das Erstgespräch!")
    print("🍺" * 30)

def main():
    print("\n" + "=" * 60)
    print(" 🚀 ESTEBAN REYES // SENIOR ENTERPRISE & AI ARCHITECT")
    print("=" * 60)
    
    print("\n📌 Quick Overview:")
    print(" - Name: M.Sc. Esteban J. Reyes Klapka")
    print(" - Rolle: Senior SAP Technology, Cloud & AI Architect (18+ Jahre Experience)")
    print(" - Aktuell: SAP Technology Architect @ Robert Bosch GmbH")
    print(" - Focus: Enterprise Architecture, SAP BTP, AWS & AI Strategy")
    
    while True:
        print("\n" + "-" * 60)
        print("Wähle eine Option:")
        print(" [1] Warum Software Brauerei?")
        print(" [2] Kontaktdaten anzeigen")
        print(" [3] README.md direkt im Terminal lesen")
        print(" [q] Beenden / Exit")
        print("-" * 60)

        try:
            raw_choice = input("\nDeine Wahl (1/2/3/q): ")
            choice = sanitize_input(raw_choice).lower()
            
            if choice == "1":
                print_slow(
                    "\n👉 Weil ihr 'Just Fucking Do It' lebt, pragmatische Lösungen schätzt "
                    "und echte KI- & Integrations-Architekturen baut!"
                )
            elif choice == "2":
                print("\n📧 E-Mail: ejklapka@gmail.com")
                print("📞 Telefon: +49 151 10196771")
                print("📍 Furtwangen")
            elif choice == "3":
                show_readme()
            # 🤫 Hidden Easter Eggs
            elif choice in ["hobbies", "hobby"]:
                trigger_ninja_egg()
            elif choice in ["bier", "beer", "prost", "zapfen"]:
                trigger_beer_egg()
            elif choice in ["q", "exit", "quit"]:
                print("\nCiao! Bis bald bei einem Bier 🍻\n")
                break
            else:
                print("\n⚠️ Ungültige Eingabe – probier '1', '2', '3' oder 'q'!")
                
        except (KeyboardInterrupt, EOFError):
            print("\n\nProzess abgebrochen. Bis bald! 🍻\n")
            break

if __name__ == "__main__":
    main()
