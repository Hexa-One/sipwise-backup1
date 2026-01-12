#!/usr/bin/env python3
"""
sipwise-backup CLI Application
Main Menu Interface
Version: 1.0.0
"""

import sys
import os
import subprocess


class SipwiseBackupCLI:
    """Main CLI class for sipwise-backup application"""

    def __init__(self):
        self.version = "1.0.0"
        self.running = True
        self.install_dir = "/opt/sipwise-backup"
        self.config_file = os.path.join(self.install_dir, "config.yml")

    def show_banner(self):
        """Display application banner"""
        print("=" * 40)
        print(f"   sipwise-backup CLI v{self.version}")
        print("=" * 40)
        print()

    def show_menu(self):
        """Display main menu options"""
        print("\n--- Main Menu ---")
        print("(1) Config Menu")
        print("(2) Exit")
        print()

    def show_config_menu(self):
        """Display config submenu options"""
        print("\n--- Config Menu ---")
        print("(1) Edit config.yml")
        print("(2) Restart service")
        print("(3) Return to main menu")
        print()

    def get_user_choice(self):
        """Get user input for menu selection"""
        try:
            choice = input("Enter your choice: ").strip()
            return choice
        except (KeyboardInterrupt, EOFError):
            print("\n\nExiting...")
            return "exit"

    def edit_config(self):
        """Open config.yml in nano editor"""
        print(f"\nOpening {self.config_file} in nano...")
        print("Press Ctrl+X to exit nano\n")
        try:
            subprocess.run(["nano", self.config_file], check=True)
            print("\nConfig file editor closed.")
        except subprocess.CalledProcessError:
            print("\nError: Failed to open nano editor.")
        except FileNotFoundError:
            print("\nError: nano editor not found. Please install nano.")

    def restart_service(self):
        """Restart the sipwise-backup systemd service"""
        print("\nRestarting sipwise-backup service...")
        try:
            result = subprocess.run(
                ["systemctl", "restart", "sipwise-backup.service"],
                capture_output=True,
                text=True,
                check=True
            )
            print("✓ Service restarted successfully!")
        except subprocess.CalledProcessError as e:
            print(f"Error: Failed to restart service.")
            print(f"You may need to run: sudo systemctl restart sipwise-backup")
        except PermissionError:
            print("Error: Permission denied. Try running:")
            print("  sudo systemctl restart sipwise-backup")

    def handle_config_menu(self):
        """Handle config menu navigation"""
        in_config_menu = True
        while in_config_menu:
            self.show_config_menu()
            choice = self.get_user_choice()

            if choice == "1":
                self.edit_config()
            elif choice == "2":
                self.restart_service()
            elif choice == "3":
                print("\nReturning to main menu...")
                in_config_menu = False
            elif choice == "exit":
                self.handle_exit()
            else:
                print(f"\nInvalid choice: {choice}")
                print("Please select a valid option.")

    def handle_exit(self):
        """Handle exit command"""
        print("\nExiting sipwise-backup...")
        self.running = False
        sys.exit(0)

    def handle_choice(self, choice):
        """Process user menu choice"""
        if choice == "1":
            self.handle_config_menu()
        elif choice == "2":
            self.handle_exit()
        elif choice == "exit":
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
