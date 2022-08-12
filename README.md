# Add-Signature-to-Certificate

### Pre-requisites
- Install below packages

```bash

sudo apt install python3-pip
sudo apt install git
pip3 install pillow

```

- Store the certificates which are to be attested in 'Certificates' folder
- Store the signature as signature.png
- Identify the co-ordinates where signature is to be overlayed. You can use GIMP/Photoshop to manually place the image and then identify the x and y co-ordinates

### Usage
```bash

python3 Add\ Signature.py

```
- Enter the x and y co-ordinates
- Find the signed certificates inside 'Signed Certificates' folder