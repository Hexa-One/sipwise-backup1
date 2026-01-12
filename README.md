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

1. Download the distribution package which contains:
   - `sipwise-backup.zip` - The application package
   - `install.sh` - The installation script

2. Place both files in the same directory and navigate to it:
   ```bash
   cd /path/to/download/directory
   ```

3. Run the installation script with sudo:
   ```bash
   sudo ./install.sh
   ```

The installation script will:
- Check for Python 3
- Extract the application to `/opt/sipwise-backup/`
- Create a wrapper script in `/usr/bin/sipwise-backup`
- Register and enable the systemd service
- Automatically start the service

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

To remove sipwise-backup from your system, run the uninstallation script:

```bash
sudo /opt/sipwise-backup/uninstall.sh
```

The uninstallation script will:
- Stop and disable the systemd service
- Remove the systemd service file
- Remove the wrapper script from `/usr/bin`
- Remove all application files from `/opt/sipwise-backup`

## Development

This is the initial version with basic CLI functionality. Additional features will be developed in future releases.

## File Structure

### Distribution Package
```
distribution/
├── sipwise-backup.zip       # Application package
└── install.sh               # Installation script (outside zip)
```

### Installed System
```
/opt/sipwise-backup/
├── CLI/
│   └── main.py              # Main Python CLI application
├── service/
│   └── sipwise-backup.service   # systemd service file
├── uninstall.sh             # Uninstallation script
└── README.md                # Documentation

/usr/bin/
└── sipwise-backup           # Wrapper script

/etc/systemd/system/
└── sipwise-backup.service   # Registered systemd service
```

### Repository Structure
```
sipwise-backup/
├── CLI/
│   └── main.py              # Main Python CLI application
├── service/
│   └── sipwise-backup.service   # systemd service file
├── install.sh               # Installation script (not included in zip)
├── uninstall.sh             # Uninstallation script
└── README.md                # This file
```

## Architecture

- **CLI/main.py**: Python-based menu interface for the application
- **service/sipwise-backup.service**: systemd service configuration
- **install.sh**: Extracts zip package and handles installation to `/opt`, including Python checks and systemd registration
- **uninstall.sh**: Handles complete removal of the application and service from the system

## License

Copyright © 2026

## Support

For issues and questions, please contact your system administrator.