**Compass Software Update Tool**

Manage and Download Updates/Patches for [Compass-Software](https://www.compass-software.de/)

**Why I wrote this Program:**

Our Workshop is in a small town, Internet is slow an and downloading huge Updates and installing them on every workstation was a very time consuming task.
The Programm should be easy2use, with centralized storage for downloaded update files and decentralized for updating every single workstation.

**Installation:**

- Set up a Network folder on your Companies Server. Create a Folder with the CompassUpdateHelper.exe and config.yaml in it.
- on every machine which needs Updates mount the Folder always with the same path.
- create a link to the CompassUpdateHelper.exe on every machine and tell your coworkers to only use that link, (so nothing gets deleted every 10 days :D) 
- modify the path in the Config file as you like, but they all have to point too the **same** folder/networkdrive etc.!!

**Workflow is like that:**

- Compass-Software sends you an update link
- Fire up the Programm and select 'Download Update/Patch'
- Insert Url and hit >Enter<
- The Programm recognizes through the url which type of Update it is and stores it then in the right folder.
- Back in the Main Menu select the corresponding Installiere... menu item and choose your Update. (the latest one is always the first)
- Enjoy easy updating lots of Machines :)

## Disclaimer

The information and code provided in this repository are for educational and informational purposes only. While every effort has been made to ensure the accuracy and reliability of the information and code presented, the author makes no warranties, express or implied, regarding the completeness, accuracy, or reliability of the content.

The author disclaims any liability, loss, or risk incurred as a consequence of using or relying on the information and code provided in this repository. The examples and code snippets provided are not intended to be used in production environments without proper review, testing, and customization.

Users are solely responsible for any actions they take based on the information and code provided in this repository. The author shall not be liable for any damages, direct or indirect, including but not limited to any lost profits, lost savings, or any other incidental, consequential, or special damages arising out of the use or misuse of the information and code provided.

It is recommended to review and test the code thoroughly in your own development and production environments before using it in any critical or production systems.

Use at your own risk.

