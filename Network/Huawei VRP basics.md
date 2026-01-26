### Command views

* **user view**: \<Huawei>
* **system view**: [Huawei]
* **interface view**: [Huawei-Ethernet0/0/1]
* **protocol view**: [Huawei-ospf-1]

```bash
# Moving between views
<Huawei> system-view 
[Huawei]


[Huawei] interface Ethernet 0/0/1
[Huawei-Ethernet0/0/1]


[Huawei-Ethernet0/0/1] quit
[Huawei] quit
<Huawei> 
```

**Notes**
* You can press `Tab` to autocomplete the command
* You can write `?` to get help
* You can press `ctrl + z` to go to the user view



### Basic commands

```bash
<Huawei> display version      #  display basic info about the device


# Change device name 
<Huawei> system-view
[Huawei] sysname Device-Name
[Device-Name]


# Give an IP to an interface
<Huawei> system-view
[Huawei] interface Ethernet 0/0/0
[Huawei-interface-Ethernet0/0/0] ip address 192.168.1.10 24
[Huawei-interface-Ethernet0/0/0] display this      # display the running configuration in the current view


# Remove an IP from an interface
<Huawei> system-view
[Huawei] interface Ethernet 0/0/0
[Huawei-interface-Ethernet0/0/0] undo ip address 


# Display current device configuration
<Huawei> system-view
[Huawei] display current-configuration


# Save current configuration
<Huawei> save
<Huawei> save filename.cfg          # save running configuration in a file


# Compare running configuration with startup configuration
<Huawei> compare configuration
```



### Shortcuts

| Shortcut / Key        | Function |
|-----------------------|----------|
| `?`                   | Display help for available commands or parameters |
| `Tab`                 | Auto-complete a command or keyword |
| `↑ / ↓` (Arrow keys)  | Browse command history |
| `Ctrl + A`            | Move cursor to the beginning of the line |
| `Ctrl + B`            | Move cursor one character left |
| `Ctrl + C`            | Stop the current command |
| `Ctrl + E`            | Move cursor to the end of the line |
| `Ctrl + X`            | Delete all the characters on the left of the cursor |
| `Ctrl + Y`            | Delete the characters at the cursor and all the characters on the right |
| `Ctrl + Z`            | Return to the user view |


**Note**

> There are 4 user-defined shortcut keys that can be customized `ctrl + G`, `ctrl + L`, `ctrl + O`, `ctrl + U`



### Dealing with filesystem


```bash
# -------------------------------
# Directory navigation & viewing
# -------------------------------

<Huawei> pwd            # Show the current working directory
<Huawei> dir            # List files and directories in the current path
<Huawei> more           # Display the contents of a file page by page
<Huawei> cd             # Change the current working directory

# -------------------------------
# Directory management
# -------------------------------

<Huawei> mkdir          # Create a new directory
<Huawei> rmdir          # Remove an empty directory

# -------------------------------
# File management
# -------------------------------

<Huawei> copy           # Copy a file from one location to another
<Huawei> move           # Move a file to a different directory
<Huawei> rename         # Rename a file
<Huawei> delete         # Delete a file (moves it to the recycle bin)

# -------------------------------
# Recycle bin operations
# -------------------------------

<Huawei> undelete           # Restore a deleted file from the recycle bin
<Huawei> reset recycle-bin  # Permanently clear all files in the recycle bin
```

**Notes** 💡

* `delete` ≠ permanent removal — files go to the **recycle bin**
* `reset recycle-bin` is **irreversible**



### Commands part 2


```bash
# -------------------------------
# Startup Configuration
# -------------------------------

# Save a file as a startup configuraion
<Huawei> startup saved-configuraion filename.cfg


# Display the startup configuraion file
<Huawei> display startup


# Clear the configuraion file
<Huawei> reset saved-configuraion


# Restart the device
<Huawei> reboot


# -------------------------------
# CLock
# -------------------------------
<Huawei> display clock          # Display the current system time
2026-01-25 14:32:10+01:00

<Huawei> clock datetime 14:30:00 2026-01-25     # Set the system clock manually



# -------------------------------
# Set passwords
# -------------------------------

# Remote access password (maximum 15 users)
[Huawei] user-interface vty 0 4
[Huawei-ui-vty0-4] set authentication password cipher VTY@123


# Console password
[Huawei] user-interface console 0
[Huawei-ui-console0] set authentication password cipher Console@123


# idle timeout
<Huawei> system-view
[Huawei] user-interface console 0    OR    [Huawei] user-interface vty 0 4
[Huawei-ui-console0] idle-timeout 10 0     # 10 min  0 seconds

```