# sipwise-backup

A Python-based CLI application for Debian servers to manage Sipwise backups.

## Version

1.0.0

## Requirements

- Debian-based Linux server
- Python 3.x
- systemd (for service management)
- Root/sudo privileges for installation

## Installation

1. Navigate to the sipwise-backup directory:
   ```bash
   cd /path/to/sipwise-backup
   ```

2. Run the installation script with sudo:
   ```bash
   sudo ./install.sh
   ```

The installation script will:
- Check for Python 3 installation
- Install the CLI application to `/usr/local/share/sipwise-backup/`
- Create a wrapper script in `/usr/local/bin/sipwise-backup`
- Register the systemd service

## Usage

### Running the CLI

After installation, you can run the application from anywhere:

```bash
sipwise-backup
```

### Available Menu Options

Once the CLI is running, you can use the following menu options:

- `(1) Exit` - Exit the application

### Running as a Service

You can also run sipwise-backup as a systemd service:

```bash
# Enable the service to start on boot
sudo systemctl enable sipwise-backup

# Start the service
sudo systemctl start sipwise-backup

# Check service status
sudo systemctl status sipwise-backup

# Stop the service
sudo systemctl stop sipwise-backup

# Disable the service
sudo systemctl disable sipwise-backup
```

## Uninstallation

To remove sipwise-backup from your system:

1. Navigate to the sipwise-backup directory:
   ```bash
   cd /path/to/sipwise-backup
   ```

2. Run the uninstallation script with sudo:
   ```bash
   sudo ./uninstall.sh
   ```

The uninstallation script will:
- Stop and disable the systemd service
- Remove the systemd service file
- Remove the wrapper script
- Remove all application files

## Development

This is the initial version with basic CLI functionality. Additional features will be developed in future releases.

## File Structure

```
sipwise-backup/
├── CLI/
│   └── main.py              # Main Python CLI application
├── service/
│   └── sipwise-backup.service   # systemd service file
├── install.sh               # Installation script
├── uninstall.sh             # Uninstallation script
└── README.md                # This file
```

## Architecture

- **CLI/main.py**: Python-based menu interface for the application
- **service/sipwise-backup.service**: systemd service configuration
- **install.sh**: Handles installation, including Python checks and systemd registration
- **uninstall.sh**: Handles complete removal of the application and service

## License

Copyright © 2026

## Support

For issues and questions, please contact your system administrator.