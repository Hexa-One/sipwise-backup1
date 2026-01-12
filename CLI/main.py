#!/usr/bin/env python3
"""
sipwise-backup CLI Application
Main Menu Interface
Version: 1.0.0
"""

import sys


class SipwiseBackupCLI:
    """Main CLI class for sipwise-backup application"""

    def __init__(self):
        self.version = "1.0.0"
        self.running = True

    def show_banner(self):
        """Display application banner"""
        print("=" * 40)
        print(f"   sipwise-backup CLI v{self.version}")
        print("=" * 40)
        print()

    def show_menu(self):
        """Display main menu options"""
        print("\n--- Main Menu ---")
        print("(1) Exit")
        print()

    def get_user_choice(self):
        """Get user input for menu selection"""
        try:
            choice = input("Enter your choice: ").strip()
            return choice
        except (KeyboardInterrupt, EOFError):
            print("\n\nExiting...")
            return "1"

    def handle_exit(self):
        """Handle exit command"""
        print("\nExiting sipwise-backup...")
        self.running = False
        sys.exit(0)

    def handle_choice(self, choice):
        """Process user menu choice"""
        if choice == "1":
            self.handle_exit()
        else:
            print(f"\nInvalid choice: {choice}")
            print("Please select a valid option.")

    def run(self):
        """Main application loop"""
        self.show_banner()

        while self.running:
            self.show_menu()
            choice = self.get_user_choice()
            self.handle_choice(choice)


def main():
    """Entry point for the application"""
    try:
        cli = SipwiseBackupCLI()
        cli.run()
    except KeyboardInterrupt:
        print("\n\nInterrupted. Exiting...")
        sys.exit(0)
    except Exception as e:
        print(f"\nError: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
