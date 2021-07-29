# ImgurDownloader
 Uses the Imgur API to download all images from an album.
 
 ## Step1: Create an Imgur API Key
 Visit the [Imgur API Key Creation Website](https://api.imgur.com/oauth2/addclient) and create an API key.  Once you have created your API key, enter the key in the `.apicreds` file, replacing the 15 #'s
 - Ex: `{'Authorization': 'Client-ID 1234567890abcdef'}`

 ## How to Use:
 1. Install the required python libraries ("os", "requests", "wget" located within `requirements.txt` ).
 2. Populate the `.apicreds` file with your Imgur API Key.
 3. Run the albumDownloader.py file.
 4. Enter the Imgur Album Hash (Ex: https://imgur.com/a/GFUzVMK -> **GFUzVMK**)
 5. The images should be downloaded in order and will have an index added to them so they are sorted in order.
 6. Let me know if you run into any issues.
