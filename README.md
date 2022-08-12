# Add Signature to Certificates

This program is meant to add signatures on top of several certificates at once

### Pre-requisites
- A Ubuntu/Linux machine with Python3 installed
- Install the below packages using Terminal

```bash
sudo apt install python3-pip
sudo apt install git
pip3 install pillow
```
### Installation
- Clone the repository by running below command in Terminal
```bash
git clone https://github.com/khamsakamal48/Add-Signature-to-Certificate.git

cd Add-Signature-to-Certificate/
```
- Store the certificates which are to be attested in the '**Certificates**' folder
  - Make sure that the certificate images are in .png format
- Store the signature as **signature.png**
  - Make sure that the signature.png is resized beforehand
  - Make sure that the background of signature.png is transparent beforehand
- Identify the co-ordinates where the signature is to be overlayed
  - You can use GIMP/Photoshop to manually place the image and then identify the x and y co-ordinates
  - You can use either GIMP/Photoshop to resize the signature while identifying the co-ordinates

### Usage
- Run below command in Terminal
```bash
python3 Add\ Signature.py
```
- Enter the x and y co-ordinates
- Find the signed certificates inside the '**Signed Certificates**' folder