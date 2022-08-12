#!/usr/bin/env python3

import glob, os
from PIL import Image

# Set current directory
os.chdir(os.getcwd())

def add_signature():
    certificate = Image.open(each_certificate)
    signature = Image.open(r"signature.png")
    
    # No transparency mask specified, 
    # simulating an raster overlay
    certificate.paste(signature, (x,y), mask = signature)
    certificate.save(f"{each_certificate}_new.png", "PNG")
    
def move_new_certificates():
    new_certificates = glob.glob("Certificates/*_new.png")
    
    for each_new_certificate in new_certificates:
        os.rename(each_new_certificate, f"Signed {each_certificate}")
        
def housekeeping():
    old_certificates = glob.glob("Signed Certificates/*")
    
    for every_certiifcate in old_certificates:
        try:
            os.remove(every_certiifcate)
        except:
            pass
    
try:
    # Cleaning old certificate files
    housekeeping()
    
    print("Please make sure that the signature is saved as 'signature.png' before proceeding")
    print("")
    
    # Checking if signature exists
    if os.path.exists("signature.png"):
        print("Signature file found")
        print("")
        print("Please make sure that the certificates are stored in 'Certificates' folder before proceeding")
        print("")
        
        # Checking if certificates exists in the folder
        if len(os.listdir("Certificates")) != 0:
            print("Certificates found...")
            print("")
            print("The topmost and leftmost co-ordinate of the certificate is 0,0 where x = 0 and y = 0")
            print("")
            print("You now need to enter these co-oridnates of the certificate from where you will position the signature")
            print("")
            
            # Asking the co-ordinates on where to position the signature in the certificate
            x = int(input("Enter the X co-ordinates: "))
            
            y = int(input("Enter the Y co-ordinates: "))
            
            certificates = glob.glob("Certificates/*")
            for each_certificate in certificates:
                
                # Add signature on certificate
                add_signature()
                
                # Move certifcates to signed certificate folder
                move_new_certificates()
                
                # Remove certificate that is signed
                os.remove(each_certificate)
                
        else:
            print("No certificates found")
            print("")
            print("Please make sure that the certificates are stored in 'Certificates' folder before proceeding")
            print("")
            
    else:
        print("No signature found")
        print("")
        print("Please make sure that the signature is saved as 'signature.png' before proceeding")
        print("")
    
except Exception as Argument:
    print("Below Error while attesting signature to certificates:")
    print(Argument)
    
finally:
    print("Exiting the script")
    exit()