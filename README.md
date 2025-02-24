# Snapsync <img src="path/to/logo.png" width="100" alt="Snapsync Logo">
Snapsync is an innovative social media platform designed to deepen connections by uncovering shared past experiences. Using advanced geolocation and timestamp analysis, Snapsync enables users to discover if they have unknowingly crossed paths ("synced") with friends or acquaintances at events, travels, or in everyday situations. This application not only enhances social interactions by revealing surprising coincidences but also adds a layer of nostalgia and excitement to rediscovering one's past through a modern, digital lens.

## Table of Contents
- [Introduction](#introduction)
  Overview of Snapsync and its unique approach to social connectivity.
- [Installation](#installation)
  Instructions for downloading and setting up Snapsync on your device.
- [Usage](#usage)
  How to operate Snapsync effectively, with examples and use cases to help users get started.
- [Files Included](#files-included)
  Descriptions of the content and structure of the directories and files included in Snapsync.
- [Privacy and Security](#privacy-and-security)
  Detailed information on the privacy and security measures Snapsync employs to protect user data.
- [Authors and Acknowledgment](#authors-and-acknowledgment)
  Credits to the team and contributors behind Snapsync.
- [FAQs](#faqs)
  Commonly asked questions about Snapsync with detailed answers to help users.


## Introduction
### Snapsync: Revolutionizing Social Connections

Snapsync introduces a groundbreaking approach to social media, focusing on deepening human connections through the power of shared past experiences. At its core, Snapsync leverages advanced metadata analysis from user-uploaded images to identify instances where individuals have crossed paths ("synced") unknowingly, providing a unique platform for rediscovery and connection.

### Unlocking the Power of Shared Memories
Snapsync is not just about sharing moments, it's about rediscovering them. By analyzing geolocation data and timestamps, Snapsync identifies "syncs" — moments when two people were in the same place at the same time without realizing it. This technology allows users to:

Discover Unexpected Connections: Reconnect with people from your past, discover commonalities you never knew existed, and explore a web of shared experiences stretching back years.
Strengthen Existing Bonds: Enhance relationships with friends and family by uncovering forgotten shared moments, adding depth and richness to your social interactions.
Forge New Friendships: Connect with new people who share similar interests and experiences, fostering meaningful relationships based on common historical threads.

### How Snapsync Works
The process begins with the user providing a personal database of images. Snapsync then meticulously analyzes the metadata — focusing solely on geolocation and timestamps — ensuring a privacy-first approach. The platform operates transparently, guiding users through each step with detailed explanations and alerts, ensuring full understanding and consent before proceeding. Once a potential "sync" is detected, the corresponding metadata is securely deleted to protect user privacy.

### A Sustainable Approach to Social Media
Snapsync offers a sustainable business model that includes:

Sponsored Content: Integrated seamlessly within the platform, enhancing user experience without compromising privacy or usability.
Premium Features: For users seeking deeper insights and more detailed sync detections, Snapsync provides optional premium features, enhancing the overall experience and discovery potential.

By prioritizing user privacy, fostering genuine social connections, and providing an engaging user experience, Snapsync is poised to redefine social interactions. Join us on this revolutionary journey to connect the world through shared memories.


## Installation
To get started with Snapsync, follow these simple steps:

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/snapsync.git
2. Navigate to the project directory:
   ```bash
   cd snapsync
3. Install the necessary dependencies: Depending on the project's setup, you might use npm, pip, or another package manager.
   ```bash
   pip install -r requirements.txt
4. Set up the environment: Configure your environment variables or settings as required by the project (create a .env file in your cloned project directory).
5. Run the application:
   ```bash
    python app.py

## Usage
Here's how to start using Snapsync:

- **Launching the Application:**
  Run the application using the command line or by executing a script, depending on the platform.
  ```bash
  python app.py  # For Python applications

![image](https://github.com/user-attachments/assets/cb2cd666-a611-43af-a16b-de76879a59b3)

- Uploading Images: Navigate to the 'Upload' section in the application to add your images for syncing.

- Discovering Connections: Use the 'Syncs' feature to find past connections based on the locations and timestamps of the uploaded images.

- Viewing 'Syncs': Syncs will be displayed under the 'Connections' tab, where you can see past intersections with other users.

## Files Included

- `app.py`: The main application script for Snapsync.
- `checkPaths.py`: The algorithm for checking between two sets of images whether there is a cross in geolocation and timestamp.
- `extractingMetadata.py`: The algorithm to access the metadate of the images using exifread module.
- `Static/`: css files and profile images of the 'first demonstration' users.
- `templates/`: Utility scripts (html) to support application functions.
- `SnapUsers/`: The 'first demonstration' user's images database.
- `requirements.txt`: A list of Python dependencies necessary to run the application.

## Privacy and Security

Snapsync is committed to maintaining the highest standards of privacy and security. Detailed information about our privacy policies and security measures can be found in the `PRIVACY.md` file included in this repository.

**Key Points:**
- Only metadata from images is used to find matches.
- All data processing is done locally on your device.
- Metadata is deleted immediately after processing.

For a full understanding of our data handling practices, please review our [Privacy Protocol](PRIVACY.md).


## Authors and Acknowledgment

- **Omer Schlesinger**: Co-Founder & CEO.
- **Nayef Kais**: Co-Founder & CTO, Lead developer.
- **Yuval Atias**: Co-Founder & COO.


## FAQs

1. **How does Snapsync ensure the privacy of my data?**
   Snapsync only accesses the metadata of the images you upload, and this data is not stored or transmitted online.

2. **What types of connections can Snapsync discover?**
   Snapsync can discover any instances where two users have been in the same place at the same time, based on the geolocation and timestamp data from their images.

3. **Can I suggest features or report issues for Snapsync?**
   While we do not have a formal contribution section in this document, we highly value community feedback and support. If you have suggestions for features or have encountered any issues, please feel free to report them by opening an issue on our GitHub repository page. We appreciate       your input in making Snapsync better for everyone!

4. **Can I use Snapsync for commercial purposes?**
   Yes, Snapsync is available for both personal and commercial use. For extensive commercial use, consider our premium services.

